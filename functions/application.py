from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from ui import main_window_ui
from functions.read_device import list_files_in_usb

class MAIN_WINDOW(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(MAIN_WINDOW, self).__init__()

        ## GUI
        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## CONNECTIONS
        self.ui.btn_source_upload.clicked.connect(list_files_in_usb)
        