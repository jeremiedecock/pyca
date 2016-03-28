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

        # Make widgets
        # TODO make the window, the canvas, btn open state files and others widgets...

        # GUI parameters
        self.time_step = 500               # in ms
        self.cell_size = 5                 # in pixels
        self.cell_margin = 1               # in pixels
        self.cell_color = "black"
        self.cell_margin_color = "white"   # canvas background color
        self.export_canvas = False

        # Make rules
        self.rules = Rules()   # TODO should be parametrized with args to choose the rule

        # Set the initial state
        self.current_state = None

        # Tk event loop (TODO or move it outside the constructor ???)
        self.root.mainloop()

    def update_state(self):
        self.current_state = self.rules.next_state(self.current_state)

        self.draw_current_state()

        # Set the next alarm
        self.canvas.after(self.timestep, self.update_state)

    def draw_current_state(self):
        # TODO update self.canvas...

    def start(self, initial_state):
        # Reset the canvas: dimensions, num squares, ...
        # TODO

        self.current_state = initial_state
        self.draw_current_state()

        # Set the next alarm
        self.canvas.after(self.timestep, self.update_state)

    def open_state_file(self, file_path):
        # Check and parse the file
        # TODO

        self.start(initial_state)

def run():
    gui = TkGUI()

if __name__ == '__main__':
    main()

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
