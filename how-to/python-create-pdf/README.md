# How to Generate PDF Documents in Python

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***


Automating PDF document creation in Python facilitates developers to include PDF generation within their software solutions. This feature is particularly useful for automatic report, invoice, or any other PDF output generation.

This guide demonstrates how to use IronPDF in Python scripts to programmatically produce PDF files.

## IronPDF: A Python PDF Library

IronPDF is an efficient library in Python tailored for converting HTML into PDF documents. It offers straightforward APIs that allow developers to easily create and modify PDF documents, inclusive of capabilities such as:

1. Inserting text, images, and diverse content types
2. Selecting different fonts, colors, and managing the document’s layout and style.

IronPDF integrates smoothly into [.NET](https://ironpdf.com/), [Java](https://ironpdf.com/java/), and [Python](https://ironpdf.com/python/) environments, permitting diverse and adaptable PDF creation possibilities.

Further, IronPDF is enriched with features like file format transformation, effective PDF text and data retrieval, and securing PDF files through password protection.

## Step-by-Step Creation of PDF Documents in Python Scripts

### Prerequisites

Before using IronPDF in Python, ensure the installation of:

1. **.NET 6.0 SDK**: The IronPDF Python library utilizes the IronPDF .NET library, requiring the .NET 6.0 SDK on your device. Download it from the [official Microsoft site](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).
2. **Python**: Install the most recent Python 3.x from [Python's official website](https://www.python.org/downloads/). During setup, opt to add Python to the system PATH for easier command line access.
3. **Pip**: Generally included with Python 3.4 or later versions. Check if pip is present, or install it if needed.
4. **IronPDF Library**: Install IronPDF using pip with the command:

```shell
pip install ironpdf
```

If Python 2.x is default on your system, use the `pip3` command to ensure Python 3's pip is used.

### Preparation before Coding

Append the following import statement at the beginning of your script:

```py
# IronPDF Python Import

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

from ironpdf import *
```

Configure the library by setting the license key prior to other commands:

```py
# Setting the IronPDF License Key

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

To produce non-watermarked PDFs, a valid license is required. [Purchase a license](https://ironpdf.com/python/licensing/) or [get a trial license](https://ironpdf.com/python/licensing/#trial-license).

## HTML String to PDF Conversion

Execute the `RenderHtmlAsPdf` method to transform an HTML string into a PDF document.

Provide the HTML content to the function, allowing IronPDF to process and convert it into a PDF document, accessed via a `PdfDocument` instance.

```py
# PDF Rendering from HTML String

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()
pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is sample HTML content.</p>")
```

After processing, utilize the `SaveAs` method to export the PDF document locally:

```py
# Saving the PDF Document

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("output_html_to_pdf.pdf")
```

A file named **"output_html_to_pdf.pdf"** will be generated, containing the contents from the HTML input.

## Convert an HTML File to a PDF in Python

To transform a local HTML file into a PDF, use the subsequent steps:

```py
# Renderer Initialization

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()

# Generating PDF from HTML File

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderHtmlFileAsPdf("example.html")

# File Saving

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("output_htmlfile_to_pdf.pdf")
```

In the snippet above, `RenderHtmlFileAsPdf` converts an HTML file into a PDF. Specify the HTML file's path, and IronPDF renders it accurately, including all styles and behaviors as a browser would.

Finally, save the output PDF to a desired location using `SaveAs`.

## Generate a PDF from a Web URL in Python

To create a PDF from a webpage, follow the outlined approach:

```py
# Renderer Setup

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()

# PDF Creation from URL

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")

# Output to File

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("website_to_pdf.pdf")
```

Further details on converting web pages to PDFs can be found on the [Web to PDF guide](https://ironpdf.com/python/examples/converting-a-url-to-a-pdf/).

## Exploring PDF Formatting Options

For tailoring PDF appearance and layout, utilize the `RenderingOptions` facility. Modify settings such as page size, orientation, margins through this class. See the [PDF Settings guide](https://ironpdf.com/python/examples/pdf-generation-settings/) for detailed usage.

## Encrypting PDFs with Passwords

Secure your PDF file via the `SecuritySettings` mechanism:

```py
pdf.SecuritySettings.UserPassword = "sharable"
pdf.SaveAs("secure_pdf.pdf")
```

This password-protects the file requiring a password on opening. Further security details can be found [here](https://ironpdf.com/python/examples/security-and-metadata/).

Embedding a password-protected PDF for interactive use:

```html
<iframe loading="lazy" src="https://ironpdf.com/static-assets/ironpdf-python/howto/python-create-pdf-tutorial/protected.pdf" width="100%" height="500px"></iframe>
```

Visit the [security and metadata documentation](https://ironpdf.com/python/examples/security-and-metadata/) for additional adjustments.

## Complete Code

Here is a complete script showing how to create and manipulate PDFs through IronPDF:

```py
# IronPDF Python Import

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

from ironpdf import *

# Set License Key

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"

# Initialize PDF renderer

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()
# PDF from HTML String

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf = renderer.RenderHtmlAsPdf("<h1>Hello World!</h1><p>This is sample HTML content.</p>")
# Save the generated PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SaveAs("htmlstring_to_pdf.pdf")

# Another Renderer for HTML file to PDF

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()
pdf = renderer.RenderHtmlFileAsPdf("example.html")
pdf.SaveAs("htmlfile_to_pdf.pdf")

# Renderer for PDF from URL

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

renderer = ChromePdfRenderer()
pdf = renderer.RenderUrlAsPdf("https://ironpdf.com")
pdf.SaveAs("url.pdf")

# Apply password protection

***Based on <https://ironpdf.com/how-to/python-create-pdf/>***

pdf.SecuritySettings.UserPassword = "sharable"
pdf.SaveAs("secure_pdf.pdf")
```

## Conclusion

This guide outlined the workflow of creating PDF documents in Python using IronPDF. The API simplifies PDF generation from HTML content, files, and URLs. IronPDF is a commercial library requiring licensing, but a [free trial is available](https://ironpdf.com/python/licensing/#trial-license) for evaluation.

*To download the demo, visit [IronPDF Downloads](https://ironpdf.com/downloads/python-create-pdf.zip)*.