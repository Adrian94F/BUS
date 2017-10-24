# -*- coding: utf-8 -*-


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import socket
import re
from message import *
from thread import *
import socket
import sys
import json
import threading
from threading import Thread
import time
from message import *
from random import randint
import base64
from time import sleep
import re


def app_version():
    msg_box("Application Version", "JSONchat v1.0\nAdrian Frydmanski")


def msg_box(title, data):
    w = QWidget()
    QMessageBox.information(w, title, data)


def update_list(self, data):
    self.listWidget.addItem(data)
    print('\a')


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(845, 435)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame_top_bar = QFrame(self.centralwidget)
        self.frame_top_bar.setGeometry(QRect(10, 10, 825, 41))
        self.frame_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_top_bar.setFrameShadow(QFrame.Raised)
        self.frame_top_bar.setObjectName(_fromUtf8("frame_top_bar"))
        self.label_ip = QLabel(self.frame_top_bar)
        self.label_ip.setGeometry(QRect(10, 10, 131, 21))
        self.label_ip.setObjectName(_fromUtf8("label_ip"))
        self.lineEdit_ip = QLineEdit(self.frame_top_bar)
        self.lineEdit_ip.setGeometry(QRect(90, 10, 131, 21))
        self.lineEdit_ip.setObjectName(_fromUtf8("lineEdit_ip"))
        self.label_port = QLabel(self.frame_top_bar)
        self.label_port.setGeometry(QRect(230, 10, 131, 21))
        self.label_port.setObjectName(_fromUtf8("label_port"))
        self.lineEdit_port = QLineEdit(self.frame_top_bar)
        self.lineEdit_port.setGeometry(QRect(270, 10, 71, 21))
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.label_encryption = QLabel(self.frame_top_bar)
        self.label_encryption.setGeometry(QRect(350, 10, 81, 21))
        self.label_encryption.setObjectName(_fromUtf8("label_encryption"))
        self.lineEdit_encryption = QLineEdit(self.frame_top_bar)
        self.lineEdit_encryption.setGeometry(QRect(435, 10, 51, 21))
        self.lineEdit_encryption.setObjectName(_fromUtf8("lineEdit_encryption"))
        self.label_nick = QLabel(self.frame_top_bar)
        self.label_nick.setGeometry(QRect(500, 10, 41, 21))
        self.label_nick.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_nick = QLineEdit(self.frame_top_bar)
        self.lineEdit_nick.setGeometry(QRect(540, 10, 90, 21))
        self.lineEdit_nick.setObjectName(_fromUtf8("lineEdit_nick"))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setGeometry(QRect(10, 60, 301, 321))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QRect(10, 10, 281, 261))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_send = QPushButton(self.frame_2)
        self.pushButton_send.setGeometry(QRect(10, 280, 170, 31))
        self.pushButton_send.setObjectName(_fromUtf8("pushButton_send"))


        #############################################################
        # Executes When The Send Message Button Is Clicked
        self.pushButton_send.clicked.connect(self.client_send_message)
        ############################################################

        self.pushButton_connect = QPushButton(self.frame_top_bar)
        self.pushButton_connect.setGeometry(QRect(640, 5, 171, 31))
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))


        #############################################################
        # Executes When The Connect  Button Is Clicked
        self.pushButton_connect.clicked.connect(self.connect_with_server)
        ############################################################


        self.pushButton_clear = QPushButton(self.frame_2)
        self.pushButton_clear.setGeometry(QRect(190, 280, 93, 31))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))


        #############################################################
        # Executes When The Clear Logs Button Is Clicked
        self.pushButton_clear.clicked.connect(self.clear_logs)
        ##############################################################


        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setGeometry(QRect(320, 60, 515, 321))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.listWidget = QListWidget(self.frame_3)
        self.listWidget.setGeometry(QRect(10, 10, 496, 301))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 662, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(_fromUtf8("menuAction"))
        MainWindow.setMenuBar(self.menubar)
        self.actionExit_version = QAction(MainWindow)
        self.actionExit_version.setObjectName(_fromUtf8("actionExit_version"))

        #######################################################
        # Executes When The SubMenu Item Version Is Clicked
        self.actionExit_version.triggered.connect(app_version)
        #######################################################

        self.actionExit_exit = QAction(MainWindow)
        self.actionExit_exit.setObjectName(_fromUtf8("actionExit_exit"))

        #######################################################
        # Executes When The SubMenu Item Exit Is Clicked
        self.actionExit_exit.triggered.connect(qApp.quit)
        #######################################################

        self.menuAction.addAction(self.actionExit_version)
        self.menuAction.addAction(self.actionExit_exit)
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def clear_logs(self):
        self.listWidget.clear()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "JSONmessenger", None, QApplication.UnicodeUTF8))
        self.label_ip.setText(QApplication.translate("MainWindow", "IP Address:", None, QApplication.UnicodeUTF8))
        self.label_port.setText(QApplication.translate("MainWindow", "Port: ", None, QApplication.UnicodeUTF8))
        self.label_encryption.setText(QApplication.translate("MainWindow", "Encryption: ", None, QApplication.UnicodeUTF8))
        self.label_nick.setText(QApplication.translate("MainWindow", "Nick: ", None, QApplication.UnicodeUTF8))
        self.pushButton_send.setText(QApplication.translate("MainWindow", "Send Message", None, QApplication.UnicodeUTF8))
        self.pushButton_connect.setText(QApplication.translate("MainWindow", "Connect", None, QApplication.UnicodeUTF8))
        self.pushButton_clear.setText(QApplication.translate("MainWindow", "Clear Logs", None, QApplication.UnicodeUTF8))
        self.menuAction.setTitle(QApplication.translate("MainWindow", "Menu", None, QApplication.UnicodeUTF8))
        self.actionExit_version.setText(QApplication.translate("MainWindow", "Version", None, QApplication.UnicodeUTF8))
        self.actionExit_exit.setText(QApplication.translate("MainWindow", "Exit", None, QApplication.UnicodeUTF8))
        self.lineEdit_ip.setText('localhost')
        self.lineEdit_port.setText('2580')
        self.lineEdit_encryption.setText('none')
        self.lineEdit_nick.setText('name')

    def connect_with_server(self):
        self.pushButton_connect.setDisabled(True)
        self.addr = self.lineEdit_ip.text()
        self.port = int(self.lineEdit_port.text())
        self.encryption = self.lineEdit_encryption.text()
        self.name = self.lineEdit_nick.text()

        buffer_size = 1024

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.addr, self.port)
        print('[+] trying to connect to {} with encryption set to \'{}\''.format(server_address, self.encryption))
        try:
            self.sock.connect(server_address)
        except:
            self.pushButton_connect.setEnabled(True)
            return

        alive = 1

        # Request keys
        data = Msg.req_keys
        self.sock.send(data)

        # Wait for keys
        data = self.sock.recv(buffer_size)

        try:
            received = json.loads(data)
            p = received['p']
            g = received['g']
        except KeyError:
            error()

        # Send to server A and wait for B
        b = randint(0, 100)
        B = g ** b % p
        data = Msg.b % B
        self.sock.send(data)

        data = self.sock.recv(buffer_size)
        try:
            received = json.loads(data)
            A = received['a']
        except KeyError:
            error()

        # key
        self.K = A ** b % p

        # Send info about encryption
        data = Msg.encr_req % self.encryption
        sleep(0.1)
        self.sock.send(data)

        while alive == 1:
            data = self.sock.recv(buffer_size)
            try:
                data = json.loads(data)
                msg = data['msg']
                sender = data['from']
            except ValueError:
                error()
                return
            msg = base64.b64decode(msg)
            msg = decrypt(msg, self.encryption, self.K)
            self.textEdit.append('[{}] {}'.format(sender, msg))

    def client_send_message(self):
        # nick = self.lineEdit_port.text()
        # rmessage = self.textEdit.toPlainText()
        # rmessage = rmessage.replace("#>","")
        #
        # rmsg = nick + " #> " + rmessage
        #
        # c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #
        # try:
        #     c.connect((ip_address, port))
        # except:
        #     msg_box("Connection Refused", "The Address You Are Trying To Reach Is Currently Unavailable.")
        #     return
        #
        # try:
        #     c.send(rmsg)
        #     self.listWidget.addItem(rmsg)
        #     self.textEdit.setText("")
        # except:
        #     msg_box("Connection Refused", "The Message Cannot Be Sent. End-Point Not Connected!")
        #
        # c.close()
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    