from ironpdf import *

def run():
    # Set user password for PDF document security
    pdf.SecuritySettings.UserPassword = "sharable"
    # Save the password-protected PDF
    pdf.SaveAs("protected.pdf")