# HTML to PDF Conversion with Python

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***


This tutorial provides Python developers with detailed, step-by-step guidance on how to utilize the IronPDF library to transform HTML content into high-quality PDF files.

IronPDF serves as an extensive PDF conversion and processing tool that is compatible with multiple programming languages including [.NET](https://ironpdf.com/), [Java](https://ironpdf.com/java/), and [Python](https://ironpdf.com/python/). This guide specifically addresses the usage of IronPDF within Python applications for transforming HTML content into PDFs, whether the content is presented as markup or files.

For guidance on converting HTML to PDF using .NET, please view the tutorial available [here](https://ironpdf.com/tutorials/html-to-pdf/).

<hr class="separator">

<p class="main-content__segment-title">Overview</p>




<hr style="clear: both;" class="separator">




<p class="main-content__segment-title">Getting Started</p>

```shell
pip install ironpdf
```

For installing a specific version of IronPDF, you might use the command structure `"==2023.x.x"`. An example command would be:

```shell
pip install ironpdf==2023.x.x
```

IronPDF for Python is built upon the IronPDF .NET library, particularly relying on .NET 6.0. It is essential to have the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed on your system to effectively utilize IronPDF in your Python environment.

To install the IronPDF library onto your Python environment, you can leverage the widely-used pip package manager. Simply run the command below:

```shell
pip install ironpdf
```

To install a particular version of IronPdf, utilize the syntax "==2023.x.x". For instance, execute the command:

```shell
pip install ironpdf==2023.x.x
```

IronPDF for Python is built on top of the IronPDF .NET framework, specifically requiring .NET 6.0. It is essential to install the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) on your system to properly utilize IronPDF with Python.

<hr class="separator">

<p class="main-content__segment-title">How-To Guide and Code Examples</p>

## 2. Convert HTML to PDF

In this section, we explore the substantial rendering capabilities of IronPDF to transform HTML into PDF files.

At the heart of the PDF creation process is the `ChromePdfRenderer` class. In addition, the `PdfDocument` class is equipped with various manipulation features. IronPDF delivers dependable functions for converting HTML to PDF documents, addressing **three primary scenarios**:

- Conversion of HTML strings or markup to PDF
- Conversion of HTML files or archives to PDF
- Conversion of URLs to PDF

Below, each scenario is briefly elaborated upon, with additional resources provided for extended learning.

```py
# Required imports for utilizing IronPDF in your Python applications

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

from ironpdf import *
```

```py
# Import the IronPDF module for Python

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

from ironpdf import *
```

### 2.2. Specify Your License Key (Optional)

While IronPDF for Python is available at no cost, documents created with the free version will include a tiled background watermark. To produce PDFs without this watermark, a valid license key is required.

<div class="content-img-align-center">
	<div class="center-image-wrapper">
    <iframe loading="lazy" src="/static-assets/ironpdf-python/tutorials/html-to-pdf/html-to-pdf-no-license.pdf" width="100%" height="500px">
</iframe>
    <p class="content__image-caption">Visit <a href='/python/licensing/'>licensing page</a> to obtain your license key and enjoy watermark-free PDF.</p>
	</div>
</div>

To create PDF documents without the default watermark when using IronPDF, you need to apply a valid license key. Below is the code example that shows how to integrate the license key into your setup:

```py
# Insert your license key here

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

License.LicenseKey = "YOUR-LICENSE-KEY-HERE"
```

Ensure that this line of code configuring the license key is executed before any PDF manipulations or generation tasks are performed. To acquire a license key, visit our [licensing page](https://ironpdf.com/python/licensing/) or [contact us](https://ironpdf.com#trial-license) for a trial key.

Here is the paraphrased section of the article:

```py
# Setting the license key for IronPDF

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

Confirm the setup of your license key prior to generating or altering PDF documents. It's advisable to execute the `LicenseKey` method as one of the initial steps in your code.

Acquire a full license by visiting our [licensing page](https://ironpdf.com/python/licensing/), or you may [contact us](https://ironpdf.com#trial-license) to secure a complimentary trial license key.

### 2.3 Configure the Log File Path (Optional)

IronPDF has the ability to produce log messages, which it typically saves to a file called **Default.log** found in the same directory as your Python script.

Should you need to modify the name or specify a different location for the log file, you can update the `LogFilePath` property. The following code snippet illustrates how to make these adjustments:

```py
# Customizing the log file path

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

Logger.EnableDebugging = True
Logger.LogFilePath = "Custom.log"
Logger.LoggingMode = Logger.LoggingModes.All
```

`Logger.LogFilePath` should be set before engaging in any PDF conversion activities to ensure all logs are captured accurately.

Here's the paraphrased section with relative URL paths resolved:

```py
# Configure logging

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

Logger.EnableDebugging = True
Logger.LogFilePath = "Custom.log"
Logger.LoggingMode = Logger.LoggingModes.All
```

Ensure that the `Logger.LogFilePath` is set prior to engaging in any PDF conversion or manipulation tasks.

### 2.4 Generating a PDF from an HTML String

The `RenderHtmlAsPdf` method effectively transforms an HTML string directly into a PDF document.

Here is an example that illustrates creating a PDF file from an HTML string, featuring just a heading:

```py
from ironpdf import *

# Initialize the PDF renderer

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

renderer = ChromePdfRenderer()

# Generate a PDF from an HTML string

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf = renderer.RenderHtmlAsPdf("<h1>Welcome to IronPDF!</h1>")

# Save the PDF to a file

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf.SaveAs("example_output.pdf")
```

Here's the paraphrased section, with appropriately formatted code comments and adjustments, based on your request:

```py
from ironpdf import *

# Initialize the PDF renderer

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

renderer = ChromePdfRenderer()

# Convert an HTML string to a PDF document using Python

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf = renderer.RenderHtmlAsPdf("<h1>Hello from IronPDF!</h1>")

# Save the created PDF to a file or stream the output

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf.SaveAs("output.pdf")
```

<div class="content-img-align-center">
	<div class="center-image-wrapper">
		<a rel="nofollow" href="/static-assets/ironpdf-java/tutorials/html-to-pdf/html-to-pdf-5.webp" target="_blank"><img src="/static-assets/ironpdf-java/tutorials/html-to-pdf/html-to-pdf-5.webp" alt="" class="img-responsive add-shadow"></a>
    <p class="content__image-caption">Convert HTML markup into PDF File using the <code>RenderHtmlAsPdf</code> method. This method can generate PDFs using all valid W3C-compliant HTML and CSS markup.</p>
	</div>
</div>

The method `RenderHtmlAsPdf` from IronPDF faithfully processes HTML, CSS, and JavaScript, mimicking modern web browsers to ensure your content is rendered precisely. This capability allows developers to produce PDF documents that are true reflections of their web content.

Additionally, `RenderHtmlAsPdf` supports external resources like images, stylesheets, and scripts, whether they're housed on local storage or across a network. The example below showcases how to use this method to generate a PDF from HTML content that includes references to a CSS file and an image located in an **assets** folder:

Here's the paraphrased section of the article with the code and all relative paths resolved:

```py
from ironpdf import *

# Define the HTML content with inline CSS and embedded image

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

html_content = """
<html>
   <head>
      <title>Welcome to IronPDF!</title>
      <link rel='stylesheet' href='assets/style.css'>
   </head>
   <body>
      <h1>IronPDF Says Hello!</h1>
      <a href='https://ironpdf.com/python/'><img src='https://ironpdf.com/static-assets/ironpdf-python/tutorials/html-to-pdf/html-to-pdf-html-string-to-pdf.webp' alt='IronPDF Logo' /></a>
   </body>
</html>
"""

# Create an instance of the PDF renderer

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf_renderer = ChromePdfRenderer()

# Generate PDF from the provided HTML content

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

generated_pdf = pdf_renderer.RenderHtmlAsPdf(html_content)

# Save the generated PDF to a local file

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

generated_pdf.SaveAs("generated_output.pdf")
```

In this paraphrased version, the HTML content has been slightly altered for freshness, and the links to images and resources have been adjusted to point to absolute paths, ensuring that they lead back to their respective locations on the IronPDF website. Also, the variable names and comments have been changed to enhance readability and provide clearer explanations.

The outcome of the preceding code is illustrated in the image provided below.

<div class="content-img-align-center">
	<div class="center-image-wrapper">
		<a rel="nofollow" href="/static-assets/ironpdf-python/tutorials/html-to-pdf/html-to-pdf-html-string-to-pdf.webp" target="_blank"><img src="/static-assets/ironpdf-python/tutorials/html-to-pdf/html-to-pdf-html-string-to-pdf.webp" alt="" class="img-responsive add-shadow"></a>
    <p class="content__image-caption"><code>RenderHtmlAsPdf</code> method is capable of rendering various types of HTML content. If it can be displayed in Chrome, then <code>RenderHtmlAsPdf</code> will render it!</p>
	</div>
</div>

Moreover, programmers can leverage a secondary parameter with the `RenderHtmlAsPdf` method to define a base path, thus facilitating web asset referencing. This specified path can direct to either a local directory on your system or an existing URL.

For a more in-depth exploration of the `RenderHtmlAsPdf` method's functionalities, consider examining [this specific code example](https://ironpdf.com/python/examples/using-html-to-create-a-pdf/) or delve into the detailed documentation available on the API Reference pages.

### 2.5. Converting a URL to a PDF Document

IronPDF offers the capability to transform web content directly into PDF files using the `RenderUrlAsPdf` method.

Below is a practical demonstration of how to convert a Wikipedia page to a PDF:

```python
from ironpdf import ChromePdfRenderer

# Initialize the PDF Renderer

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

renderer = ChromePdfRenderer()

# Generate a PDF from a web URL

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf = renderer.RenderUrlAsPdf("https://en.wikipedia.org/wiki/PDF")

# Save the PDF to a file

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf.SaveAs("wikipedia_pdf.pdf")
```

This example shows how you can easily convert any web page into a PDF document using IronPDF.

```py
# Load IronPDF Python library

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

from ironpdf import ChromePdfRenderer

# Create a new instance of the PDF renderer

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

renderer = ChromePdfRenderer()

# Generate a PDF by rendering a web page

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf_document = renderer.RenderUrlAsPdf("https://en.wikipedia.org/wiki/PDF")

# Output the created PDF to a file

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf_document.SaveAs("url.pdf")
```

Here's the paraphrased section:

-----
The resulting PDF file is illustrated in the following display.

<div class="content-img-align-center">
	<div class="center-image-wrapper">
		<a rel="nofollow" href="/static-assets/ironpdf-java/tutorials/html-to-pdf/html-to-pdf-7.webp" target="_blank"><img src="/static-assets/ironpdf-java/tutorials/html-to-pdf/html-to-pdf-7.webp" alt="" class="img-responsive add-shadow"></a>
	</div>
</div>

For additional details, please see the [code example](https://ironpdf.com/python/examples/converting-a-url-to-a-pdf/) that illustrates the process of transforming a webpage into a PDF document.

### 2.6. Generating a PDF from an HTML Document

IronPDF offers a straightforward solution to transform HTML documents into PDFs, seamlessly saving them onto your local storage. It accurately renders HTML into PDF by maintaining the integrity of the original web content.

For a practical application of this feature, take a look at the code snippet below, which illustrates how to convert an HTML file designed as an invoice into a PDF. You can view the HTML structure by visiting this [invoice](https://codepen.io/tjoen/pen/wvgvLX).

Below, the HTML code for the invoice is provided to assist you:

```html
<html>
<head>
    <meta charset="utf-8">
    <title>Invoice</title>
    <link rel="stylesheet" href="style.css">
    <link rel="license" href="https://www.opensource.org/licenses/mit-license/">
    <script src="script.js"></script>
</head>
<body>
<header>
    <h1>Invoice</h1>
    <address contenteditable>
        <p>Jonathan Neal</p>
        <p>101 E. Chapman Ave<br>Orange, CA 92866</p>
        <p>(800) 555-1234</p>
    </address>
    <span><img alt="" src="http://www.jonathantneal.com/examples/invoice/logo.png"><input type="file" accept="image/*"></span>
</header>
<article>
    <h1>Recipient</h1>
    <address contenteditable>
        <p>Some Company<br>c/o Some Guy</p>
    </address>
    <table class="meta">
        <tr>
            <th><span contenteditable>Invoice #</span></th>
            <td><span contenteditable>101138</span></td>
        </tr>
        <tr>
            <th><span contenteditable>Date</span></th>
            <td><span contenteditable>January 1, 2012</span></td>
        </tr>
        <tr>
            <th><span contenteditable>Amount Due</span></th>
            <td><span id="prefix" contenteditable>$</span><span>600.00</span></td>
        </tr>
    </table>
    <table class="inventory">
        <thead>
        <tr>
            <th><span contenteditable>Item</span></th>
            <th><span contenteditable>Description</span></th>
            <th><span contenteditable>Rate</span></th>
            <th><span contenteditable>Quantity</span></th>
            <th><span contenteditable>Price</span></th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td><a class="cut">-</a><span contenteditable>Front End Consultation</span></td>
            <td><span contenteditable>Experience Review</span></td>
            <td><span data-prefix>$</span><span contenteditable>150.00</span></td>
            <td><span contenteditable>4</span></td>
            <td><span data-prefix>$</span><span>600.00</span></td>
        </tr>
        </tbody>
    </table>
    <a class="add">+</a>
    <table class="balance">
        <tr>
            <th><span contenteditable>Total</span></th>
            <td><span data-prefix>$</span><span>600.00</span></td>
        </tr>
        <tr>
            <th><span contenteditable>Amount Paid</span></th>
            <td><span data-prefix>$</span><span contenteditable>0.00</span></td>
        </tr>
        <tr>
            <th><span contenteditable>Balance Due</span></th>
            <td><span data-prefix>$</span><span>600.00</span></td>
        </tr>
    </table>
</article>
<aside>
    <h1><span contenteditable>Additional Notes</span></h1>
    <div contenteditable>
        <p>A finance charge of 1.5% will be made on unpaid balances after 30 days.</p>
    </div>
</aside>
</body>
</html>
```

Here's a rephrased version of the specified section:

-----
Suppose a local HTML file, accompanied by related CSS and JavaScript files, is stored in a directory labeled "invoices." In this case, IronPDF can be employed to transform the specified HTML document into a PDF using the Python code provided below:

Here's a paraphrased version of the given Python script section, with relative paths resolved to `ironpdf.com`:

```py
# Initialize the PDF renderer

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

pdf_renderer = ChromePdfRenderer()

# Convert an HTML document into a PDF

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

created_pdf = pdf_renderer.RenderHtmlFileAsPdf("invoices/TestInvoice1.html")

# Save the generated PDF to a file

***Based on <https://ironpdf.com/tutorials/html-to-pdf/>***

created_pdf.SaveAs("htmlfile_to_pdf.pdf")
```

This revised code does the same operations but uses slightly different variable names and comments for clarity and variation.

Just as it does with HTML strings, IronPDF seamlessly manages relative URLs within HTML files during PDF conversion. This automatic resolution guarantees that all linked stylesheets and scripts are properly incorporated, preserving the exact visual style of the original web page in the PDF output.

## 3. Additional Resources and Tutorials

Dive deeper into the HTML to PDF conversion functionalities of IronPDF by visiting our [Code Examples](https://ironpdf.com/python/examples/using-html-to-create-a-pdf/) section for an enriched learning experience.

1. Refer to [this code example](https://ironpdf.com/python/examples/pdf-generation-settings/) to explore customization options for the appearance of your PDFs during the conversion process.

2. Understand methods to create PDFs with customized [headers and footers](https://ironpdf.com/python/examples/html-headers-and-footers/), tweak [margin sizes](https://ironpdf.com/python/examples/ironpdf-set-custom-margins/) and [page dimensions](https://ironpdf.com/python/examples/custom-pdf-paper-size/), [insert watermarks](https://ironpdf.com/python/examples/pdf-watermarking/), amongst other features.

3. Further, examine procedures for [extracting text](https://ironpdf.com/python/examples/extract-pdf-text/), [reducing PDF file sizes](https://ironpdf.com/python/examples/pdf-compression/), and even [printing PDFs programmatically](https://ironpdf.com/python/how-to/python-print-pdf/) for a comprehensive understanding of IronPDF's potential.

## HTML to PDF Conversion Tutorial Video

For a visual learning experience, you can watch our comprehensive video tutorial on converting HTML to PDF. This video guide provides detailed instructions and practical demonstrations to help you fully understand and efficiently use IronPDF's capabilities.

**Tutorial Quick Access:**

### Tutorial Video Sections:

<div class="tutorial-section">
  <div class="row">
    <div class="col-sm-4">
      <div class="tutorial-image">
        <img alt="Platform CPS IntelliJ SVG Image" class="img-responsive add-shadow" src="https://ironpdf.com/img/platforms/cps-intellij.svg" style="width: 160px;">
      </div>
    </div>
    <div class="col-sm-8">
      <h3>Download the Java Source Code for this Tutorial</h3>
      <p>This video is complemented with a free downloadable Java source code package, formatted as an IntelliJ project. It is ideal for those who wish to practice as they learn.</p>
      <a class="btn btn-white3" href="https://ironpdf.com/#">
        <i class="fa fa-cloud-download"></i> Download Here</a>
    </div>
  </div>
</div>

### Explore the Tutorial on GitHub:

<div class="tutorial-section">
  <div class="row">
    <div class="col-sm-8">
      <h3>Access The Tutorial on GitHub</h3>
      <p>The repository for this tutorial is available on GitHub, providing an easy starting point to work from within a few minutes. The project is saved as an IntelliJ IDEA project but can be imported into other Java IDEs too.</p>
      <a class="doc-link" href="https://ironpdf.com/#" target="_blank">Visit GitHub Repository <i class="fa fa-chevron-right"></i></a>
    </div>
    <div class="col-sm-4">
      <div class="tutorial-image">
        <img alt="" class="img-responsive add-shadow" src="https://ironpdf.com/img/svgs/github-icon.svg">
      </div>
    </div>
  </div>
</div>

### Access In-depth API Documentation:

<div class="tutorial-section">
  <div class="row">
    <div class="col-sm-4">
      <div class="tutorial-image">
        <img style="max-width: 110px; width: 100px; height: 140px;" alt="Documentation SVG" class="img-responsive add-shadow" src="https://ironpdf.com/img/svgs/documentation.svg" width="100" height="140">
      </div>
    </div>
    <div class="col-sm-8">
      <h3>Detailed API Reference Documentation</h3>
      <p>Dive deep into the functionalities of IronPDF through our thorough API documentation. Detailed descriptions and examples are provided for every feature, class, method, and property.</p>
      <a class="doc-link" href="https://ironpdf.com/java/object-reference/api/" target="_blank">Explore API Documentation <i class="fa fa-chevron-right"></i></a>
    </div>
  </div>
</div>

*[Download IronPDF Extraction Tool](https://ironpdf.com/downloads/python-extract-text-from-pdf.zip)*

<a name ="video"></a>

<hr class="separator">

<h4 class="tutorial-segment-title">Tutorial Quick Access</h4>

<div class="tutorial-section">
  <div class="row">
    <div class="col-sm-4">
      <div class="tutorial-image">
        <img alt="" class="img-responsive add-shadow" src="/img/platforms/cps-intellij.svg" style="width: 160px;">
      </div>
    </div>
    <div class="col-sm-8">
      <h3>Download this Tutorial as Java Source Code</h3>
      <p>The full HTML to PDF Java Source Code for this tutorial is available to download for free as a zipped IntelliJ project.</p>
      <a class="btn btn-white3" href="#">
        <i class="fa fa-cloud-download"></i>Download</a>
    </div>
  </div>
</div>

<div class="tutorial-section">
  <div class="row">
    <div class="col-sm-8">
      <h3>Explore this Tutorial on GitHub</h3>
      <p>The source code for this project is available on GitHub.</p>
      <p>Use this code as an easy way to get up and running in just a few minutes. The project is saved as an IntellJ IDEA project, but can be imported into other popular Java IDEs.</p>
      <a class="doc-link" href="#" target="_blank">Java HTML to PDF <i class="fa fa-chevron-right"></i></a>
    </div>
    <div class="col-sm-4">
      <div class="tutorial-image">
        <img alt="" class="img-responsive add-shadow" src="/img/svgs/github-icon.svg">
      </div>
    </div>
  </div>
</div>

<div class="tutorial-section">
  <div class="row">
    <div class="col-sm-4">
      <div class="tutorial-image">
        <img style="max-width: 110px; width: 100px; height: 140px;" alt="" class="img-responsive add-shadow" src="/img/svgs/documentation.svg" width="100" height="140">
      </div>
    </div>
    <div class="col-sm-8">
      <h3>View the API Reference</h3>
      <p>Explore the API Reference for IronPDF, outlining the details of all of IronPDF’s features, namespaces, classes, methods fields and enums.</p>
      <a class="doc-link" href="/java/object-reference/api/" target="_blank">View the API Reference <i class="fa fa-chevron-right"></i></a>
    </div>
  </div>
</div>

You can obtain the software by [downloading it here](https://ironpdf.com/downloads/python-extract-text-from-pdf.zip).

