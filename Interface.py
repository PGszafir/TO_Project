import sys
import os
from dearpygui.core import *
from dearpygui.simple import *
import matplotlib.pyplot as plt
from mesh import *
#import matplotlib as plt
from operations import *
from draw3d import *

class Interface:

    def __init__(self):
        set_theme('Red')
        set_global_font_scale(1.25)
        set_main_window_size(1000, 600)
        self.nop = 10
        self.figure = 0
        self.r = 1

    def setup_(self):
        with window("Main"):
            tab = ['cube', '45 degrre rotated cube', 'sphere']
            add_text(
                "Aplikacja Symulujaca kolizje czasteczek z brylami 3D wedlug przyblizonych zasad dynamiki Newtona",
                bullet=True)
            add_separator()


            add_listbox(name="Chose_3d_solid", items=tab, num_items=5)
            add_input_int('chose_number_of_particles_per_iteration')
            add_input_float('enter_r')
            values = add_button('zatwierdz', callback=self.run_symulation)


    def run(self):
        values = start_dearpygui(primary_window="Main")

    def run_symulation(self):
        with window("Start"):
            tab = ['cube', '45 degrre rotated cube', 'sphere']
            i = get_value('chose_number_of_particles_per_iteration')
            type = get_value('Chose_3d_solid')
            r = get_value('enter_r')

            add_text('strat configuration:')
            add_separator()
            string = str('type of component: ' + str(tab[type]))
            add_text(string)
            add_text('number of particles: '+str(i))
            add_text('scale :'+str(r))

            self.nop = int(i)
            self.figure = int(type)
            self.r = float(r)

    def get_values(self):
        return self.nop,self.r,self.figure