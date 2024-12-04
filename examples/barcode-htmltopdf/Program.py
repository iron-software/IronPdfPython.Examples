from ironpdf import *

# Instantiate Renderer
renderer = ChromePdfRenderer()
renderer.RenderingOptions.WaitFor.RenderDelay(500)

# Load barcode via HTML
barcode_html = '''<link href="https://fonts.googleapis.com/css?family=Libre%20Barcode%20128" rel="stylesheet">
<p style="font-family: 'Libre Barcode 128', serif; font-size:30px;">Hello Google Fonts</p>'''
doc = renderer.RenderHtmlAsPdf(barcode_html)

# or use the BarcodeStamper
barcode_stamp = BarcodeStamper("Hello World", BarcodeEncoding.Code39)
doc.ApplyStamp(barcode_stamp)

# Export to a file or Stream
doc.SaveAs("bc-test.pdf")