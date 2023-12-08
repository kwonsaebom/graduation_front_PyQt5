from PyQt5.QtWidgets import QApplication, QTextBrowser, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtWidgets
import sys

from bardapi import Bard
img = "btn.png"

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Graduation Project"
        self.resize(600, 700)

        self.setStyleSheet("background-color: rgb(192, 206, 236);")
        self.setWindowTitle(self.title)
        #self.setGeometry(self.top, self.left, self.width, self.height)
        self.setup_ui()

    def setup_ui(self):
        self.browser = QTextBrowser(self)
        self.browser.setGeometry(QtCore.QRect(20, 110, 561, 501))
        self.browser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browser.setObjectName("textBrowser")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(20, 620, 481, 61))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.btn = QPushButton(self)
        self.btn.setGeometry(QtCore.QRect(505, 620, 77, 61))
        self.btn.setObjectName("button")

        send_icon = QIcon(QPixmap("btn_icon.png"))
        self.btn.setIcon(send_icon)
        self.btn.setIconSize(self.btn.size())

        self.btn.clicked.connect(self.update_browser)
        
        self.main_btn = QPushButton(self)
        self.main_btn.setGeometry(QtCore.QRect(200, 5, 180, 100))
        self.main_btn.setObjectName("main_button")

        main_icon = QIcon(QPixmap("chat.png"))
        self.main_btn.setIcon(main_icon)
        self.main_btn.setIconSize(self.main_btn.size())

        self.main_btn.clicked.connect(self.clear_browser)

        self.lineEdit.returnPressed.connect(self.update_browser)

    def update_browser(self):
        
        token = 'Your API Token'
        
        bard = Bard(token=token)

        question = str(self.lineEdit.text())
        response = bard.get_answer(question)['content']

        self.browser.append("<font color='gray'>%s</font>"  % question)
        self.browser.append(response)
        self.lineEdit.clear()
        
    def clear_browser(self):
        self.browser.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
