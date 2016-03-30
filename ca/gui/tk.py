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

__all__ = ['TkGUI']

from ca.rules.conway import Rules
from ca.grid.grid2d import Grid

import tkinter as tk

class TkGUI:
    def __init__(self):
        # GUI parameters ##############
        self.time_step = 500               # in ms
        self.cell_size = 5                 # in pixels
        self.cell_margin = 0               # in pixels
        self.cell_alive_color = "black"
        self.cell_dead_color = "white"
        self.background_color = "white"   # canvas background color
        self.export_canvas = False

        # Make widgets ################
        self.root = tk.Tk()   # TODO

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(padx=10, pady=10)

        # TODO btn open state files and others widgets...

        # Make rules ##################
        self.rules = Rules()   # TODO should be parametrized with args to choose the rule

        # Set the initial state #######
        self.current_state = None

        # Tk event loop ###############
        # TODO or move it outside the constructor ???)
        self.root.mainloop()

    def update_state(self):
        self.current_state = self.rules.next_state(self.current_state)

        self.draw_current_state()

        # Set the next alarm
        self.canvas.after(self.timestep, self.update_state)

    def draw_current_state(self):
        # Update self.canvas
        for idx in range(self.current_state.width):
            for idy in range(self.current_state.height):
                cell_state = self.current_state[idy][idx]

                if cell_state == 0:
                    cell_color = self.cell_dead_color
                else:
                    cell_color = self.cell_alive_color

                cell_tag = "{}x{}".format(idx, idy)

                canvas.itemconfig(cell_tag, fill=color)

    def start(self, initial_state):
        # Reset the canvas (dimensions and number of cells)
        self.canvas.config(width=initial_state.width * self.cell_size,
                           height=initial_state.height * self.cell_size)

        for idx in range(initial_state.width):
            for idy in range(initial_state.height):
                tags = ("cell", "{}x{}".format(idx, idy))

                canvas.create_rectangle(self.cell_size * idx,       # x1
                                        self.cell_size * idy,       # y1
                                        self.cell_size * (idx + 1), # x2
                                        self.cell_size * (idy + 1), # y2
                                        tag=tags,
                                        width=self.cell_margin)

        # Update the current state
        self.current_state = initial_state

        # Draw the canvas
        self.draw_current_state()

        # Set the next alarm
        self.canvas.after(self.timestep, self.update_state)

    def open_state_file(self, file_path):
        # Check and parse the file
        # TODO

        self.start(initial_state)

if __name__ == '__main__':
    gui = TkGUI()

    initial_state = Grid(width=3, height=3)
    initial_state[0][1] = 1
    initial_state[1][1] = 1
    initial_state[2][1] = 1
    #gui.start(initial_state)

# Ce module utilise les fonctions "métier" suivantes
# - ca.get_initial_state()
#   appelé à l'initialisation de la gui, notement pour définir la taille de la grille et le nombre de cellule
# - ca.next_state(current_state)

# ou mieux (?): "ca" devient "rules" et l'état initial est géré par la gui (ie supprime ca.get_initial_state)

# L'objet "state" échangé avec la classe métier n'est qu'un nested tuple (ou liste ?) (à 2 dimensions) contenant des 0 et des 1 => pas besoin d'installer numpy
# ou mieux (?)https://docs.python.org/3/library/array.html

# Paramètres de la GUI:
# - taille en pixel des cellules
# - valeur du timestep en ms
# - export vers des fichiers PS ?
# - classe "métier"

# L'état initial (et les règles ?) sont écrites dans un fichier JSON, choisi avec argparse ou via la GUI et passé au constructeur de la classe métier
