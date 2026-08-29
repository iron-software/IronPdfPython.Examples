> Full guide: [Multi frame TIFF to PDF](https://ironpdf.com/examples/multi-frame-tiff-to-pdf/?utm_source=github)

IronPDF for Python offers a feature through the `ImageToPdfConverter` class that facilitates the transformation of TIFF images into PDF formats. Specifically, when employing `ImagePdfConverter.ImageToPdf` with a multi-framed TIFF, it distributes each frame across separate PDF pages.

Below is a step-by-step guide on using the `ImageToPdfConverter` to transform a TIFF image with multiple frames into a PDF document:

### Code Walkthrough

1. **Importing Necessary Classes**:
   - The classes `PdfDocument` and `ImageToPdfConverter` are extracted from the `ironpdf` package, allowing for efficient PDF rendering.

2. **Defining `convert_tiff_to_pdf(tiff_path: str, pdf_output_path: str)` Function**:
   - This function accepts a path to a TIFF file (`tiff_path`) and converts it to a PDF, which is then saved to the designated path (`pdf_output_path`).

3. **Creating an Instance of ImageToPdfConverter**:
   - This involves establishing a new `ImageToPdfConverter` instance to utilize its `image_to_pdf` method for the conversion process.

4. **Executing the PDF Conversion**:
   - The `image_to_pdf(tiff_path)` method processes the multi-framed TIFF, arranging each frame onto a new PDF page.

5. **Storing the PDF File**:
   - Post-conversion, the resultant PDF is stored at the intended path using the `save` method from the `PdfDocument` class.

To execute this conversion, replace `'path/to/your/tiff_file.tiff'` and `'path/to/output/pdf_document.pdf'` with the actual paths to your files.

[Learn How to Convert PDF to Image with Python](https://ironpdf.com/python/how-to/python-pdf-to-image/?utm_source=github)