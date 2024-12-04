# Compressing PDF Files Using IronPDF in Python

***Based on <https://ironpdf.com/how-to/python-compress-pdf/>***


PDF documents are essential for sharing and storing data, but their often large sizes can pose challenges in terms of storage management and file sharing. To address these issues, compressing PDF files is a vital solution. This tutorial will explore how to effectively compress PDF files using IronPDF, accompanied by detailed code examples that you can integrate into your projects to enhance file management efficiency.

## Introduction to IronPDF: A PDF Library for Python

IronPDF stands as a comprehensive PDF library in Python that offers robust capabilities for creating, manipulating, reading, and compressing PDF documents. Its ability to compress PDF files while maintaining high-quality output is particularly useful for handling large files, facilitating easier distribution via the internet or email.

## Setting Up IronPDF

To get started with IronPDF, install the library using pip with the following command:

```shell
pip install ironpdf
```

Please note that IronPDF Python is built upon the IronPDF .NET library targeting .NET 6.0. Ensure that the .NET 6.0 SDK is installed on your system. You can download it from the [official Microsoft website](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).

## Compressing PDF Files with IronPDF in Python

Below is a Python script demonstrating how to compress PDF documents using the IronPDF library:

```python
from ironpdf import PdfDocument

# Load an image-based PDF

***Based on <https://ironpdf.com/how-to/python-compress-pdf/>***

pdf = PdfDocument("Image based PDF.pdf")

# Compress the images in the PDF file (Quality range from 1-100)

***Based on <https://ironpdf.com/how-to/python-compress-pdf/>***

pdf.CompressImages(60)
pdf.SaveAs("document_compressed.pdf")

# Optionally, reduce image resolution based on visibility in PDF

***Based on <https://ironpdf.com/how-to/python-compress-pdf/>***

pdf.CompressImages(90, True)
pdf.SaveAs("Compressed.pdf")
```

This script will take a PDF named "Image based PDF.pdf" and compress its images to different quality levels, saving the new versions under "document_compressed.pdf" and "Compressed.pdf". The optional parameter allows for the reduction of resolution based on the image's visibility, which might alter the image appearance.

You can compare the original and compressed PDFs to evaluate the changes in file size and image specifications.

### Before Compression

![Original PDF](https://ironpdf.com/static-assets/ironpdf-python/howto/python-compress-pdf/python-compress-pdf-1.webp)

### After Compression

![Compressed PDF Output](https://ironpdf.com/static-assets/ironpdf-python/howto/python-compress-pdf/python-compress-pdf-2.webp)

## Conclusion

IronPDF provides an affordable and effective means for Python developers to compress PDF files. Its extensive features, such as HTML-to-PDF conversion, image manipulation, and more, make it a valuable tool for developers needing comprehensive and cost-effective solutions. IronPDF's licensing starts from `$liteLicense`, and further information is provided on their [licensing page](https://ironpdf.com/python/licensing/), ensuring you have access to affordable, high-quality PDF management tools.