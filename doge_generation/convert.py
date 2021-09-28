from PIL import Image
import numpy as np
import os

# special colors:
# bork_eye = (34, 177, 76)
# vizor doubles for bork_eye outline, space doge helmet, and doc doge mirror

def swap_color(data, color1, color2):
    # convert color tuples to arrays
    col1 = np.asarray(color1)
    col2 = np.asarray(color2)
    # extract rgb arrays
    #red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3] 
    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    # crate truth value matrix to apply new colors
    mask = (red == col1[0]) & (green == col1[1]) & (blue == col1[2])
    # apply colors against mask
    # data[:,:,:4][mask] = [col2[0], col2[1], col2[2], 0]
    data[:,:,:3][mask] = [col2[0], col2[1], col2[2]]
    return data


def convert_frames(doge_type, doge_id, hd, th, ew, ep, nz, bg, ol, name):
    # create output dir
    home_dir = os.getcwd()
    out_dir = home_dir + "/doge_data/" + str(doge_id) + "_" + name + "/"
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
        

    # get correct skeleton based on doge_type
    skeleton_dir = home_dir + "/skeletons/" + str(doge_type) + "/"
    filelist = [file for file in os.listdir(skeleton_dir) if file.endswith('.png')]

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

    # Replace colors for each skeleton
    img_count = 0
    frames = []
    for file in filelist:
        # Open each fram in RGBA format and conver to array
        img = Image.open(skeleton_dir + file)
        img = img.convert("RGBA")
        alpha = img.split()[3]
        dat = np.array(img)

        # Swap each of the skeleton colors
        dat = swap_color(dat, background, bg)
        dat = swap_color(dat, eye_pupil, ep)
        dat = swap_color(dat, eye_white, ew)
        dat = swap_color(dat, vizor, gr)
        dat = swap_color(dat, moon_glass, gl)
        dat = swap_color(dat,bork_eye_pico, be)
        dat = swap_color(dat, nose, nz)
        dat = swap_color(dat, head, hd)
        dat = swap_color(dat, throat, th)
        dat = swap_color(dat, black, ol)
        img = Image.fromarray(dat)

        img = img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
        mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
        img.paste(255, mask)
        
        # first image converted should be skeleton_n so should be excluded from gif frames
        if img_count != 0:
            outfile = out_dir + name + "_frame_" + str(img_count) + '.png'
            frames.append(img)
            img.save(outfile)
        else:
            outfile = out_dir + name + '.png'
            img.save(outfile)

        img_count += 1

    # Generate gif from recolored frame images
    frames[0].save(out_dir + name + '.gif', save_all=True, append_images=frames[1:], interlace=False, optimize=False, duration=50, palette='RGB', loop=0, disposal=1, transparency=255) 





