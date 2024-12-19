from ironpdf import *

def run():
    printer_setting = pdf.GetPrintDocument()
    printer_setting.PrinterSettings.FromPage = 2
    printer_setting.PrinterSettings.ToPage = 4
    printer_setting.Print()