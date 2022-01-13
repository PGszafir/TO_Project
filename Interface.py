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
        with window("Main"):
            tab = ['cube','45 degrre rotated cube', 'sphere']
            add_text(
                "Aplikacja Symulujaca kolizje czasteczek z brylami 3D wedlug przyblizonych zasad dynamiki Newtona",
                bullet=True)
            add_separator()


            add_listbox(name="Chose_3d_solid", items=tab, num_items=5)
            add_input_int('chose_number_of_particles_per_iteration')
            #add_input_text("Haslo##inputtext", password=True)
            add_button('zatwierdz', callback=self.run_symulation)


    def run(self):
        start_dearpygui(primary_window="Main")

    def run_symulation(self):
        with window("Start"):
            add_text('strat configuration:')
            #add_text(get_value('chose_number_of_particles_per_iteration'))

        vector0 = Vector([0, 0, 0])
        vector1 = Vector([0, 0, 0])







