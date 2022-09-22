# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransferTransformation_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(587, 360)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnOpenPort = QPushButton(self.groupBox)
        self.btnOpenPort.setObjectName(u"btnOpenPort")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenPort.sizePolicy().hasHeightForWidth())
        self.btnOpenPort.setSizePolicy(sizePolicy)
        self.btnOpenPort.setStyleSheet(u"border-width:0 px;")
        self.btnOpenPort.setFlat(False)

        self.gridLayout_3.addWidget(self.btnOpenPort, 0, 1, 1, 1)

        self.btnStartServerHook = QPushButton(self.groupBox)
        self.btnStartServerHook.setObjectName(u"btnStartServerHook")
        sizePolicy.setHeightForWidth(self.btnStartServerHook.sizePolicy().hasHeightForWidth())
        self.btnStartServerHook.setSizePolicy(sizePolicy)
        self.btnStartServerHook.setStyleSheet(u"")
        self.btnStartServerHook.setFlat(False)

        self.gridLayout_3.addWidget(self.btnStartServerHook, 0, 0, 1, 1)

        self.btnUpdateSelectionTransformation = QPushButton(self.groupBox)
        self.btnUpdateSelectionTransformation.setObjectName(u"btnUpdateSelectionTransformation")

        self.gridLayout_3.addWidget(self.btnUpdateSelectionTransformation, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.btnExportTransformData = QPushButton(self.groupBox_2)
        self.btnExportTransformData.setObjectName(u"btnExportTransformData")
        self.btnExportTransformData.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.btnExportTransformData, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.listTransformationData = QListWidget(self.centralwidget)
        self.listTransformationData.setObjectName(u"listTransformationData")

        self.gridLayout_2.addWidget(self.listTransformationData, 1, 0, 1, 1)

        self.listMissingObjects = QListWidget(self.centralwidget)
        self.listMissingObjects.setObjectName(u"listMissingObjects")

        self.gridLayout_2.addWidget(self.listMissingObjects, 1, 1, 1, 1)

        self.labelTransformationData = QLabel(self.centralwidget)
        self.labelTransformationData.setObjectName(u"labelTransformationData")
        self.labelTransformationData.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelTransformationData, 0, 0, 1, 1)

        self.btnDeleteTransformationData = QPushButton(self.centralwidget)
        self.btnDeleteTransformationData.setObjectName(u"btnDeleteTransformationData")

        self.gridLayout_2.addWidget(self.btnDeleteTransformationData, 3, 0, 1, 1)

        self.btnImportTransformData = QPushButton(self.centralwidget)
        self.btnImportTransformData.setObjectName(u"btnImportTransformData")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnImportTransformData.sizePolicy().hasHeightForWidth())
        self.btnImportTransformData.setSizePolicy(sizePolicy1)
        self.btnImportTransformData.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.btnImportTransformData, 2, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Online", None))
        self.btnOpenPort.setText(QCoreApplication.translate("MainWindow", u"Click To Open Port", None))
        self.btnStartServerHook.setText(QCoreApplication.translate("MainWindow", u"Choose current Maya for working", None))
        self.btnUpdateSelectionTransformation.setText(QCoreApplication.translate("MainWindow", u"Update Selection Transformation", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.btnExportTransformData.setText(QCoreApplication.translate("MainWindow", u"Export Transform Data", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Missing Objects In Target Scenes", None))
        self.labelTransformationData.setText(QCoreApplication.translate("MainWindow", u"Exported Transformation Data", None))
        self.btnDeleteTransformationData.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Transformation Data", None))
        self.btnImportTransformData.setText(QCoreApplication.translate("MainWindow", u"Import Recent Transform Data", None))
    # retranslateUi

