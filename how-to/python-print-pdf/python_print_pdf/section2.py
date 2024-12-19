from ironpdf import *

def run():
    License.LicenseKey = "Enter-Your-License"  
    pdf = PdfDocument.FromFile("MyPdf.pdf")