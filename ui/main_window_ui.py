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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 723)
        self.actionOpen_Sesseion = QAction(MainWindow)
        self.actionOpen_Sesseion.setObjectName(u"actionOpen_Sesseion")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tx_destiny = QLineEdit(self.centralwidget)
        self.tx_destiny.setObjectName(u"tx_destiny")
        self.tx_destiny.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        self.tx_destiny.setFont(font)

        self.gridLayout_2.addWidget(self.tx_destiny, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.tr_source = QTreeWidget(self.splitter)
        QTreeWidgetItem(self.tr_source)
        self.tr_source.setObjectName(u"tr_source")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tr_source.sizePolicy().hasHeightForWidth())
        self.tr_source.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(10)
        self.tr_source.setFont(font1)
        self.splitter.addWidget(self.tr_source)
        self.tr_destiny = QTreeWidget(self.splitter)
        QTreeWidgetItem(self.tr_destiny)
        self.tr_destiny.setObjectName(u"tr_destiny")
        sizePolicy.setHeightForWidth(self.tr_destiny.sizePolicy().hasHeightForWidth())
        self.tr_destiny.setSizePolicy(sizePolicy)
        self.tr_destiny.setFont(font1)
        self.splitter.addWidget(self.tr_destiny)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)

        self.cb_sources = QComboBox(self.centralwidget)
        self.cb_sources.addItem("")
        self.cb_sources.setObjectName(u"cb_sources")
        self.cb_sources.setMinimumSize(QSize(0, 50))
        self.cb_sources.setFont(font)

        self.gridLayout_2.addWidget(self.cb_sources, 0, 0, 1, 1)

        self.btn_source_upload = QPushButton(self.centralwidget)
        self.btn_source_upload.setObjectName(u"btn_source_upload")
        self.btn_source_upload.setMinimumSize(QSize(120, 50))
        self.btn_source_upload.setMaximumSize(QSize(120, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_source_upload.setFont(font2)

        self.gridLayout_2.addWidget(self.btn_source_upload, 0, 1, 1, 1)

        self.btn_sync = QPushButton(self.centralwidget)
        self.btn_sync.setObjectName(u"btn_sync")
        self.btn_sync.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.btn_sync.setFont(font3)

        self.gridLayout_2.addWidget(self.btn_sync, 3, 0, 1, 2)

        self.btn_destiny_find = QPushButton(self.centralwidget)
        self.btn_destiny_find.setObjectName(u"btn_destiny_find")
        self.btn_destiny_find.setMinimumSize(QSize(120, 50))
        self.btn_destiny_find.setMaximumSize(QSize(120, 16777215))
        self.btn_destiny_find.setFont(font2)

        self.gridLayout_2.addWidget(self.btn_destiny_find, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1016, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen_Sesseion)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FAST BACKUP", None))
        self.actionOpen_Sesseion.setText(QCoreApplication.translate("MainWindow", u"Open Sesseion", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        ___qtreewidgetitem = self.tr_source.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Extension", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Col 1", None));

        __sortingEnabled = self.tr_source.isSortingEnabled()
        self.tr_source.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tr_source.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"file.exe", None));
        self.tr_source.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem2 = self.tr_destiny.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Extension", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Col 1", None));

        __sortingEnabled1 = self.tr_destiny.isSortingEnabled()
        self.tr_destiny.setSortingEnabled(False)
        ___qtreewidgetitem3 = self.tr_destiny.topLevelItem(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"file.exe", None));
        self.tr_destiny.setSortingEnabled(__sortingEnabled1)

        self.cb_sources.setItemText(0, QCoreApplication.translate("MainWindow", u"sdf", None))

        self.btn_source_upload.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.btn_sync.setText(QCoreApplication.translate("MainWindow", u"SYNC", None))
        self.btn_destiny_find.setText(QCoreApplication.translate("MainWindow", u"FIND", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

