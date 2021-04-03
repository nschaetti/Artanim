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
import artanim
from artanim.widgets import Image
from artanim.geometry import Point
from artanim.animations import Move, Modify, Rotate
import pyglet

# New window
window = pyglet.window.Window(1920, 1080)

# New scene at 120fps
intro_scene = artanim.Scene(
    window=window,
    duration=8,
    width=1920,
    height=1080,
    frame_rate=120,
    background_image='./resources/background.png',
    output_streams=[artanim.streams.VideoStream(
        output_image_dir='./outputs',
        output_video_file='./outputs/video.mp4',
        frame_rate=120,
        delete_tmp_image_files=True
    )],
    preview=False
)

# Add objects
intro_scene.add([
    Image("mini_cubes", Point(0, 0), './resources/mini_cubes.png', opacity=0.0, scale=0.0),
    Image("rayons", Point(0, 0), "./resources/rayons.png", opacity=0.0, scale=1.0),
    Image("red_cube", Point(0, 0), './resources/red_cube.png', opacity=0.0, scale=0.0),
    Image("blue_cube", Point(0, 0), './resources/blue_cube.png', opacity=0.0, scale=0.0),
    Image("green_cube", Point(0, 0), './resources/green_cube.png', opacity=0.0, scale=0.0),
    Image("purple_cube", Point(0, 0), './resources/purple_cube.png', opacity=0.0, scale=0.0),
    Image("little_green_cube", Point(0, 0), './resources/little_green_cube.png', opacity=0.0, scale=0.0),
    Image("artificialis_code", Point(0, 0), './resources/artificialis_code.png', opacity=0.0, scale=0.0),
    Image("robot", Point(0, -850), "./resources/robot.png", opacity=1.0, scale=1.0),
])

# Move the background
intro_scene.animate([
    # Background start
    Modify(intro_scene.background_image, 'scale', 1.2, 0.0, duration=8.0, easing_function='LinearInOut'),
    # Background end
    # Modify(intro_scene.background_image, 'scale', 0.0, 7.9, duration=0.1, easing_function='CubicEaseInOut'),
    # Robot
    Move(intro_scene['robot'], Point(0, 0), 0, duration=6.0, easing_function='ElasticEaseOut'),
    Move(intro_scene['robot'], Point(0, -850), 7.5, duration=0.5, easing_function='CubicEaseIn'),
    # Title start
    Modify(intro_scene['artificialis_code'], 'scale', 1.10, 2, duration=1, easing_function='CubicEaseIn'),
    Modify(intro_scene['artificialis_code'], 'opacity', 1.10, 2, duration=1, easing_function='CubicEaseIn'),
    Rotate(intro_scene['artificialis_code'], -5, 2, duration=5.75, easing_function='LinearInOut'),
    # Title middle
    Modify(intro_scene['artificialis_code'], 'scale', 1.30, 3, duration=4.75, easing_function='LinearInOut'),
    # Title end
    Modify(intro_scene['artificialis_code'], 'scale', 0.00, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Modify(intro_scene['artificialis_code'], 'opacity', 0.00, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Rotate(intro_scene['artificialis_code'], 90, 7.75, duration=0.25, easing_function='LinearInOut'),
    # Minicubes start
    Modify(intro_scene['mini_cubes'], 'scale', 1.0, 2.25, duration=0.75, easing_function='CubicEaseIn'),
    Modify(intro_scene['mini_cubes'], 'opacity', 1.0, 2.25, duration=0.75, easing_function='CubicEaseIn'),
    # Minicubes middle
    Modify(intro_scene['mini_cubes'], 'scale', 1.20, 3, duration=4.75, easing_function='LinearInOut'),
    # Minicubes end
    Modify(intro_scene['mini_cubes'], 'scale', 0.00, 7.65, duration=0.35, easing_function='CubicEaseInOut'),
    Modify(intro_scene['mini_cubes'], 'opacity', 0.00, 7.65, duration=0.35, easing_function='CubicEaseInOut'),
    # Rayons
    Modify(intro_scene['rayons'], 'opacity', 1.0, 2.5, duration=1.25, easing_function='CubicEaseInOut'),
    Modify(intro_scene['rayons'], 'opacity', 0.0, 7.5, duration=0.5, easing_function='CubicEaseInOut'),
    Rotate(intro_scene['rayons'], 25, 2.5, duration=5.5, easing_function='LinearInOut'),
    # Red cube start
    Modify(intro_scene['red_cube'], 'opacity', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Modify(intro_scene['red_cube'], 'scale', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Move(intro_scene['red_cube'], Point(150, 300), 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Rotate(intro_scene['red_cube'], 180, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    # Red cube middle
    Move(intro_scene['red_cube'], Point(200, 400), 3.3, duration=4.45, easing_function='LinearInOut'),
    Rotate(intro_scene['red_cube'], 270, 3.3, duration=4.45, easing_function='LinearInOut'),
    # Red cube end
    Modify(intro_scene['red_cube'], 'opacity', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Modify(intro_scene['red_cube'], 'scale', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Move(intro_scene['red_cube'], Point(0, 0), 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    # Blue cube start
    Modify(intro_scene['blue_cube'], 'opacity', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Modify(intro_scene['blue_cube'], 'scale', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Move(intro_scene['blue_cube'], Point(200, 50), 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Rotate(intro_scene['blue_cube'], 180, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    # Blue cube middle
    Move(intro_scene['blue_cube'], Point(400, 100), 3.3, duration=4.45, easing_function='LinearInOut'),
    Rotate(intro_scene['blue_cube'], 270, 3.3, duration=4.45, easing_function='LinearInOut'),
    # Blue cube end
    Modify(intro_scene['blue_cube'], 'opacity', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Modify(intro_scene['blue_cube'], 'scale', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Move(intro_scene['blue_cube'], Point(0, 0), 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    # Green cube start
    Modify(intro_scene['green_cube'], 'opacity', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Modify(intro_scene['green_cube'], 'scale', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Move(intro_scene['green_cube'], Point(-300, -150), 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Rotate(intro_scene['green_cube'], 180, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    # Green cube middle
    Move(intro_scene['green_cube'], Point(-600, -300), 3.3, duration=4.45, easing_function='LinearInOut'),
    Rotate(intro_scene['green_cube'], 270, 3.3, duration=4.45, easing_function='LinearInOut'),
    # Green cube end
    Modify(intro_scene['green_cube'], 'opacity', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Modify(intro_scene['green_cube'], 'scale', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Move(intro_scene['green_cube'], Point(0, 0), 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    # Green cube start
    Modify(intro_scene['purple_cube'], 'opacity', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Modify(intro_scene['purple_cube'], 'scale', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Move(intro_scene['purple_cube'], Point(-600, 300), 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Rotate(intro_scene['purple_cube'], 180, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    # Green cube middle
    Move(intro_scene['purple_cube'], Point(-800, 400), 3.3, duration=4.45, easing_function='LinearInOut'),
    Rotate(intro_scene['purple_cube'], 270, 3.3, duration=4.45, easing_function='LinearInOut'),
    # Green cube end
    Modify(intro_scene['purple_cube'], 'opacity', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Modify(intro_scene['purple_cube'], 'scale', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Move(intro_scene['purple_cube'], Point(0, 0), 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    # Little Green cube start
    Modify(intro_scene['little_green_cube'], 'opacity', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Modify(intro_scene['little_green_cube'], 'scale', 1.0, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Move(intro_scene['little_green_cube'], Point(200, -100), 2.3, duration=1.0, easing_function='CubicEaseIn'),
    Rotate(intro_scene['little_green_cube'], 180, 2.3, duration=1.0, easing_function='CubicEaseIn'),
    # Little Green cube middle
    Move(intro_scene['little_green_cube'], Point(800, -400), 3.3, duration=4.45, easing_function='LinearInOut'),
    Rotate(intro_scene['little_green_cube'], 270, 3.3, duration=4.45, easing_function='LinearInOut'),
    # Little Green cube end
    Modify(intro_scene['little_green_cube'], 'opacity', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Modify(intro_scene['little_green_cube'], 'scale', 0.0, 7.75, duration=0.25, easing_function='CubicEaseInOut'),
    Move(intro_scene['little_green_cube'], Point(0, 0), 7.75, duration=0.25, easing_function='CubicEaseInOut'),
])

# Play and save
intro_scene.run()
