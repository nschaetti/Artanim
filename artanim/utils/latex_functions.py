# -*- coding: utf-8 -*-
#
# File : utils/latex_functions.py
# Description : Latex utility functions
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
import logging
import subprocess
from svgpathtools import svg2paths2


# Transform tex file to DVI file
def convert_tex_to_dvi(latex_file, tmp_output_dir):
    """
    Transform tex file to DVI file
    :param latex_file: Latex file
    :param tmp_output_dir: Temporary directory
    """
    # Latex command line
    command = [
        'latex',
        '-interaction=batchmode',
        '-halt-on-error',
        '-output-directory={}'.format(tmp_output_dir),
        "{}".format(latex_file)
    ]

    # Debug command
    logging.log(logging.DEBUG, "Latex to dvi command: {}".format(command))

    # Run command
    latex_output = subprocess.run(command, stdout=subprocess.PIPE)

    # Log output
    logging.log(logging.DEBUG, "Latex stdout: {}".format(latex_output.stdout))
    logging.log(logging.DEBUG, "Latex stderr: {}".format(latex_output.stderr))

    # Latex file name and base name
    latex_file_basename = os.path.basename(latex_file)

    # Handle error
    if latex_output.returncode != 0:
        # Log file
        log_file = os.path.join(tmp_output_dir, latex_file_basename.replace('.tex', '.log'))

        # Log error
        logging.log(logging.ERROR, "Error converting TeX file to DVI with LaTeX !")

        # Read the log file
        with open(log_file, 'r') as log_f:
            for line in log_f.readlines():
                if line.startswith("!"):
                    logging.log(logging.INFO, line)
                # end if
            # end for
        # end with

        # End of program
        sys.exit(2)
    # end if

    # Return DVI file
    return os.path.join(tmp_output_dir, latex_file_basename.replace(".tex", ".dvi"))
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
        '{}'.format(output_svg_file)
    ]

    # Debug command
    logging.log(logging.DEBUG, "Latex to dvi command: {}".format(command))

    # Run command
    latex_output = subprocess.run(command, stdout=subprocess.PIPE)

    # Log output
    logging.log(logging.DEBUG, "Latex stdout: {}".format(latex_output.stdout))
    logging.log(logging.DEBUG, "Latex stderr: {}".format(latex_output.stderr))

    # Handle error
    if latex_output.returncode != 0:
        # Log error
        logging.log(logging.ERROR, "Error converting DVI file to SVG with dvisvgm !")
        logging.log(logging.ERROR, "Latex stdout: {}".format(latex_output.stdout))
        logging.log(logging.ERROR, "Latex stderr: {}".format(latex_output.stderr))

        # Out
        sys.exit(2)
    # end if
# end convert_dvi_to_svg


# Transform tex to svg
def convert_tex_to_svg(tex_file):
    """
    Transform tex to svg
    :param tex_file:
    :param tex_file:
    :return: SVG data
    """
    # Temporary file
    with tempfile.TemporaryDirectory() as tmp_output_dir:
        # Convert tex file to dvi
        dvi_file = convert_tex_to_dvi(tex_file, tmp_output_dir)

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
        with tempfile.NamedTemporaryFile(mode='w', suffix='.tex') as tmp_latex_file:
            # Write tex content
            tmp_latex_file.write(template_tex)
            tmp_latex_file.flush()

            # Convert tex file to SVG
            return convert_tex_to_svg(tmp_latex_file.name)
        # end with
    # end with
# end convert_math_formula_to_svg