***Based on <https://ironpdf.com/examples/file-to-pdf/>***

Transform an HTML document into a flawless PDF using IronPDF for Python's `RenderHtmlFileAsPdf` function.

Begin by providing the `RenderHtmlAsPdf` function with a path in string format to your local HTML file. This function will generate a new `PdfDocument` object which encapsulates the contents of the HTML file located at the given path. The appearance of the PDF will mirror that of the webpage, assuming the HTML is well-formed with [valid markup](https://validator.w3.org/).

For enhanced customization such as adding headers, footers, custom margins, backgrounds, and page numbers, initiate a `ChromePdfRenderer` object along with the HTML file path. For more details on how to tailor your PDF output, consider reviewing [this programming example](https://ironpdf.com/python/examples/pdf-generation-settings/) to understand how to [alter PDF settings](https://ironpdf.com/python/examples/pdf-generation-settings/).