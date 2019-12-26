#!/usr/bin/python
import PyQt5.Qt as Qt
import PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView , QWebEnginePage, QWebEngineSettings
from PyQt5.QtNetwork import *
import sys
from optparse import OptionParser

class MyBrowser(QWebEnginePage):
    ''' Settings for the browser.'''
    
    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0"

class Browser(QWebEngineView):
    def __init__(self):
        # QWebEngineView
        self.view = QWebEngineView.__init__(self)
        #self.view.setPage(MyBrowser())
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        #super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&amp;)"), self.adjustTitle)

    def load(self,url):
        self.setUrl(QUrl(url))
    
    def adjustTitle(self):
        self.setWindowTitle(self.title())
    
    def disableJS(self):
        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)

    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            webView = Browser()
            # self.webView.setAttribute(Qt.WA_DeleteOnClose, True)
            webView.show()
            return webView
        # return Browser.createWindow(self,windowType)

app = QApplication(sys.argv)
view = Browser()
view.showMaximized()
view.load("https://www.ntcltd.org/Home.aspx")
app.exec_()