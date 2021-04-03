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
import sys
import os
import tempfile
from svgpathtools import svg2paths, wsvg, svg2paths2


# Transform tex file to DVI file
def convert_tex_to_dvi(latex_file, tmp_dir):
    """
    Transform tex file to DVI file
    :param latex_file: Latex file
    :param tmp_dir: Temporary directory
    """
    # Latex command line
    command = [
        'latex',
        '-interaction=batchmod',
        '-halt-on-error',
        '-output',
        '-directory=\"{}\"'.format(latex_file),
        latex_file,
        '>',
        os.devnull
    ]
    print(latex_file)
    # Run command
    os.system(' '.join(command))

    # Return DVI file
    return os.path.join(tmp_dir, latex_file.replace(".tex", ".dvi"))
# end convert_tex_to_dvi


# Transform a DVI to a SVG file
def convert_dvi_to_svg(dvi_file, output_svg_file):
    """
    Convert a DVI to
    :param dvi_file: DVI file
    :param output_svg_file: Output SVG file
    """
    # Command
    command = [
        'dvisvgm',
        dvi_file,
        '-n',
        '-v',
        '0',
        '-o',
        '\"{}\"'.format(output_svg_file),
        '>',
        os.devnull
    ]

    # Run command
    os.system(' '.join(command))
# end convert_dvi_to_svg


# Transform tex to svg
def convert_tex_to_svg(tex_file):
    """
    Transform tex to svg
    :param tex_file:
    :param output_svg_file:
    :param tmp_dir: Temporary directory
    :return:
    """
    # Temporary file
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Convert tex file to dvi
        dvi_file = convert_tex_to_dvi(tex_file, tmp_dir)

        # SVG file
        tmp_svg_file = tex_file.replace(".tex", ".svg")

        # Convert DVI to SVG
        convert_dvi_to_svg(dvi_file, tmp_svg_file)

        # Load SVG file
        svg_data = svg2paths2(tmp_svg_file)
        return svg_data
    # end with
# end convert_tex_to_svg


# Transform tex formula to SVG
def convert_math_formula_to_svg(template_file_path: str, math_formula: str):
    """
    Transform tex formula to SVG
    :param math_formula:
    :return:
    """
    # Open template file
    with open(template_file_path, 'r') as file:
        # Read all
        template_tex = file.read()

        # Replace with formulas
        template_tex = template_tex.replace("[math_formula]", math_formula)

        # Create a temporary file
        with tempfile.TemporaryFile(mode='w') as tmp_file:
            # Write tex content
            tmp_file.write(template_tex)
            print("tmp_file: {}".format(tmp_file))
            # Convert tex file to SVG
            svg_data = convert_tex_to_svg(tmp_file.name)
            print(svg_data)
        # end with
    # end with
# end convert_math_formula_to_svg


convert_math_formula_to_svg("../tex_template.tex", "\sum_{x=0}^{2} x=2")

