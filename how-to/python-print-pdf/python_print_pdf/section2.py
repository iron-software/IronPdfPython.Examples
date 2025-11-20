from ironpdf import *

def run():
    # Set your license key to use IronPDF
    License.LicenseKey = "Enter-Your-License"
    # Load the PDF file from the filesystem
    pdf = PdfDocument.FromFile("MyPdf.pdf")