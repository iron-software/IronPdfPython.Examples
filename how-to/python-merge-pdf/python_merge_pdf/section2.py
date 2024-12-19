from ironpdf import *

def run():
    html_a = """<p> [PDF_A] </p>
                <p> [PDF_A] 1st Page </p>
                <div style='page-break-after: always;'></div>
                <p> [PDF_A] 2nd Page</p>"""
    html_b = """<p> [PDF_B] </p>
                <p> [PDF_B] 1st Page </p>
                <div style='page-break-after: always;'></div>
                <p> [PDF_B] 2nd Page</p>"""
    renderer = ChromePdfRenderer()
    pdfdoc_a = renderer.RenderHtmlAsPdf(html_a)
    pdfdoc_b = renderer.RenderHtmlAsPdf(html_b)
    merged = PdfDocument.Merge(pdfdoc_a, pdfdoc_b)