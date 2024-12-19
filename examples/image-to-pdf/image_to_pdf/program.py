from ironpdf import *

# One or more images as a list. This example selects all JPEG images in a specific 'assets' folder.
image_files = [os.path.join("assets", f) for f in os.listdir("assets") if f.lower().endswith(('.jpg', '.jpeg'))]

directory_list = List[str]()
for i in range(len(image_files)):
    directory_list.Add(image_files[i])

# Converts the images to a PDF and save it.
ImageToPdfConverter.ImageToPdf(directory_list).SaveAs("composite.pdf")

# Also see PdfDocument.RasterizeToImageFiles() method to flatten a PDF to images or thumbnails