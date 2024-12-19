from ironpdf import *

def run():
    # Create from existing PDF file on the file system
        existing_pdf = PdfDocument("existing.pdf")
        # Create from HTML!
        new_pdf = ChromePdfRenderer().RenderHtmlAsPdf("<h1>Hello world!</h1>")