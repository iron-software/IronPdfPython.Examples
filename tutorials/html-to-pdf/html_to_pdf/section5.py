from ironpdf import *

def run():
    html = """
    <html>
       <head>
          <title>Hello world!</title>
          <link rel='stylesheet' href='assets/style.css'>
       </head>
       <body>
          <h1>Hello from IronPDF!</h1>
          <a href='https://ironpdf.com/python/'><img src='assets/logo.png' /></a>
       </body>
    </html>
    """
    renderer = ChromePdfRenderer()
    pdf = renderer.RenderHtmlAsPdf(html)
    pdf.SaveAs("output.pdf")