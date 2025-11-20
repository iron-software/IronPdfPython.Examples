from ironpdf import *

def run():
    # Access and modify the print settings
    printer_setting = pdf.GetPrintDocument()
    # Set the range of pages to print
    printer_setting.PrinterSettings.FromPage = 2
    printer_setting.PrinterSettings.ToPage = 4
    # Print with the customized settings
    printer_setting.Print()