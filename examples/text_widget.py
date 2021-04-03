# -*- coding: utf-8 -*-
#
# File : examples/text_widget.py
# Description : Example with text widget
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


# Create a window
window = pyglet.window.Window()

# Create a label
label = pyglet.text.Label(
    "Hello World",
    font_name="Bebas",
    font_size=36,
    x=window.width/2,
    y=window.height/2,
    anchor_x='center',
    anchor_y='center',
    width=window.width
)

# Create a document
document = pyglet.text.decode_text("Hello, world.")
document.text = "Goodbye"
print(document)
layout = pyglet.text.layout.TextLayout(document, 10, 10)
font_name = document.get_style('font_name', 0)
print(layout)
print("Font name: {}".format(font_name))
document.set_style(0, 5, dict(font_name='Arial', font_size=12))


@window.event
def on_draw():
    window.clear()
    label.draw()
    layout.draw()
# end on_draw


# Run app
pyglet.app.run()
