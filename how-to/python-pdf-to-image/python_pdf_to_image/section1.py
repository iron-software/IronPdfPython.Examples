from ironpdf import PdfDocument

def run():
    # Load the PDF document
    pdf = PdfDocument.FromFile("my-content.pdf")
    # Extract all pages to a folder as image files
    # Ensure the directory "assets/images" exists before executing the code
    pdf.RasterizeToImageFiles("assets/images/*.png", DPI=96)