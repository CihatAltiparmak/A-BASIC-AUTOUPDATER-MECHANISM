from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import app_gui


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = app_gui.Ui_MainWindow()
        self.ui.setupUi(self)


def start_application():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
