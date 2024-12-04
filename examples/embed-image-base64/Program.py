from ironpdf import *
import base64

# Instantiate Renderer
renderer = ChromePdfRenderer()

# Example 1: From an Image File or Bytes
with open(".\icons\iron.png", "rb") as f:
    pngBinaryData = f.read()
    imgDataUri = "data:image/png;base64," + base64.b64encode(pngBinaryData).decode("utf-8")
    imgHtml = f"<img src='{imgDataUri}'>"

pdf = renderer.RenderHtmlAsPdf(imgHtml)
pdf.SaveAs("embedded_example_1.pdf")