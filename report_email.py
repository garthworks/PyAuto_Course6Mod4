#!/usr/bin/env python3

import os
from datetime import datetime
from reports import generate_report

# iterates over the txt file, sets the first line to name, the second line to weight
# add that onto the same string with the proper line breaks to create format
def read_data(folder_path):
    data = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                file_content = file.read()
                # Extracting name and weight from file content
                name = file_content.split('\n')[0].strip()
                weight = file_content.split('\n')[0].strip()
                # Formatting data
                data += f"<p>name: {name} <br/>weight: {weight}<br/><br/></p>"
  
    return data

if __name__ == "__main__":
    # where to get supplier txt files
    folder_path = "D:/files/CareerGrowth/GoogleITAutomationPython/PythonAutomation_Git/PyAuto_Course6Mod4/supplier-data/descriptions"
    # name and destination for new pdf file
    output_pdf = "D:/files/CareerGrowth/GoogleITAutomationPython/PythonAutomation_Git/PyAuto_Course6Mod4/supplier-data/processed.pdf"
    # grabbing the date at execution
    current_date = datetime.now().strftime("%B %d, %Y")
    # including the date in the report title
    report_title = f"Processed Update on {current_date}"
    # call the read_data function and passes the supplier file location
    report_paragraph = read_data(folder_path)
    # generates the actual pdf
    generate_report(output_pdf, report_title, report_paragraph)
