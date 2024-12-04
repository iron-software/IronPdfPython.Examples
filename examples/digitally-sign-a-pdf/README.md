***Based on <https://ironpdf.com/examples/digitally-sign-a-pdf/>***

This Python example demonstrates leveraging the IronPDF library to both cryptographically sign an existing PDF and also to generate a new PDF that includes a digital signature. Through these capabilities, developers can enhance the security and authenticity of their PDF documents.

```python
# Importing necessary classes from the IronPdf namespace
from IronPdf import IronPdfDocument

# Create an instance of PdfDocument
pdf_document = IronPdfDocument('path/to/your/input.pdf')

# Signing the PDF with a digital certificate (.p12 or .pfx file)
signed_pdf = pdf_document.sign('path/to/your/certificate.p12', 'certificate-password')

# Save the signed PDF to a specified path
signed_pdf.saveAs('path/to/your/signed_output.pdf')
```

### Key Features of This Code:
- **IronPdfDocument**: This class is utilized to create an instance of the PDF to be signed.
- **sign() method**: This method is called on the PDF instance with parameters pointing to the certificate and its password.
- **saveAs() method**: After the signing process, the signed PDF is saved in the desired location with this method.

This approach ensures that the PDFs are securely signed using a digital certificate, maintaining the integrity and non-repudiation of the documents .