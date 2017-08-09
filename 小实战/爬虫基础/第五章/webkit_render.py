#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try: 
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtWebKit import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtWebKit import *
import lxml.html
import downloader

def direct_download(url):
    download = downloader.Downloader()
    return download(url)

def webkit_download(url):
    app = QApplication([])
    webview = QWebView() # QWebView是Web文档的容器
    webview.loadFinished.connect(app.quit)
    webview.load(url)
    app.exec_() # delay here until download finished
    return webview.page().mainFrame().toHtml()

def parse(html):
    # print(html)
    tree = lxml.html.fromstring(html)
    print(tree.cssselect('#result')[0].text_content())

def main(): 
    url = 'http://example.webscraping.com/places/default/dynamic'
    parse(direct_download(url))
    parse(webkit_download(url))
    return

if __name__ == '__main__':
    main()