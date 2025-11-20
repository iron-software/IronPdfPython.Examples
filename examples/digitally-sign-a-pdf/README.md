***Based on <https://ironpdf.com/examples/digitally-sign-a-pdf/>***

This Python example details the process for cryptographically signing an existing PDF or creating a new one with a digital signature using libraries such as `PyPDF2`.

## Generating a Digital Signature in Python

1. **Install a Python Module for Digital Signatures.**  
   Utilize libraries like `PyPDF2` or `PyPDF4` to manage PDF files. For digital signatures, consider using `reportlab` alongside `PyPDF2`.

2. **Create or Modify a PDF Document.**  
   Employ `reportlab` for generating new PDF documents or altering current ones.

3. **Use the `PdfSignature` Class for Handling Digital Certificates.**  
   The following snippet serves as an example of how to utilize a `PdfSignature` class. This will need to be adapted depending on the specific functionality of your selected library.

4. **Include Additional Signature Details.**  
   Add necessary metadata, define the appearance, or specify the signature placement within the document.

5. **Apply the Signature with the `sign` Method.**  
   The Python script below demonstrates creating a PDF with `reportlab` and adding a digital signature using `PyPDF2`.


Note: Implementing a digital signature in a PDF with `reportlab` and `PyPDF2` involves a sophisticated process, possibly requiring multiple libraries. Ensure you are prepared with the appropriate digital certificates and a clear understanding of cryptographic techniques.

[Explore the Digital Signature PDF Example on GitHub](https://ironpdf.com/IronPdfPython.Examples/tree/main/examples/digitally-sign-a-pdf)