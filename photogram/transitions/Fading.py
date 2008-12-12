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
## Filename:      Fading.py
## Author:        Goedson Teixeira Paixao <goedson@debian.org>
## Description:   
##                
## Created at:    Mon Dec  1 18:31:34 2008
## Modified at:   Fri Dec  5 17:27:04 2008
## Modified by:   Goedson Teixeira Paixao <goedson@debian.org>
######################################################################
import Image

class Fading(Transition):
    def __init__(self, **params):
        Transition.__init__(self,**params)

    def render(self, total_frames):
        alpha_step = 1.0/total_frames
        alpha = 0.0
        while alpha <=1.0:
            img = Image.blend(self.initial_frame, self.final_frame, alpha)
            yield img
            alpha += alpha_step

def create_crossfade(**params):
    return Fading(**params)


register_transition('Crossfade', TransitionFactory('Crossfade',create_crossfade))
