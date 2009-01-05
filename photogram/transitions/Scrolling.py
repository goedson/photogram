######################################################################
##                
## Copyright (C) 2008-2009,  Goedson Teixeira Paixao
##                
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License
## as published by the Free Software Foundation; either version 3
## of the License, or (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
## 02110-1301, USA.
##                
## Filename:      Scrolling.py
## Author:        Goedson Teixeira Paixao <goedson@debian.org>
## Description:   
##                
## Created at:    Mon Dec  1 17:48:01 2008
## Modified at:   Mon Jan  5 16:58:27 2009
## Modified by:   Goedson Teixeira Paixao <goedson@debian.org>
######################################################################

import ImageChops


class Direction:
    def __init__(self, xdelta, ydelta):
        if xdelta not in (0,1,-1):
            raise ValueError("xdelta must be 0, 1 or -1")
        if ydelta not in (0,1,-1):
            raise ValueError("ydelta must be 0, 1 or -1")

        self.xdelta = xdelta
        self.ydelta = ydelta

left = Direction(1,0)
right = Direction(-1,0)
top = Direction(0,1)
bottom = Direction(0,-1)
top_left = Direction(1,1)
top_right = Direction(-1,1)
bottom_left = Direction(1,-1)
bottom_right = Direction(-1,-1)


class Scrolling(Transition):
    def __init__(self, **params):
        self.movement = params.pop('movement','enter')
        self.direction = params.pop('direction',left)
        Transition.__init__(self, **params)

    def render(self, total_frames):
        img_width, img_height = self.initial_frame.size

        if self.movement == 'enter':
            bg_image = self.initial_frame.copy()
            fg_image = self.final_frame.copy()
        else:
            bg_image = self.final_frame.copy()
            fg_image = self.initial_frame.copy()

        width_step = (img_width / total_frames) * abs(self.direction.xdelta)
        height_step = (img_height / total_frames) * abs(self.direction.ydelta)

        if self.movement == 'enter':
            if width_step != 0:
                region_width = width_step + (img_width % total_frames)
            else:
                region_width = img_width

            if height_step != 0:
                region_height = height_step + (img_height % total_frames)
            else:
                region_height = img_height

            if self.direction.xdelta > 0:
                region_x = img_width - region_width
                region_x_step = -width_step
            else:
                region_x = 0
                region_x_step = 0

            if self.direction.ydelta > 0:
                region_y = img_height - region_height
                region_y_step = -height_step
            else:
                region_y = 0
                region_y_step = 0

            if self.direction.xdelta < 0:
                paste_x = img_width - region_width
                paste_x_step = -width_step
            else:
                paste_x = 0
                paste_x_step = 0


            if self.direction.ydelta < 0:
                paste_y = img_height - region_height
                paste_y_step = -height_step
            else:
                paste_y = 0
                paste_y_step = 0
        else: #if movement == 'exit'
            width_step = -width_step
            height_step = -height_step

            if width_step != 0:
                region_width = img_width - (abs(width_step) + (img_width % total_frames))
            else:
                region_width = img_width
            if height_step != 0:
                region_height = img_height - (abs(height_step) + (img_height % total_frames))
            else:
                region_height = img_height

            if self.direction.xdelta > 0:
                region_x = img_width - region_width
                region_x_step = -width_step
            else:
                region_x = 0
                region_x_step = 0

            if self.direction.ydelta > 0:
                region_y = img_height - region_height
                region_y_step = -height_step
            else:
                region_y = 0
                region_y_step = 0

            if self.direction.xdelta < 0:
                paste_x = img_width - region_width
                paste_x_step = -width_step
            else:
                paste_x = 0
                paste_x_step = 0


            if self.direction.ydelta < 0:
                paste_y = img_height - region_height
                paste_y_step = -height_step
            else:
                paste_y = 0
                paste_y_step = 0

        for frame in xrange(total_frames):
            crop_region = (region_x, region_y, region_x + region_width, region_y + region_height)
            paste_region = (paste_x, paste_y, paste_x + region_width, paste_y + region_height)
            croped_img = fg_image.crop(crop_region)
            img = bg_image.copy()
            img.paste(croped_img, paste_region)
            yield img
            region_width += width_step
            region_height += height_step
            paste_x += paste_x_step
            paste_y += paste_y_step
            region_x += region_x_step
            region_y += region_y_step


def create_slider(movement, direction):
    def creator_function(**params):
        params['movement'] = movement
        params['direction'] = direction
        return Scrolling(**params)
    return creator_function

register_transition('Enter from left', TransitionFactory('Enter from left', create_slider('enter', left)))
register_transition('Enter from right', TransitionFactory('Enter from right', create_slider('enter', right)))
register_transition('Enter from top', TransitionFactory('Enter from top', create_slider('enter', top)))
register_transition('Enter from bottom', TransitionFactory('Enter from bottom', create_slider('enter', bottom)))
register_transition('Enter from topleft', TransitionFactory('Enter from topleft', create_slider('enter', top_left)))
register_transition('Enter from topright', TransitionFactory('Enter from topright', create_slider('enter', top_right)))
register_transition('Enter from bottomleft', TransitionFactory('Enter from bottomleft', create_slider('enter', bottom_left)))
register_transition('Enter from bottomright', TransitionFactory('Enter from bottomright', create_slider('enter', bottom_right)))

register_transition('Exit to left', TransitionFactory('Exit to left', create_slider('exit', left)))
register_transition('Exit to right', TransitionFactory('Exit to right', create_slider('exit', right)))
register_transition('Exit to top', TransitionFactory('Exit to top', create_slider('exit', top)))
register_transition('Exit to bottom', TransitionFactory('Exit to bottom', create_slider('exit', bottom)))
register_transition('Exit to topleft', TransitionFactory('Exit to topleft', create_slider('exit', top_left)))
register_transition('Exit to topright', TransitionFactory('Exit to topright', create_slider('exit', top_right)))
register_transition('Exit to bottomleft', TransitionFactory('Exit to bottomleft', create_slider('exit', bottom_left)))
register_transition('Exit to bottomright', TransitionFactory('Exit to bottomright', create_slider('exit', bottom_right)))

