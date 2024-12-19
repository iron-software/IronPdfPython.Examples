from ironpdf import *

def run():
    # Set a log path
    Logger.EnableDebugging = True
    Logger.LogFilePath = "Custom.log"
    Logger.LoggingMode = Logger.LoggingModes.All