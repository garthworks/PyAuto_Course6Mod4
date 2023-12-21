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
    
    # TEST file_path var
    # print(file_path)
    # open the file
    im_src = Image.open(file_path)

    # convert file to JPEG
    # The raw images from images subdirectory contains alpha transparency layers. 
    # first convert RGBA 4-channel format to RGB 3-channel format before processing the images. 
    # Use convert("RGB") method for converting RGBA to RGB image.
    conv_im = im_src.convert('RGB')

    # resize file and set it the fin_im
    fin_im = conv_im.resize(new_size)

    # create a variable consisting of path and file name including jpg extension
    # I'm using the variable image_dir as my destination path,
    # I'm splitting the original filename from variable im in my for loop, ex. 007.tiff,
    # use the first part of the name at index position 0 and adding .jpeg
    destination_path = os.path.join(image_dir, os.path.splitext(im)[0] + '.jpeg')

    # save the finished image file
    fin_im.save(destination_path)