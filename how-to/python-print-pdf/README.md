# How To Print PDF Files Using Python

***Based on <https://ironpdf.com/how-to/python-print-pdf/>***


## Introduction

In the realm of Python development, the ability to print PDF files represents a crucial skill, particularly for managing and distributing documents across various platforms. PDFs are widely used for both purposes due to their universal compatibility and reliability.

This guide delves into Python-based techniques for PDF generation and printing, highlighting the use of the IronPDF library. With IronPDF, developers can easily produce and manage PDF documents directly from their Python code.

---

## IronPDF: Python PDF Library

IronPDF serves as a robust library for Python, enabling the creation, manipulation, and conversion of PDF documents. Drawing inspiration from the IronPDF C# .NET library, this tool adapits its rich functionalities to fit the Python environment.

This library simplifies PDF interactions through a high-level API, removing the complexity of direct PDF manipulation. It includes a variety of methods for PDF tasks such as document creation, content addition, and document merging or splitting.

A key advantage of IronPDF is its ability to transform HTML, CSS, and JavaScript into PDFs seamlessly. This is invaluable for producing PDFs from web content or HTML sources. IronPDF also supports direct PDF printing, enhancing its practicality for various applications.

## Install IronPDF via Pip

To integrate IronPDF into your project, install it using pip with this command:

```shell
pip install ironpdf
```

Then, incorporate the IronPDF library into your script as follows:

```py
from ironpdf import *
```

## Load a PDF

IronPDF in Python offers a straightforward approach to import PDFs into your application. It supports several input types, including file paths or byte arrays. For password-protected documents, it allows password specification as well.

Below is an example on how to import a PDF file from your local storage:

```py
License.LicenseKey = "Enter-Your-License"  
pdf = PdfDocument.FromFile("MyPdf.pdf")
```

## Print a PDF Document With Default Settings

IronPDF facilitates two primary methods for printing PDFs.

The first method uses the `Print` function to immediately send the document to the default printer with standard settings.

```py
pdf.Print()
```

## Customize Print Settings

Alternatively, users can customize their print settings using the `GetPrintDocument` function. This function provides a **PrintDocument** object, where the **PrinterSettings** can be modified according to user preferences.

```py
printer_setting = pdf.GetPrintDocument()
printer_setting.PrinterSettings.FromPage = 2
printer_setting.PrinterSettings.ToPage = 4
printer_setting.Print()
```

## Full Source Code

Here's the complete script from this tutorial:

```py
from ironpdf import *

License.LicenseKey = "Enter-Your-License"  
pdf = PdfDocument.FromFile("MyPdf.pdf")

pdf.Print()

printer_setting = pdf.GetPrintDocument()
printer_setting.PrinterSettings.FromPage = 2
printer_setting.PrinterSettings.ToPage = 4
printer_setting.Print()
```

## Summary

IronPDF stands out as a powerful and intuitive library that streamlines the process of printing PDFs in Python projects. It offers a rich set of features and detailed documentation to help users easily generate and print high-quality PDF documents. Whether creating invoices, reports, or other documents, IronPDF provides the necessary tools for the job.

Explore IronPDF with its free trial version in a live environment. [Pricing starts at](https://ironpdf.com/python/licensing/) `$liteLicense`. Try out IronPDF with a [trial license](https://ironpdf.com/#trial-license) and see how it enhances your PDF handling workflows.

*Download the software [here](https://ironpdf.com/downloads/python-print-pdf.zip).*