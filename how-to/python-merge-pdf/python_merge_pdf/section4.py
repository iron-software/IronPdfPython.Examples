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
    # HTML content for the third PDF
    html_c = """<p> [PDF_C] </p>
                <p> [PDF_C] 1st Page </p>
                <div style='page-break-after: always;'></div>
                <p> [PDF_C] 2nd Page</p>"""
    # Initialize ChromePdfRenderer
    renderer = ChromePdfRenderer()
    # Convert HTML to PDF documents
    pdfdoc_a = renderer.RenderHtmlAsPdf(html_a)
    pdfdoc_b = renderer.RenderHtmlAsPdf(html_b)
    pdfdoc_c = renderer.RenderHtmlAsPdf(html_c)
    # List of PDF documents to merge
    pdfs = [pdfdoc_a, pdfdoc_b, pdfdoc_c]
    # Merge the list of PDFs into a single PDF
    pdf = PdfDocument.Merge(pdfs)
    # Save the merged PDF document
    pdf.SaveAs("merged.pdf")