from ironpdf import *

def run():
    # The guide renders a PDF before this snippet; render one here so the
    # example runs on its own.
    renderer = ChromePdfRenderer()
    pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")

    # Export to a file or Stream
    pdf.SaveAs("htmlstring_to_pdf.pdf")
