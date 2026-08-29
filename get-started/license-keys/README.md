# Licensing IronPDF for Python Projects

> Full guide: [Licensing IronPDF for Python Projects](https://ironpdf.com/get-started/license-keys/?utm_source=github)


## Acquiring a License Key

Incorporating a license key for IronPDF enables the live deployment of your project without any limitations or watermark intrusion.

You can [purchase a license key here](https://ironpdf.com/python/licensing/?utm_source=github) or sign up for a [free 30-day trial key](https://ironpdf.com/trial-license?utm_source=github).

## Step 1: Include IronPDF in Your Python Project as a Dependency

To utilize the IronPDF library in your Python project, you should first install it as a dependency. This can be done via the `pip` package manager. Simply open your command line interface and run the following command:

```shell
pip install ironpdf
```

This command retrieves and installs the latest version of IronPDF, readying it for use within your project.

Note that IronPDF for Python is built on top of the IronPDF .NET library, specifically targeting .NET 6.0. As such, the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) must be installed on your system to properly use the IronPDF for Python.

## Step 2: Implement Your License Key

After acquiring your license key, you'll need to implement it within your Python script. This is crucial to do before invoking any IronPDF functionalities:

```python
from ironpdf import License

# Setting the license key

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

## Step 3: Confirm License Key Application and Validation

### Confirming the License Key Installation

To check if the license key has been correctly applied in your script, inspect the `IsLicensed` attribute using the code snippet below:

```python
from ironpdf import License

# Verify the license application

is_licensed = License.IsLicensed
```

### License Key Validation

To validate your license or trial key, you can employ the following code:

```python
from ironpdf import License

# Validate the provided license key

is_valid = License.IsValidLicense("IRONPDF-MYLICENSE-KEY-1EF01")
```

A return value of `True` confirms that your key is valid, enabling the continued use of IronPDF. Conversely, a `False` indicates an issue with the license key.

Ensure to clean and republish your application after integrating the license to promote flawless deployment and to avoid errors.

## Step 4: Begin working on your Project

We strongly recommend consulting our extensive tutorial on [How to Get Started with IronPDF](https://ironpdf.com/python/docs/?utm_source=github) for an initial guide. This resource offers in-depth instructions and practical examples, ensuring you gain a solid grasp of implementing IronPDF in your Python endeavors.

## Assistance or Further Inquiries

While in development, `IronPDF for Python` may be tested with the presence of the IronPDF watermark. However, for watermark-free live applications, a license must be acquired. Learn more about [acquiring a trial license](https://ironpdf.com/trial-license?utm_source=github) for testing purposes.

For additional resources such as coding examples, tutorials, detailed licensing information, and comprehensive documentation, please visit the [IronPDF for Python](https://ironpdf.com/python/?utm_source=github) section on our site.

Our dedicated support team is available to offer help or answer any questions. Feel free to [contact our support team](https://ironpdf.com/?utm_source=github#live-chat-support) anytime.