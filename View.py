import sys

from PIL import Image
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, Qt
from ViewModel import ViewModel
from mainview import Ui_MainWindow


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

    def analysis_process(self):
        """ Вызов метода анализа из файла ViewModel, отображение возвращённого изображения из нейросети и текста"""

        # self.vm.analysis()
        # """ Placing image in image holder from slot get_image in ViewModel"""
        # pixmap = QPixmap(self.vm.get_image(417, 586))
        # self.ui.imgHolder.setPixmap(pixmap)
        # self.ui.imgHolder.resize(417, 586)
        # self.show()

        status = self.vm.analysis()
        if status == 1:

            self.ui.textBrowser.setPlainText("Больные лёгкие")
            self.show()
        else:
            self.ui.textBrowser.setPlainText("Лёгкие здоровы")
            self.show()

    def open_file_dialog(self):
        """ Открытие диалогового окна выбора файла, проверка на наличие пути, вывод выбранного изображения на экран """

        fname = QFileDialog.getOpenFileName(self, 'Open file', '.\\', "Image files (*.dcm)")[0]

        if len(fname) < 2:
            return

        self.vm.input_of_image(fname)
        im = self.vm.xray
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)

        pixmap = QPixmap().fromImage(qim)
        pixmap = pixmap.scaled(417,586, QtCore.Qt.KeepAspectRatio)
        self.ui.imgHolder.setPixmap(pixmap)
        self.ui.imgHolder.resize(417, 586)
        self.show()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
