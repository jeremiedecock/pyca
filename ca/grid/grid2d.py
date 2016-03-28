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

__all__ = ['Grid']

import os

class Grid:

    def __init__(self, width=None, height=None, grid=None):

        # Set the grid
        if (width is not None) and (height is not None):
            self._grid = [[0 for idx in range(width)] for idy in range(height)]
        elif grid is not None:
            self._grid = grid
        else:
            raise Exception("Wrong parameters")                         # TODO

        # Check the grid
        for line in self._grid:
            if len(line) != self.width:
                raise Exception("Ill-formed grid: " + str(self._grid))  # TODO

        if self.width < 3 or self.height < 3:
            raise Exception("Ill-formed grid: " + str(self._grid))      # TODO

    def __getitem__(self, key):
        return self._grid[key]

    def __setitem__(self, key, value):
        self._grid[key] = value

    def __str__(self):
        return os.linesep.join([' '.join([str(cell) for cell in line]) for line in self._grid])

    # READ ONLY PROPERTIES

    @property
    def width(self):
        """The width of the grid.

        This member is a read-only property.
        """
        return len(self._grid[0])

    @property
    def height(self):
        """The height of the grid.

        This member is a read-only property.
        """
        return len(self._grid)



if __name__ == '__main__':

    # Init the grid
    WIDTH = 4
    HEIGHT = 3
    initial_grid = [[0 for idx in range(WIDTH)] for idy in range(HEIGHT)]
    initial_grid[0][0] = 1

    g = Grid(grid=initial_grid)
    print(g)
    print()

    g[0][1] = 1
    print(g)
    print()

    g[1][0] = 2
    print(g)
    print()

    print(g[0][1])
    print(g[1][1])
    print(g.width)
    print(g.height)
    print()

    g = Grid(width=6, height=3)
    g[1][1] = 1
    print(g)
