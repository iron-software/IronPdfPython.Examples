# Generating PDF Files in Python

> Full guide: [Generating PDF Files in Python](https://ironpdf.com/python/how-to/python-create-pdf/)


Incorporating PDF creation capabilities into your Python applications can significantly enhance functionality, particularly in tasks such as producing invoices, reports, and other documents dynamically.

This guide creates PDF documents programmatically from a Python script with IronPDF.

## Overview of IronPDF for Python

IronPDF is a Python library that generates PDFs from HTML. Its API covers generation and modification, including:

1. Embedding text, images, and various content types.
2. Customizing fonts, colors, and managing overall document layout.

IronPDF ships for [.NET](https://ironpdf.com/), [Java](https://ironpdf.com/java/), and [Python](https://ironpdf.com/python/).

Key features of IronPDF include converting file formats, extracting text and data, and securing documents through password encryption.

## Steps to Create a PDF Document in Python

### Prerequisites

Ensure your system is equipped with the following before using IronPDF in Python:

1. `.NET 6.0 SDK`: IronPDF for Python requires the .NET 6.0 SDK, which can be downloaded from the [official Microsoft website](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).
2. `Python`: Install the latest Python 3.x from [https://www.python.org/downloads/](https://www.python.org/downloads/). Include Python in your system PATH during installation.
3. `Pip`: Typically comes with Python installations from version 3.4 onwards. Confirm if it's installed, or install separately if necessary.
4. `IronPDF Library`: Install IronPDF using pip with the following command:

```shell
pip install ironpdf
```

For systems defaulting to Python 2.x, use `pip3` instead of `pip`.

### Pre-code Configuration

Include the following import statement at the beginning of your Python script:

```python
# Import IronPDF Python Library
# This snippet is the import statement itself; the sections that follow use it.
from ironpdf import *

pass
```

Next, activate IronPDF by assigning your license key to the `LicenseKey` attribute of `License`:

```python
from ironpdf import *

# Apply your license key
License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

Obtain a license key by [purchasing](https://ironpdf.com/python/licensing/) or acquiring a [free trial key](https://ironpdf.com/python/licensing/).

## HTML String to PDF Conversion

Convert HTML markup into a PDF document using the `RenderHtmlAsPdf` method:

```python
from ironpdf import *

# Instantiate Renderer
renderer = ChromePdfRenderer()
# Create a PDF from an HTML string using Python
pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")
```

Then, save the newly created PDF file:

```python
from ironpdf import *

# The guide renders a PDF before this snippet; render one here so the
# example runs on its own.
renderer = ChromePdfRenderer()
pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")

# Export to a file or Stream
pdf.SaveAs("htmlstring_to_pdf.pdf")
```

The saved file, `"htmlstring_to_pdf.pdf"`, retains the HTML content it was generated from.

## Create PDF from Local HTML File

Convert a local HTML file to a PDF:

```python
from ironpdf import *

# Instantiate Renderer
renderer = ChromePdfRenderer()
# Create a PDF from an existing HTML file using Python
pdf = renderer.RenderHtmlFileAsPdf("example.html")
# Export to a file or Stream
pdf.SaveAs("htmlfile_to_pdf.pdf")
```

IronPDF processes the HTML content—rendering styles and scripts like a browser—to product an accurate PDF rendition.

## Generate PDF from a Web URL

Create a PDF from a webpage using `RenderUrlAsPdf`:

```python
from ironpdf import *

# Instantiate Renderer
renderer = ChromePdfRenderer()
# Create a PDF from a URL or local file path
pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")
# Export to a file or Stream
pdf.SaveAs("url.pdf")
```

More details on web page to PDF conversion can be found [here](https://ironpdf.com/python/examples/converting-a-url-to-a-pdf/).

## PDF Formatting Options

Tailor the PDF appearance using the `RenderingOptions` attribute. Change settings like orientation, page size, and margins. Consult the [formatting guide](https://ironpdf.com/python/examples/pdf-generation-settings/) for details.

## Adding Password Protection to PDFs

Secure your PDF with a password using `SecuritySettings`:

```python
from ironpdf import *

# The guide renders a PDF before this snippet; render one here so the
# example runs on its own.
renderer = ChromePdfRenderer()
pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")

# Set user password for PDF document security
pdf.SecuritySettings.UserPassword = "sharable"
# Save the password-protected PDF
pdf.SaveAs("protected.pdf")
```

When opened, the PDF will prompt for the password "sharable" to allow access.

## Complete Source Code

The listing below carries the full tutorial source, password security included.

```python
from ironpdf import *

# Apply your license key
License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"

# --- HTML string to PDF ---
renderer = ChromePdfRenderer()
pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")
pdf.SaveAs("htmlstring_to_pdf.pdf")

# --- Local HTML file to PDF ---
renderer = ChromePdfRenderer()
pdf = renderer.RenderHtmlFileAsPdf("example.html")
pdf.SaveAs("htmlfile_to_pdf.pdf")

# --- URL to PDF ---
renderer = ChromePdfRenderer()
pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")
pdf.SaveAs("url.pdf")

# --- Password-protected PDF ---
pdf.SecuritySettings.UserPassword = "sharable"
pdf.SecuritySettings.OwnerPassword = "admin123"
# The guide writes `AllowUserPrinting = True`. It is a PdfPrintSecurity
# enum, not a bool, and assigning True raises TypeError under Python.NET 3.
pdf.SecuritySettings.AllowUserPrinting = PdfPrintSecurity.FullPrintRights
pdf.SecuritySettings.AllowUserCopyPasteContent = False
pdf.SaveAs("protected.pdf")
```

*[Download the software product.](https://ironpdf.com/downloads/python-create-pdf.zip)*