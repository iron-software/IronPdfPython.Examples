from ironpdf import *

def run():
    # The guide renders a PDF before this snippet; render one here so the
    # example runs on its own.
    renderer = ChromePdfRenderer()
    pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")

    # Set user password for PDF document security
    pdf.SecuritySettings.UserPassword = "sharable"
    # Save the password-protected PDF
    pdf.SaveAs("protected.pdf")
