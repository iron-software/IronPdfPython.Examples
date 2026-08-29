from ironpdf import *

def run():
    # The guide loads a PDF before this snippet; load one here so the example
    # runs on its own.
    License.LicenseKey = "Enter-Your-License"
    pdf = PdfDocument.FromFile("MyPdf.pdf")

    # Print the PDF using default settings
    pdf.Print()
