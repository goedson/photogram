######################################################################
##                
## Copyright (C) 2009,  Goedson Teixeira Paixao
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
## Filename:      Zoom.py
## Author:        Goedson Teixeira Paixao <goedson@debian.org>
## Description:   Zooming transition effects
##                
## Created at:    Thu Jan 22 17:16:08 2009
## Modified at:   Thu Jan 22 18:58:54 2009
## Modified by:   Goedson Teixeira Paixao <goedson@debian.org>
######################################################################

import ImageChops

class ZoomIn(Transition):
    def __init__(self, **params):
        Transition.__init__(self, **params)

    def render(self, total_frames):
        img_width, img_height = self.initial_frame.size

        zoomed_width = (img_width / total_frames) + (img_width % total_frames)
        zoomed_height = img_height / total_frames + (img_height % total_frames)
        width_step = img_width / total_frames
        height_step = img_height / total_frames

        for i in range(total_frames):
            img = self.initial_frame.copy()
            zoomed_image = self.final_frame.resize((zoomed_width, zoomed_height))
            paste_x = (img_width - zoomed_width) / 2
            paste_y = (img_height - zoomed_height) / 2
            paste_region = (paste_x, paste_y, paste_x + zoomed_width, paste_y + zoomed_height)
            img.paste(zoomed_image, paste_region)
            yield img
            zoomed_width += width_step
            zoomed_height += height_step

class ZoomOut(Transition):
    def __init__(self, **params):
        Transition.__init__(self, **params)

    def render(self, total_frames):
        img_width, img_height = self.initial_frame.size

        crop_width = (img_width / total_frames) + (img_width % total_frames)
        crop_height = img_height / total_frames + (img_height % total_frames)
        width_step = img_width / total_frames
        height_step = img_height / total_frames

        for i in range(total_frames):
            crop_x = (img_width - crop_width) / 2
            crop_y = (img_height - crop_height) / 2
            crop_region = (crop_x, crop_y, crop_x + crop_width, crop_y + crop_height)
            cropped_image = self.final_frame.crop(crop_region)
            img = cropped_image.resize((img_width, img_height))
            yield img
            crop_width += width_step
            crop_height += height_step

register_transition('Zoom in', TransitionFactory('Zoom in', ZoomIn))
register_transition('Zoom out', TransitionFactory('Zoom out', ZoomOut))
