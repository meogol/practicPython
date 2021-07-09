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

        vm = ViewModel


        """ Connection of download image button to slot input_of_image in ViewModel"""
        self.ui.downloadBtn.clicked.connect(self.open_file_dialog)


        """ Connection of start analyze button to slot analysis in ViewModel"""
        self.ui.analyzeBtn.clicked.connect(self.analysis_process)




    def analysis_process(self):
        vm = ViewModel
        vm.analysis
        """ Placing image in image holder from slot get_image in ViewModel"""
        pixmap = vm.get_image(self, 417, 586)
        self.ui.imgHolder.setPixmap(pixmap)

    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg)")
        self.ui.downloadBtn.clicked.connect(self, vm.input_of_image(fname))


        """ Placing image in image holder from slot get_image in ViewModel"""
        pixmap = vm.get_image(self, 417, 586)
        self.ui.imgHolder.setPixmap(pixmap)




app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())