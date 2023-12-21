#!/usr/bin/env python3

import os
from PIL import Image

# creates variable but it is saved as a string
# IMPROVE determine absolute path and combine it with /images
image_dir = r'supplier-data/images'
# get a list of file in the source directory
file_list = os.listdir(image_dir)

# Set the desire size
new_size = (600, 400)


# iterate over images in source directory
for im in file_list:
  if 'tiff' in im:
    # put the filename with the absolute path
    file_path = os.path.join(image_dir, im)
    # in script test
    # print(file_path)
    # open the file
    im_src = Image.open(file_path)

    # convert file to JPEG
    # The raw images from images subdirectory contains alpha transparency layers. 
    # first convert RGBA 4-channel format to RGB 3-channel format before processing the images. 
    # Use convert("RGB") method for converting RGBA to RGB image.
    conv_im = im_src.convert('RGB')

    # resize file
    fin_im = conv_im.resize(new_size)

    # set the file extenstion as JPEG in the destination folder
    # we are splitting the filename into two parts, name and file type and appending .jpg to the name
    # joining the new file name with destionation folder and setting it to a new variable
    destination_path = os.path.join(image_dir, os.path.splitext(im)[0] + '.jpeg')

    # save file
    fin_im.save(destination_path)