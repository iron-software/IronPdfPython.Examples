from ironpdf import *

def run():
    License.LicenseKey = "Enter-Your-License"  
    pdf = PdfDocument.FromFile("MyPdf.pdf")
    pdf.Print()
    printer_setting = pdf.GetPrintDocument()
    printer_setting.PrinterSettings.FromPage = 2
    printer_setting.PrinterSettings.ToPage = 4
    printer_setting.Print()