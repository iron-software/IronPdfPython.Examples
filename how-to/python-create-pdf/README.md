# Generating PDF Files with Python

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***


Creating automated PDF documents within Python-driven applications is a powerful capability, enabling developers to generate necessary reports, invoices, and other document types on-the-fly.

This guide dives into the use of IronPDF, a comprehensive tool for programmatically generating PDF files within Python environments.

## Overview of IronPDF Python Library

IronPDF excels as a Python library aimed at efficiently crafting PDFs from HTML content. Below are key features and capabilities provided by IronPDF:

1. Supports addition of diverse content types including texts and images.
2. Allows extensive customization of fonts, colors, and document layout.

The library integrates smoothly into applications across [.NET](/), [Java](/java/), and [Python](/python/) environments, offering a broad platform support for versatile PDF generation needs.

IronPDF not only facilitates robust PDF creation but also enables functionalities like file format transformation, extracting text and data from PDFs, and securing documents with password protection.

## Steps to Create a PDF in Python

### Setting Up

Ensure your system is equipped with the following to leverage IronPDF:
1. **.NET 6.0 SDK**: Necessary for IronPDF's operation as it utilizes the .NET library from IronPDF. Obtain it from the [official Microsoft site](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).
2. **Python Installation**: Install Python 3.x from the [official Python site](https://www.python.org/downloads/), ensuring to tick the option to add Python to your system PATH.
3. **Installation of Pip**: Generally included with Python 3.4 onwards. Verify its installation or install, if necessary.
4. **IronPDF Installation**: Execute the following command to install IronPDF via pip:

```shell
pip install ironpdf
```

On systems where Python 2.x is default, use `pip3` to ensure Python 3 compatibility.

### Preliminary Code Setup

Start by importing IronPDF at the beginning of your script:

```python
# Import IronPDF into Python script

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

from ironpdf import *
```

Prioritize configuring the license key to utilize IronPDF fully:

```python
# Set the IronPDF license key

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

Ensure a valid license for watermark-free PDF creation or [purchase](/python/licensing/) one, or secure [a free trial](/python/licensing/).

## Converting HTML to PDF

Turn any HTML content into a PDF with just a few lines of code using IronPDF:

```python
# Setup PDF Renderer

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()

# Convert HTML string to PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")
```

After conversion, save the PDF locally:

```python
# Save the PDF file

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("htmlstring_to_pdf.pdf")
```

This produces a PDF named **"htmlstring_to_pdf.pdf"** encapsulated from the prescribed HTML string.

## Produce PDF from an HTML File

Create a PDF from a local HTML file:

```python
# Initialize Renderer

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()

# Generate PDF from HTML file

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderHtmlFileAsPdf("example.html")

# Save the generated PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("htmlfile_to_pdf.pdf")
```

This method reads the HTML and its styling faithfully just like a browser, rendering a precise PDF output.

## Convert Webpage URL to PDF

Generate a PDF directly from a webpage URL:

```python
# Renderer initialization

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()

# Convert from URL to PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")

# Output the PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("url_to_pdf.pdf")
```

Details for converting web pages to PDFs can be found [here](/python/examples/converting-a-url-to-a-pdf/).

## Customize PDF Appearance

IronPDF's **RenderingOptions** allows detailed control over PDF formatting. Adjust settings like orientation, size, and margins for custom PDF layout. See more on this [here](/python/examples/pdf-generation-settings/).

## Secure PDFs with Passwords

Add security to your PDFs by setting a password:

```python
# Set the security password

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SecuritySettings.UserPassword = "sharable"
pdf.SaveAs("protected.pdf")
```

This method ensures your PDF can only be accessed by entering the designated password.

## Complete Source Code

The provided source demonstrates full usage of IronPDF to create, render, and secure PDF documents from various sources:

```python
# Import IronPDF into Python script

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

from ironpdf import *

# Set the IronPDF license key

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"

# Setup PDF Renderer and create PDF from HTML

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()
pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")
pdf.SaveAs("htmlstring_to_pdf.pdf")

# Repeat for HTML file

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderHtmlFileAsPdf("example.html")
pdf.SaveAs("htmlfile_to_pdf.pdf")

# URL to PDF conversion

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")
pdf.SaveAs("url_to_pdf.pdf")

# Apply security

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SecuritySettings.UserPassword = "sharable"
pdf.SaveAs("protected.pdf")
```

## Summary

This guide illustrates using the IronPDF library to efficiently craft and manipulate PDF documents in Python. From HTML strings to full web pages, IronPDF handles various input types to generate quality PDFs directly within your applications. IronPDF is a premium tool requiring a [commercial license](/python/licensing/), available for evaluation through a [free trial](/python/licensing/).

*[Download](https://ironpdf.com/downloads/python-create-pdf.zip) the software here.*