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
from .latex_functions import convert_tex_to_svg, convert_dvi_to_svg, convert_tex_to_dvi, convert_math_formula_to_svg

# All
__all__ = [
    'convert_dvi_to_svg',
    'convert_tex_to_dvi',
    'convert_math_formula_to_svg',
    'convert_tex_to_svg'
]
