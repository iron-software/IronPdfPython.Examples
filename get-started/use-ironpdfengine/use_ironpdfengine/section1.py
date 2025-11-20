from ironpdf import Installation, IronPdf

def run():
    # Import necessary modules
    # Configure the connection settings to connect to the remote IronPdfEngine
    Installation.ConnectToIronPdfHost(
        IronPdf.GrpcLayer.IronPdfConnectionConfiguration.RemoteServer("123.456.7.8:33350")
    )