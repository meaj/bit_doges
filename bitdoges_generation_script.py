# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 512x512 pixels after expansion from 24x24
dimensions = 512, 512

# open fh to generation_0_data.csv
doge_data_out = open(dirname + '\\doge_data\\generation_0_data.csv', "w")
doge_data_out.write("ID,Style,Eyes,Snoz,Foil,Wow,Coat,Undercoat\n")


# Generates and saves each doge image
def generate_doge(doge_type, doge_id, hd, th, ew, ep, nz, bg, ol):
    print("generating funny doge picture")
    if doge_type == 0:
        # Basic Doge image
        pixels = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, ol, bg, bg, bg, bg, bg, ol, th, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, th, ol, ol, ol, ol, ol, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ep, ep, ew, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ep, ep, ew, hd, hd, hd, ep, ep, ew, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ep, ep, ew, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, nz, nz, nz, hd, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, th, th, th, th, th, hd, hd, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, nz, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, nz, nz, nz, nz, nz, th, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
    elif doge_type == 1:
        # Cutie Doge image
        pixels = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, ol, bg, bg, bg, bg, bg, ol, th, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, th, ol, ol, ol, ol, ol, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ep, ew, ew, hd, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ep, ew, ew, hd, hd, ep, ep, ew, hd, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ep, ep, ew, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, nz, nz, nz, hd, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, th, th, th, th, th, hd, hd, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, nz, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, nz, th, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, nz, nz, nz, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
    elif doge_type == 2:
        # Angry Doge image
        pixels = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, ol, bg, bg, bg, bg, bg, ol, th, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, th, ol, ol, ol, ol, ol, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, hd, hd, ew, ew, ep, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ew, ew, ep, hd, hd, ew, ep, ep, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ew, ep, ep, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, nz, nz, nz, hd, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, th, th, th, th, th, hd, hd, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, nz, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, nz, th, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, nz, nz, nz, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, nz, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
    elif doge_type == 3:
        # Beanie Doge image
        pixels = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, ol, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, th, th, th, th, th, th, th, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg],
            [bg, bg, ol, hd, th, th, th, th, th, ol, ol, ol, ol, hd, hd, hd, hd, ew, ew, ew, hd, ol, bg, bg],
            [bg, bg, ol, th, th, th, th, ol, ol, hd, hd, ew, ew, ew, hd, hd, hd, ew, ep, ep, hd, ol, bg, bg],
            [bg, ol, th, th, th, ol, ol, hd, hd, hd, hd, ew, ep, ep, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg],
            [bg, ol, th, th, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, nz, nz, nz, hd, ol, bg],
            [bg, ol, th, ol, hd, hd, hd, hd, th, th, th, th, th, th, hd, hd, hd, hd, nz, nz, nz, th, ol, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, hd, hd, nz, nz, nz, th, ol, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, nz, th, th, ol, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, nz, nz, nz, th, th, th, ol, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, nz, nz, th, th, th, th, th, ol, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
    elif doge_type == 4:
        # Vizor Doge image
        gr = (100, 100, 100)
        pixels = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, ol, bg, bg, bg, bg, bg, ol, th, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, th, ol, ol, ol, ol, ol, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, hd, hd, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, gr, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, gr, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, gr, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, gr, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, nz, nz, nz, hd, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, th, th, th, th, th, hd, hd, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, nz, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, nz, nz, nz, th, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
    elif doge_type == 5:
        # Fedora doge image
        pixels = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, th, th, th, th, th, ol, bg, ol, ol, ol, ol, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, th, th, th, th, th, th, th, hd, ol, th, th, th, th, ol, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, th, th, th, th, th, hd, hd, hd, hd, ol, th, th, th, ol, bg],
            [bg, bg, bg, bg, bg, ol, th, th, th, th, hd, hd, hd, hd, hd, hd, th, th, th, th, th, ol, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, hd, hd, hd, hd, hd, hd, th, th, th, th, ol, ol, ol, bg, bg, bg],
            [bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, th, th, th, th, th, th, ol, ol, hd, ol, bg, bg, bg, bg],
            [bg, bg, ol, th, th, ol, hd, hd, th, th, th, ol, ol, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, ol, th, th, th, th, th, th, th, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, ol, th, th, th, th, th, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
            [bg, bg, ol, ol, ol, ol, ol, hd, hd, hd, ew, ep, ep, hd, hd, hd, ep, ep, ew, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, nz, nz, nz, hd, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, th, th, th, th, th, hd, hd, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, nz, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, nz, nz, nz, nz, nz, th, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]
    elif doge_type == 6:
        # Glasses doge image
        pixels = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, ol, bg, bg, bg, bg, bg, ol, th, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, th, th, th, ol, ol, ol, ol, ol, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, ep, hd, hd, hd, hd, ep, ew, ew, ep, hd, hd, ep, ew, ew, ep, ol, bg, bg, bg],
            [bg, bg, bg, ol, ep, hd, hd, hd, hd, hd, hd, ep, ep, hd, hd, hd, hd, ep, ep, hd, ol, bg, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, nz, nz, nz, hd, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, hd, th, th, th, th, th, hd, hd, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, hd, hd, nz, nz, nz, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, nz, nz, th, th, th, nz, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, nz, nz, nz, th, th, th, ol, bg, bg],
            [bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, hd, hd, hd, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/doge_images/' + (str(doge_id)) + '.png'
    new_image.save(imgname)


def generate_data(x):
    # this seed gives classic as #1
    s = 641616287
    seed(x+s)
    wow = 0

    # head color - randomly generate each number in an RGB color
    head_color = (randint(0, 256), randint(0, 256), randint(0, 256))
    c = randint(0, 500)
    seed(c)

    # throat color - same as head color
    throat_color = (randint(0, 256), randint(0, 256), randint(0, 256))
    d = randint(0, 1000)
    seed(d)

    # eye color
    # if random number between 1-1000 is 50 or less - gilded eyes
    if d > 100:
        # normal eyes are always the same color
        eye_white = (240, 248, 255)
        eye_pupil = (10, 10, 10)
        eyes = "normal"
    elif 100 >= d > 50:
        # silver eyes are always the same color
        eye_white = (240, 248, 255)
        eye_pupil = (152, 152, 152)
        eyes = "silvered"
        wow += 10
    else:
        # gilded eyes have the same golden pupil and a random 'eye white' color
        eye_white = (randint(0, 256), randint(0, 256), randint(0, 256))
        eye_pupil = (204, 172, 0)
        eyes = "gilded"
        wow += 15
    e = randint(0, 1000)
    seed(e)

    # nose color
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> black nose
        snoz_color = (0, 0, 0)
        snoz = "normal"
    elif 500 >= f > 50:
        # 48-500 >> silver nose
        snoz_color = (152, 152, 152)
        snoz = "silvered"
        wow += 10
    else:
        # random number is 50 or less >> gold nose
        snoz_color = (204, 172, 0)
        snoz = "gilded"
        wow += 15

    # background color
    if snoz == "gilded" or eyes == "gilded" or x == 1 or x == 13 or x == 69 or x == 420:
        foil = "holo"
        background = (204, 172, 0)
        wow += 10
    elif snoz == "silvered" or eyes == "silvered":
        foil = "silver"
        background = (162, 162, 162)
        wow += 5
    else:
        foil = "none"
        background = (242, 242, 242)

    # outline color
    outline = (0, 0, 0)

    # choose which doge image to use
    seed(f)
    g = randint(0, 1000)
    if g > 500:
        # if random number is 500 - 1000 >> basic
        generate_doge(0, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline)
        style = "basic"
        wow += 5
    elif 501 >= g > 250:
        # 501 - 250 cutie
        generate_doge(1, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline)
        style = "cutie"
        wow += 10
    elif 250 >= g > 100:
        # 101 - 250 >> angry
        generate_doge(2, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline)
        style = "angry"
        wow += 15
    elif 100 >= g > 50:
        # 51 - 100 >> beanie
        generate_doge(3, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline)
        style = "beanie"
        wow += 20
    elif 50 >= g > 25:
        # 50 - 25 >> vizor
        generate_doge(4, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline)
        style = "vizor"
        wow += 25
    elif 25 >= g > 5:
        # 6 - 25 >> fedora
        generate_doge(5, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline)
        style = "fedora"
        wow += 30
    else:
        # less than 5 >> glasses
        generate_doge(6, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline)
        style = "glasses"
        wow += 35

    # Write stats to output
    print("\nID: " + str(x) + "\nStyle: " + style + "\nFoil: " + foil + "\nEyes: " + eyes + "\nSnoz: "
          + snoz + "\nCoat: " + str(head_color) + "\nUndercoat: " + str(throat_color) + "\nTotal wow: " + str(wow))
    # Write Metadata to file
    doge_data_out.write(str(x) + "," + style + "," + eyes + "," + snoz + "," + foil
                        + "," + str(wow) + ",\"" + str(head_color) + "\",\"" + str(throat_color) + "\"\n")


if __name__ == '__main__':
    # Make negative gen doges
    # TODO: change ultra foil to have purple background
    generate_doge(6, -1, (247, 117, 256), (237, 191, 136), (204, 172, 0),
                  (219, 49, 190), (204, 172, 0), (204, 172, 0), (0, 0, 0))
    doge_data_out.write("-1,glasses,pink,gilded,ultra,420,\"(247, 117, 256)\",\"(237, 191, 136)\"\n")

    generate_doge(5, -2, (247, 117, 256), (237, 191, 136), (204, 172, 0),
                  (219, 49, 190), (204, 172, 0), (204, 172, 0), (0, 0, 0))
    doge_data_out.write("-2,fedora,pink,gilded,ultra,420,\"(247, 117, 256)\",\"(237, 191, 136)\"\n")

    generate_doge(4, -3, (247, 117, 256), (237, 191, 136), (204, 172, 0),
                  (219, 49, 190), (204, 172, 0), (204, 172, 0), (0, 0, 0))
    doge_data_out.write("-3,vizor,pink,gilded,ultra,420,\"(247, 117, 256)\",\"(237, 191, 136)\"\n")

    generate_doge(3, -4, (247, 117, 256), (237, 191, 136), (204, 172, 0),
                  (219, 49, 190), (204, 172, 0), (204, 172, 0), (0, 0, 0))
    doge_data_out.write("-4,beanie,pink,gilded,ultra,420,\"(247, 117, 256)\",\"(237, 191, 136)\"\n")

    generate_doge(2, -5, (247, 117, 256), (237, 191, 136), (204, 172, 0),
                  (219, 49, 190), (204, 172, 0), (204, 172, 0), (0, 0, 0))
    doge_data_out.write("-5,angry,pink,gilded,ultra,420,\"(247, 117, 256)\",\"(237, 191, 136)\"\n")

    generate_doge(1, -6, (247, 117, 256), (237, 191, 136), (204, 172, 0),
                  (219, 49, 190), (204, 172, 0), (204, 172, 0), (0, 0, 0))
    doge_data_out.write("-6,cutie,pink,gilded,ultra,420,\"(247, 117, 256)\",\"(237, 191, 136)\"\n")

    generate_doge(0, -7, (247, 117, 256), (237, 191, 136), (204, 172, 0),
                  (219, 49, 190), (204, 172, 0), (204, 172, 0), (0, 0, 0))
    doge_data_out.write("-7,normal,pink,gilded,ultra,420,\"(247, 117, 256)\",\"(237, 191, 136)\"\n")

    # Generation 1 Doge Generation
    # Generate 419 doges starting from 1
    for entry in range(1, 420):
        generate_data(entry)
    # TODO: Generate doge 420 which has gilded nose and eyes and glasses but random colors with ultra background

    doge_data_out.close()
