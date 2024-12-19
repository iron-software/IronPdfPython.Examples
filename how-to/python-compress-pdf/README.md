# How to Optimize PDF File Sizes in Python

***Based on <https://ironpdf.com/how-to/python-compress-pdf/>***


PDF files are commonly utilized for various purposes such as document storage and sharing. However, large file sizes can pose issues during file transfers or when managing disk space. To address these concerns, implementing PDF compression techniques can help minimize PDF file sizes effectively.

In this tutorial, we explore the use of IronPDF to efficiently reduce the file sizes of PDF documents. We provide you with actionable code samples that you can integrate into your applications, facilitating the compression of PDFs to optimize their storage and transfer.

## IronPDF: Your PDF Manipulation Tool

Discover IronPDF, a comprehensive and dynamic Python PDF library that enables you to manage PDF files effectively. IronPDF supports a multitude of operations including creation, editing, compression, and reading of PDFs. It is equipped with numerous features that enhance your document processing tasks.

A particularly impressive feature of IronPDF is its ability to compress PDFs. This function allows users to significantly decrease file sizes while preserving the quality of the documents. This feature is especially useful for large files that need to be distributed quickly via the internet or email.

## Installing IronPDF with Pip

You can easily install IronPDF in your Python environment using pip with the following command:

```shell
pip install ironpdf
```

IronPDF for Python leverages the IronPDF .NET library, and specifically requires .NET 6.0. To use this library, ensure that the .NET 6.0 SDK is installed on your system. You can download the .NET 6.0 SDK directly from the [official Microsoft website](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).

## Reducing PDF Size with IronPDF in Python

The following Python code demonstrates how to use the IronPDF library to compress PDF files:

```py
from ironpdf import *

pdf = PdfDocument("Image based PDF.pdf")

# Set image quality (1-100): a higher number maintains more of the original quality

***Based on <https://ironpdf.com/how-to/python-compress-pdf/>***

pdf.CompressImages(60)
pdf.SaveAs("document_compressed.pdf")

# Optionally adjust image resolution based on its display size in the PDF, which might alter image appearance

***Based on <https://ironpdf.com/how-to/python-compress-pdf/>***

pdf.CompressImages(90, True)
pdf.SaveAs("Compressed.pdf")
```

This script loads a PDF named `"Image based PDF.pdf"`, compresses the images inside, and saves the outcome as `"document_compressed.pdf"`. A secondary example compresses and saves the file as `"Compressed.pdf"`, using an optional feature to adjust image resolutions based on display size within the PDF, which may affect how the images appear.

We recommend examining both the original and compressed PDFs to see how the compression affects file size and image clarity.

### Visual Comparison: Before and After Compression

#### Original PDF

![Original PDF](https://ironpdf.com/static-assets/ironpdf-python/howto/python-compress-pdf/python-compress-pdf-1.webp)

#### Compressed PDF Output

![Compressed PDF Output](https://ironpdf.com/static-assets/ironpdf-python/howto/python-compress-pdf/python-compress-pdf-2.webp)

## Conclusion

IronPDF provides an efficient, cost-effective solution for PDF compression in Python, featuring capabilities such as page manipulation, HTML to PDF conversion, and detailed image control. Starting at just `$liteLicense`, IronPDF offers [affordable licensing options](https://ironpdf.com/python/licensing/) that provide access to top-tier software without significant investment. Use IronPDF's robust optimization features for smooth and effective PDF compression.