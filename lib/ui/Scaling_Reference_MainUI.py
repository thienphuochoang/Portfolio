# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Scaling_Reference_MainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Scaling_Reference_MainWindow(object):
    def setupUi(self, Scaling_Reference_MainWindow):
        if not Scaling_Reference_MainWindow.objectName():
            Scaling_Reference_MainWindow.setObjectName(u"Scaling_Reference_MainWindow")
        Scaling_Reference_MainWindow.resize(518, 43)
        Scaling_Reference_MainWindow.setMinimumSize(QSize(518, 43))
        Scaling_Reference_MainWindow.setMaximumSize(QSize(518, 43))
        self.centralwidget = QWidget(Scaling_Reference_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnOpenRefFolder = QPushButton(self.centralwidget)
        self.btnOpenRefFolder.setObjectName(u"btnOpenRefFolder")
        self.btnOpenRefFolder.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.btnOpenRefFolder, 0, 2, 1, 1)

        self.cbbRefFiles = QComboBox(self.centralwidget)
        self.cbbRefFiles.setObjectName(u"cbbRefFiles")

        self.gridLayout_2.addWidget(self.cbbRefFiles, 0, 0, 1, 1)

        self.btnImportRef = QPushButton(self.centralwidget)
        self.btnImportRef.setObjectName(u"btnImportRef")
        self.btnImportRef.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.btnImportRef, 0, 1, 1, 1)

        Scaling_Reference_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Scaling_Reference_MainWindow)

        QMetaObject.connectSlotsByName(Scaling_Reference_MainWindow)
    # setupUi

    def retranslateUi(self, Scaling_Reference_MainWindow):
        Scaling_Reference_MainWindow.setWindowTitle(QCoreApplication.translate("Scaling_Reference_MainWindow", u"Scaling Ref Main Window", None))
        self.btnOpenRefFolder.setText(QCoreApplication.translate("Scaling_Reference_MainWindow", u"Open Ref Folder", None))
        self.btnImportRef.setText(QCoreApplication.translate("Scaling_Reference_MainWindow", u"Import Ref", None))
    # retranslateUi

