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

# Imports


# Object base class
class Widget(object):
    """
    Object base class
    """

    # region CONSTRUCTORS

    # Constructor
    def __init__(self, name, position, opacity, visible=True):
        """
        Constructor
        :param position: Position (Point)
        :param opacity: Opacity
        """
        # Properties
        self._name = name
        self._position = position
        self._opacity = opacity
        self._visible = visible
    # end __init__

    # endregion CONSTRUCTORS

    # region PROPERTIES

    # Name (getter)
    @property
    def name(self):
        """
        Name
        :return:
        """
        return self._name
    # end name

    # Name (setter)
    @name.setter
    def name(self, value):
        """
        Position
        :return:
        """
        self._name = value
    # end name

    # Position (getter)
    @property
    def position(self):
        """
        Position
        :return:
        """
        return self._position
    # end position

    # Position (setter)
    @position.setter
    def position(self, value):
        """
        Position
        :return:
        """
        self._position = value
    # end position

    # X position (getter)
    @property
    def x(self):
        """
        X position
        :return:
        """
        return self._position.x
    # end x

    # X position (setter)
    @x.setter
    def x(self, value):
        """
        X position (setter)
        :return:
        """
        self._position.x = value
    # end x

    # Y position (getter)
    @property
    def y(self):
        """
        X position
        :return:
        """
        return self._position.y
    # end y

    # Y position (setter)
    @y.setter
    def y(self, value):
        """
        X position
        :return:
        """
        self._position.y = value
    # end y

    # Opacity (getter)
    @property
    def opacity(self):
        """
        X position
        :return:
        """
        value = self._opacity
        value = 1.0 if value > 1.0 else value
        value = 0.0 if value < 0.0 else value
        return value
    # end opacity

    # Opacity (setter)
    @opacity.setter
    def opacity(self, value):
        """
        Opacity
        :return:
        """
        value = 1.0 if value > 1.0 else value
        value = 0.0 if value < 0.0 else value
        self._opacity = value
    # end opacity

    # endregion PROPERTIES

    # region PUBLIC

    # Add the object to an animation

    # Draw the object
    def draw(self, context):
        """
        Draw the object
        :return:
        """
        pass
    # end draw

    # endregion PUBLIC

# end Widget
