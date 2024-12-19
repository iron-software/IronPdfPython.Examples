from ironpdf import *

def run():
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from an existing HTML file using Python
    pdf = renderer.RenderHtmlFileAsPdf("invoices/TestInvoice1.html")
    # Export to a file or Stream
    pdf.SaveAs("htmlfile_to_pdf.pdf")