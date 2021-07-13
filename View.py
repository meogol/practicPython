from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QInputDialog, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from mainview import Ui_MainWindow
from ViewModel import ViewModel
from PIL import Image, ImageTk
import sys


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vm = ViewModel()

        """ Connection of download image button to slot input_of_image in ViewModel"""
        self.ui.downloadBtn.clicked.connect(self.open_file_dialog)

        """ Connection of start analyze button to slot analysis in ViewModel"""
        self.ui.analyzeBtn.clicked.connect(self.analysis_process)

        """ Changing background color of image holder """
        self.ui.imgHolder.setStyleSheet("background-color: #D9D9D9")

    def analysis_process(self):
        # self.vm.analysis()
        # """ Placing image in image holder from slot get_image in ViewModel"""
        # pixmap = QPixmap(self.vm.get_image(417, 586))
        # self.ui.imgHolder.setPixmap(pixmap)
        # self.ui.imgHolder.resize(417, 586)
        # self.show()

        """ Displaying information about lungs on picture in text window """
        percent = self.vm.analysis()
        self.ui.textBrowser.setPlainText(str(percent))
        self.show()

    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg)")[0]

        if len(fname) < 2:
            return

        self.vm.input_of_image(fname)

        """ Placing original image in image holder """
        pixmap = QPixmap(fname)
        self.ui.imgHolder.setPixmap(pixmap)
        self.ui.imgHolder.resize(417, 586)
        self.show()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
