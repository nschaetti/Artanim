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
import pyglet
from .Widget import Widget
from artanim.geometry import Point


# Image object
class Image(Widget):
    """
    Image object
    """

    # region CONSTRUCTORS

    # Constructors
    def __init__(self, name: str, position: Point, image_file_path: str, opacity: float, scale=1.0, rotation=0,
                 batch=None, group=None):
        """
        Constructors
        :param position:
        :param image_file_path:
        """
        # Super
        super(Image, self).__init__(name, position, opacity)

        # Properties
        self.opacity = opacity
        self._scale = scale
        self._rotation = rotation

        # Load image
        pic_img = pyglet.image.load(image_file_path)
        pic_img.anchor_x = pic_img.width // 2
        pic_img.anchor_y = pic_img.height // 2

        # Load image
        self._sprite = pyglet.sprite.Sprite(
            img=pic_img,
            batch=batch,
            group=group
        )
    # end __init__

    # endregion CONSTRUCTORS

    # region PROPERTIES

    # Sprite (getter)
    @property
    def sprite(self):
        """
        Sprite
        :return:
        """
        return self._sprite
    # end sprite

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
        # Change position
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

    # Scale (getter)
    @property
    def scale(self):
        """
        Scale
        :return:
        """
        return self._scale
    # end y

    # Scale (setter)
    @scale.setter
    def scale(self, value):
        """
        Scale
        :return:
        """
        self._scale = value
    # end scale

    # Rotation (getter)
    @property
    def rotation(self):
        """
        rotation
        :return:
        """
        return self._rotation
    # end rotation

    # Rotation (setter)
    @rotation.setter
    def rotation(self, value):
        """
        Rotation
        :return:
        """
        self._rotation = value
    # end rotation

    # endregion PROPERTIES

    # region PRIVATE

    # Set update sprite position
    def _compute_sprite_position(self):
        """
        Set update sprite position
        :return:
        """
        sprite_x = self._position.x - int(self._sprite.width / 2.0)
        sprite_y = self._position.y - int(self._sprite.height / 2.0)
        return Point(sprite_x, sprite_y)
    # end _update_sprite_position

    # Update sprite
    def _update_sprite(self, context):
        """
        Update sprite
        :return:
        """
        # Opacity
        self._sprite.opacity = self.opacity * 255.0

        # Scale
        self._sprite.scale = self._scale

        # Rotation
        self._sprite.rotation = self._rotation

        # To screen space
        # sprite_pos = context.transform(self._compute_sprite_position(), new_point=True)
        sprite_pos = context.transform(self._position, new_point=True)

        # Update
        self._sprite.x = sprite_pos.x
        self._sprite.y = sprite_pos.y
    # end _update_sprite

    # endregion PRIVATE

    # region OVERRIDE

    # Draw the object
    def draw(self, context):
        """
        Draw the object
        """
        # Update sprite properties
        self._update_sprite(context)

        # Draw
        self._sprite.draw()
    # end draw

    # endregion OVERRIDE

# end Image
