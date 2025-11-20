from ironpdf import *

def run():
    # Instantiate ChromePdfRenderer
    renderer = ChromePdfRenderer()
    # Create a PDF from an HTML string
    pdf = renderer.RenderHtmlAsPdf("<h1>Hello World</h1>")
    # Save the generated PDF to a file
    pdf.SaveAs("html_to_pdf.pdf")