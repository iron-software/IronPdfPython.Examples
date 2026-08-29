# How to Print PDF Files Using Python

> Full guide: [How to Print PDF Files Using Python](https://ironpdf.com/python/how-to/python-print-pdf/)


## Introduction

The ability to print PDF files in Python is incredibly useful, allowing developers to handle documents independently of the platform they operate on. PDFs are widely used for the archival and distribution of files, a critical part of Python-based applications that manage documents or complex workflows.

Python supports a variety of methods for creating and printing PDFs, with libraries offering specialized classes for PDF manipulation being a particularly popular solution. This detailed tutorial explains how to use the IronPDF library to create and print PDF files easily in Python scripts.

---

## IronPDF: Python PDF Library

IronPDF is an advanced Python library designed to create, manipulate, and convert PDF documents. Modeled after its [IronPDF C# .NET counterpart](https://ironsoftware.com/), it brings a rich feature set to the Python environment.

This library provides a high-level API that simplifies PDF tasks, avoiding the complexities associated with lower-level operations. It includes methods for common PDF tasks such as creating, adding content, formatting text, and splitting or merging documents.

A key strength of IronPDF is its ability to convert HTML, CSS, and JavaScript into PDFs. This feature makes it easy to get PDF outputs from web pages or HTML sources. Additionally, IronPDF supports PDF printing, enhancing its broad applicability and usefulness.

## Install IronPDF with Pip

IronPDF can be integrated into your Python project with ease using pip. Install the library with the command:

```shell
pip install ironpdf
```

Incorporate IronPDF by adding this line to your script:

```python
from ironpdf import *

pass
```

## Load a PDF

IronPDF provides a handy function to load PDFs from various sources like byte arrays or file paths. It also supports opening password-protected documents by specifying a password.

Here’s how to load a PDF from a file:

```python
from ironpdf import *

# Set your license key to use IronPDF
License.LicenseKey = "Enter-Your-License"
# Load the PDF file from the filesystem
pdf = PdfDocument.FromFile("MyPdf.pdf")
```

## Print a PDF with Default Settings

There are two approaches to printing PDFs with IronPDF.

The simplest method uses the `Print` function to automatically print the document with the default settings on the default printer:

```python
from ironpdf import *

# The guide loads a PDF before this snippet; load one here so the example
# runs on its own.
License.LicenseKey = "Enter-Your-License"
pdf = PdfDocument.FromFile("MyPdf.pdf")

# Print the PDF using default settings
pdf.Print()
```

## Customize Print Settings

For greater control over the printing process, IronPDF allows customization of print settings. The `GetPrintDocument` function provides a **PrintDocument** object where you can modify its **PrinterSettings**.

```python
from ironpdf import *

# The guide loads a PDF before this snippet; load one here so the example
# runs on its own.
License.LicenseKey = "Enter-Your-License"
pdf = PdfDocument.FromFile("MyPdf.pdf")

# Access and modify the print settings
printer_setting = pdf.GetPrintDocument()
# Set the range of pages to print
printer_setting.PrinterSettings.FromPage = 2
printer_setting.PrinterSettings.ToPage = 4
# Print with the customized settings
printer_setting.Print()
```

## Complete Source Code

Below is the full source code used in this guide.

```python
from ironpdf import *

# Set your license key to use IronPDF
License.LicenseKey = "Enter-Your-License"
# Load the PDF file from the filesystem
pdf = PdfDocument.FromFile("MyPdf.pdf")
# Print the PDF using default settings
pdf.Print()
# Access and modify the print settings
printer_setting = pdf.GetPrintDocument()
# Set the range of pages to print
printer_setting.PrinterSettings.FromPage = 2
printer_setting.PrinterSettings.ToPage = 4
# Print the document with the customized settings
printer_setting.Print()
```

## Summary

IronPDF prints PDFs from Python projects. Offering a broad range of features and comprehensive support documentation, it enables users to easily create, customize, and print high-quality PDF documents. IronPDF is ideal for producing everything from invoices to reports.

Utilize IronPDF's free trial in a real-world setting. The [pricing](https://ironpdf.com/python/licensing/) starts from `$liteLicense`. Try the [trial license](https://ironpdf.com#trial-license) to explore how IronPDF can enhance your PDF printing workflow efficiently.

*[Download](https://ironpdf.com/downloads/python-print-pdf.zip) the software product.*