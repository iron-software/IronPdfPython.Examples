from ironpdf import *

# Convert a TIFF with 1 or more pages to a PDF
pdf = ImageToPdfConverter.ImageToPdf("multipleTiffSample.tiff")
 
# Export to a file or Stream
pdf.SaveAs("multi-page-pdf.pdf")