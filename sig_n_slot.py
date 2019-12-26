#!/usr/bin/env python
import sys
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class RootClass(QDialog):

    def __init__(self):
        super(QDialog, self).__init__()

        button = QPushButton("Click")
        button.setToolTip("Will Trigger Click func")
        button.clicked.connect(self.click_func)

        mainLayout = QGridLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle("Click")

    def  click_func(self):
        print("Click!")

if __name__=="__main__":
    app=QApplication(sys.argv)
    o=RootClass()
    sys.exit(o.exec_())
