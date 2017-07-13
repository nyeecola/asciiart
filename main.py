import math
from PIL import Image

# returns the brightness of a given color
def brightness(color):
    return (color['r'] / 255) * 0.3 + (color['g'] / 255) * 0.59 + (color['b'] / 255) * 0.11

# characters in a spectrum where leftmost is brightest and rightmost is darkest
#characters = ['&', '@', '0', 'm', 'w', 'a', 'n', 'u', 's', 'x', 'l', 'i', 'v', '*', 'r', '~', '-', '.']
characters = ['&', '@', '0', 'm', 'w', 'a', 'n', 'u', 's', 'x', 'l', 't', 'i', '*', 'r', '~', '-', '.']
characters.reverse()

# CONSTANTS
BLOCK_WIDTH = 4
BLOCK_HEIGHT = 8

# DON'T CHANGE THIS ONE
RANGE_FACTOR = (255 * 3) / len(characters)

im = Image.open("<img-path-here>")

block_x = 0
while block_x + BLOCK_HEIGHT <= im.height:
    block_y = 0
    while block_y + BLOCK_WIDTH <= im.width:
        brightness_total = 0
        brightness_avg = 0
        for i in range(BLOCK_WIDTH):
            for j in range(BLOCK_HEIGHT):
                color_pixel = {
                    'r': im.getpixel((block_y + i, block_x + j))[0],
                    'g': im.getpixel((block_y + i, block_x + j))[1],
                    'b': im.getpixel((block_y + i, block_x + j))[2]
                }
                brightness_total += brightness(color_pixel)

        pixel_count = BLOCK_WIDTH * BLOCK_HEIGHT

        brightness_avg = brightness_total / pixel_count

        print((characters[int(brightness_avg * len(characters))]), end = "")

        block_y += BLOCK_WIDTH

    print()
    block_x += BLOCK_HEIGHT
