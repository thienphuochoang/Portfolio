# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Thien Phuoc\Documents\maya\2018\scripts\TransferTransformation\UI\TransferTransformation_UI.ui',
# licensing of 'C:\Users\Thien Phuoc\Documents\maya\2018\scripts\TransferTransformation\UI\TransferTransformation_UI.ui' applies.
#
# Created: Thu Mar  5 23:29:01 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnOpenPort = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenPort.sizePolicy().hasHeightForWidth())
        self.btnOpenPort.setSizePolicy(sizePolicy)
        self.btnOpenPort.setStyleSheet("border-width:0 px;")
        self.btnOpenPort.setFlat(False)
        self.btnOpenPort.setObjectName("btnOpenPort")
        self.gridLayout_3.addWidget(self.btnOpenPort, 0, 1, 1, 1)
        self.btnStartServerHook = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartServerHook.sizePolicy().hasHeightForWidth())
        self.btnStartServerHook.setSizePolicy(sizePolicy)
        self.btnStartServerHook.setStyleSheet("")
        self.btnStartServerHook.setFlat(False)
        self.btnStartServerHook.setObjectName("btnStartServerHook")
        self.gridLayout_3.addWidget(self.btnStartServerHook, 0, 0, 1, 1)
        self.btnUpdateSelectionTransformation = QtWidgets.QPushButton(self.groupBox)
        self.btnUpdateSelectionTransformation.setObjectName("btnUpdateSelectionTransformation")
        self.gridLayout_3.addWidget(self.btnUpdateSelectionTransformation, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnExportTransformData = QtWidgets.QPushButton(self.groupBox_2)
        self.btnExportTransformData.setMinimumSize(QtCore.QSize(0, 25))
        self.btnExportTransformData.setObjectName("btnExportTransformData")
        self.gridLayout_4.addWidget(self.btnExportTransformData, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.listTransformationData = QtWidgets.QListWidget(self.centralwidget)
        self.listTransformationData.setObjectName("listTransformationData")
        self.gridLayout_2.addWidget(self.listTransformationData, 1, 0, 1, 1)
        self.listMissingObjects = QtWidgets.QListWidget(self.centralwidget)
        self.listMissingObjects.setObjectName("listMissingObjects")
        self.gridLayout_2.addWidget(self.listMissingObjects, 1, 1, 1, 1)
        self.labelTransformationData = QtWidgets.QLabel(self.centralwidget)
        self.labelTransformationData.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTransformationData.setObjectName("labelTransformationData")
        self.gridLayout_2.addWidget(self.labelTransformationData, 0, 0, 1, 1)
        self.btnDeleteTransformationData = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteTransformationData.setObjectName("btnDeleteTransformationData")
        self.gridLayout_2.addWidget(self.btnDeleteTransformationData, 3, 0, 1, 1)
        self.btnImportTransformData = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImportTransformData.sizePolicy().hasHeightForWidth())
        self.btnImportTransformData.setSizePolicy(sizePolicy)
        self.btnImportTransformData.setMinimumSize(QtCore.QSize(0, 25))
        self.btnImportTransformData.setObjectName("btnImportTransformData")
        self.gridLayout_2.addWidget(self.btnImportTransformData, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Online", None, -1))
        self.btnOpenPort.setText(QtWidgets.QApplication.translate("MainWindow", "Click To Open Port", None, -1))
        self.btnStartServerHook.setText(QtWidgets.QApplication.translate("MainWindow", "Choose current Maya for working", None, -1))
        self.btnUpdateSelectionTransformation.setText(QtWidgets.QApplication.translate("MainWindow", "Update Selection Transformation", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Offline", None, -1))
        self.btnExportTransformData.setText(QtWidgets.QApplication.translate("MainWindow", "Export Transform Data", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Missing Objects In Target Scenes", None, -1))
        self.labelTransformationData.setText(QtWidgets.QApplication.translate("MainWindow", "Exported Transformation Data", None, -1))
        self.btnDeleteTransformationData.setText(QtWidgets.QApplication.translate("MainWindow", "Delete Selected Transformation Data", None, -1))
        self.btnImportTransformData.setText(QtWidgets.QApplication.translate("MainWindow", "Import Recent Transform Data", None, -1))

