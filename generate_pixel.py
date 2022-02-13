'this file is used to generate future pixel nfts'
from ctypes.wintypes import RGB
import os
import sys

import random as rand
from turtle import color
import PIL as pil

from PIL import Image, ImageColor

import requests
from bs4 import BeautifulSoup



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

def scrape_hexvalues():
    URL = "https://opensea.io/collection/the-colors-dot-art"
    page = requests.get(URL)
    print(page.text) # Returning a security alert, have to work with api 


if __name__ == "__main__":

    Folder = False
    for i in range ( len (sys.argv) ): #Checking if user wants to set a outputfolder
        if sys.argv[i].lower() == '--folder': 
            output_folder = sys.argv[i+1]
            Folder = True
            
    if not Folder:
        
        '''print("ERROR: No defined output_path")
        print("python generate_pixel.py <output_folder> (<r> <g> <b>)")
        print("Aborting...")
        sys.exit(-1) ''' 
        #I would rather give it a relative path as default, remove it again if you dont want that
        
        print('Using standard folder \Pixels')
        dirname = os.getcwd()
        output_folder = str(dirname) + '\Pixels'
        

    Colors = False #checking if user wants to configure colors
    for i in range ( len ( sys.argv)):
        if sys.argv[i].lower() == '--colors':
            r = int(sys.argv[i+1])
            g = int(sys.argv[i+2])
            b = int(sys.argv[i+3])
            Colors = True
    
    
    if not Colors:
        print("generating random pixel...")
        r = rand.randint(0, 255)
        g = rand.randint(0, 255)
        b = rand.randint(0, 255)
    
    
    if not os.path.isdir(output_folder):
        print("ERROR: output_path is a file not a folder!")
        print("Aborting...")
        sys.exit(-1)
        
        
    iterations = 1
    for i in range ( len ( sys.argv)):
        if sys.argv[i].lower() == '--number':
            iterations = int(sys.argv[i+1])
            print('Will be generating %s elements' %(str(iterations)))
    
    scrape_hexvalues()
    
    for i in range(iterations): # still only generates one element, dont know why yet
        nft = generate_pixel(r, g, b)
        hex_value = get_hex(r, g, b)

        path = f"{output_folder}\\{hex_value}.png" # only works for windows!!

        store_pixel(nft, path)
