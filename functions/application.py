from datetime import datetime
from dataclasses import dataclass

from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

from ui import main_window_ui
from functions.read_device import *

@dataclass
class FILE:
    file_name: str
    size: float
    extension: str
    last_change: datetime

class MAIN_WINDOW(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(MAIN_WINDOW, self).__init__()

        ## GUI
        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## CONNECTIONS
        self.ui.btn_source_upload.clicked.connect(self.re_load_drives)
    
    def re_load_drives(self):
        self.ui.cb_sources.clear()
        drives = get_mounted_drives()
        self.ui.cb_sources.addItems(
            [f'{drive.letter} {drive.label} ({drive.fstype})' for drive in drives]
        )
        