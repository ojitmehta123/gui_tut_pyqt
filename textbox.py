#!/usr/bin/env python
import sys
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMainWindow, QMessageBox)

class Root(QDialog):
    def __init__(self):
        super(QDialog , self).__init__()
        
        self.textBox = QLineEdit()
        self.textBox.resize(280,40)
        button = QPushButton("&Show Text")
        button.clicked.connect(self.on_click)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.textBox , 0, 0)
        mainLayout.addWidget(button , 1 , 0 , 1 , 2)

        self.setLayout(mainLayout)
        self.setWindowTitle("TextBox")

    # @pyqtSlot()
    def on_click(self):
        msg_widget = QWidget()
        msg = QMessageBox.question(msg_widget,"Result", "You Typed: "+self.textBox.text(),QMessageBox.Ok, QMessageBox.Ok)
        # msg_widget.show()
        self.textBox.setText("")

if __name__=="__main__":
    app=QApplication(sys.argv)
    o=Root()
    sys.exit(o.exec_())