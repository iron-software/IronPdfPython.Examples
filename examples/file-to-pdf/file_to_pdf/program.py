from ironpdf import *

# Instantiate Renderer
renderer = ChromePdfRenderer()

# Create a PDF from an existing HTML file using Python
pdf = renderer.RenderHtmlFileAsPdf("example.html")

# Export to a file or Stream
pdf.SaveAs("output.pdf")
