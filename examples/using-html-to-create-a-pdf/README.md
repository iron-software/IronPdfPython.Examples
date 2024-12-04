***Based on <https://ironpdf.com/examples/using-html-to-create-a-pdf/>***

This code snippet demonstrates the core functionality of IronPDF for Python's HTML to PDF conversion feature.

Python developers can leverage the `RenderHtmlAsPdf` method to transform simple or complex HTML code into PDF files. IronPDF accurately converts all HTML elements into their corresponding PDF representations. This includes straightforward "Hello World" examples and more intricate HTML structures with nested elements.

As indicated earlier, the `RenderHtmlAsPdf` method accepts a string with HTML markup to be transformed into a PDF. It's important to note that this method also properly handles images, iframes, and other external assets embedded in the HTML string. These elements appear in the finished PDF as they would in any compliant web browser.

Enhance the PDF documents created with the `RenderHtmlAsPdf` method by adding custom headers, footers, margins, and adjusting other page settings. For detailed guidance, refer to [this code example](https://ironpdf.com/python/examples/pdf-generation-settings/).