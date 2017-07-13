import math
from PIL import Image

# returns the brightness of a given color
def brightness(color):
    return (color['r'] / 255) * 0.3 + (color['g'] / 255) * 0.59 + (color['b'] / 255) * 0.11

# characters in a spectrum where leftmost is brightest and rightmost is darkest
characters = ['@', '&', '0', 'm', 'w', 'a', 'e', 'n', 'u', 'x', 'l', 'i', 'v', '*', 'r', '~', '-']
characters.reverse()

# CONSTANTS
BLOCK_WIDTH = 4
BLOCK_HEIGHT = 8

# DON'T CHANGE THIS ONE
RANGE_FACTOR = (255 * 3) / len(characters)

im = Image.open("<img-path-here>")

block_map = []

block_x = 0
while block_x + BLOCK_HEIGHT <= im.height:
    block_map.append([])
    block_y = 0
    while block_y + BLOCK_WIDTH <= im.width:
        color_total = {'r': 0, 'g': 0, 'b': 0}
        for i in range(BLOCK_WIDTH):
            for j in range(BLOCK_HEIGHT):
                color_total['r'] += im.getpixel((block_y + i, block_x + j))[0]
                color_total['g'] += im.getpixel((block_y + i, block_x + j))[1]
                color_total['b'] += im.getpixel((block_y + i, block_x + j))[2]

        pixel_count = BLOCK_WIDTH * BLOCK_HEIGHT
        color_avg = {'r': color_total['r'] / pixel_count, 'g': color_total['g'] / pixel_count, 'b': color_total['b'] / pixel_count}

        block_map[-1].append(color_avg)

        # NOT BRIGHTNESS
        #color_avg['r'] /= RANGE_FACTOR
        #color_avg['g'] /= RANGE_FACTOR
        #color_avg['b'] /= RANGE_FACTOR
        #print((characters[int(color_avg['r']) + int(color_avg['g']) + int(color_avg['b'])]), end = "")

        # BRIGHTNESS
        print((characters[int((brightness(color_avg) * len(characters)))]), end = "")

        block_y += BLOCK_WIDTH

    print()
    block_x += BLOCK_HEIGHT
