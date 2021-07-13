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

        # Связь кнопки загруки изображения (downloadBtn) с методом открытия файлового диалога (open_file_dialog)
        self.ui.downloadBtn.clicked.connect(self.open_file_dialog)


        # Связь кнопки analyzeBtn и метода analysis_process
        self.ui.analyzeBtn.clicked.connect(self.analysis_process)

        # Изменение цвета заднего фона поля изображения
        self.ui.imgHolder.setStyleSheet("background-color: #D9D9D9")

    """ Вызов метода анализа из файла ViewModel, отображение возвращённого изображения из нейросети и текста"""
    def analysis_process(self):
        # self.vm.analysis()
        # """ Placing image in image holder from slot get_image in ViewModel"""
        # pixmap = QPixmap(self.vm.get_image(417, 586))
        # self.ui.imgHolder.setPixmap(pixmap)
        # self.ui.imgHolder.resize(417, 586)
        # self.show()


        percent = self.vm.analysis()
        self.ui.textBrowser.setPlainText(str(percent))
        self.show()

    """ Открытие диалогового окна выбора файла, проверка на наличие пути, вывод выбранного изображения на экран """
    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.dcm)")[0]

        if len(fname) < 2:
            return

        self.vm.input_of_image(fname)

        #Вывод изображения на экран с помощью pixmap
        pixmap = QPixmap(fname)
        self.ui.imgHolder.setPixmap(pixmap)
        self.ui.imgHolder.resize(417, 586)
        self.show()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
