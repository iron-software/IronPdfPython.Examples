from ironpdf import *

def run():
    # Enable debugging for logging
    Logger.EnableDebugging = True
    # Specify the log file path
    Logger.LogFilePath = "Default.log"
    # Set the logging mode to log all activities
    Logger.LoggingMode = Logger.LoggingModes.All