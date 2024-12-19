***Based on <https://ironpdf.com/examples/using-html-to-create-a-pdf/>***

This code snippet showcases IronPDF for Python’s premier HTML to PDF conversion feature.

Developers using Python can leverage the `RenderHtmlAsPdf` method to transform raw HTML into PDF documents. IronPDF is designed to accurately replicate all HTML content within a PDF, from simple "Hello World" messages to more intricate HTML constructs with nested elements.

As illustrated, the `RenderHtmlAsPdf` method takes a string of HTML markup and converts it into a PDF document. It’s important to note that this method comprehensively handles HTML elements including images, iframes, and other assets that are referenced externally, ensuring they appear in the final PDF as they would in a compliant web browser.

Further customization of PDFs created using the `RenderHtmlAsPdf` method is possible. Adjustments can be made to headers, footers, margins, and various other page settings. For additional details, check out [this example](https://ironpdf.com/python/examples/pdf-generation-settings/).