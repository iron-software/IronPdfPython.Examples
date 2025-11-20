from ironpdf import *

def run():
    # Set your license key to use IronPDF
    License.LicenseKey = "Enter-Your-License"
    # Load the PDF file from the filesystem
    pdf = PdfDocument.FromFile("MyPdf.pdf")
    # Print the PDF using default settings
    pdf.Print()
    # Access and modify the print settings
    printer_setting = pdf.GetPrintDocument()
    # Set the range of pages to print
    printer_setting.PrinterSettings.FromPage = 2
    printer_setting.PrinterSettings.ToPage = 4
    # Print the document with the customized settings
    printer_setting.Print()