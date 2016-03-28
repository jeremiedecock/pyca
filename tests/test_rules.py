#!/usr/bin/env python3
# -*- coding : utf-8 -*-

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
This module contain unit tests for the "Rules" class.
"""

from ca.rules.conway import Rules
from ca.grid.grid2d import Grid

import unittest

class RulesPacket(unittest.TestCase):
    """
    Contains unit tests for the "rules" module.
    """

    # Tests for the next_state function #######################################

    def test_next_state_func(self):
        """Check that the next_state function returns the expected result."""

        rules = Rules()                             # TODO mone in the preprocessing function
        state = Grid(grid=[[0, 1, 0], [0, 1, 0], [0, 1, 0]])   # TODO mone in the preprocessing function

        next_state = rules.next_state(state)
        expected_next_state = Grid(grid=[[0, 0, 0], [1, 1, 1], [0, 0, 0]])

        self.assertEqual(next_state, expected_next_state)


if __name__ == '__main__':
    unittest.main()

