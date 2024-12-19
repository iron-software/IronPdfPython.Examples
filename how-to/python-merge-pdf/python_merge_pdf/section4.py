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
    html_c = """<p> [PDF_C] </p>
                <p> [PDF_C] 1st Page </p>
                <div style='page-break-after: always;'></div>
                <p> [PDF_C] 2nd Page</p>"""
    renderer = ChromePdfRenderer()
    pdfdoc_a = renderer.RenderHtmlAsPdf(html_a)
    pdfdoc_b = renderer.RenderHtmlAsPdf(html_b)
    pdfdoc_c = renderer.RenderHtmlAsPdf(html_c)
    pdfs = List [PdfDocument]()
    pdfs.Add(pdfdoc_a)
    pdfs.Add(pdfdoc_b)
    pdfs.Add(pdfdoc_c)
    pdf = PdfDocument.Merge(pdfs)
    pdf.SaveAs("merged.pdf")