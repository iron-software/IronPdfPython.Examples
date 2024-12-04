# Licensing IronPDF for Python Applications

***Based on <https://ironpdf.com/how-to/license-keys/>***


## Obtaining a License Key

Deploy your projects with ease by acquiring an IronPDF license key, which enables live deployment sans any logo marks or restrictions.

You can [purchase a license here](https://ironpdf.com/python/licensing/) or receive a [free 30 day trial key](#trial-license) by signing up here.

## Step 1: Incorporating IronPDF into Your Python Project

For incorporating the IronPDF library into your project, you'll need to add it as a dependency. This can be accomplished through **pip**, a common tool for managing Python packages. In your terminal, run:

```shell
pip install ironpdf
```

This command fetches and installs the IronPDF package into your Python environment.

IronPDF for Python leverages the IronPDF .NET library, thus requiring the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) to be installed on your system.

## Step 2: Implementing Your License Key

Once the library is installed, you should input your license or trial key in your script. Insert the following line at the start of your Python script:

```py
# Setting the license key

***Based on <https://ironpdf.com/how-to/license-keys/>***

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

## Step 3: Confirming Your License Key Is Active

### Checking the Implemented License

To check whether your license key is operational, evaluate the `IsLicensed` method on the `License` class using this code:

```py
# Verifying the license implementation

***Based on <https://ironpdf.com/how-to/license-keys/>***

is_licensed = License.IsLicensed
```

### Testing License Validity

To confirm the authenticity of your license key, use:

```py
# Validating the license key

***Based on <https://ironpdf.com/how-to/license-keys/>***

is_valid = License.IsValidLicense("IRONPDF-MYLICENSE-KEY-1EF01")
```

If it returns **True**, your license is authentic and you are set to proceed. A **False** return suggests an issue with the license key.

Ensure to republish your application after licensing, to commit any changes and prevent deployment errors.

## Step 4: Initiating Your IronPDF Project

Begin your IronPDF journey by visiting our detailed start guide on [getting started with IronPDF](https://ironpdf.com/python/docs/). This guide is filled with instructions and illustrative examples that clarify how to effectively implement IronPDF in Python environments.

## Inquiries or Requiring Assistance?

During development, IronPDF for Python is available for use with an IronPDF watermark. For active projects, please ensure to [invest in a full license](https://ironpdf.com/python/licensing/). We also offer trial licenses for initial assessments. Further details and the trial option are available [here](#trial-license).

For a full range of examples, comprehensive guides, licensing information, and detailed documentation, visit our [IronPDF for Python section](https://ironpdf.com/python/).

Our support team is ready to assist with any questions or support needs. Feel free to [contact our team](#live-chat-support) whenever needed.