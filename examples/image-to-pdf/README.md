> Full guide: [Image to PDF](https://ironpdf.com/examples/image-to-pdf/)

The `ImageToPdfConverter` class enables the creation of PDF documents from images.

Invoke the `ImageToPdfConverter.ImageToPdf` method with a valid image file path to generate a new PDF document from the provided image.

Utilize the `ImageToPdfConverter.ImageToPdf` method with an array of image paths to create a single PDF document that incorporates each image on individual pages.

- Include the necessary libraries: `FPDF` for generating PDF files, `Image` from PIL for image manipulation, and `os` for file handling.
- The function `image_to_pdf` accepts either a single image path or a collection of image paths and transforms them into a PDF file, storing it at the designated output location.
- To ensure compatibility, images are converted to RGB format.
- Temporary files are employed to preserve the uniformity of image formats.
- The function efficiently handles both single image paths and multiple image paths.

[Learn how to convert PDFs to images with IronPDF](https://ironpdf.com/python/how-to/python-pdf-to-image/)