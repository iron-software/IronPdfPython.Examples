from ironpdf import *

def run():
    # Create a PDF with editable forms from HTML using form and input tags
    form_html = """
    <html>
    <body>
    <h2>Editable PDF Form</h2>
    <form>
    First name: <br> <input type='text' name='firstname' value=''> <br>
    Last name: <br> <input type='text' name='lastname' value=''>
    </form>
    </body>
    </html>
    """
    # Instantiate Renderer
    renderer = ChromePdfRenderer()
    renderer.RenderingOptions.CreatePdfFormsFromHtml = True
    renderer.RenderHtmlAsPdf(form_html).SaveAs("BasicForm.pdf")
    # Read and Write PDF form values
    form_document = PdfDocument.FromFile("BasicForm.pdf")
    # Set and Read the value of the "firstname" field
    first_name_field = form_document.Form.GetFieldByName("firstname")
    first_name_field.Value = "Minnie"
    print("FirstNameField value: {}".format(first_name_field.Value))
    # Set and Read the value of the "lastname" field
    last_name_field = form_document.Form.GetFieldByName("lastname")
    last_name_field.Value = "Mouse"
    print("LastNameField value: {}".format(last_name_field.Value))
    form_document.SaveAs("FilledForm.pdf")