# How to Programmatically Fill PDF Forms with Python

***Based on <https://ironpdf.com/how-to/python-fill-pdf-form/>***


Automating the process of filling out PDF forms can significantly enhance user experiences and streamline document workflows. This tutorial will guide you on how to programmatically generate PDF forms using Python, which is particularly beneficial for archiving electronic versions.

Upon gathering all necessary user inputs, the next step is to automate the PDF form creation process, allowing the produced documents to be saved or updated as necessary. Several Python libraries can be utilized for PDF manipulation, including PyPDF2, ReportLab, and notably, IronPDF. This tutorial will delve into utilizing IronPDF to manage interactive PDF forms.

## IronPDF — A Tool for Python Developers

IronPDF serves as a robust PDF library tailored for Python developers, enabling straightforward creation, editing, and management of PDF files in Python environments.

This library offers a wide array of functionalities, such as text and image manipulation, document encryption, and digital signatures, allowing developers to produce high-quality PDF files. Such capabilities make IronPDF a valuable addition to any Python-based project.

## Installing IronPDF via Pip

You can easily integrate IronPDF into your Python environment using pip. Install IronPDF by executing the following command:

```shell
pip install ironpdf
```

With IronPDF installed, you can now enhance your Python scripts with powerful PDF processing capabilities.

## Programmatic PDF Form Filling with Python Code

Explore how to use IronPDF for generating and filling PDF forms with the following Python code example, which leverages HTML templates to create editable forms:

```python
from ironpdf import *

# Define an HTML template with form elements

***Based on <https://ironpdf.com/how-to/python-fill-pdf-form/>***

form_html = """
<html>
<body>
<h2>Editable PDF Form</h2>
<form>
First Name: <br> <input type='text' name='firstname' value=''> <br>
Last Name: <br> <input type='text' name='lastname' value=''>
</form>
</body>
</html>
"""

# Configure Renderer

***Based on <https://ironpdf.com/how-to/python-fill-pdf-form/>***

renderer = ChromePdfRenderer()
renderer.RenderingOptions.CreatePdfFormsFromHtml = True
renderer.RenderHtmlAsPdf(form_html).SaveAs("BasicEditableForm.pdf")

# Access and modify PDF form fields

***Based on <https://ironpdf.com/how-to/python-fill-pdf-form/>***

form_pdf = PdfDocument.FromFile("BasicEditableForm.pdf")

# Modify and read the "firstname" input field

***Based on <https://ironpdf.com/how-to/python-fill-pdf-form/>***

first_name_field = form_pdf.Form.GetFieldByName("firstname")
first_name_field.Value = "John"
print("First Name Field: {}".format(first_name_field.Value))

# Modify and read the "lastname" input field

***Based on <https://ironpdf.com/how-to/python-fill-pdf-form/>***

last_name_field = form_pdf.Form.GetFieldByName("lastname")
last_name_field.Value = "Doe"
print("Last Name Field: {}".format(last_name_field.Value))

form_pdf.SaveAs("CompletedForm.pdf")
```

Initially, we convert an HTML form to a PDF by using the `renderer.RenderHtmlAsPdf` method. The **RenderingOptions** setting allows enabling the creation of editable forms from HTML code, which are then stored in a designated file.

#### Output

![](https://ironpdf.com/static-assets/ironpdf-python/howto/python-fill-pdf-form/python-fill-pdf-form-1.webp)

Following that, we open the newly created PDF and dynamically populate the form fields using the `GetFieldByName` method to specify the form elements, updating their **Value** properties accordingly. The filled form is then saved to a new file.

#### Output

![](https://ironpdf.com/static-assets/ironpdf-python/howto/python-fill-pdf-form/python-fill-pdf-form-2.webp)

## Conclusion

IronPDF proves to be a powerful and efficient tool for handling PDF operations in Python, especially for automating form filling tasks. This library not only accelerates document workflows but also offers a free trial and flexible, cost-effective [licensing options](https://ironpdf.com/python/licensing/), with prices starting at `$liteLicense`.