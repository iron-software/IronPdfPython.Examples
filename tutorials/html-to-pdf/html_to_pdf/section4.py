from ironpdf import *

def run():
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from a HTML string using Python
    pdf = renderer.RenderHtmlAsPdf("<h1>Hello from IronPDF!</h1>")
    # Export to a file or Stream
    pdf.SaveAs("output.pdf")