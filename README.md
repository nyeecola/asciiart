# Image to ascii converter

To get good results you must use this in a dark background-color terminal/editor.

## HOW TO USE

- Go to the main.py file and change the image path to the one you want to convert to ascii.

- Change BLOCK_WIDTH and BLOCK_HEIGHT values as you wish.
    - These are the constants that define the final size of the converted image.
    - A smaller block size means a bigger ascii art.
    - The minimum value for BLOCK_WIDTH and BLOCK_HEIGHT is 1. This means that if they are 1 each pixel of the input image will be translated to exactly 1 ascii character.
