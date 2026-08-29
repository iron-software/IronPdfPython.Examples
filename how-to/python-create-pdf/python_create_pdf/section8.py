from ironpdf import *

def run():
    # Apply your license key
    License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"

    # --- HTML string to PDF ---
    renderer = ChromePdfRenderer()
    pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")
    pdf.SaveAs("htmlstring_to_pdf.pdf")

    # --- Local HTML file to PDF ---
    renderer = ChromePdfRenderer()
    pdf = renderer.RenderHtmlFileAsPdf("example.html")
    pdf.SaveAs("htmlfile_to_pdf.pdf")

    # --- URL to PDF ---
    renderer = ChromePdfRenderer()
    pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")
    pdf.SaveAs("url.pdf")

    # --- Password-protected PDF ---
    pdf.SecuritySettings.UserPassword = "sharable"
    pdf.SecuritySettings.OwnerPassword = "admin123"
    # The guide writes `AllowUserPrinting = True`. It is a PdfPrintSecurity
    # enum, not a bool, and assigning True raises TypeError under Python.NET 3.
    pdf.SecuritySettings.AllowUserPrinting = PdfPrintSecurity.FullPrintRights
    pdf.SecuritySettings.AllowUserCopyPasteContent = False
    pdf.SaveAs("protected.pdf")
