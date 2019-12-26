# import sys
# from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

# app = QtWidgets.QApplication(sys.argv)
# loader = QtWebEngineWidgets.QWebEngineView()
# loader.setZoomFactor(1)
# loader.page().pdfPrintingFinished.connect(
#     lambda *args: print('finished:', args))
# loader.load(QtCore.QUrl('https://en.wikipedia.org/wiki/Main_Page'))

# def emit_pdf(finished):
#     loader.show()
#     loader.page().printToPdf("test.pdf")

# loader.loadFinished.connect(emit_pdf)

# app.exec()

# from PyQt5.QtWidgets import QMainWindow , QLabel , QApplication , QPushButton
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         btn = QPushButton('Click me!', self)
#         btn.clicked.connect(self.onClick)

#     def onClick(self):
#         self.SW = SecondWindow()
#         self.SW.show()

# class SecondWindow(QMainWindow):
#     def __init__(self):
#         super(SecondWindow, self).__init__()
#         lbl = QLabel('Second Window', self)

# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     MW = MainWindow()
#     MW.show()
#     sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd

from PandasModel import PandasModel

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()
        self.pathLE = QtWidgets.QLineEdit(self)
        hLayout.addWidget(self.pathLE)
        self.loadBtn = QtWidgets.QPushButton("Select File", self)
        hLayout.addWidget(self.loadBtn)
        vLayout.addLayout(hLayout)
        self.pandasTv = QtWidgets.QTableView(self)
        vLayout.addWidget(self.pandasTv)
        self.loadBtn.clicked.connect(self.loadFile)
        self.pandasTv.setSortingEnabled(True)

    def loadFile(self):
        fileName, _ftype = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv);;XLS files (*.xls)")
        self.pathLE.setText(fileName)
        if _ftype == 'XLS files (*.xls)':
            df = pd.read_excel(fileName)
        else:
            df = pd.read_csv(fileName)
        model = PandasModel(df)
        self.pandasTv.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
sys.exit(app.exec_())