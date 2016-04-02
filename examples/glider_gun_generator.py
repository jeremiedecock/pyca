#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cellular Automaton

# The MIT License
#
# Copyright (c) 2016 Jeremie DECOCK (http://www.jdhp.org)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
TODO...
"""

from ca.grid.grid2d import Grid

import json

# Make the initial state ##############

initial_state = Grid(width=48, height=48)

# First "block"
initial_state[5][1] = 1
initial_state[6][1] = 1
initial_state[5][2] = 1
initial_state[6][2] = 1

# Second "block"
initial_state[3][35] = 1
initial_state[4][35] = 1
initial_state[3][36] = 1
initial_state[4][36] = 1

# First "bullet"
initial_state[5][11] = 1
initial_state[6][11] = 1
initial_state[7][11] = 1

initial_state[4][12] = 1
initial_state[8][12] = 1

initial_state[3][13] = 1
initial_state[9][13] = 1

initial_state[3][14] = 1
initial_state[9][14] = 1

initial_state[6][15] = 1

initial_state[4][16] = 1
initial_state[8][16] = 1

initial_state[5][17] = 1
initial_state[6][17] = 1
initial_state[7][17] = 1

initial_state[6][18] = 1

# Second "bullet"
initial_state[3][21] = 1
initial_state[4][21] = 1
initial_state[5][21] = 1

initial_state[3][22] = 1
initial_state[4][22] = 1
initial_state[5][22] = 1

initial_state[2][23] = 1
initial_state[6][23] = 1

initial_state[1][25] = 1
initial_state[2][25] = 1
initial_state[6][25] = 1
initial_state[7][25] = 1

# Write the json file #################

json_dict = {"initial_state": initial_state._grid}

with open("glider_gun.json", "w") as fd:
    json.dump(json_dict, fd, sort_keys=True, indent=4)

