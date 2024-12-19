from ironpdf import *

def run():
    pdf.SecuritySettings.UserPassword = "sharable"
    pdf.SaveAs("protected.pdf")