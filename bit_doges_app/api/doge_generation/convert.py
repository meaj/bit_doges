from PIL import Image
import numpy as np
import os
import re
import codecs


# Converts RGB to HEX values
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def swap_color_png(data, color1, color2):
    # convert color tuples to arrays
    col1 = np.asarray(color1)
    col2 = np.asarray(color2)
    # extract rgb arrays
    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    # crate truth value matrix to apply new colors
    mask = (red == col1[0]) & (green == col1[1]) & (blue == col1[2])
    # apply colors against mask
    data[:,:,:3][mask] = [col2[0], col2[1], col2[2]]
    return data


def swap_color_svg(fileContent, rgb_color1, rgb_color2):
    # convert RGBs to HEX
    color1 = rgb_to_hex(rgb_color1)
    # print("Converted '" + str(rgb_color1) + "' to '" + color1 + "'")
    color2 = rgb_to_hex(rgb_color2)
    # print("Converted '" + str(rgb_color2) + "' to '" + color2 + "'")
    # swap content into new variable
    new_fileContent = fileContent.replace(color1, color2)
    return new_fileContent


def convert_frames(doge_type, doge_id, hd, th, ew, ep, nz, bg, ol, name):
    # create output dir
    home_dir = os.path.dirname(__file__)
    out_dir = home_dir + "/doge_data/" + str(doge_id) 
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
        
    # Skeleton colors to replace
    background = (41, 173, 255)
    head = (95, 87, 79)
    throat = (194, 195, 199)
    nose = (0, 228, 54)
    eye_pupil = (255, 204, 170)
    eye_white = (171, 82, 54)
    vizor = (131, 118, 156)
    bork_eye_pico = (255, 0, 77)
    moon_glass = (0, 135, 81)
    black = (0, 0, 0)

    # colors hardcoded for replacement
    gr = (105, 105, 105)
    be = (34, 177, 76)
    gl = (153,217, 234)

    # get correct skeleton based on doge_type
    skeleton_dir = home_dir + "/skeletons/" + str(doge_type) + "/"
    # get the frame list
    filelist = [file for file in os.listdir(skeleton_dir) if file.endswith('.png')]
    filelist.sort()
    # get the svg to swap
    svgFile = skeleton_dir + "skeleton_" + str(doge_type) + ".svg"

    # replace the colors in the svg:
    with codecs.open(svgFile, encoding='utf-8', errors='ignore') as f:
        svgContent = f.read()
    # Swap each of the skeleton colors
    svgContent = swap_color_svg(svgContent, background, bg)
    svgContent = swap_color_svg(svgContent, eye_pupil, ep)
    svgContent = swap_color_svg(svgContent, eye_white, ew)
    svgContent = swap_color_svg(svgContent, vizor, gr)
    svgContent = swap_color_svg(svgContent, moon_glass, gl)
    svgContent = swap_color_svg(svgContent, bork_eye_pico, be)
    svgContent = swap_color_svg(svgContent, nose, nz)
    svgContent = swap_color_svg(svgContent, head, hd)
    svgContent = swap_color_svg(svgContent, throat, th)
    svgContent = swap_color_svg(svgContent, black, ol)
    # write svg out
    outSVG = str(out_dir+ "/" + name + ".svg")
    f = open(outSVG, "x")
    f.write(svgContent)
    f.close()

    # Replace colors for each skeleton frame
    frames = []
    for file in filelist:
        # Open each frame in RGBA format and conver to array
        img = Image.open(skeleton_dir + file)
        img = img.convert("RGBA")
        alpha = img.split()[3]
        dat = np.array(img)

        # Swap each of the skeleton colors
        dat = swap_color_png(dat, background, bg)
        dat = swap_color_png(dat, eye_pupil, ep)
        dat = swap_color_png(dat, eye_white, ew)
        dat = swap_color_png(dat, vizor, gr)
        dat = swap_color_png(dat, moon_glass, gl)
        dat = swap_color_png(dat,bork_eye_pico, be)
        dat = swap_color_png(dat, nose, nz)
        dat = swap_color_png(dat, head, hd)
        dat = swap_color_png(dat, throat, th)
        dat = swap_color_png(dat, black, ol)
        img = Image.fromarray(dat)

        img = img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
        mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
        img.paste(255, mask)
        
        # first image converted should be skeleton_n so should be excluded from gif frames
        t = re.compile('skeleton_\d\.png')
        if t.match(file):
            outfile = out_dir + "/" + name + '.png'
            img.save(outfile)
        else:
            frames.append(img)

    # Generate gif from recolored frame images
    frames[0].save(out_dir + "/" + name + '.gif', save_all=True, append_images=frames[1:], interlace=False, optimize=False, duration=50, palette='RGB', loop=0, disposal=1, transparency=255)
