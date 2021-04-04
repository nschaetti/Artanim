# -*- coding: utf-8 -*-
#
# File : svg.py
# Description : Handle SVG files
# Date : 3th of April, 2021
#
# This file is part of Artanim.  Artanim is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Nils Schaetti <n.schaetti@gmail.com>


# Imports
import pyglet
import numpy as np
import math
import random
from artanim.utils import convert_math_formula_to_svg

# Parameters
zoom = 30
n_points = 10

# Transform math expression to SVG
paths, attributes, svg_attributes = convert_math_formula_to_svg("../tex_template.tex", "\sum_{i=0}^{k} i=2")

# SVG size
svg_width = int(math.ceil(float(svg_attributes['width'][:-2])))
svg_height = int(math.ceil(float(svg_attributes['height'][:-2])))

# Window size
window_width = svg_width * zoom
window_height = svg_height * zoom

# Create window
config = pyglet.gl.Config(sample_buffers=1, samples=4)
window = pyglet.window.Window(width=svg_width * zoom, height=svg_height * zoom, config=config)

# List of symbols
symbols = list()

# For each path
for path in paths:

    # Check if continuous
    if path.iscontinuous():
        cont_path = [path]
    else:
        cont_path = path.continuous_subpaths()
    # end if

    # For each continuous subpath
    for sub_path in cont_path:
        # Keep points
        points = list()
        point_colors = list()

        # For each curve in the path
        for curve in sub_path:
            print(curve)
            # To numpy object
            poly_obj = curve.poly()

            # Append point
            for n in np.linspace(0.0, 1.0, n_points):
                # Get position
                poly_point = poly_obj(n)

                # Add point and color
                points += [poly_point.real * zoom, poly_point.imag * zoom + window_height / 2]
                point_colors += [255, 255, 255]
            # end for
        # end for

        # Add a list of vertex
        symbols.append(
            pyglet.graphics.vertex_list(
                len(points) // 2,
                ('v2f', points),
                ('c3B', point_colors)
            )
        )
    # end for
    break
# end for


# Draw
@window.event
def on_draw():
    """
    Draw
    :return:
    """
    # For each vertex list
    # pyglet.gl.glPolygonMode(pyglet.gl.GL_FRONT_AND_BACK, pyglet.gl.GL_FILL)
    for vertex_list in symbols:
        vertex_list.draw(pyglet.gl.GL_POLYGON)
    # end for
# end on_draw


pyglet.app.run()
