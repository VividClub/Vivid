'this file is used to generate future pixel nfts'
from ctypes.wintypes import RGB
import os
import sys

import random as rand
import PIL as pil

from PIL import Image, ImageColor



def generate_pixel(r, g, b):
    '''
        generates 1x1 Image with given color
    Parameters:
        r: int -> red-value from 0-255
        g: int -> green-value from 0-255
        b: int -> blue-value from 0-255
    returns:
        1x1 Image
    '''
    im = Image.new('RGB', (1,1)) # create the Image of size 1 pixel
    im.putpixel((0,0), (r, g, b))
    
    return im


def store_pixel(image, path):
    
    image.save(path)

    return


def get_hex(r, g, b):

    hex_value = '#%02x%02x%02x' % (r, g, b)

    return hex_value


if __name__ == "__main__":

    try:
        output_folder = sys.argv[1]
    
    except IndexError:
        print("ERROR: No defined output_path")
        print("python generate_pixel.py <output_folder> (<r> <g> <b>)")
        print("Aborting...")
        sys.exit(-1)

    try:
        r = int(sys.argv[2])
        g = int(sys.argv[3])
        b = int(sys.argv[4])

    except IndexError:
        print("generating random pixel...")
        r = rand.randint(0, 255)
        g = rand.randint(0, 255)
        b = rand.randint(0, 255)
    
    if not os.path.isdir(output_folder):
        print("ERROR: output_path is a file not a folder!")
        print("Aborting...")
        sys.exit(-1)

    nft = generate_pixel(r, g, b)
    hex_value = get_hex(r, g, b)

    path = f"{output_folder}\\{hex_value}.png" # only works for windows!!

    store_pixel(nft, path)


