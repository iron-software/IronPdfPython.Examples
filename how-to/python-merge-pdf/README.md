# Merge Multiple PDF Documents into a Unified PDF via Python

***Based on <https://ironpdf.com/how-to/python-merge-pdf/>***


The Portable Document Format (PDF) is widely adopted for its robust portrayal of text and graphics consistent across various devices and operating systems.

Python, noted for being a high-level programming language, shines with its flexibility and accessibility when operating across different computing environments. However, merging source PDFs or handling files can be intricate in Python. This is where IronPDF comes into play – a Python library that simplifies PDF manipulation.

In this tutorial, we'll guide you on how to install IronPDF for Python and use it to combine several PDFs into one singular file.

## IronPDF: A Python PDF Library

IronPDF stands out as a comprehensive Python library dedicated to PDF operations, allowing developers to effortlessly create, read, and modify PDF documents. Whether generating PDFs from the ground up or transforming web content via HTML, CSS, and JavaScript into PDFs, IronPDF equips developers with the tools they need. It also allows for the straightforward merging of multiple PDFs into one file and operates independently of any external frameworks.

Given its compatibility with **Python 3.x** and support for both Windows and Linux systems, IronPDF can be utilized across different platforms.

## Installation Guide for IronPDF

To initiate using IronPDF, first install the library through pip by executing this command:

```shell
pip install ironpdf
```

Now, integrate IronPDF in your Python project by including:

```python
from ironpdf import *
```

## Merging Two PDFs Using IronPDF

Merging PDFs involves creating individual PDF files first, then combining them into one. Here's how you can achieve this:

```python
html_a = """<p> [PDF_A] </p>
            <p> [PDF_A] 1st Page </p>
            <div style='page-break-after: always;'></div>
            <p> [PDF_A] 2nd Page</p>"""

html_b = """<p> [PDF_B] </p>
            <p> [PDF_B] 1st Page </p>
            <div style='page-break-after: always;'></div>
            <p> [PDF_B] 2nd Page</p>"""

renderer = ChromePdfRenderer()

pdfdoc_a = renderer.RenderHtmlAsPdf(html_a)
pdfdoc_b = renderer.RenderHtmlAsPdf(html_b)
merged = PdfDocument.Merge(pdfdoc_a, pdfdoc_b)
```

In the example, each HTML contains data for two pages which are converted into separate PDF files using the `RenderHtmlAsPdf` method. These are then merged into a single PDF document using `PdfDocument.Merge`.

### Saving the Merged PDF File

To finalize and save your merged PDF, utilize:

```python
merged.SaveAs("Merged.pdf")
```

Here’s the result of the merged documents:

<div class="content-img-align-center">
	<div class="center-image-wrapper">
		<a rel="nofollow" href="https://ironpdf.com/static-assets/ironpdf-java/howto/java-merge-pdf/java-merge-pdf-2.webp" target="_blank"><img src="https://ironpdf.com/static-assets/ironpdf-java/howto/java-merge-pdf/java-merge-pdf-2.webp" alt="Python Merge PDFs - Figure 2: Merge Multiple PDF Documents" class="img-responsive add-shadow"></a>
    <p class="content__image-caption">Merge Two PDF Documents</p>
	</div>
</div>

## How to Merge More Than Two PDF Documents

For merging more than two PDFs, you'd typically:

- Compile a list of the PdfDocument objects you intend to merge
- Use this list as the argument in the `PdfDocument.Merge` method

Example code to demonstrate this:

```python
html_c = """<p> [PDF_C] </p>
            <p> [PDF_C] 1st Page </p>
            <div style='page-break-after: always;'></div>
            <p> [PDF_C] 2nd Page</p>"""

renderer = ChromePdfRenderer()

pdfdoc_a = renderer.RenderHtmlAsPdf(html_a)
pdfdoc_b = renderer.RenderHtmlAsPdf(html_b)
pdfdoc_c = renderer.RenderHtmlAsPdf(html_c)

pdfs = List [PdfDocument]()
pdfs.Add(pdfdoc_a)
pdfs.Add(pdfdoc_b)
pdfs.Add(pdfdoc_c)

pdf = PdfDocument.Merge(pdfs)
pdf.SaveAs("merged.pdf")
```

This example extends our earlier method by introducing three PDF documents merged through a list.

<div class="content-img-align-center">
	<div class="center-image-wrapper">
		<a rel="nofollow" href="https://ironpdf.com/static-assets/ironpdf-java/howto/java-merge-pdf/java-merge-pdf-3.webp" target="_blank"><img src="https://ironpdf.com/static-assets/ironpdf-java/howto/java-merge-pdf/java-merge-pdf-3.webp" alt="Python Merge PDFs - Figure 3: Merge More Than Two PDF Documents" class="img-responsive add-shadow"></a>
    <p class="content__image-caption">Merge More Than Two PDF Files</p>
	</div>
</div>

## Concluding Thoughts

From installation to complex merging tasks, this guide has detailed using IronPDF in Python for manipulating and merging PDF files.

IronPDF provides a potent suite for managing PDFs in Python environments, enabling seamless transitions from web content to PDF and supporting a multitude of formats. Designed with modern technologies, IronPDF is a dependable option for your PDF needs.

Discover more about IronPDF and explore additional code samples at our comprehensive [Code Examples](https://ironpdf.com/python/examples/using-html-to-create-a-pdf/).

For development or commercial use, visit [Licensing Information](https://ironpdf.com/python/licensing/) for IronPDF.

*[Download the software here](https://ironpdf.com/downloads/python-merge-pdf.zip).*