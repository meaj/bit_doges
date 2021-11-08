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

from doge_generation import json_template, convert
import json

import base64

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 512x512 pixels after expansion from 24x24
#dimensions = 512, 512
dimensions = 24, 24

# read in the names of all the doges
doge_names_in = open(dirname + "/config/names.txt", "r")
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


def get_doge_data(doge_id):
    doge_data_in = dirname + "/doge_data/" + str(doge_id)
    if os.path.isdir(doge_data_in):
        doge_gif = [file for file in os.listdir(doge_data_in) if file.endswith('.gif')][0]
        json_file = [file for file in os.listdir(doge_data_in) if file.endswith('.json')][0]
        df = open(doge_data_in + "/" + json_file, 'r')
        doge_json = json.load(df)
        df.close()
        if doge_gif and doge_json:
            return doge_json, str(doge_data_in + "/" + doge_gif)

    return False, False


def generate_metadata (doge_id, doge_type, name, eye_type, snoz_type, foil_type, wow_value, bd_time, addr, b64_doge):
    doge_metadata = json_template.doge_metadata_template
    metadata_out = dirname + "/doge_data/" + str(doge_id) + "/" + name + '.json'
    print("Generating metadata for funny doge picture")
    doge_metadata["name"] = name
    doge_metadata["external_url"] = "https://bitdoges.com/bitdoge?id=" + str(doge_id)
    doge_metadata["image_data"] = "data:image/svg+xml;base64," + str(b64_doge, 'utf-8')
    doge_metadata["attributes"] = [
        {"trait_type": "Type", "value": doge_type},
        {"trait_type": "Eyes", "value": eye_type},
        {"trait_type": "Snoz", "value": snoz_type},
        {"trait_type": "Foil", "value": foil_type},
        {"display_type": "number", "trait_type": "WOW", "value": wow_value},
        {"display_type": "date", "trait_type": "birthday", "value": bd_time},
        {"display_type": "string", "trait_type:": "Minter Doge Address", "value": addr}
    ]
    with open(metadata_out, "w") as file:
        json.dump(doge_metadata, file)

    return doge_metadata


# Generates and saves each doge image
def generate_bitdoge(doge_type, doge_id, hd, th, ew, ep, nz, bg, ol, name):
    print("generating funny doge picture")
    convert.convert_frames(doge_type, doge_id, hd, th, ew, ep, nz, bg, ol, name)
    with open(dirname + "/doge_data/" + str(doge_id) + "/" + name + ".svg", "rb") as svg_bytes:
        base64_svg = base64.b64encode(svg_bytes.read())
    return base64_svg


def generate_data(x, name, addr):
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
        eye_pupil = (1, 1, 1)
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
        snoz_color = (1, 1, 1)
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
    outline = (1, 1, 1)

    # choose which doge image to use
    seed(f)
    g = randint(0, 1000)
    if g > 500:
        # if random number is 500 - 1000 >> basic
        doge_style = 6
        style = "normal"
        wow += 5
    elif 600 >= g > 300:
        # 501 - 250 cutie
        doge_style = 5
        style = "cutie"
        wow += 10
    elif 300 >= g > 150:
        # 101 - 250 >> angry
        doge_style = 4
        style = "angry"
        wow += 15
    elif 150 >= g > 75:
        # 51 - 100 >> beanie
        doge_style = 3
        style = "beanie"
        wow += 20
    elif 75 >= g > 50:
        # 50 - 25 >> vizor
        doge_style = 2
        style = "vizor"
        wow += 25
    elif 50 >= g > 30:
        # 6 - 25 >> fedora
        doge_style = 1
        style = "fedora"
        wow += 30
    elif 30 >= g > 15:
        # less than 5 >> glasses
        doge_style = 0
        style = "glasses"
        wow += 35
    elif 15 >= g > 5:
        doge_style = 7
        style = "bork"
        wow += 40
    elif 5 >= g > 2:
        doge_style = 8
        style = "doc"
        wow += 45
    else:
        doge_style = 9
        style = "moon"
        wow += 50

    # Write stats to output
    print("\nID: " + str(x) + "\nStyle: " + style + "\nFoil: " + foil + "\nEyes: " + eyes + "\nSnoz: "
          + snoz + "\nCoat: " + str(head_color) + "\nUndercoat: " + str(throat_color) + "\nTotal wow: " + str(wow))
    # forge the doge
    b64_doge = generate_bitdoge(doge_style, x, head_color, throat_color, eye_white, eye_pupil, snoz_color, background, outline, name)

    # Write Metadata to file and get JSON to return
    doge_json = generate_metadata(str(x), style, name, eyes, snoz, foil, str(wow), str(int(time.time())), addr, b64_doge)

    return doge_json


def generate_preset_doge(token_id):
    name = names[token_id-1]
    t_addr = "DEBA4cGspNuT6paX4kzSrNduttLcMrau5Z"
    if token_id == 1:
        b64_doge = generate_bitdoge(0, 1, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("1", "glasses", name, "pink", "gilded", "ultra", "420", str(int(time.time())), "DEBA4cGspNuT6paX4kzSrNduttLcMrau5Z", b64_doge)
    elif token_id == 2:
        b64_doge = generate_bitdoge(1, 2, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("2", "fedora", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    elif token_id == 3:
        b64_doge = generate_bitdoge(2, 3, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("3", "vizor", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    elif token_id == 4:
        b64_doge = generate_bitdoge(3, 4, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("4", "beanie", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    elif token_id == 5:
        b64_doge = generate_bitdoge(4, 5, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("5", "angry", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    elif token_id == 6:
        b64_doge = generate_bitdoge(5, 6, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("6", "cutie", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    elif token_id == 7:
        b64_doge = generate_bitdoge(6, 7, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("7", "normal", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)    
    elif token_id == 8:
        b64_doge = generate_bitdoge(7, 8, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("8", "bork", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    elif token_id == 9:
        b64_doge = generate_bitdoge(8, 9, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("9", "doc", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    elif token_id == 10:
        b64_doge = generate_bitdoge(9, 10, (247, 117, 0), (237, 191, 136), (184, 134, 11),
                      (255, 20, 147), (184, 134, 11), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("10", "normal", name, "pink", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    elif token_id == 11:
        b64_doge = generate_bitdoge(6, 11, (247, 117, 0), (237, 191, 136), (240, 248, 255),
                      (1, 1, 1), (1, 1, 1), (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("11", "normal", name, "normal", "normal", "ultra", "420", str(int(time.time())), "DFGV8dmBfbkbJw2xEfnSK2qpNGyr4sMn97", b64_doge)
    elif token_id == 420:
        b64_doge = generate_bitdoge(0, 420, (45, 232, 6), (111, 160, 140), (128, 0, 128), (184, 134, 11), (184, 134, 11),
                      (128, 0, 128), (1, 1, 1), name)
        doge_json = generate_metadata("420", "glasses", name, "gilded", "gilded", "ultra", "420", str(int(time.time())), t_addr, b64_doge)
    return doge_json


def doge_factory(token_id, addr):
    name = names[token_id-1]
    if token_id < 12 or token_id == 420:
        print("Special Doge minted, passed in address ignored!")
        doge_json = generate_preset_doge(token_id)
    else:
        doge_json = generate_data(token_id, name, addr)
    return doge_json


if __name__ == '__main__':
    # Generate 1000 doges starting from 1
    for entry in range(1, 1001):
        dat = doge_factory(entry, "DEBA4cGspNuT6paX4kzSrNduttLcMrau5Z")

    doge_names_in.close()
