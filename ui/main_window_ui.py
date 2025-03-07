# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 723)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cb_sources = QComboBox(self.centralwidget)
        self.cb_sources.setObjectName(u"cb_sources")
        self.cb_sources.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.cb_sources, 0, 0, 1, 1)

        self.btn_source_upload = QPushButton(self.centralwidget)
        self.btn_source_upload.setObjectName(u"btn_source_upload")
        self.btn_source_upload.setMinimumSize(QSize(120, 40))
        self.btn_source_upload.setMaximumSize(QSize(120, 16777215))
        font = QFont()
        font.setBold(True)
        self.btn_source_upload.setFont(font)

        self.gridLayout_2.addWidget(self.btn_source_upload, 0, 1, 1, 1)

        self.tx_destiny = QLineEdit(self.centralwidget)
        self.tx_destiny.setObjectName(u"tx_destiny")
        self.tx_destiny.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.tx_destiny, 1, 0, 1, 1)

        self.btn_destiny_find = QPushButton(self.centralwidget)
        self.btn_destiny_find.setObjectName(u"btn_destiny_find")
        self.btn_destiny_find.setMinimumSize(QSize(120, 40))
        self.btn_destiny_find.setMaximumSize(QSize(120, 16777215))
        self.btn_destiny_find.setFont(font)

        self.gridLayout_2.addWidget(self.btn_destiny_find, 1, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(self.frame)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.treeWidget_2 = QTreeWidget(self.frame)
        QTreeWidgetItem(self.treeWidget_2)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        sizePolicy.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.treeWidget_2, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)

        self.btn_sync = QPushButton(self.centralwidget)
        self.btn_sync.setObjectName(u"btn_sync")
        self.btn_sync.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_sync.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_sync, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1016, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FAST BACKUP", None))
        self.btn_source_upload.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.btn_destiny_find.setText(QCoreApplication.translate("MainWindow", u"FIND", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Extension", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Col 1", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"file.exe", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem2 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Extension", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Col 1", None));

        __sortingEnabled1 = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        ___qtreewidgetitem3 = self.treeWidget_2.topLevelItem(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"file.exe", None));
        self.treeWidget_2.setSortingEnabled(__sortingEnabled1)

        self.btn_sync.setText(QCoreApplication.translate("MainWindow", u"SYNC", None))
    # retranslateUi

