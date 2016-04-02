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

__all__ = ['Rules']

from ca.grid.grid2d import Grid

class Rules:
    def __init__(self):
        pass

    def next_state(self, current_state):
        # Init the next state
        next_state = Grid(width=current_state.width, height=current_state.height)

        for idx in range(current_state.width):
            for idy in range(current_state.height):
                num_live_neighbors = sum(self.get_neighbors(current_state, idx, idy))

                # Game of life rules (https://en.wikipedia.org/wiki/Conway's_Game_of_Life):
                # - Any live cell with fewer than two live neighbours dies, as if caused by under-population.
                # - Any live cell with two or three live neighbours lives on to the next generation.
                # - Any live cell with more than three live neighbours dies, as if by over-population.
                # - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if (current_state[idy][idx] == 0) and (num_live_neighbors == 3):
                    next_state[idy][idx] = 1
                elif (current_state[idy][idx] == 1) and (2 <= num_live_neighbors <= 3):
                    next_state[idy][idx] = 1

        return next_state

    def get_neighbors(self, grid, x, y):
        neighbors = []

        # The left cell
        if x != 0:
            neighbors.append(grid[y][x-1])

        # The right cell
        if x != grid.width-1:
            neighbors.append(grid[y][x+1])

        # The top cell
        if y != 0:
            neighbors.append(grid[y-1][x])

        # The bottom cell
        if y != grid.height-1:
            neighbors.append(grid[y+1][x])

        # The top left cell
        if x != 0 and y != 0:
            neighbors.append(grid[y-1][x-1])

        # The top right cell
        if x != grid.width-1 and y != 0:
            neighbors.append(grid[y-1][x+1])

        # The bottom left cell
        if x != 0 and y != grid.height-1:
            neighbors.append(grid[y+1][x-1])

        # The bottom right cell
        if x != grid.width-1 and y != grid.height-1:
            neighbors.append(grid[y+1][x+1])

        return neighbors



if __name__ == '__main__':

    rules = Rules()

    # Init the grid
    state = Grid(width=3, height=3)
    state[0][1] = 1
    state[1][1] = 1
    state[2][1] = 1
    print(state)
    print()

    state = rules.next_state(state)
    print(state)
    print()

    state = rules.next_state(state)
    print(state)
    print()

