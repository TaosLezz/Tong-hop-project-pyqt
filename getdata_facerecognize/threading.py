# from PyQt6 import QtGui, QtWidgets, QtCore
import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import cv2

class MainWindow(QtWidgets):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.VBL = QVBoxLayout()
        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.cancelbtn = QPushButton("Cancel")
        self.VBL.addWidget(self.cancelbtn)

        self.setLayout = (self.VBL)

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret,

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())

