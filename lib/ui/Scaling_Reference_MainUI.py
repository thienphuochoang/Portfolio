# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/WIP_Portfolio/lib/ui/Scaling_Reference_MainUI.ui',
# licensing of 'D:/WIP_Portfolio/lib/ui/Scaling_Reference_MainUI.ui' applies.
#
# Created: Wed Mar 10 21:58:57 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Scaling_Reference_MainWindow(object):
    def setupUi(self, Scaling_Reference_MainWindow):
        Scaling_Reference_MainWindow.setObjectName("Scaling_Reference_MainWindow")
        Scaling_Reference_MainWindow.resize(518, 43)
        Scaling_Reference_MainWindow.setMinimumSize(QtCore.QSize(518, 43))
        Scaling_Reference_MainWindow.setMaximumSize(QtCore.QSize(518, 43))
        self.centralwidget = QtWidgets.QWidget(Scaling_Reference_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnOpenRefFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenRefFolder.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnOpenRefFolder.setObjectName("btnOpenRefFolder")
        self.gridLayout_2.addWidget(self.btnOpenRefFolder, 0, 2, 1, 1)
        self.cbbRefFiles = QtWidgets.QComboBox(self.centralwidget)
        self.cbbRefFiles.setObjectName("cbbRefFiles")
        self.gridLayout_2.addWidget(self.cbbRefFiles, 0, 0, 1, 1)
        self.btnImportRef = QtWidgets.QPushButton(self.centralwidget)
        self.btnImportRef.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnImportRef.setObjectName("btnImportRef")
        self.gridLayout_2.addWidget(self.btnImportRef, 0, 1, 1, 1)
        Scaling_Reference_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Scaling_Reference_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Scaling_Reference_MainWindow)

    def retranslateUi(self, Scaling_Reference_MainWindow):
        Scaling_Reference_MainWindow.setWindowTitle(QtWidgets.QApplication.translate("Scaling_Reference_MainWindow", "Scaling Ref Main Window", None, -1))
        self.btnOpenRefFolder.setText(QtWidgets.QApplication.translate("Scaling_Reference_MainWindow", "Open Ref Folder", None, -1))
        self.btnImportRef.setText(QtWidgets.QApplication.translate("Scaling_Reference_MainWindow", "Import Ref", None, -1))

