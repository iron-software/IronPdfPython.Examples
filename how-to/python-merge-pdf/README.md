# Combining PDF Documents into One Using Python

***Based on <https://ironpdf.com/how-to/python-merge-pdf/>***


The Portable Document Format (PDF) is renowned for its ability to consistently display text and graphics across various devices and software platforms.

Python is a robust high-level programming language known for its flexibility in interfacing with different computer systems. Although handling PDF files and input streams can be difficult using standard Python tools, IronPDF, a Python library, simplifies the manipulation and merging of PDF files.

In this tutorial, we will guide you on installing IronPDF and illustrate how to combine several PDF files into one using Python.


## Introduction to IronPDF for Python

IronPDF is a versatile Python library designed for comprehensive PDF manipulation. It allows for the creation, reading, and editing of PDF files with ease. You can craft new PDFs from the ground up, style them using HTML, CSS, and JavaScript, and add metadata like titles and author details. IronPDF stands out for its ability to merge multiple PDFs into one single file without needing additional frameworks.

Additionally, IronPDF supports Python 3.x and operates seamlessly across both Windows and Linux platforms, making it ideal for diverse working environments.

## Installation of IronPDF Using Pip

To integrate the IronPDF library into your workspace, use the following pip command:

```shell
pip install ironpdf
```

Ensure you include these import statements in your Python script to access IronPDF functionalities for PDF generation and merging:

```py
from ironpdf import *
```

## Steps to Combine Two PDF Files Using IronPDF

[Combining PDF Files](https://ironpdf.com/python/examples/merge-pdfs/) involves the following steps:
- Creating individual PDF files
- Merging them into one comprehensive PDF

Here’s the example code displaying this merging process:

```py
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

In this script, two HTML templates are created and then turned into separate PDF documents using the `RenderHtmlAsPdf` method. These documents are merged into a single PDF using `PdfDocument.Merge` method, which appends the second document to the first.

### Saving the Combined PDF File

To store the combined PDF to a local file, use the command:

```py
merged.SaveAs("Merged.pdf")
```

A visual representation of the output can be seen here:

<div class="content-img-align-center">
	<div class="center-image-wrapper">
		<a rel="nofollow" href="https://ironpdf.com/static-assets/ironpdf-java/howto/java-merge-pdf/java-merge-pdf-2.webp" target="_blank"><img src="https://ironpdf.com/static-assets/ironpdf-java/howto/java-merge-pdf/java-merge-pdf-2.webp" alt="Python Merge PDFs - Figure 2: Merging Multiple PDF Documents" class="img-responsive add-shadow"></a>
    <p class="content__image-caption">Merge Two PDF Documents</p>
	</div>
</div>

## Merging More Than Two PDF Files

To merge a collection of more than two PDFs in Python, follow these instructions:
- Assemble a list of PDF documents
- Utilize the list in the `PdfDocument.Merge` method for merging

Here's how that looks in code:

```py
html_a = """<p> [PDF_A] </p>
            <p> [PDF_A] 1st Page </p>
            <div style('page-break-after: always;'></div>
            <p> [PDF_A] 2nd Page</p>"""

html_b = """<p> [PDF_B] </p>
            <p> [PDF_B] 1st Page </p>
            <div style('page-break-after: always;'></div>
            <p> [PDF_B] 2nd Page</p>"""

html_c = """<p> [PDF_C] </p>
            <p> [PDF_C] 1st Page </p>
            <div style('page-break-after: always;'></div>
            <p> [PDF_C] 2nd Page</p>"""

renderer = ChromePdfRenderer()

pdfdoc_a = renderer.RenderHtmlAsPdf(html_a)
pdfdoc_b = renderer.RenderHtmlAsPdf(html_b)
pdfdoc_c = renderer.RenderHtmlAsPdf(html_c)

pdfs = List[PdfDocument]()
pdfs.Add(pdfdoc_a)
pdfs.Add(pdfdoc_b)
pdfs.Add(pdfdoc_c)
merged_doc = PdfDocument.Merge(pdfs)
merged_doc.SaveAs("merged.pdf")
```

Images for visual aid:

<div class="content-img-align-center">
	<div class="center-image-wrapper">
		<a rel="nofollow" href="https://ironpdf.com/static-assets/ironpdf-java/howto/java-merge-pdf/java-merge-pdf-3.webp" target="_blank"><img src="https://ironpdf.com/static-assets/ironpdf-java/howto/java-merge-pdf/java-merge-pdf-3.webp" alt="Python Merge PDFs - Figure 3: Merge More Than Two PDF Files" class="img-responsive add-shadow"></a>
    <p class="content__image-caption">Merge More Than Two PDF Files</p>
	</div>
</div>

## Conclusion

This tutorial provides a detailed walkthrough on using IronPDF to merge PDF files in Python.

Starting with the installation of IronPDF, we covered how to generate and combine PDFs seamlessly using the library’s features. IronPDF is an excellent tool for handling PDF files in Python. You can explore its full capabilities through our [Code Examples](https://ironpdf.com/python/examples/using-html-to-create-a-pdf/).

IronPDF is free for development and offers license packages for commercial use. For more details on licensing terms, visit [this page](https://ironpdf.com/python/licensing/).

*[Download IronPDF here.](https://ironpdf.com/downloads/python-merge-pdf.zip)*