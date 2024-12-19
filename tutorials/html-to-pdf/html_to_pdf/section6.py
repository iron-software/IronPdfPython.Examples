from ironpdf import *

def run():
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from a URL or local file path
    pdf = renderer.RenderUrlAsPdf("https://en.wikipedia.org/wiki/PDF")
    # Export to a file or Stream
    pdf.SaveAs("url.pdf")