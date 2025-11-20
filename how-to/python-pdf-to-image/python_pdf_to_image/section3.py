from ironpdf import *

def run():
    # Generate images with specified maximum dimensions and DPI
    pdf.RasterizeToImageFiles("assets/images/*.png", ImageMaxWidth=500, ImageMaxHeight=500, DPI=200)