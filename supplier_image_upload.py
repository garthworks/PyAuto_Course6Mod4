#!/usr/bin/env python3
import requests
import os

# using the requests module to upload images to URL

# url
url = "http://localhost/upload/"
# setting images folder as variable
image_dir = r'supplier-data/images'
# create a list of files from the images directory only when thye end in  .jpeg
image_list = [f for f in os.listdir(image_dir) if f.endswith('.jpeg')]

#iterate over file list
for im in image_list:
  # put the file path and image name together
  file_path = os.path.join(image_dir, im)
  # opening file
  with open(file_path, 'rb') as opened:
    # uploading file
    r = requests.post(url, files={'file': opened})
    # print server response
    print(r.text)