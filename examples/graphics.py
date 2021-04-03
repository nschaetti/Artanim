# -*- coding: utf-8 -*-
#
# File : graphics.py
# Description : Handle graphics
# Date : 3th of April, 2021
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

# Window configuration
config = pyglet.gl.Config(sample_buffers=1, samples=5)

# Create a window
window = pyglet.window.Window(width=1000, height=800, caption="Graphics", config=config, resizable=True)
# window = pyglet.window.Window(width=1000, height=800, caption="Graphics")


# Draw
@window.event
def on_draw():
    pyglet.graphics.draw(
        2,
        pyglet.gl.GL_LINES,
        ('v2i', (10, 15, 300, 350)),
        ('c3B', (0, 255, 0, 0, 0, 255))
    )
# end on_draw


pyglet.app.run()


