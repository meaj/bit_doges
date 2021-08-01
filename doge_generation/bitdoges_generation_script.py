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
from random import seed, randint, shuffle

# used to get a birthdate timestamp
import time

import json_template
import json

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 512x512 pixels after expansion from 24x24
dimensions = 512, 512

# read in the names of all the doges
doge_names_in = open(dirname + "\\config\\names.txt", "r")
names = doge_names_in.read().splitlines()

# Array of 69 (nice) colors that are used to create the doges
color_array = [(139, 0, 0), (178, 34, 34), (255, 0, 0), (255, 127, 80), (205, 92, 92), (233, 150, 122), (250, 128, 114),
               (255, 69, 0), (255, 165, 0), (255, 215, 0), (240, 230, 140), (128, 128, 0), (255, 255, 0),
               (154, 205, 50), (85, 107, 47), (107, 142, 35), (127, 255, 0), (173, 255, 47), (0, 100, 0), (34, 139, 34),
               (0, 255, 0), (50, 205, 50), (152, 251, 152), (0, 255, 127), (46, 139, 87), (60, 179, 113),
               (32, 178, 170), (0, 139, 139), (0, 255, 255), (0, 206, 209), (127, 255, 212), (95, 158, 160),
               (70, 130, 180), (100, 149, 237), (0, 191, 255), (30, 144, 255), (135, 206, 250), (0, 0, 205),
               (0, 0, 255), (65, 105, 225), (138, 43, 226), (75, 0, 130), (123, 104, 238), (148, 0, 211),
               (186, 85, 211), (221, 160, 221), (238, 130, 238), (255, 0, 255), (218, 112, 214), (219, 112, 147),
               (255, 105, 180), (255, 192, 203), (250, 235, 215), (255, 228, 196), (139, 69, 19), (160, 82, 45),
               (210, 105, 30), (205, 133, 63), (244, 164, 96), (255, 228, 181), (237,  191,  136), (245, 255, 250),
               (119, 136, 153), (240, 255, 240), (255, 255, 240), (240, 255, 255), (255, 250, 250), (128, 128, 128)]
# Arrays used to ensure unique doge colors are chosen
head_pool = color_array.copy()
throat_pool = color_array.copy()
used_colors = []
eye_pool = color_array.copy()


def generate_metadata (doge_id, doge_type, name, eye_type, snoz_type, foil_type, gen, wow_value, bd_time, addr):
    doge_metadata = json_template.doge_metadata_template
    metadata_out = dirname + '\\doge_data\\doge_json\\' + doge_id + '.json'
    print("Generating metadata for funny doge picture")
    doge_metadata["name"] = name
    doge_metadata["external_url"] = "https:\\\\bitdoges.com\\" + str(doge_id)
    doge_metadata["image"] = dirname + "\\doge_data\\doge_images\\" + doge_id + ".png"
    doge_metadata["attributes"] = [
        {"trait_type": "Type", "value": doge_type},
        {"trait_type": "Eyes", "value": eye_type},
        {"trait_type": "Snoz", "value": snoz_type},
        {"trait_type": "Foil", "value": foil_type},
        {"display_type": "number", "trait_type": "Generaton", "value": gen},
        {"display_type": "number", "trait_type": "WOW", "value": wow_value},
        {"display_type": "date", "trait_type": "birthday", "value": bd_time},
        {"display_type": "string", "trait_type:": "Minter Doge Address", "value": addr}
    ]
    with open(metadata_out, "w") as file:
        json.dump(doge_metadata, file)


# Generates and saves each doge image
def generate_doge(doge_type, doge_id, hd, th, ew, ep, nz, bg, ol, name):
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
        gr = (105, 105, 105)
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
            [bg, bg, bg, bg, ol, hd, hd, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ep, ol, bg, bg, bg],
            [bg, bg, bg, bg, ol, hd, ep, hd, hd, hd, ep, ew, ew, ep, hd, hd, ep, ew, ew, ep, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, ep, hd, hd, hd, hd, hd, ep, ep, hd, hd, hd, hd, ep, ep, hd, ol, bg, bg, bg],
            [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
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
    imgname = dirname + '/doge_data/doge_images/' + (str(doge_id)) + '.png'
    new_image.save(imgname)


def generate_data(x, name, gen):
    # this seed gives classic as #1
    s = 641616287
    seed(x+s)
    wow = 0

    # Shuffle head color pool and reseed function
    shuffle(head_pool)
    c = randint(0, 500)
    seed(c)

    # Shuffle head color pool and reseed function
    shuffle(throat_pool)
    d = randint(0, 1000)
    seed(d)

    # loop through different color combinations until we get a unique one
    # should allow for only unique color combinations though efficiency is not great
    cont = True
    while cont:
        shuffle(head_pool)
        shuffle(throat_pool)
        head_color = head_pool[-1]
        throat_color = throat_pool[-1]
        color_choice = [head_color, throat_color]
        if color_choice not in used_colors and head_color != throat_color:
            cont = False

    # add the chosen color to the pool of used colors
    used_colors.append(color_choice)

    # eye color
    # if random number between 1-1000 is 50 or less - gilded eyes
    if d > 333:
        # normal eyes are always the same color
        eye_white = (240, 248, 255)
        eye_pupil = (0, 0, 0)
        eyes = "normal"
    elif 333 >= d > 84:
        # silver eyes are always the same color
        eye_white = (240, 248, 255)
        eye_pupil = (192, 192, 192)
        eyes = "silvered"
        wow += 10
    else:
        # gilded eyes have the same golden pupil and a random 'eye white' color that must be different from the head
        eye_white = None
        while not eye_white:
            shuffle(eye_pool)
            if eye_pool[-1] != head_color:
                eye_white = eye_pool[-1]
        print(str(eye_white))
        eye_pupil = (184, 134, 11)
        eyes = "gilded"
        wow += 15

    e = randint(0, 1000)
    seed(e)

    # nose color
    f = randint(0, 1000)
    if f > 333:
        # if random number is 501-1000 >> black nose
        snoz_color = (0, 0, 0)
        snoz = "normal"
    elif 333 >= f > 84:
        # 48-500 >> silver nose
        snoz_color = (192, 192, 192)
        snoz = "silvered"
        wow += 10
    else:
        # random number is 50 or less >> gold nose
        snoz_color = (184, 134, 11)
        snoz = "gilded"
        wow += 15

    # background color
    if snoz == "gilded" or eyes == "gilded" or x == 1 or x == 13 or x == 69 or x == 420:
        foil = "holo"
        background = (184, 134, 11)
        wow += 10
    elif snoz == "silvered" or eyes == "silvered":
        foil = "silver"
        background = (192, 192, 192)
        wow += 5
    else:
        foil = "none"
        background = (245, 245, 245)

    # outline color
    outline = (0, 0, 0)

    # choose which doge image to use
    seed(f)
    g = randint(0, 1000)
    if g > 500:
        # if random number is 500 - 1000 >> basic
        doge_style = 0
        style = "normal"
        wow += 5
    elif 500 >= g > 250:
        # 501 - 250 cutie
        doge_style = 1
        style = "cutie"
        wow += 10
    elif 250 >= g > 100:
        # 101 - 250 >> angry
        doge_style = 2
        style = "angry"
        wow += 15
    elif 100 >= g > 50:
        # 51 - 100 >> beanie
        doge_style = 3
        style = "beanie"
        wow += 20
    elif 50 >= g > 25:
        # 50 - 25 >> vizor
        doge_style = 4
        style = "vizor"
        wow += 25
    elif 25 >= g > 5:
        # 6 - 25 >> fedora
        doge_style = 5
        style = "fedora"
        wow += 30
    else:
        # less than 5 >> glasses
        doge_style = 6
        style = "glasses"
        wow += 35

    # forge the doge
    generate_doge(doge_style, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline, name)

    # Write stats to output
    print("\nID: " + str(x) + "\nStyle: " + style + "\nFoil: " + foil + "\nEyes: " + eyes + "\nSnoz: "
          + snoz + "\nCoat: " + str(head_color) + "\nUndercoat: " + str(throat_color) + "\nTotal wow: " + str(wow))
    # Write Metadata to file
    generate_metadata(str(x), style, name, eyes, snoz, foil, gen, str(wow), str(int(time.time())), "")


def doge_factory(token_id, generation):
    name = names[token_id]
    if token_id == 0:
        generate_doge(6, 0, (247, 117, 256), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (0, 0, 0), name)
        generate_metadata("0", "glasses", name, "pink", "gilded", "ultra", str(generation), "420", str(int(time.time())), "")
    elif token_id == 1:
        generate_doge(5, 1, (247, 117, 256), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (0, 0, 0), name)
        generate_metadata("1", "fedora", name, "pink", "gilded", "ultra", str(generation), "420", str(int(time.time())), "")
    elif token_id == 2:
        generate_doge(4, 2, (247, 117, 256), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (0, 0, 0), name)
        generate_metadata("2", "vizor", name, "pink", "gilded", "ultra", str(generation), "420", str(int(time.time())), "")
    elif token_id == 3:
        generate_doge(3, 3, (247, 117, 256), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (0, 0, 0), name)
        generate_metadata("3", "beanie", name, "pink", "gilded", "ultra", str(generation), "420", str(int(time.time())), "")
    elif token_id == 4:
        generate_doge(2, 4, (247, 117, 256), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (0, 0, 0), name)
        generate_metadata("4", "angry", name, "pink", "gilded", "ultra", str(generation), "420", str(int(time.time())), "")
    elif token_id == 5:
        generate_doge(1, 5, (247, 117, 256), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (0, 0, 0), name)
        generate_metadata("5", "cutie", name, "pink", "gilded", "ultra", str(generation), "420", str(int(time.time())), "")
    elif token_id == 6:
        generate_doge(0, 6, (247, 117, 256), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (0, 0, 0), name)
        generate_metadata("6", "normal", name, "pink", "gilded", "ultra", str(generation), "420", str(int(time.time())), "")
    elif token_id == 7:
        generate_doge(0, 7, (247, 117, 256), (237, 191, 136), (240, 248, 255),
                      (0, 0, 0), (0, 0, 0), (128, 0, 128), (0, 0, 0), name)
        generate_metadata("7", "normal", name, "normal", "normal", "ultra", str(generation), "420", str(int(time.time())), "")
    elif token_id == 420:
        generate_doge(6, 420, (45, 232, 6), (111, 160, 140), (128, 0, 128), (184, 134, 11), (184, 134, 11),
                      (128, 0, 128), (0, 0, 0), name)
        generate_metadata("420", "glasses", name, "gilded", "gilded", "ultra", str(generation), "420", str(int(time.time())), "")
    else:
        generate_data(token_id, name, str(generation))


if __name__ == '__main__':
    # Generation 1 Doge Generation
    # Generate 500 doges starting from 0
    for entry in range(0, 500):
        doge_factory(entry, 1)

    doge_names_in.close()