import os
from datetime import datetime
from dataclasses import dataclass

from PySide6.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem
from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import QFile, QIODevice
from PySide6.QtCore import QThread, Signal

from ui import main_window_ui
from functions.read_device import *

@dataclass
class FILE:
    file_name: str
    size: float
    extension: str
    last_change: datetime

class FileScannerThread(QThread):
    """Hilo para escanear archivos sin bloquear la GUI."""
    files_scanned = Signal(QTreeWidgetItem)  # Señal para actualizar el árbol

    def __init__(self, root_path):
        super().__init__()
        self.root_path = root_path
        # self.files_scanned = Signal(QTreeWidgetItem)  # Señal para actualizar el árbol

    def run(self):
        root_item = QTreeWidgetItem([os.path.basename(self.root_path), "Carpeta", ""])
        
        for foldername, subfolders, filenames in os.walk(self.root_path):
            parent_item = self.find_parent_item(root_item, foldername)

            # Agregar carpetas
            for subfolder in subfolders:
                folder_item = QTreeWidgetItem(parent_item, [subfolder, "Carpeta", ""])
                parent_item.addChild(folder_item)

            # Agregar archivos
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                file_size = os.path.getsize(file_path) // 1024  # Tamaño en KB
                file_item = QTreeWidgetItem(parent_item, [filename, "Archivo", str(file_size)])
                parent_item.addChild(file_item)

            # Emitir señal para actualizar GUI
            self.files_scanned.emit(root_item)

        # files = os.listdir(self.root_path)
        # for file in files:
        #     if os.path.isdir(os.path.join(self.root_path, file)):
        #         print(file)
        #         root_item = QTreeWidgetItem([file, "Carpeta", ""])
        #         self.files_scanned.emit(root_item)
        # print(files)

    def find_parent_item(self, root_item: QTreeWidgetItem, foldername):
        """Encuentra el item padre correspondiente en el QTreeWidget."""
        for i in range(root_item.childCount()):
            child = root_item.child(i)
            if child.text(0) == os.path.basename(foldername):
                return child
        return root_item

class MAIN_WINDOW(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(MAIN_WINDOW, self).__init__()

        ## GUI
        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tr_source.setHeaderLabels(["Nombre", "Tipo", "Tamaño (KB)"])
        self.files_scanned = Signal(QTreeWidgetItem)

        self.drives = list[HDD]
        
        ## CONNECTIONS
        self.ui.btn_source_upload.clicked.connect(self.re_load_drives)
        self.ui.btn_sync.clicked.connect(self.read_source)
    
    def re_load_drives(self):
        self.ui.cb_sources.clear()
        self.drives = get_mounted_drives()
        self.ui.cb_sources.addItems(
            [f'{drive.letter} {drive.label} ({drive.fstype})' for drive in self.drives]
        )
    
    def read_source(self):
        indx = self.ui.cb_sources.currentIndex()
        if indx >= 0:
            # print(indx)
            # print(self.drives[indx])
            # list_files_in_usb(self.drives[indx].letter)
            self.populate_tree(self.drives[indx].letter)

    def populate_tree(self, root_path):
        # """Llena el QTreeWidget con los archivos y carpetas de la unidad extraíble."""
        # root_item = QTreeWidgetItem(self.ui.tr_source, [os.path.basename(root_path), "Carpeta", ""])
        # self.ui.tr_source.addTopLevelItem(root_item)

        # for foldername, subfolders, filenames in os.walk(root_path):
        #     parent_item = self.find_parent_item(root_item, foldername)

        #     # Agregar subcarpetas
        #     for subfolder in subfolders:
        #         folder_path = os.path.join(foldername, subfolder)
        #         folder_item = QTreeWidgetItem(parent_item, [subfolder, "Carpeta", ""])
        #         parent_item.addChild(folder_item)

        #     # Agregar archivos
        #     for filename in filenames:
        #         file_path = os.path.join(foldername, filename)
        #         file_size = os.path.getsize(file_path) // 1024  # Tamaño en KB
        #         file_item = QTreeWidgetItem(parent_item, [filename, "Archivo", str(file_size)])
        #         parent_item.addChild(file_item)
        self.start_scan_thread(root_path)

    def find_parent_item(self, root_item: QTreeWidgetItem, foldername):
        """Encuentra el item padre correspondiente en el QTreeWidget."""
        for i in range(root_item.childCount()):
            child = root_item.child(i)
            if child.text(0) == os.path.basename(foldername):
                return child
        return root_item


    def start_scan_thread(self, root_path):
        """Inicia el hilo para escanear archivos."""
        self.thread = FileScannerThread(root_path)
        self.thread.files_scanned.connect(self.update_tree)
        self.thread.start()

    def update_tree(self, root_item: QTreeWidgetItem):
        """Recibe la señal del hilo y actualiza el QTreeWidget."""
        self.ui.tr_source.addTopLevelItem(root_item)
        