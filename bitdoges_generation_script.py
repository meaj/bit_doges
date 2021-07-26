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

# open fh to metadatacsv
doge_data_out = open(dirname + '\doge_data\generation_0_data.csv', "w")
doge_data_out.write("ID,Style,Eyes,Snoz,Foil,Wow,Coat,Undercoat\n")

# Generation 1 Doge Generation
# Generate 520 doges starting from -99
# Doges -99 to 0 are for testing
for x in range(-99, 421):

    # this seed gives classic as #1
    b = 641616287
    seed(x+b)
    wow = 0

    # head color - randomly generate each number in an RGB color
    hd = (randint(0, 256), randint(0, 256), randint(0, 256))
    c = randint(0, 500)
    seed(c)

    # throat color - same as head color
    th = (randint(0, 256), randint(0, 256), randint(0, 256))
    d = randint(0, 1000)
    seed(d)

    # eye "white" color
    # if random number between 1-1000 is 47 or less - gilded eyes
    if d > 47:
        # normal eyes are always the same color
        ew = (240, 248, 255)
        ep = (10, 10, 10)
        eyes = "normal"
    else:
        # gilded eyes have the same golden pupil and a random 'eye white' color
        ew = (randint(0, 256), randint(0, 256), randint(0, 256))
        ep = (204, 172, 0)
        eyes = "gilded"
        wow += 15
    e = randint(0, 1000)
    seed(e)

    # nose color
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> black nose
        nz = (0, 0, 0)
        snoz = "normal"
    elif 500 >= f > 47:
        # 48-500 >> silver nose
        nz = (152, 152, 152)
        snoz = "silvered"
        wow += 5
    elif 47 >= f > 7:
        # 8 >> 47 >> red nose
        nz = (204, 0, 0)
        snoz = "shiny"
        wow += 10
    else:
        # random number is 7 or less >> gold nose
        nz = (204, 172, 0)
        snoz = "gilded"
        wow += 15

    # background color
    if snoz == "gilded" or eyes == "gilded" or x == 1 or x == 13 or x == 69 or x == 420:
        foil = "holo"
        bg = (204, 172, 0)
        wow += 15
    elif snoz == "shiny":
        foil = "pink"
        bg = (219, 49, 190)
        wow += 10
    elif snoz == "silvered":
        foil = "silver"
        bg = (162, 162, 162)
        wow += 5
    else:
        foil = "none"
        bg = (242, 242, 242)

    # outline color
    ol = (0, 0, 0)

    # Define each style with the determined colors
    basic_doge = [
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

    disappoint_doge = [
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

    angry_doge = [
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

    glasses_doge = [
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

    # choose which doge image to use
    seed(f)
    g = randint(0, 1000)
    if g > 250:
        # if random number is 251 - 1000 >> basic
        pixels = basic_doge
        style = "basic"
        wow += 5
    elif 250 >= g > 100:
        # 101 - 250 >> disappoint
        pixels = disappoint_doge
        style = "disappoint"
        wow += 10
    elif 100 >= g > 40:
        # 41 - 100 >> angry
        pixels = angry_doge
        style = "angry"
        wow += 15
    else:
        # 1 - 40 >> glasses
        pixels = glasses_doge
        style = "glasses"
        wow += 20

    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/doge_images/' + (str(x)) + '.png'
    new_image.save(imgname)
    print("\nID: " + str(x) + "\nStyle: " + style + "\nFoil: " + foil + "\nEyes: " + eyes + "\nSnoz: "
          + snoz + "\nCoat: " + str(hd) + "\nUndercoat: " + str(th) + "\nTotal wow: " + str(wow))
    doge_data_out.write(str(x) + "," + style + "," + eyes + "," + snoz + "," + foil
                        + "," + str(wow) + "," + str(hd) + "," + str(th) + "\n")

doge_data_out.close()
