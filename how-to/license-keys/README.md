# Licensing IronPDF for Python Scripts

***Based on <https://ironpdf.com/how-to/license-keys/>***


## Acquiring a License Key

Obtaining an IronPDF license key is essential for deploying your project without limitations or watermarks.

You can [purchase a license here](https://ironpdf.com/python/licensing/) or register for a [free 30-day trial key](#trial-license) by clicking on the link.

## Step 1: Installing IronPDF as a Dependency in Your Python Environment

To use IronPDF in your Python environment, you need to install it as a dependency. This can be done using **pip**, the popular Python package management system. Run the command below in your terminal:

```shell
pip install ironpdf
```

This command installs IronPDF and prepares it for use in your project. IronPDF for Python utilizes the IronPDF .NET library, specifically targeting .NET 6.0. Make sure the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) is installed on your computer for IronPDF Python to function.

## Step 2: Implementing Your License Key

Following the installation, implement your license or trial key by setting the **LicenseKey** property early in your Python script, prior to using IronPDF functionalities.
```py
# Set up your license key

***Based on <https://ironpdf.com/how-to/license-keys/>***

License.LicenseKey = "IRONPDF-MYLICENSE-KEY-1EF01"
```

## Step 3: Confirming Your License Key

### Confirm the License Key Installation

To confirm your license key has been successfully implemented, the **IsLicensed** property in the **License** module should be checked:
```py
# Validate the license key implementation

***Based on <https://ironpdf.com/how-to/license-keys/>***

is_licensed = License.IsLicensed
```

### Check License Key Validity

It’s essential to verify the legitimacy of your license or trial key using the following code:
```py
# Verify the validity of the license key

***Based on <https://ironpdf.com/how-to/license-keys/>***

is_valid = License.IsValidLicense("IRONPDF-MYLICENSE-KEY-1EF01")
```

A return value of **True** indicates the key is valid and you can continue using IronPDF. A **False** result suggests the key may be invalid.

After applying a license, it's advisable to clean and republish your application to ensure everything runs smoothly during deployment.

## Step 4: Initiating Your Project

Begin your IronPDF integration by exploring our detailed guide on [how to start with IronPDF](https://ironpdf.com/python/docs/). This guide offers in-depth instructions and examples that provide a solid foundation for using IronPDF.

## Questions or Support Needed?

While developing, you can use `IronPDF for Python` albeit with a watermark. For live deployment and watermark removal, a [license purchase](https://ironpdf.com/python/licensing/) is necessary. Trial licenses for evaluation are also available [here](#trial-license).

Visit the [IronPDF for Python section](https://ironpdf.com/python/) for a wealth of resources like code samples, tutorials, and detailed documentation.

For further assistance or questions, our support team is ready to help. Feel free to [contact our support team](#live-chat-support) anytime.