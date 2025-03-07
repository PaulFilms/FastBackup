'''
'''

import os, sys
from PySide6.QtWidgets import QApplication, QMainWindow
from functions import application

if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WINDOW = application.MAIN_WINDOW()
    WINDOW.show()
    sys.exit(APP.exec())