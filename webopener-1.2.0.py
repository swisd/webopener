import random

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtNetwork import *
import os
import sys
import http.client
import random
# from PIL import Image
import io
from time import sleep  # ADDED

http_server = str(input("IP: "))
port = int(input("Port: "))
id_name = str(random.randrange(0, 999999))
"""
# create a connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified outgoing port
sock.bind(('', 8000))

# Connect to the server
sock.connect((http_server, port))
"""

conn = http.client.HTTPConnection(http_server, port)
# conn.sock = sock
conn.request("SeperateInterfaceID", id_name)
downloadsDir = "C:/Network/downloads/"
rsp = conn.getresponse()
print(rsp.status, rsp.reason)
data_received = (rsp.read()).decode("utf-8")
print(data_received)


class App(QMainWindow):

    def __init__(self):

        super(App, self).__init__()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.window = QWidget()

        self.window.setStyleSheet("background-color: #f0f0ff; title: webopener-1.2.0")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.textbox = QTextEdit()
        self.textbox.setMaximumHeight(30)
        self.textbox.setMinimumWidth(100)

        self.go_btn = QPushButton("GO")
        self.go_btn.setMaximumWidth(40)

        self.back_btn = QPushButton("⮜")
        self.back_btn.setMaximumWidth(40)

        self.forward_btn = QPushButton("⮞")
        self.forward_btn.setMaximumWidth(40)

        self.reload_btn = QPushButton("⟳")
        self.reload_btn.setMaximumWidth(40)

        self.home_btn = QPushButton("⌂")
        self.home_btn.setMaximumWidth(40)

        self.add_tab_btn = QPushButton("+")
        self.add_tab_btn.setMaximumWidth(40)

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.home_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.textbox)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.on_click())

        # todo: use for later
        """
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)
        """

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        # todo: use for later
        """
        self.tabs.tabBar().setContextMenuPolicy(Qt.PreventContextMenu)
        self.tabs.tabBar().setTabsClosable(True)
        self.tabs.tabBar().tabCloseRequested.connect(lambda index: self.tabs.removeTab(index))
        self.tabs.tabBar().addTab("+")
        self.tabs.tabBar().tabBarClicked.connect(self.tab_bar_clicked)

        self.browser.setUrl(QUrl("https://google.com"))
        """

        self.window.setLayout(self.layout)

        self.window.show()

    @pyqtSlot()
    def on_click(self):
        self.textboxValue = self.textbox.toPlainText()
        conn.request("_dtp", "source=web:hl=" + self.textboxValue)
        try:
            rsp = conn.getresponse()
        except:
            print("Server did not respond")
        rsn = rsp.reason
        rsts = int(rsp.status)
        print(rsts)
        self.data_received = (rsp.read()).decode("utf-8")
        self.browser.setHtml(self.data_received)

        self.data_received_script1 = ''
        self.data_received_script2 = ''
        self.data_received_script3 = ''
        self.data_received_script4 = ''
        self.data_received_style1 = ''
        self.data_received_style2 = ''

        self.check_reference()

    def check_reference(self):
        line = ''
        iXe = 0
        for char in self.data_received:
            if char != ">":
                line += char
                iXe += 1
                print(f"\r{iXe}", end="")
            else:
                iXe += 1
                if 'script src="' in line:
                    sourcename = (line.split('src="')[1]).split('"')[0]
                    print(sourcename)
                    conn.request("_dtp", self.textboxValue + "/" + sourcename)
                    try:
                        rsp = conn.getresponse()
                    except:
                        print("Server did not respond")
                    rsts_scr = int(rsp.status)
                    print(rsts_scr)
                    self.data_received_script1 = (rsp.read()).decode("utf-8", errors="ignore")
                    if not os.path.exists(
                            os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                         "https%3A///")):
                        os.makedirs(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                 "https%3A///"))
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "x") as _script:
                            _script.write(self.data_received_script1)
                    elif os.path.exists(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                     "https%3A///")):
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "w") as _script:
                            _script.write(self.data_received_script1)
                elif "script src='" in line:
                    sourcename = (line.split("src='")[1]).split("'")[0]
                    print(sourcename)
                    conn.request("_dtp", self.textboxValue + "/" + sourcename)
                    try:
                        rsp = conn.getresponse()
                    except:
                        print("Server did not respond")
                    rsts_scr = int(rsp.status)
                    print(rsts_scr)
                    self.data_received_script2 = (rsp.read()).decode("utf-8", errors="ignore")
                    if not os.path.exists(
                            os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                         "https%3A///")):
                        os.makedirs(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                 "https%3A///"))
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "x") as _script:
                            _script.write(self.data_received_script2)
                    elif os.path.exists(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                     "https%3A///")):
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "w") as _script:
                            _script.write(self.data_received_script2)

                if 'script async src="' in line:
                    sourcename = (line.split('src="')[1]).split('"')[0]
                    print(sourcename)
                    conn.request("_dtp", self.textboxValue + "/" + sourcename)
                    try:
                        rsp = conn.getresponse()
                    except:
                        print("Server did not respond")
                    rsts_scr = int(rsp.status)
                    print(rsts_scr)
                    self.data_received_script3 = (rsp.read()).decode("utf-8", errors="ignore")
                    if not os.path.exists(
                            os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                         "https%3A///")):
                        os.makedirs(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                 "https%3A///"))
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "x") as _script:
                            _script.write(self.data_received_script3)
                    elif os.path.exists(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                     "https%3A///")):
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "w") as _script:
                            _script.write(self.data_received_script3)
                elif "script async src='" in line:
                    sourcename = (line.split("src='")[1]).split("'")[0]
                    print(sourcename)
                    conn.request("_dtp", self.textboxValue + "/" + sourcename)
                    try:
                        rsp = conn.getresponse()
                    except:
                        print("Server did not respond")
                    rsts_scr = int(rsp.status)
                    print(rsts_scr)
                    self.data_received_script4 = (rsp.read()).decode("utf-8", errors="ignore")
                    if not os.path.exists(
                            os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                         "https%3A///")):
                        os.makedirs(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                 "https%3A///"))
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "x") as _script:
                            _script.write(self.data_received_script4)
                    elif os.path.exists(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                     "https%3A///")):
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "w") as _script:
                            _script.write(self.data_received_script4)

                if 'link rel="stylesheet" href="' in line:

                    sourcename = (line.split('href="')[1]).split('"')[0]
                    print(sourcename)
                    conn.request("_dtp", self.textboxValue + "/" + sourcename)
                    try:
                        rsp = conn.getresponse()
                    except:
                        print("Server did not respond")
                    rsts_sty = int(rsp.status)
                    print(rsts_sty)
                    self.data_received_style1 = (rsp.read()).decode("utf-8", errors="ignore")
                    if not os.path.exists(
                            os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                         "https%3A///")):
                        os.makedirs(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                 "https%3A///"))
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "x") as _style:
                            _style.write(self.data_received_style1)
                            _style.close()
                    elif os.path.exists(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                     "https%3A///")):
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "w") as _style:
                            _style.write(self.data_received_style1)
                            _style.close()
                elif "link rel='stylesheet' href='" in line:

                    sourcename = (line.split("href='")[1]).split("'")[0]
                    print(sourcename)
                    conn.request("_dtp", self.textboxValue + "/" + sourcename)
                    try:
                        rsp = conn.getresponse()
                    except:
                        print("Server did not respond")
                    rsts_sty = int(rsp.status)
                    print(rsts_sty)
                    self.data_received_style2 = (rsp.read()).decode("utf-8", errors="ignore")
                    if not os.path.exists(
                            os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                         "https%3A///")):
                        os.makedirs(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                 "https%3A///"))
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "x") as _style:
                            _style.write(self.data_received_style2)
                    elif os.path.exists(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                                                                                                                                                     "https%3A///")):
                        with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "w") as _style:
                            _style.write(self.data_received_style2)

                # sleep(0.1)

                # if "img " in line:
                #     if "src" in line:
                #         sourcename = (line.split('src="')[1]).split('"')[0]
                #         print(sourcename)
                #         conn.request("_dtp", self.textboxValue + "/" + sourcename)
                #         try:
                #             rsp = conn.getresponse()
                #         except:
                #             print("Server did not respond")
                #         rsts_sty = int(rsp.status)
                #         print(rsts_sty)
                #         self.data_received = (rsp.read()).decode("utf-8")
                #         if not os.path.exists(
                #                 os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                #                                                                                                                              "https%3A///")):
                #             os.makedirs(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                #                                                                                                                                      "https%3A///"))
                #             with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "xb") as _img:
                #                 targetImage = Image.open(io.BytesIO(bytes(self.data_received, "utf-8")))
                #                 targetImage.save()
                #                 _img.close()
                #         elif os.path.exists(os.getcwd() + "/" + (sourcename.removesuffix(sourcename.split("/")[len(sourcename.split("/")) - 1])).replace("https://",
                #                                                                                                                                          "https%3A///")):
                #             with open(os.getcwd() + "/" + (sourcename.replace("https://", "https%3A///")).split("?")[0], "wb") as _img:
                #                 targetImage = Image.open(io.BytesIO(bytes(self.data_received, "utf-8")))
                #                 targetImage.save()
                #                 _img.close()

                line = ''


app = QApplication([])
window = App()
app.exec_()

"""self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('SEND', self)
        self.button.move(20, 80)"""
