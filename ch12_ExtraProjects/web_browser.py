"""
Listing 12-6
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
import os
import sys

from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget, QLabel,
                             QLineEdit, QMainWindow, QProgressBar, QStatusBar,
                             QTabWidget, QToolBar, QVBoxLayout, QWidget)

style_sheet = """
    QTabWidget:pane{
        border: none
    }
"""


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create lists that will keep track of the new windows,
        # tabs and urls
        self.window_list = []
        self.list_of_web_pages = []
        self.list_of_urls = []

        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(300, 200)
        self.setWindowTitle("12.6 – Web Browser")
        self.setWindowIcon(QIcon(os.path.join('images', 'pyqt_logo.png')))

        self.positionMainWindow()

        self.createMenu()
        self.createToolbar()
        self.createTabs()

        self.show()

    def createMenu(self):
        """
        Set up the menu bar.
        """
        new_window_act = QAction('New Window', self)
        new_window_act.setShortcut('Ctrl+N')
        new_window_act.triggered.connect(self.openNewWindow)

        new_tab_act = QAction('New Tab', self)
        new_tab_act.setShortcut('Ctrl+T')
        new_tab_act.triggered.connect(self.openNewTab)

        quit_act = QAction("Quit Browser", self)
        quit_act.setShortcut('Ctrl+Q')
        quit_act.triggered.connect(self.close)

        # Create the menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(new_window_act)
        file_menu.addAction(new_tab_act)
        file_menu.addSeparator()
        file_menu.addAction(quit_act)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def createToolbar(self):
        """
        Set up the navigation toolbar.
        """
        tool_bar = QToolBar("Address Bar")
        tool_bar.setIconSize(QSize(30, 30))
        self.addToolBar(tool_bar)

        # Create toolbar actions
        back_page_button = QAction(QIcon(os.path.join('icons', 'back.png')),
                                   "Back", self)
        back_page_button.triggered.connect(self.backPageButton)

        forward_page_button = QAction(
            QIcon(os.path.join('icons', 'forward.png')), "Forward", self)
        forward_page_button.triggered.connect(self.forwardPageButton)

        refresh_button = QAction(QIcon(os.path.join('icons', 'refresh.png')),
                                 "Refresh", self)
        refresh_button.triggered.connect(self.refreshButton)

        home_button = QAction(QIcon(os.path.join('icons', 'home.png')), "Home",
                              self)
        home_button.triggered.connect(self.homeButton)

        stop_button = QAction(QIcon(os.path.join('icons', 'stop.png')), "Stop",
                              self)
        stop_button.triggered.connect(self.stopButton)

        # Set up the address bar
        self.address_line = QLineEdit()
        # addAction() is used here to merely display the icon in the line
        # edit.
        self.address_line.addAction(QIcon('icons/search.png'),
                                    QLineEdit.LeadingPosition)
        self.address_line.setPlaceholderText("Enter website address")
        self.address_line.returnPressed.connect(self.searchForUrl)

        tool_bar.addAction(home_button)
        tool_bar.addAction(back_page_button)
        tool_bar.addAction(forward_page_button)
        tool_bar.addAction(refresh_button)
        tool_bar.addWidget(self.address_line)
        tool_bar.addAction(stop_button)

    def createTabs(self):
        """
        Create the QTabWidget object and the different pages.
        Handle when a tab is closed.
        """
        self.tab_bar = QTabWidget()
        self.tab_bar.setTabsClosable(True)  # Add close buttons to tabs
        self.tab_bar.setTabBarAutoHide(
            True)  # Hides tab bar when less than 2 tabs
        self.tab_bar.tabCloseRequested.connect(self.closeTab)

        # Create tab
        self.main_tab = QWidget()
        self.tab_bar.addTab(self.main_tab, "New Tab")

        # Call method that sets up each page
        self.setupTab(self.main_tab)

        self.setCentralWidget(self.tab_bar)

    def setupWebView(self):
        """
        Create the QWebEngineView object that is used to view
        web docs. Set up the main page, and handle web_view signals.
        """
        web_view = QWebEngineView()
        web_view.setUrl(QUrl("https://google.com"))

        # Create page loading progress bar that is displayed in
        # the status bar.
        self.page_load_pb = QProgressBar()
        self.page_load_label = QLabel()
        web_view.loadProgress.connect(self.updateProgressBar)

        # Display url in address bar
        web_view.urlChanged.connect(self.updateUrl)

        ok = web_view.loadFinished.connect(self.updateTabTitle)
        if ok:
            # Web page loaded
            return web_view
        else:
            print("The request timed out.")

    def setupTab(self, tab):
        """
        Create individual tabs and widgets. Add the tab's url and
        web view to the appropriate list.
        Update the address bar if the user switches tabs.
        """
        # Create the web view that will be displayed on the page.
        self.web_page = self.setupWebView()

        tab_v_box = QVBoxLayout()
        # Sets the left, top, right, and bottom margins to use around the
        # layout.
        tab_v_box.setContentsMargins(0, 0, 0, 0)
        tab_v_box.addWidget(self.web_page)

        # Append new web_page and url to the appropriate lists
        self.list_of_web_pages.append(self.web_page)
        self.list_of_urls.append(self.address_line)
        self.tab_bar.setCurrentWidget(self.web_page)

        # If user switches pages, update the url in the address to
        # reflect the current page.
        self.tab_bar.currentChanged.connect(self.updateUrl)

        tab.setLayout(tab_v_box)

    def openNewWindow(self):
        """
        Create new instance of the WebBrowser class.
        """
        new_window = WebBrowser()
        new_window.show()
        self.window_list.append(new_window)

    def openNewTab(self):
        """
        Create new tabs.
        """
        new_tab = QWidget()
        self.tab_bar.addTab(new_tab, "New Tab")
        self.setupTab(new_tab)

        # Update the tab_bar index to keep track of the new tab.
        # Load the url for the new page.
        tab_index = self.tab_bar.currentIndex()
        self.tab_bar.setCurrentIndex(tab_index + 1)
        self.list_of_web_pages[self.tab_bar.currentIndex()].load(
            QUrl("https://google.com"))

    def updateProgressBar(self, progress):
        """
        Update progress bar in status bar.
        This provides feedback to the user that page is still loading.
        """
        if progress < 100:
            self.page_load_pb.setVisible(progress)
            self.page_load_pb.setValue(progress)
            self.page_load_label.setVisible(progress)
            self.page_load_label.setText(
                "Loading Page... ({}/100)".format(str(progress)))
            self.status_bar.addWidget(self.page_load_pb)
            self.status_bar.addWidget(self.page_load_label)
        else:
            self.status_bar.removeWidget(self.page_load_pb)
            self.status_bar.removeWidget(self.page_load_label)

    def updateTabTitle(self):
        """
        Update the title of the tab to reflect the website.
        """
        tab_index = self.tab_bar.currentIndex()
        title = self.list_of_web_pages[
            self.tab_bar.currentIndex()].page().title()
        self.tab_bar.setTabText(tab_index, title)

    def updateUrl(self):
        """
        Update the url in the address to reflect the current page being
        displayed.
        """
        url = self.list_of_web_pages[self.tab_bar.currentIndex()].page().url()
        formatted_url = QUrl(url).toString()
        self.list_of_urls[self.tab_bar.currentIndex()].setText(formatted_url)

    def searchForUrl(self):
        """
        Make a request to load a url.
        """
        url_text = self.list_of_urls[self.tab_bar.currentIndex()].text()

        # Append http to url
        url = QUrl(url_text)
        if url.scheme() == "":
            url.setScheme("http")

        # Request url
        if url.isValid():
            self.list_of_web_pages[self.tab_bar.currentIndex()].page().load(
                url)
        else:
            url.clear()

    def backPageButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].back()

    def forwardPageButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].forward()

    def refreshButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].reload()

    def homeButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].setUrl(QUrl("https://google.com"))

    def stopButton(self):
        tab_index = self.tab_bar.currentIndex()
        self.list_of_web_pages[tab_index].stop()

    def closeTab(self, tab_index):
        """
        This signal is emitted when the close button on a tab is clicked.
        The index is the index of the tab that should be removed.
        """
        self.list_of_web_pages.pop(tab_index)
        self.list_of_urls.pop(tab_index)

        self.tab_bar.removeTab(tab_index)

    def positionMainWindow(self):
        """
        Use QDesktopWidget class to access information about your screen
        and use it to position the application window when starting a new
        application.
        """
        desktop = QDesktopWidget().screenGeometry()
        screen_width = desktop.width()
        screen_height = desktop.height()
        self.setGeometry(0, 0, screen_width, screen_height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = WebBrowser()
    app.exec_()