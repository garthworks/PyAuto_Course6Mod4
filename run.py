#! /usr/bin/env python3

import os
import requests

# process text files in supplier-data/descriptions/
# convert txt file data into
# notice the weight filed is an integer not a string
# {"name": "Test Fruit", 
# "weight": 100, 
# "description": "This is the description of my test fruit",
# "image_name": "icon.sheet.png"}

# post to http://[linux-instance-external-IP]/fruits

# location of text files to process
desc_path = "supplier-data/descriptions/"

for txt_item in os.listdir(desc_path):
  img_name = txt_item.replace(".txt", ".jpeg")
  txt_file = os.path.join(desc_path, txt_item)
  with open(txt_file, 'r') as f:
    # Creating a dictionary for each file
    current_desc_dict = {
      'name': f.readline().strip(),
      'weight': int(''.join(filter(str.isdigit, f.readline().strip()))),
      'description': f.readline().strip(),
      'image_name': img_name
      }
      # requests.post 
    response = requests.post("http://34.16.183.79/fruits/", json=current_desc_dict)
      # check response of post
    response.raise_for_status()
    print(response)

    