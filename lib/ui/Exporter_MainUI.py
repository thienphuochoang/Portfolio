# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Exporter_MainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindowExporter(object):
    def setupUi(self, MainWindowExporter):
        if not MainWindowExporter.objectName():
            MainWindowExporter.setObjectName(u"MainWindowExporter")
        MainWindowExporter.resize(384, 287)
        self.centralwidget = QWidget(MainWindowExporter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnFixMaterial = QPushButton(self.centralwidget)
        self.btnFixMaterial.setObjectName(u"btnFixMaterial")
        self.btnFixMaterial.setMinimumSize(QSize(0, 21))
        self.btnFixMaterial.setMaximumSize(QSize(16777215, 16777215))
        self.btnFixMaterial.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(159, 169, 163);\n"
"	border: 1px;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btnFixMaterial)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cbBinary = QCheckBox(self.centralwidget)
        self.cbBinary.setObjectName(u"cbBinary")
        self.cbBinary.setMaximumSize(QSize(60, 16777215))
        self.cbBinary.setStyleSheet(u"background-color: rgb(103, 77, 60);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.cbBinary)

        self.cbKeepInstance = QCheckBox(self.centralwidget)
        self.cbKeepInstance.setObjectName(u"cbKeepInstance")
        self.cbKeepInstance.setMaximumSize(QSize(60, 16777215))
        self.cbKeepInstance.setStyleSheet(u"background-color: rgb(103, 77, 60);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.cbKeepInstance)

        self.cbKeepVertexNormal = QCheckBox(self.centralwidget)
        self.cbKeepVertexNormal.setObjectName(u"cbKeepVertexNormal")
        self.cbKeepVertexNormal.setMaximumSize(QSize(60, 16777215))
        self.cbKeepVertexNormal.setStyleSheet(u"background-color: rgb(159, 169, 163);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.cbKeepVertexNormal)

        self.cbKeepGroup = QCheckBox(self.centralwidget)
        self.cbKeepGroup.setObjectName(u"cbKeepGroup")
        self.cbKeepGroup.setMaximumSize(QSize(60, 16777215))
        self.cbKeepGroup.setStyleSheet(u"background-color: rgb(159, 169, 163);\n"
"color: rgb(0, 0, 0);")
        self.cbKeepGroup.setTristate(False)

        self.horizontalLayout.addWidget(self.cbKeepGroup)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnExport = QPushButton(self.centralwidget)
        self.btnExport.setObjectName(u"btnExport")
        self.btnExport.setMinimumSize(QSize(0, 54))
        self.btnExport.setMaximumSize(QSize(70, 16777215))
        self.btnExport.setStyleSheet(u"QPushButton { \n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(103, 77, 60);\n"
"	border: 1px;\n"
"}\n"
"")
        self.btnExport.setCheckable(False)

        self.horizontalLayout_8.addWidget(self.btnExport)

        self.btnImport = QPushButton(self.centralwidget)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setMinimumSize(QSize(0, 54))
        self.btnImport.setMaximumSize(QSize(70, 16777215))
        self.btnImport.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(159, 169, 163);\n"
"	border: 1px;\n"
"}\n"
"")
        self.btnImport.setAutoDefault(False)

        self.horizontalLayout_8.addWidget(self.btnImport)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 1, 2, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnExportSP = QPushButton(self.centralwidget)
        self.btnExportSP.setObjectName(u"btnExportSP")
        self.btnExportSP.setMinimumSize(QSize(0, 23))
        self.btnExportSP.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_4.addWidget(self.btnExportSP)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnExportSeparatePart = QPushButton(self.centralwidget)
        self.btnExportSeparatePart.setObjectName(u"btnExportSeparatePart")
        self.btnExportSeparatePart.setMinimumSize(QSize(0, 0))
        self.btnExportSeparatePart.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.btnExportSeparatePart)

        self.btnExportCurrentFolder = QPushButton(self.centralwidget)
        self.btnExportCurrentFolder.setObjectName(u"btnExportCurrentFolder")
        self.btnExportCurrentFolder.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btnExportCurrentFolder)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnExportHigh = QPushButton(self.centralwidget)
        self.btnExportHigh.setObjectName(u"btnExportHigh")
        self.btnExportHigh.setMinimumSize(QSize(70, 0))
        self.btnExportHigh.setMaximumSize(QSize(70, 16777215))
        self.btnExportHigh.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btnExportHigh)

        self.btnExportLow = QPushButton(self.centralwidget)
        self.btnExportLow.setObjectName(u"btnExportLow")
        self.btnExportLow.setMinimumSize(QSize(70, 0))
        self.btnExportLow.setMaximumSize(QSize(70, 16777215))
        self.btnExportLow.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btnExportLow)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 1, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnExportWorking = QPushButton(self.centralwidget)
        self.btnExportWorking.setObjectName(u"btnExportWorking")
        self.btnExportWorking.setMinimumSize(QSize(0, 21))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.btnExportWorking.setFont(font)
        self.btnExportWorking.setAutoFillBackground(False)
        self.btnExportWorking.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(103, 77, 60);\n"
"	border: 1px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btnExportWorking)

        self.btnImportWorking = QPushButton(self.centralwidget)
        self.btnImportWorking.setObjectName(u"btnImportWorking")
        self.btnImportWorking.setMinimumSize(QSize(0, 21))
        self.btnImportWorking.setStyleSheet(u"QPushButton { \n"
"	background-color: rgb(159, 169, 163);\n"
"	border: 1px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btnImportWorking)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnOpenFolder = QPushButton(self.centralwidget)
        self.btnOpenFolder.setObjectName(u"btnOpenFolder")
        self.btnOpenFolder.setMinimumSize(QSize(70, 0))
        self.btnOpenFolder.setMaximumSize(QSize(70, 16777215))
        self.btnOpenFolder.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btnOpenFolder)

        self.btnDeleteFolder = QPushButton(self.centralwidget)
        self.btnDeleteFolder.setObjectName(u"btnDeleteFolder")
        self.btnDeleteFolder.setMinimumSize(QSize(70, 0))
        self.btnDeleteFolder.setMaximumSize(QSize(70, 16777215))
        self.btnDeleteFolder.setFlat(True)

        self.horizontalLayout_7.addWidget(self.btnDeleteFolder)


        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 1, 1, 2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.rbFBX = QRadioButton(self.centralwidget)
        self.rbFBX.setObjectName(u"rbFBX")
        self.rbFBX.setMaximumSize(QSize(60, 16777215))
        self.rbFBX.setChecked(True)

        self.horizontalLayout_9.addWidget(self.rbFBX)

        self.rbObj = QRadioButton(self.centralwidget)
        self.rbObj.setObjectName(u"rbObj")
        self.rbObj.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_9.addWidget(self.rbObj)

        self.rbSelf = QRadioButton(self.centralwidget)
        self.rbSelf.setObjectName(u"rbSelf")
        self.rbSelf.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_9.addWidget(self.rbSelf)

        self.cbKeepID = QCheckBox(self.centralwidget)
        self.cbKeepID.setObjectName(u"cbKeepID")
        self.cbKeepID.setEnabled(True)
        self.cbKeepID.setMaximumSize(QSize(60, 16777215))
        self.cbKeepID.setStyleSheet(u"background-color: rgb(103, 77, 60);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cbKeepID)


        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.btnAddID = QPushButton(self.centralwidget)
        self.btnAddID.setObjectName(u"btnAddID")
        self.btnAddID.setMinimumSize(QSize(70, 0))
        self.btnAddID.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.btnAddID, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnExportToUnity = QPushButton(self.centralwidget)
        self.btnExportToUnity.setObjectName(u"btnExportToUnity")

        self.gridLayout_2.addWidget(self.btnExportToUnity, 0, 0, 1, 1)

        self.btnExportToUnreal = QPushButton(self.centralwidget)
        self.btnExportToUnreal.setObjectName(u"btnExportToUnreal")

        self.gridLayout_2.addWidget(self.btnExportToUnreal, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        MainWindowExporter.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowExporter)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 384, 29))
        MainWindowExporter.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowExporter)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowExporter.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowExporter)

        self.btnExport.setDefault(True)
        self.btnImport.setDefault(True)
        self.btnExportSeparatePart.setDefault(True)
        self.btnExportCurrentFolder.setDefault(True)
        self.btnExportHigh.setDefault(True)
        self.btnExportLow.setDefault(True)
        self.btnExportWorking.setDefault(True)
        self.btnImportWorking.setDefault(True)
        self.btnOpenFolder.setDefault(True)
        self.btnDeleteFolder.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindowExporter)
    # setupUi

    def retranslateUi(self, MainWindowExporter):
        MainWindowExporter.setWindowTitle(QCoreApplication.translate("MainWindowExporter", u"Exporter", None))
        self.btnFixMaterial.setText(QCoreApplication.translate("MainWindowExporter", u"FIX MAT", None))
        self.cbBinary.setText(QCoreApplication.translate("MainWindowExporter", u"Bin", None))
#if QT_CONFIG(tooltip)
        self.cbKeepInstance.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">N\u1ebfu tick ch\u1ecdn s\u1ebd gi\u1eef Instance khi export file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbKeepInstance.setText(QCoreApplication.translate("MainWindowExporter", u"Ins", None))
#if QT_CONFIG(tooltip)
        self.cbKeepVertexNormal.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">N\u1ebfu tick ch\u1ecdn s\u1ebd Lock Normal khi Import(Ch\u1ec9 c\u00f3 t\u00e1c d\u1ee5ng khi Import)<br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbKeepVertexNormal.setText(QCoreApplication.translate("MainWindowExporter", u"Nor", None))
#if QT_CONFIG(tooltip)
        self.cbKeepGroup.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">N\u1ebfu tick ch\u1ecdn S\u1ebd t\u1ea1o group khi import file v\u00e0o scene v\u1edbi t\u00ean &quot;ZZZ_imported_group&quot;</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbKeepGroup.setText(QCoreApplication.translate("MainWindowExporter", u"Grp", None))
#if QT_CONFIG(tooltip)
        self.btnExport.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">Export Standard</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnExport.setText(QCoreApplication.translate("MainWindowExporter", u"Export ", None))
#if QT_CONFIG(tooltip)
        self.btnImport.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">Import Standard</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnImport.setText(QCoreApplication.translate("MainWindowExporter", u" Import", None))
        self.btnExportSP.setText(QCoreApplication.translate("MainWindowExporter", u"Export to Substance Painter", None))
        self.btnExportSeparatePart.setText(QCoreApplication.translate("MainWindowExporter", u"Separate", None))
        self.btnExportCurrentFolder.setText(QCoreApplication.translate("MainWindowExporter", u"Current Folder", None))
        self.btnExportHigh.setText(QCoreApplication.translate("MainWindowExporter", u"HIGH", None))
        self.btnExportLow.setText(QCoreApplication.translate("MainWindowExporter", u"LOW", None))
#if QT_CONFIG(tooltip)
        self.btnExportWorking.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">Export Working File</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnExportWorking.setText(QCoreApplication.translate("MainWindowExporter", u"Export W>", None))
#if QT_CONFIG(tooltip)
        self.btnImportWorking.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">Import Working File</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnImportWorking.setText(QCoreApplication.translate("MainWindowExporter", u"Import W<", None))
        self.btnOpenFolder.setText(QCoreApplication.translate("MainWindowExporter", u"OPEN", None))
        self.btnDeleteFolder.setText(QCoreApplication.translate("MainWindowExporter", u"CLEAN  ", None))
#if QT_CONFIG(tooltip)
        self.rbFBX.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">Export ra file \u0111\u1ecbnh d\u1ea1ng .FBX</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rbFBX.setText(QCoreApplication.translate("MainWindowExporter", u"FBX", None))
#if QT_CONFIG(tooltip)
        self.rbObj.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">Export ra file \u0111\u1ecbnh d\u1ea1ng .OBJ</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rbObj.setText(QCoreApplication.translate("MainWindowExporter", u"OBJ", None))
#if QT_CONFIG(tooltip)
        self.rbSelf.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">Export ra file \u0111\u1ecbnh d\u1ea1ng theo Software \u0111ang s\u1eed d\u1ee5ng</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rbSelf.setText(QCoreApplication.translate("MainWindowExporter", u"Self", None))
#if QT_CONFIG(tooltip)
        self.cbKeepID.setToolTip(QCoreApplication.translate("MainWindowExporter", u"<html><head/><body><p><span style=\" font-size:10pt;\">N\u1ebfu tick ch\u1ecdn s\u1ebd th\u00eam suffix ID* v\u00e0o t\u00ean Material khi Export(Ch\u1ec9 d\u00f9ng cho Multisub Material trong 3dsmax)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbKeepID.setText(QCoreApplication.translate("MainWindowExporter", u"ID", None))
        self.btnAddID.setText(QCoreApplication.translate("MainWindowExporter", u"Add ID", None))
        self.btnExportToUnity.setText(QCoreApplication.translate("MainWindowExporter", u"Export To Unity", None))
        self.btnExportToUnreal.setText(QCoreApplication.translate("MainWindowExporter", u"Export To Unreal", None))
    # retranslateUi

