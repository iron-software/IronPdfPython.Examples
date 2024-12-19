***Based on <https://ironpdf.com/examples/digitally-sign-a-pdf/>***

The following Python script outlines the process of utilizing the IronPDF library to both digitally sign an existing PDF document and generate a new PDF with an embedded digital signature. This is crucial for adding security and authenticity to your PDFs, which can be vital for various business and legal documents.

```python
# Import the necessary library
from IronPdf import PdfDocument

# Load an existing PDF document from a specific path
existing_pdf = PdfDocument("path/to/your/existing/document.pdf")

# Sign the PDF using a digital signature file
signature = "path/to/your/signature.pfx"
password = "your_password"
signed_pdf = existing_pdf.Sign(signature, password)

# Save the signed PDF to a new file
signed_pdf.SaveAs("path/to/your/signed_document.pdf")

# Create a new PDF document
new_pdf = PdfDocument()
new_pdf.AddPage()

# Optionally, add some content to the new PDF
new_pdf.AddText("This is a digitally signed new PDF document.")

# Sign the newly created PDF
new_pdf.Sign(signature, password)

# Save the newly created and signed PDF
new_pdf.SaveAs("path/to/your/new_signed_document.pdf")
```

This script demonstrates a straightforward method to secure your PDF files using IronPDF's robust features, making it an essential tool in today's digital document workflows. Whether you're securing transactional documents or ensuring the authenticity of reports, IronPDF provides the functionality necessary to protect your PDFs effectively.