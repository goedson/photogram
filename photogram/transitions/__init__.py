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
## Filename:      __init__.py
## Author:        Goedson Teixeira Paixao <goedson@debian.org>
## Description:   
##                
## Created at:    Mon Dec  1 18:27:19 2008
## Modified at:   Thu Dec 18 22:42:41 2008
## Modified by:   Goedson Teixeira Paixao <goedson@debian.org>
######################################################################
import glob
import os.path
import Image

class TransitionFactory:
    def __init__(self, name, factory):
        self.name = name
        self.factory = factory

    def create_transition(self, **params):
        return self.factory(**params)

class Transition:
    def __init__(self, initial_frame, final_frame, bgcolor):
        self.initial_frame = initial_frame
        self.final_frame = final_frame
        self.bgcolor = bgcolor

factories = {}

def register_transition(name, transition_factory):
    factories[name] = transition_factory


#
# Process all transition plugin files
#
files = glob.glob(os.path.join(__path__[0],'*.py'))

for module in files:
    if not module.endswith('__init__.py'):
        execfile(module, globals())

print 'Registered %d transition effects' % len(factories)
