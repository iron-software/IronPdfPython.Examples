from ironpdf import *

def run():
    # The guide merges two documents before this snippet; build the merged
    # document here so the example runs on its own.
    renderer = ChromePdfRenderer()
    pdfdoc_a = renderer.RenderHtmlAsPdf("<p> [PDF_A] 1st Page </p>")
    pdfdoc_b = renderer.RenderHtmlAsPdf("<p> [PDF_B] 1st Page </p>")
    merged = PdfDocument.Merge([pdfdoc_a, pdfdoc_b])

    # Save the merged PDF document
    merged.SaveAs("Merged.pdf")
