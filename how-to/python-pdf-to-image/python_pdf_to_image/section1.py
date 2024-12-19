from ironpdf import *

def run():
    pdf = PdfDocument.FromFile("my-content.pdf")
    # Extract all pages to a folder as image files
    pdf.RasterizeToImageFiles("assets/images/*.png",DPI=96)