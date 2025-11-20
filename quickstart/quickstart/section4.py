from ironpdf import *

def run():
    # Instantiate ChromePdfRenderer
    renderer = ChromePdfRenderer()
    # Create a PDF from a URL or local file path
    pdf = renderer.RenderUrlAsPdf("https://ironpdf.com/")
    # Save the generated PDF to a file
    pdf.SaveAs("url_to_pdf.pdf")