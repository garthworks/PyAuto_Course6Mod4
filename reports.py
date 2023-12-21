# Directions from LAB
# Using the reportlab Python library, 
# define the method generate_report to build the PDF reports. 
# We have already covered how to generate PDF reports in an earlier lesson; 
# you will want to use similar concepts to create a PDF report named processed.pdf.

#!/usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(pdf_path, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(pdf_path)
    report_title = Paragraph(title, styles["h1"])
    report_paragraph = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)

    report.build([report_title, empty_line, report_paragraph, empty_line])
