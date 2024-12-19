from ironpdf import *

def run():
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from a URL or local file path
    pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")
    # Export to a file or Stream
    pdf.SaveAs("url.pdf")