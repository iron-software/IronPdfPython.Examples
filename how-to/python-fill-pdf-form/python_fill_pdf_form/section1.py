from ironpdf import *

def run():
    # Define HTML content for a simple form
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
    # Instantiate a PDF renderer
    renderer = ChromePdfRenderer()
    # Set the option to create PDF forms from HTML
    renderer.RenderingOptions.CreatePdfFormsFromHtml = True
    # Render the HTML content as a PDF file and save it
    renderer.RenderHtmlAsPdf(form_html).SaveAs("BasicForm.pdf")
    # Load the created PDF document
    form_document = PdfDocument.FromFile("BasicForm.pdf")
    # Access the "firstname" field and set its value
    first_name_field = form_document.Form.FindFormField("firstname")
    first_name_field.Value = "Minnie"
    print("FirstNameField value: {}".format(first_name_field.Value))
    # Access the "lastname" field and set its value
    last_name_field = form_document.Form.FindFormField("lastname")
    last_name_field.Value = "Mouse"
    print("LastNameField value: {}".format(last_name_field.Value))
    # Save the filled form to a new PDF file
    form_document.SaveAs("FilledForm.pdf")