# How to Compress PDF Files in Python

> Full guide: [How to Compress PDF Files in Python](https://ironpdf.com/how-to/python-compress-pdf/)


PDFs are essential for storing and distributing documents, yet their large sizes can be burdensome. This size issue can hinder efficient document sharing and storage management. Fortunately, by using PDF compression methods, you can significantly reduce the size of your PDF files.

This tutorial will explore how to use IronPDF for effective PDF compression. We'll provide you with code examples that you can easily adapt for use in your projects, helping you shrink PDF file sizes proficiently.

## IronPDF: PDF Library

Discover IronPDF, a powerful and flexible Python library for PDF handling. IronPDF allows you to create, manipulate, compress, and read PDF documents. It comes packed with features designed to simplify your PDF management tasks.

A key feature of IronPDF is its superior compression capabilities, which let you reduce the size of existing PDFs while maintaining high quality. This feature is especially useful for large documents that need to be transferred quickly via the web or email.

## Install IronPDF via Pip

Install IronPDF simpl by running this command:

```shell
pip install ironpdf
```

IronPDF for Python uses IronPDF .NET library, particularly targeting .NET 6.0. Make sure to install the .NET 6.0 SDK on your system to use IronPDF for Python. You can download it from the [official Microsoft website](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).

## PDF Compression with IronPDF in Python

Below is the Python code that demonstrates how to compress PDF files using the IronPDF library.

```python
from ironpdf import PdfDocument

# Open the PDF document from a specified location

pdf = PdfDocument("Image based PDF.pdf")

# Compress the PDF images while setting a lower quality value at 60 (max is 100) for increased compression

pdf.CompressImages(60)
pdf.SaveAs("document_compressed.pdf")

# A different approach is chosen here by applying both compression and downscaling resolution based on visibility

pdf.CompressImages(90, True)
pdf.SaveAs("Compressed.pdf")
```

### Explanation

- **Loading the PDF**: The script begins by loading a PDF named "Image based PDF.pdf".
- **CompressImages**: Using the `CompressImages` function, images within the PDF are compressed. The quality setting can vary from 1 to 100, where 100 preserves the original quality.
- **Saving the Compressed PDF**: The document is then saved under the name "document_compressed.pdf".
- **Alternative Compression**: An alternative compression technique is used in the second `CompressImages` call, potentially altering the image resolution based on its display size.

You are encouraged to compare the original and compressed PDFs to see the differences in file size and image clarity.

### Before Compression

![Original PDF](https://ironpdf.com/static-assets/ironpdf-python/howto/python-compress-pdf/python-compress-pdf-1.webp)

### After Compression

![Compressed PDF Output](https://ironpdf.com/static-assets/ironpdf-python/howto/python-compress-pdf/python-compress-pdf-2.webp)

## Conclusion

IronPDF serves as an effective and economical solution for compressing PDFs in Python. It boasts a variety of features, like page manipulation, HTML to PDF conversion, and image compression. IronPDF stands out for developers looking for a budget-friendly PDF compression tool.

Starting at `$liteLicense`, IronPDF presents an economical [licensing option](https://ironpdf.com/python/licensing/), providing access to top-notch software solutions affordably. With its dependable optimization features, IronPDF is perfect for developers requiring simplified PDF compression.