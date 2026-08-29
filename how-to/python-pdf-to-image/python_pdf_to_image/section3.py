from ironpdf import *

def run():
    # The guide renders a PDF before this snippet; render one here so the
    # example runs on its own.
    renderer = ChromePdfRenderer()
    pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")

    # Generate images with specified maximum dimensions and DPI
    pdf.RasterizeToImageFiles("assets/images/*.png", ImageMaxWidth=500, ImageMaxHeight=500, DPI=200)
