#!/usr/bin/env python3

import os
from datetime import datetime
from reports import generate_report
from emails import generate_email
from emails import send_email

# iterates over the txt file, sets the first line to name, the second line to weight
# add that onto the same string with the proper line breaks to create format
def read_data(folder_path):
    data = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                # store text data as a list of strings
                file_lines = file.readlines()
                # validate length of list
                if len(file_lines) >= 2:
                # Pull the fruit name from line 1 and weight from line 2
                    name = file_lines[0].strip()
                    weight = file_lines[1].strip()
                # appending the data variable with the extracted data
                    data += f"<p>name: {name} <br/>weight: {weight}<br/><br/></p>"
                else:
                    num_lines = len(file_lines)
                    print(f"The file {filename} contains {num_lines} lines.")
    # return the data so it can be passed to the generate_report function
    return data

if __name__ == "__main__":
    # where to get supplier txt files
    folder_path = "D:/files/CareerGrowth/GoogleITAutomationPython/PythonAutomation_Git/PyAuto_Course6Mod4/supplier-data/descriptions"
    # name and destination for new pdf file
    output_pdf = "D:/files/CareerGrowth/GoogleITAutomationPython/PythonAutomation_Git/PyAuto_Course6Mod4/supplier-data/processed.pdf"
    # getting date of file execution
    current_date = datetime.now().strftime("%B %d, %Y")
    # creating a report title for the pdf
    report_title = f"Processed Update on {current_date}"
    # call the read_data function so we can build the pdf's paragraph content
    report_paragraph = read_data(folder_path)
    # calling the function to generate a pdf with the provided parameters
    generate_report(output_pdf, report_title, report_paragraph)
    # set parameters to pass to generate_email function
    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Complete - Online Fruit Store"
    body =  "ll fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = output_pdf
    message = generate_email(sender, recipient, subject, body, attachment_path)
    send_email(message)