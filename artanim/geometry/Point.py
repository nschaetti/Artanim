# -*- coding: utf-8 -*-
#
# File : artificialis_intro.py
# Description : Code for the intro of the Artificialis Code YouTube channel
# Date : 28th of March, 2021
#
# This file is part of Artificialis Intro.  Artificialis Intro is free software: you can
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


# Represents a point
class Point(object):
    """
    Represents a point
    """

    # region CONSTRUCTORS

    # Constructors
    def __init__(self, x, y):
        """
        Constructor
        """
        super(Point, self).__init__()
        self._x = x
        self._y = y
    # end __init__

    # endregion CONSTRUCTORS

    # region PROPERTIES

    # X position (getter)
    @property
    def x(self):
        """
        X position
        :return:
        """
        return self._x
    # end x

    # X position (setter)
    @x.setter
    def x(self, value):
        """
        X position (setter)
        :return:
        """
        self._x = value
    # end x

    # Y position (getter)
    @property
    def y(self):
        """
        Y position
        :return:
        """
        return self._y
    # end y

    # Y position (setter)
    @y.setter
    def y(self, value):
        """
        Y position (setter)
        :return:
        """
        self._y = value
    # end y

    # endregion PROPERTIES

    # region OVERRIDE

    # Addition
    def __add__(self, other):
        """
        Addition
        :param other:
        :return:
        """
        return Point(self._x + other.x, self._y + other.y)
    # end __add__

    # Substraction
    def __sub__(self, other):
        """
        Substraction
        :param other:
        :return:
        """
        return Point(self._x - other.x, self._y - other.y)
    # end __sub__

    # Multiplication
    def __mul__(self, other):
        """
        Multiplication
        :param other:
        :return:
        """
        return Point(self._x * other, self._y * other)
    # end __mul__

    # Representation
    def __repr__(self):
        """
        Representation
        :return:
        """
        return "Point({}, {})".format(self._x, self._y)
    # end __repr__

    # endregion OVERRIDE

# end Point
