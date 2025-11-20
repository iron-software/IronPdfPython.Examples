# Generating PDF Files in Python

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***


Incorporating PDF creation capabilities into your Python applications can significantly enhance functionality, particularly in tasks such as producing invoices, reports, and other documents dynamically.

This guide will demonstrate how to leverage IronPDF in Python scripts to create PDF documents programmatically.

## Overview of IronPDF for Python

IronPDF stands out as a robust Python library tailored for generating PDFs from HTML code. It offers intuitive APIs that simplify the generation and modification of PDFs, boasting capabilities such as:

1. Embedding text, images, and various content types.
2. Customizing fonts, colors, and managing overall document layout.

IronPDF integrates smoothly with [.NET](https://ironpdf.com/), [Java](https://ironpdf.com/java/), and [Python](https://ironpdf.com/python/), making it a versatile choice for PDF creation across different programming environments.

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

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

from ironpdf import *
```

Next, activate IronPDF by assigning your license key to the `LicenseKey` attribute of `License`:

```python
# Set the IronPDF license key

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

Obtain a license key by [purchasing](https://ironpdf.com/python/licensing/) or acquiring a [free trial key](https://ironpdf.com/python/licensing/).

## HTML String to PDF Conversion

Convert HTML markup into a PDF document using the `RenderHtmlAsPdf` method:

```python
# Initialize the PDF Renderer

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()

# Convert HTML string to PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is an example HTML string.</p>")
```

Then, save the newly created PDF file:

```python
# Save the PDF document

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("htmlstring_to_pdf.pdf")
```

The saved file, `"htmlstring_to_pdf.pdf"`, retains the HTML content it was generated from.

## Create PDF from Local HTML File

Convert a local HTML file to a PDF:

```python
# Initialize the PDF Renderer

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()

# Create a PDF from a local HTML file

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderHtmlFileAsPdf("example.html")

# Save the PDF document

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("htmlfile_to_pdf.pdf")
```

IronPDF processes the HTML content—rendering styles and scripts like a browser—to product an accurate PDF rendition.

## Generate PDF from a Web URL

Create a PDF from a webpage using `RenderUrlAsPdf`:

```python
# Initialize the PDF Renderer

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()

# Convert URL to PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")

# Save the PDF document

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("url.pdf")
```

More details on web page to PDF conversion can be found [here](https://ironpdf.com/python/examples/converting-a-url-to-a-pdf/).

## PDF Formatting Options

Tailor the PDF appearance using the `RenderingOptions` attribute. Change settings like orientation, page size, and margins. Consult the [formatting guide](https://ironpdf.com/python/examples/pdf-generation-settings/) for details.

## Adding Password Protection to PDFs

Secure your PDF with a password using `SecuritySettings`:

```python
# Adding password security to a PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SecuritySettings.UserPassword = "sharable"

# Save the protected PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("protected.pdf")
```

When opened, the PDF will prompt for the password "sharable" to allow access.

The full tutorial source code including password security and other functionalities is encapsulated in the example below, ensuring a comprehensive guide on using IronPDF in Python applications to create and manage PDF documents effectively.

*[Download the software product.](https://ironpdf.com/downloads/python-create-pdf.zip)*