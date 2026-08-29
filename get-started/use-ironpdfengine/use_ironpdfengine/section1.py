import clr

clr.AddReference("IronPdf")
from IronPdf.GrpcLayer import IronPdfConnectionConfiguration
from ironpdf import Installation

def run():
    # The guide writes this as `from ironpdf import Installation, IronPdf` and
    # then `IronPdf.GrpcLayer.IronPdfConnectionConfiguration`. The ironpdf
    # module exports no `IronPdf` attribute, so that import raises ImportError;
    # the .NET namespace is reached through clr, as above.
    #
    # RemoteServer takes the host on its own. Passing "host:port" leaves Port
    # at 0 and the engine dials "123.456.7.8:33350:0", an invalid URI.
    configuration = IronPdfConnectionConfiguration.RemoteServer("123.456.7.8")
    configuration.Port = 33350

    Installation.ConnectToIronPdfHost(configuration)
