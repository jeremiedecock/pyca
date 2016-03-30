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

import json
import os.path

import tkinter as tk
import tkinter.filedialog

class TkGUI:
    """
    TODO...
    """

    def __init__(self):
        """
        TODO...
        """

        # GUI parameters ##############

        self.time_step = 500               # in ms
        self.cell_size = 8                 # in pixels
        self.cell_margin = 1               # in pixels
        self.cell_alive_color = "black"
        self.cell_dead_color = "white"
        self.background_color = "white"   # canvas background color
        self.export_canvas = False

        # Make widgets ################

        self.root = tk.Tk()   # TODO

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(padx=5, pady=5)

        # Make a menubar ##############

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # Create a pulldown menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open...", command=self.select_state_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        menubar.add_cascade(label="File", menu=file_menu)

#        # Create a pulldown menu
#        help_menu = tk.Menu(menubar, tearoff=0)
#        help_menu.add_command(label="About...", command=callback)
#
#        menubar.add_cascade(label="Help", menu=help_menu)

        # Display the menu
        # The config method is used to attach the menu to the root window. The
        # contents of that menu is used to create a menubar at the top of the root
        # window. There is no need to pack the menu, since it is automatically
        # displayed by Tkinter.
        self.root.config(menu=menubar)

        # Make rules ##################

        self.rules = Rules()   # TODO should be parametrized with args to choose the rule

        # Set the initial state #######

        self.current_state = None
        self.next_alarm_id = None

    def run(self):
        # Tk event loop
        # TODO ???
        self.root.mainloop()

    def update_state(self):
        """
        TODO...
        """

        self.current_state = self.rules.next_state(self.current_state)

        self.draw_current_state()

        # Set the next alarm
        self.next_alarm_id = self.canvas.after(self.time_step, self.update_state)

    def draw_current_state(self):
        """
        TODO...
        """

        # Update self.canvas
        for idx in range(self.current_state.width):
            for idy in range(self.current_state.height):
                cell_state = self.current_state[idy][idx]

                if cell_state == 0:
                    cell_color = self.cell_dead_color
                else:
                    cell_color = self.cell_alive_color

                cell_tag = "({},{})".format(idx, idy)

                self.canvas.itemconfig(cell_tag, fill=cell_color)

    def start(self, initial_state):
        """
        TODO...
        """

        # Clear the canvas (remove all shapes)
        self.canvas.delete(tk.ALL)

        # Remove the next alarm
        if self.next_alarm_id is not None:
            self.canvas.after_cancel(self.next_alarm_id)
            self.next_alarm_id = None

        # Reset the canvas (dimensions and number of cells)
        self.canvas.config(width=initial_state.width * self.cell_size,
                           height=initial_state.height * self.cell_size)

        for idx in range(initial_state.width):
            for idy in range(initial_state.height):
                tags = ("cell", "({},{})".format(idx, idy))

                self.canvas.create_rectangle(self.cell_size * idx,       # x1
                                             self.cell_size * idy,       # y1
                                             self.cell_size * (idx + 1), # x2
                                             self.cell_size * (idy + 1), # y2
                                             tag=tags,
                                             outline=self.background_color,
                                             width=self.cell_margin)

        # Update the current state
        self.current_state = initial_state

        # Draw the canvas
        self.draw_current_state()

        # Set the next alarm
        self.next_alarm_id = self.canvas.after(self.time_step, self.update_state)

    def select_state_file(self):
        """
        TODO...
        """

        # Check and parse the file

        # FILE_TYPES = [(label1, pattern1), (label2, pattern2), ...]
        FILE_TYPES = [
                    ('JSON Files', '.json'),
                    ('All Files', '.*')
                ]

        HOME = os.path.expanduser("~")

        path = tk.filedialog.askopenfilename(parent=self.root,
                                             filetypes=FILE_TYPES,     # optional
                                             defaultextension='.json', # optional
                                             initialdir=HOME,          # optional
                                             #initialfile='demo.json',  # optional
                                             title='Select your file') # optional

        self.open_state_file(path)

    def open_state_file(self, file_path):
        """
        TODO...
        """

        # Check and parse the file
        # TODO: check the file
        with open(file_path, "r") as fd:
            json_dict = json.load(fd)

        initial_state_list = json_dict["initial_state"]
        initial_state = Grid(grid=initial_state_list)

        self.start(initial_state)

if __name__ == '__main__':
    gui = TkGUI()

    # Default initial state
    initial_state = Grid(width=32, height=32)
    initial_state[0][1] = 1
    initial_state[1][1] = 1
    initial_state[2][1] = 1

    initial_state[10][1] = 1
    initial_state[11][1] = 1
    initial_state[12][1] = 1

    initial_state[0][11] = 1
    initial_state[1][11] = 1
    initial_state[2][11] = 1
    gui.start(initial_state)

    # Launch the main loop
    gui.run()
