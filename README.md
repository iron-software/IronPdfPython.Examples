# IronPdfPython.Examples

Runnable Python examples for [IronPDF for Python](https://ironpdf.com/python/?utm_source=github), a PDF library that converts HTML to PDF with a real Chromium renderer and generates, edits, and extracts PDF content.

## Install

```bash
pip install ironpdf
```

## Quickstart

```python
from ironpdf import *

License.LicenseKey = "YOUR-LICENSE-KEY"

renderer = ChromePdfRenderer()
pdf = renderer.RenderHtmlAsPdf("<h1>Hello, PDF!</h1>")
pdf.SaveAs("hello.pdf")
```

To render from other sources, swap `RenderHtmlAsPdf` for `RenderUrlAsPdf(url)` or `RenderHtmlFileAsPdf(path)`, and use `PdfDocument.FromFile(path)` to open a document that already exists.

IronPDF for Python wraps the .NET library, so **members keep their .NET PascalCase names** — `SaveAs`, not `save_as`. A snake_case attribute is a sign the call is wrong. `Logger.EnableDebugging = True` together with `Logger.LogFilePath` turns on engine logging when something needs diagnosing.

Without a license key, generated PDFs include a watermark.

## What's in this repo

Each folder contains a self-contained project with a `requirements.txt`. Run `pip install -r requirements.txt`, then `python program.py`:

- `examples/` — focused snippets demonstrating individual features
- `get-started/` — first projects covering license keys and remote `IronPdfEngine`
- `how-to/` — task-oriented guides for specific PDF operations
- `quickstart/` — an end-to-end project scaffold with tests
- `tutorials/` — a longer HTML-to-PDF walkthrough

## Common tasks covered

- HTML string, HTML file, URL, and image to PDF conversion
- Merging and splitting existing PDFs
- Digital signatures and document security
- Form filling and form data extraction
- Rasterizing pages to images
- Compression and file-size reduction
- Multi-frame TIFF conversion, embedded Base64 images, and barcodes
- Printing to a physical printer
- Running against a remote `IronPdfEngine`

## Platform support

Python 3.7 and above. Windows, macOS, and Linux. See the [documentation](https://ironpdf.com/python/docs/?utm_source=github) for environment-specific notes.

## Documentation and support

- Full documentation: [ironpdf.com/python/docs](https://ironpdf.com/python/docs/?utm_source=github)
- API reference: [ironpdf.com/python/object-reference/api](https://ironpdf.com/python/object-reference/api/?utm_source=github)
- PyPI package: [pypi.org/project/ironpdf](https://pypi.org/project/ironpdf/)
- Issues with these examples: file directly on this repository
- Product support: [support@ironsoftware.com](mailto:support@ironsoftware.com)

## About

This repository is maintained by [Iron Software](https://ironsoftware.com/?utm_source=github). IronPDF for Python is a commercial library — see [licensing](https://ironpdf.com/python/licensing/?utm_source=github) for terms and trial details.
