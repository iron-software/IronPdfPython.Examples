# HTML to PDF Conversion Using Python

> Full guide: [HTML to PDF Conversion Using Python](https://ironpdf.com/tutorials/html-to-pdf/)


This document provides a guide for Python developers on how to use the IronPDF library to convert HTML content into PDF documents of superior quality.

IronPDF is an extensive library designed for converting and processing PDF documents and supports several programming languages, such as [.NET](https://ironpdf.com/), [Java](https://ironpdf.com/java/), and [Python](https://ironpdf.com/python/). This guide focuses on the Python implementation of IronPDF for transforming HTML code, whether from files or direct HTML strings, into PDFs.

For those interested in .NET implementations, consider checking out the [HTML to PDF conversion in .NET tutorial](https://ironpdf.com/tutorials/html-to-pdf/).

---

### Overview

---

### Getting Started

## Step 1: Installation of IronPDF Python Library

To incorporate IronPDF into your Python environment, the `pip` package manager offers a straightforward installation approach. Enter the following command in your terminal:

```shell
pip install ironpdf
```

For installing a specific release of IronPDF, adjust the command as follows:

```shell
pip install ironpdf==2023.x.x
```

It's important to note that IronPDF for Python operates on top of the .NET 6.0 framework, so ensure that the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) is installed on your system.

---

### Practical Guide and Examples

## Step 2: HTML to PDF Conversion Techniques

IronPDF excels in converting HTML to PDF using the `ChromePdfRenderer` and `PdfDocument` classes, supporting various conversion scenarios:

- Transforming HTML strings or markup into PDF
- Converting HTML files or zip archives into PDF
- Transforming URLs into PDFs

Each case is discussed briefly below, with links to additional resources.

### 2.1 Load the IronPDF Module

Begin by importing IronPDF at the start of your Python files where it will be utilized:

```python
from ironpdf import *
```

### 2.2 Set Up Your License Key (Optional)

IronPDF is freely usable, but free usage introduces a watermark on the resulting PDFs.

```html
<div style="text-align: center;">
    <iframe src="https://ironpdf.com/static-assets/ironpdf-python/tutorials/html-to-pdf/html-to-pdf-no-license.pdf" width="100%" height="500px"></iframe>
    <p>For a watermark-free experience, consider visiting our <a href="https://ironpdf.com/python/licensing/">licensing page</a>.</p>
</div>
```

To produce watermark-free PDFs:

```python
License.LicenseKey = "YOUR-LICENSE-KEY"
```

### 2.3 Configure Log File Location (Optional)

Customize logging options in IronPDF by setting the log file path and mode:

```python
Logger.EnableDebugging = True
Logger.LogFilePath = "Custom.log"
Logger.LoggingMode = Logger.LoggingModes.All
```

### 2.4 Generate PDF from HTML String

To convert a simple HTML snippet to PDF:

```python
from ironpdf import *

renderer = ChromePdfRenderer()
pdf = renderer.RenderHtmlAsPdf("<h1>Welcome to IronPDF!</h1>")
pdf.SaveAs("output.pdf")
```

![Conversion Preview](https://ironpdf.com/static-assets/ironpdf-java/tutorials/html-to-pdf/html-to-pdf-html-string-to-pdf.webp)
_The `RenderHtmlAsPdf` method ensures precise renderings of HTML content, complete with CSS and JavaScript._

For increased control, specify a base path to load external resources:

```python
html_content = """
<html>
   <head>
      <title>Welcome Page</title>
      <link rel='stylesheet' href='assets/main.css'>
   </head>
   <body>
      <h1>Welcome to IronPDF!</h1>
      <img src='assets/logo.png'>
   </body>
</html>
"""

pdf = renderer.RenderHtmlAsPdf(html_content)
pdf.SaveAs("welcome_output.pdf")
```

### 2.5 Generate PDF from a URL

Convert a live webpage to a PDF:

```python
pdf = renderer.RenderUrlAsPdf("https://en.wikipedia.org/wiki/PDF")
pdf.SaveAs("wikipedia_pdf.pdf")
```

### 2.6 Generate PDF from an HTML File

For converting locally stored HTML files:

```python
pdf = renderer.RenderHtmlFileAsPdf("invoices/SampleInvoice.html")
pdf.SaveAs("converted_invoice.pdf")
```

IronPDF automatically handles resource loading and integration, ensuring a faithful PDF representation of the original HTML.

## Further Exploration

Dive deeper into IronPDF's functionalities:

- Experiment with [customizing PDF settings](https://ironpdf.com/python/examples/pdf-generation-settings/).
- Add [personalized headers and footers](https://ironpdf.com/python/examples/html-headers-and-footers/), adjust margins ([IronPDF custom margins](https://ironpdf.com/python/examples/ironpdf-set-custom-margins/)) and set custom page dimensions ([custom paper sizes](https://ironpdf.com/python/examples/custom-pdf-paper-size/)).
- Additional features like [watermarking](https://ironpdf.com/python/examples/pdf-watermarking/), text extraction ([extract PDF text](https://ironpdf.com/python/examples/extract-pdf-text/)), file size optimization ([PDF compression](https://ironpdf.com/python/examples/pdf-compression/)), and direct printing ([print PDFs with Python](https://ironpdf.com/how-to/python-print-pdf/)).

*You can [download IronPDF here](https://ironpdf.com/downloads/python-extract-text-from-pdf.zip).*

Explore these resources to use the full potential of PDF generation and manipulation with IronPDF.