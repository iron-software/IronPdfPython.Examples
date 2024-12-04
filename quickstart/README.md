# IronPDF for Python: Comprehensive Guide to PDF Manipulation in Python Scripts

***Based on <https://ironpdf.com/docs/docs/>***


## Exploring IronPDF for Python

IronPDF for Python, developed by Iron Software, equips developers with tools to create, modify, and extract information from PDFs in Python 3 applications. This Python-specific library leverages the foundational features offered by [IronPDF for .NET](https://ironpdf.com).

## How to Use IronPDF for Python

### Installation Requirements

Before utilizing IronPDF for Python, ensure the following software is installed on your system:

1. **.NET 6.0 SDK**: As IronPDF for Python utilizes the IronPDF .NET library, the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) must be installed.
2. **Python**: Acquire the latest Python (version 3.x) from the [official Python site](https://www.python.org/downloads/). Ensure you select the option to add Python to your system PATH to facilitate command line use.
3. **Pip**: Generally, this tool is included with the installation of Python, version 3.4 and above. Verify its existence or install it if missing.
4. **IronPDF Library**: Installation is achieved via pip using the command:

```shell
pip install ironpdf
```

To specify a particular version of IronPDF, use the `==2023.x.x` syntax, such as `pip install ironpdf==2023.x.x`. For environments where Python 2.x remains the default, the `pip3` command might be necessary to ensure the installation is made under Python 3.

## Implementing Python Code

Begin by importing the necessary packages early in your script.

```py
# Required imports for utilizing IronPDF in Python

***Based on <https://ironpdf.com/docs/docs/>***

from ironpdf import *
```

### Activating IronPDF License

Immediately after imports, activate IronPDF by assigning your license key to the **LicenseKey** attribute of **License** object:

```py
License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

Configure all necessary settings and licensing before invoking any of the IronPDF functionalities.

### Converting HTML to PDF

To transform HTML content to a PDF, employ the `RenderHtmlAsPdf` method. Below is how a basic HTML snippet is converted to a PDF:

```py
from ironpdf import *

# Create Renderer instance

***Based on <https://ironpdf.com/docs/docs/>***

renderer = ChromePdfRenderer()

# Convert HTML to PDF

***Based on <https://ironpdf.com/docs/docs/>***

pdf = renderer.RenderHtmlAsPdf("<h1>Hello World</h1>")

# Save the new PDF

***Based on <https://ironpdf.com/docs/docs/>***

pdf.SaveAs("html_to_pdf.pdf")
```

### Transforming URL to PDF

Similarly, to convert a web URL or local file to a PDF, use the `RenderUrlAsPdf` method:

```py
from ironpdf import *

# Instance of Renderer

***Based on <https://ironpdf.com/docs/docs/>***

renderer = ChromePdfRenderer()

# Create PDF from a URL

***Based on <https://ironpdf.com/docs/docs/>***

pdf = renderer.RenderUrlAsPdf("https://ironpdf.com/")

# Save created PDF

***Based on <https://ironpdf.com/docs/docs/>***

pdf.SaveAs("url_to_pdf.pdf")
```

### Enabling Logging

To enable detailed logging, use the commands below:

```py
Logger.EnableDebugging = True
Logger.LogFilePath = "Default.log"
Logger.LoggingMode = Logger.LoggingModes.All
```

## Licensing and Support

Acquiring a live project license is possible [here](https://ironpdf.com/python/licensing/). A 30-day trial license is also available <a class="js-modal-open" data-modal-id="trial-license" href="#trial-license">here</a>.

For a comprehensive resource library including code examples and detailed documentation, visit: <a href="https://ironpdf.com/python/">IronPDF for Python</a>.

For additional support and inquiries, please [contact our support team](#live-chat-support).