# -*- coding: utf-8 -*-


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import socket
from thread import *


def app_version():
    msg_box("Application Version", "JSONchat v1.0\nAdrian Frydmanski")


def msg_box(title, data):
    w = QWidget()
    QMessageBox.information(w, title, data)


def update_list(self, data):
    self.listWidget.addItem(data)
    print "\a"


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(662, 448)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(10, 10, 651, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(10, 10, 131, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setGeometry(QRect(90, 10, 131, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QLabel(self.frame)
        self.label_2.setGeometry(QRect(230, 10, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QRect(270, 10, 71, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QLabel(self.frame)
        self.label_3.setGeometry(QRect(350, 10, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QRect(435, 10, 51, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_4 = QLabel(self.frame)
        self.label_4.setGeometry(QRect(500, 10, 41, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QRect(540, 10, 90, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setGeometry(QRect(10, 60, 301, 321))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QRect(10, 10, 281, 261))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QRect(10, 280, 171, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))


        #############################################################
        # Executes When The Send Message Button Is Clicked
        self.pushButton_3.clicked.connect(self.client_send_message)
        ############################################################


        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QRect(190, 280, 93, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))


        #############################################################
        # Executes When The Clear Logs Button Is Clicked
        self.pushButton_4.clicked.connect(self.clear_logs)
        ##############################################################


        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setGeometry(QRect(320, 60, 331, 321))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.listWidget = QListWidget(self.frame_3)
        self.listWidget.setGeometry(QRect(10, 10, 311, 301))
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
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        #######################################################
        # Executes When The SubMenu Item Version Is Clicked
        self.actionExit.triggered.connect(app_version)
        #######################################################

        self.actionExit_2 = QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))

        #######################################################
        # Executes When The SubMenu Item Exit Is Clicked
        self.actionExit_2.triggered.connect(qApp.quit)
        #######################################################

        self.menuAction.addAction(self.actionExit)
        self.menuAction.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def clear_logs(self):
        self.listWidget.clear()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow",
                                                         "JSONmessenger", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("MainWindow", "IP Address:",
                                                  None, QApplication.UnicodeUTF8))
        self.label_2.setText(QApplication.translate("MainWindow", "Port: ",
                                                    None, QApplication.UnicodeUTF8))
        self.label_3.setText(QApplication.translate("MainWindow", "Encryption: ",
                                                    None, QApplication.UnicodeUTF8))
        self.label_4.setText(QApplication.translate("MainWindow", "Nick: ",
                                                    None, QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QApplication.translate("MainWindow",
                                                         "Send Message", None, QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QApplication.translate("MainWindow",
                                                         "Clear Logs", None, QApplication.UnicodeUTF8))
        self.menuAction.setTitle(QApplication.translate("MainWindow",
                                                        "Menu Actions", None, QApplication.UnicodeUTF8))
        self.actionExit.setText(QApplication.translate("MainWindow",
                                                       "Version", None, QApplication.UnicodeUTF8))
        self.actionExit_2.setText(QApplication.translate("MainWindow",
                                                         "Exit", None, QApplication.UnicodeUTF8))
        self.lineEdit.setText('localhost')
        self.lineEdit_2.setText('2580')
        self.lineEdit_3.setText('none')
        self.lineEdit_4.setText('name')

    def client_send_message(self):
        ip_address = self.lineEdit.text()
        port = int(self.lineEdit_2.text())

        nick = self.lineEdit_2.text()
        nick = nick.replace("#>","")
        rmessage = self.textEdit.toPlainText()
        rmessage = rmessage.replace("#>","")

        rmsg = nick + " #> " + rmessage

        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            c.connect((ip_address, port))
        except:
            msg_box("Connection Refused", "The Address You Are Trying To Reach Is Currently Unavailable.")
            return

        try:
            c.send(rmsg)
            self.listWidget.addItem(rmsg)
            self.textEdit.setText("")
        except:
            msg_box("Connection Refused", "The Message Cannot Be Sent. End-Point Not Connected!")

        c.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())