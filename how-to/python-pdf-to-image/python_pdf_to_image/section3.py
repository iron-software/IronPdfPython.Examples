from ironpdf import *

def run():
    pdf.RasterizeToImageFiles("assets/images/*.png", ImageMaxWidth=500, ImageMaxHeight=500, DPI=200)