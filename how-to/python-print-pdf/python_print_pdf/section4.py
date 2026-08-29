from ironpdf import *

def run():
    # The guide loads a PDF before this snippet; load one here so the example
    # runs on its own.
    License.LicenseKey = "Enter-Your-License"
    pdf = PdfDocument.FromFile("MyPdf.pdf")

    # Access and modify the print settings
    printer_setting = pdf.GetPrintDocument()
    # Set the range of pages to print
    printer_setting.PrinterSettings.FromPage = 2
    printer_setting.PrinterSettings.ToPage = 4
    # Print with the customized settings
    printer_setting.Print()
