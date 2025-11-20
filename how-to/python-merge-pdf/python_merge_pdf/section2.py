from ironpdf import *

def run():
    # HTML content for the first PDF
    html_a = """<p> [PDF_A] </p>
                <p> [PDF_A] 1st Page </p>
                <div style='page-break-after: always;'></div>
                <p> [PDF_A] 2nd Page</p>"""
    # HTML content for the second PDF
    html_b = """<p> [PDF_B] </p>
                <p> [PDF_B] 1st Page </p>
                <div style='page-break-after: always;'></div>
                <p> [PDF_B] 2nd Page</p>"""
    # Initialize ChromePdfRenderer
    renderer = ChromePdfRenderer()
    # Convert HTML to PDF documents
    pdfdoc_a = renderer.RenderHtmlAsPdf(html_a)
    pdfdoc_b = renderer.RenderHtmlAsPdf(html_b)
    # Merge the PDF documents
    merged = PdfDocument.Merge([pdfdoc_a, pdfdoc_b])