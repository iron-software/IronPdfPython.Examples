***Based on <https://ironpdf.com/examples/embed-image-base64/>***

IronPDF for Python seamlessly transforms raw image byte data into PDF documents.

First, extract the byte stream from your chosen data source, whether it's a database, network connection, or local file. Convert this byte data into a character string. Next, incorporate this string into an HTML snippet by embedding it within a `base64` encoded `src` attribute in an `img` tag:

```html
<img src="data:image/jpeg;base64, [your_encoded_string_here]" />
```

Once your HTML string is ready, utilize the `RenderHtmlAsPdf` function and pass the HTML string as its parameter.

IronPDF excels by leveraging HTML as the backbone for layout design. Simply convert your content into valid HTML format and let IronPDF handle the conversion to PDF.

Learn more about creating PDFs using IronPDF for Python by visiting: [Learn to create PDFs with IronPDF for Python today!](https://ironpdf.com/python/how-to/python-create-pdf/).