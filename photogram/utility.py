######################################################################
##                
## Copyright (C) 2008,  Goedson Teixeira Paixao
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
## Filename:      utility.py
## Author:        Goedson Teixeira Paixao <goedson@debian.org>
## Description:   
##                
## Created at:    Thu Dec 18 16:59:33 2008
## Modified at:   Fri Dec 19 10:08:39 2008
## Modified by:   Goedson Teixeira Paixao <goedson@debian.org>
######################################################################

import Image

class ImageLoader:
    def __init__(self, size, bgcolor):
        self.size = size
        self.bgcolor = bgcolor

    def load_image(self, filename):
        image = Image.new('RGB', self.size, self.bgcolor)
        if filename:
            file_image = Image.open(filename)
            image_size = file_image.size

            x_ratio = 1.0 * image_size[0] / self.size[0]
            y_ratio = 1.0 * image_size[1] / self.size[1]

            if (x_ratio > y_ratio):
                resize_factor = 1.0 / x_ratio
            else:
                resize_factor = 1.0 / y_ratio

            new_size = tuple([int(x * resize_factor) for x in image_size])
            resized_image = file_image.resize(new_size)
            
            top_left = ((self.size[0] - new_size[0]) / 2, (self.size[1]- new_size[1]) / 2)
            bottom_right = (top_left[0] + new_size[0], top_left[1] + new_size[1])
            
            box = (top_left[0],top_left[1], bottom_right[0], bottom_right[1])
            image.paste(resized_image, box)
        return image


