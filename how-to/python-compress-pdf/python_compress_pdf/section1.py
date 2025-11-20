from ironpdf import PdfDocument

def run():
    # Load the PDF document from a file
    pdf = PdfDocument("Image based PDF.pdf")
    # Compress images in the PDF with a quality setting of 60 (out of 100)
    # Lower numbers reduce quality to increase compression
    pdf.CompressImages(60)
    pdf.SaveAs("document_compressed.pdf")
    # Compress images with an additional option to scale down image resolution according to their visible size in the PDF
    # This may cause distortion depending on the image configurations
    pdf.CompressImages(90, True)
    pdf.SaveAs("Compressed.pdf")