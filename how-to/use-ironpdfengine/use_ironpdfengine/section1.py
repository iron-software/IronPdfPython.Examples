from ironpdf import *

def run():
    Installation.ConnectToIronPdfHost(
    	IronPdf.GrpcLayer.IronPdfConnectionConfiguration.RemoteServer("123.456.7.8:33350"));