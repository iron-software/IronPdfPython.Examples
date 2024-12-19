from ironpdf import *

def run():
    # Import statement for IronPDF Python
    # Apply your license key
    License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from a HTML string using Python
    pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")
    # Export to a file or Stream
    pdf.SaveAs("htmlstring_to_pdf.pdf")
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from an existing HTML file using Python
    pdf = renderer.RenderHtmlFileAsPdf("example.html")
    # Export to a file or Stream
    pdf.SaveAs("htmlfile_to_pdf.pdf")
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    # Create a PDF from a URL or local file path
    pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")
    # Export to a file or Stream
    pdf.SaveAs("url.pdf")
    pdf.SecuritySettings.UserPassword = "sharable"
    pdf.SaveAs("protected.pdf")