import sys
import random

from PyQt6.QtGui import QFont
from PySide6 import QtCore, QtWidgets, QtGui, QtTest
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

import time
from datetime import timedelta


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        self.button_1 = MyButton()
        self.button_2 = MyButton()

        self.layout.addWidget(self.button_1)
        self.layout.addWidget(self.button_2)

        self.button_1.clicked.connect(self.click_button1)
        self.button_2.clicked.connect(self.click_button2)

    def click_button1(self):

        if self.button_2.clicked:
            self.button_2.timer.stop()
            self.button_2.setStyleSheet("background-color : white")

        self.button_2.setEnabled(True)

        self.button_1.setEnabled(False)
        MyButton.button_timer(self.button_1)
        self.button_1.setStyleSheet("background-color : yellow")



    def click_button2(self):
        if self.button_1.clicked:
            self.button_1.timer.stop()
            self.button_1.setStyleSheet("background-color : white")

        self.button_1.setEnabled(True)
        self.button_2.setEnabled(False)
        MyButton.button_timer(self.button_2)
        self.button_2.setStyleSheet("background-color : yellow")




class MyButton(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.timer = QtCore.QTimer()

        self.text = 600
        self.setText(str(timedelta(seconds=self.text)))
        self.setStyleSheet("background-color : white")
        self.setFont(('Arial',100))

    def button_timer(self):
        self.timer.timeout.connect(self.start_timer)
        self.timer.start(1000)

    def start_timer(self):
        if self.text == 0:
            self.timer.stop()

        else:
            self.text -= 1
            self.timer.start(1000)
            self.setText(str(self.text))
            self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    # widget.setSizePolicy(QtWidgets.QSizePolicy.)
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec())