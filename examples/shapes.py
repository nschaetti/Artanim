# -*- coding: utf-8 -*-
#
# File : examples/shapes.py
# Description : How to manipulate shapes
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
from pyglet import shapes


# Create Window
window = pyglet.window.Window(width=1000, height=800, caption="Shapes", resizable=True)

# Various shapes
circle = shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))
square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))

circle.opacity = 120


# Draw window
@window.event
def on_draw():
    circle.draw()
    square.draw()
# end on_draw


# Run app
pyglet.app.run()
