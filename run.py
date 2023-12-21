#! /usr/bin/env python3

import os
import requests

# pull text data from text files in supplier-data/descriptions/
# convert data into JSON format (see below example) for upload to API

# notice the weight field is an integer not a string
# {"name": "Test Fruit", 
# "weight": 100, 
# "description": "This is the description of my test fruit",
# "image_name": "icon.sheet.png"}

# post to http://[linux-instance-external-IP]/fruits
# this IP changes each time lab is launched

# location of text files to process
desc_path = "supplier-data/descriptions/"

for txt_item in os.listdir(desc_path):
  # the text file has a matching image with same name
  img_name = txt_item.replace(".txt", ".jpeg")
  # setting variable with pathname and filename to open
  txt_file = os.path.join(desc_path, txt_item)
  with open(txt_file, 'r') as f:
    # Creating a dictionary for each file
    current_desc_dict = {
      'name': f.readline().strip(),
      'weight': int(''.join(filter(str.isdigit, f.readline().strip()))),
      'description': f.readline().strip(),
      'image_name': img_name
      }
    # saving the response from my post of json formated data to the api  
    response = requests.post("http://REPLACEwIPofLab/fruits/", json=current_desc_dict)
    # this will raise an error if there is one, otherwise the script finishes with no output
    response.raise_for_status()
    # From one of my less than successful errors, I got this.
    #     raise HTTPError(http_error_msg, response=self)
    #     requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: http://IP_ADDR/fruits/
    
    # you can also print the response
    print(response)

    