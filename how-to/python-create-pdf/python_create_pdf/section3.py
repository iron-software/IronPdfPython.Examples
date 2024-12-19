from ironpdf import *

def run():
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from a HTML string using Python
    pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")