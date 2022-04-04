#!/usr/bin/python
from burp import IBurpExtender
from burp import IHttpListener
from java.io import PrintWriter
import time

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("Request Timestamp")
        callbacks.registerHttpListener(self)
        self.stdout = PrintWriter(callbacks.getStdout(), True)
        self.stderr = PrintWriter(callbacks.getStderr(), True)
        self.helpers = callbacks.getHelpers()

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not messageIsRequest:
            return

        msg = self.helpers.bytesToString(messageInfo.getRequest())
        # TODO: Expose this as a variable in the extension config
        now = str(int(time.time() * 1000.0))

        if "%TIMESTAMP%" in msg:
            msg = msg.replace("%TIMESTAMP%", now)
            messageInfo.setRequest(self.helpers.stringToBytes(msg))
            info = self.helpers.bytesToString(messageInfo.getHttpService().toString())
            self.stdout.println("[i] timestampped request: " + info)

