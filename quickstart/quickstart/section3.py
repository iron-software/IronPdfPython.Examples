from ironpdf import *

def run():
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from a HTML string using C&num;
    pdf = renderer.RenderHtmlAsPdf("<h1>Hello World</h1>")
    # Export to a file or Stream
    pdf.SaveAs("html_to_pdf.pdf")