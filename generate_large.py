'''
generates larger images
'''
import os
import sys

import random as rand
import PIL as pil

from PIL import Image, ImageColor



def gen_color_gradient(scale, r, g, b):
    
    im = Image.new('RGB', (scale, scale)) # create the Image

    for x in range(scale):
        for y in range(scale):
            im.putpixel((x,y), (r, g, b))
            r -= 5
            g -= 5
            b -= 5

    return im


def gen_color_random(scale):
    
    im = Image.new('RGB', (scale, scale)) # create the Image

    for x in range(scale):
        for y in range(scale):
            r = rand.randint(0, 255)
            g = rand.randint(0, 255)
            b = rand.randint(0, 255)
            im.putpixel((x,y), (r, g, b))

    return im


def upscale(image, scale):

    return image.resize((scale, scale), resample=Image.BOX)


def store(image, path):
    
    image.save(path)

    return



if __name__ == "__main__":
    
    try:
        output_file_loc = sys.argv[1]
    
    except IndexError:
        print("ERROR: No defined output_path")
        print("python generate_large.py <output_file_loc> (<scale>) (<r> <g> <b>)")
        print("Aborting...")
        sys.exit(-1)
    
    try:
        scale = int(sys.argv[2])
    
    except IndexError:
        scale = 2

    try:
        r = int(sys.argv[3])
        g = int(sys.argv[4])
        b = int(sys.argv[5])

    except IndexError:
        print("generating random color...")
        r = rand.randint(0, 255)
        g = rand.randint(0, 255)
        b = rand.randint(0, 255)
    
    if os.path.isdir(output_file_loc):
        print("ERROR: output_path has to be a file not a folder!")
        print("Aborting...")
        sys.exit(-1)

    if not output_file_loc.lower().endswith('.png'):
        print("ERROR: output_path has to be a .png file!")
        print("Aborting...")
        sys.exit(-1)

    # nft = gen_color_gradient(scale, r, g, b)
    nft = gen_color_random(scale)
    # nft = upscale(nft, 1024)

    store(nft, output_file_loc)

    


