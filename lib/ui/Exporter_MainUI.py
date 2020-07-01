# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Exporter_PySide2.ui',
# licensing of 'D:\Exporter_PySide2.ui' applies.
#
# Created: Wed Sep 25 17:05:26 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindowExporter(object):
    def setupUi(self, MainWindowExporter):
        MainWindowExporter.setObjectName("MainWindowExporter")
        self.centralwidget = QtWidgets.QWidget(MainWindowExporter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnFixMaterial = QtWidgets.QPushButton(self.centralwidget)
        self.btnFixMaterial.setMinimumSize(QtCore.QSize(0, 21))
        self.btnFixMaterial.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnFixMaterial.setStyleSheet("QPushButton { \n"
"    background-color: rgb(159, 169, 163);\n"
"    border: 1px;\n"
"}\n"
"")
        self.btnFixMaterial.setObjectName("btnFixMaterial")
        self.horizontalLayout_5.addWidget(self.btnFixMaterial)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbBinary = QtWidgets.QCheckBox(self.centralwidget)
        self.cbBinary.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbBinary.setStyleSheet("background-color: rgb(103, 77, 60);\n"
"color: rgb(255, 255, 255);")
        self.cbBinary.setObjectName("cbBinary")
        self.horizontalLayout.addWidget(self.cbBinary)
        self.cbKeepInstance = QtWidgets.QCheckBox(self.centralwidget)
        self.cbKeepInstance.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbKeepInstance.setStyleSheet("background-color: rgb(103, 77, 60);\n"
"color: rgb(255, 255, 255);")
        self.cbKeepInstance.setObjectName("cbKeepInstance")
        self.horizontalLayout.addWidget(self.cbKeepInstance)
        self.cbKeepVertexNormal = QtWidgets.QCheckBox(self.centralwidget)
        self.cbKeepVertexNormal.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbKeepVertexNormal.setStyleSheet("background-color: rgb(159, 169, 163);\n"
"color: rgb(0, 0, 0);")
        self.cbKeepVertexNormal.setObjectName("cbKeepVertexNormal")
        self.horizontalLayout.addWidget(self.cbKeepVertexNormal)
        self.cbKeepGroup = QtWidgets.QCheckBox(self.centralwidget)
        self.cbKeepGroup.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbKeepGroup.setStyleSheet("background-color: rgb(159, 169, 163);\n"
"color: rgb(0, 0, 0);")
        self.cbKeepGroup.setTristate(False)
        self.cbKeepGroup.setObjectName("cbKeepGroup")
        self.horizontalLayout.addWidget(self.cbKeepGroup)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btnExport = QtWidgets.QPushButton(self.centralwidget)
        self.btnExport.setMinimumSize(QtCore.QSize(0, 54))
        self.btnExport.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnExport.setStyleSheet("QPushButton { \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(103, 77, 60);\n"
"    border: 1px;\n"
"}\n"
"")
        self.btnExport.setCheckable(False)
        self.btnExport.setDefault(True)
        self.btnExport.setObjectName("btnExport")
        self.horizontalLayout_8.addWidget(self.btnExport)
        self.btnImport = QtWidgets.QPushButton(self.centralwidget)
        self.btnImport.setMinimumSize(QtCore.QSize(0, 54))
        self.btnImport.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnImport.setStyleSheet("QPushButton { \n"
"    background-color: rgb(159, 169, 163);\n"
"    border: 1px;\n"
"}\n"
"")
        self.btnImport.setAutoDefault(False)
        self.btnImport.setDefault(True)
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_8.addWidget(self.btnImport)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 1, 2, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnExportSP = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportSP.setMinimumSize(QtCore.QSize(0, 23))
        self.btnExportSP.setMaximumSize(QtCore.QSize(16777215, 23))
        self.btnExportSP.setObjectName("btnExportSP")
        self.horizontalLayout_4.addWidget(self.btnExportSP)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnExportSeparatePart = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportSeparatePart.setMinimumSize(QtCore.QSize(0, 23))
        self.btnExportSeparatePart.setMaximumSize(QtCore.QSize(16777215, 23))
        self.btnExportSeparatePart.setDefault(True)
        self.btnExportSeparatePart.setObjectName("btnExportSeparatePart")
        self.horizontalLayout_3.addWidget(self.btnExportSeparatePart)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnExportHigh = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportHigh.setMinimumSize(QtCore.QSize(70, 0))
        self.btnExportHigh.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnExportHigh.setDefault(True)
        self.btnExportHigh.setFlat(True)
        self.btnExportHigh.setObjectName("btnExportHigh")
        self.horizontalLayout_6.addWidget(self.btnExportHigh)
        self.btnExportLow = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportLow.setMinimumSize(QtCore.QSize(70, 0))
        self.btnExportLow.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnExportLow.setDefault(True)
        self.btnExportLow.setFlat(True)
        self.btnExportLow.setObjectName("btnExportLow")
        self.horizontalLayout_6.addWidget(self.btnExportLow)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 1, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnExportWorking = QtWidgets.QPushButton(self.centralwidget)
        self.btnExportWorking.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.btnExportWorking.setFont(font)
        self.btnExportWorking.setAutoFillBackground(False)
        self.btnExportWorking.setStyleSheet("QPushButton { \n"
"    background-color: rgb(103, 77, 60);\n"
"    border: 1px;\n"
"}\n"
"")
        self.btnExportWorking.setDefault(True)
        self.btnExportWorking.setObjectName("btnExportWorking")
        self.horizontalLayout_2.addWidget(self.btnExportWorking)
        self.btnImportWorking = QtWidgets.QPushButton(self.centralwidget)
        self.btnImportWorking.setMinimumSize(QtCore.QSize(0, 21))
        self.btnImportWorking.setStyleSheet("QPushButton { \n"
"    background-color: rgb(159, 169, 163);\n"
"    border: 1px;\n"
"}\n"
"")
        self.btnImportWorking.setDefault(True)
        self.btnImportWorking.setObjectName("btnImportWorking")
        self.horizontalLayout_2.addWidget(self.btnImportWorking)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnOpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFolder.setMinimumSize(QtCore.QSize(70, 0))
        self.btnOpenFolder.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnOpenFolder.setDefault(True)
        self.btnOpenFolder.setFlat(True)
        self.btnOpenFolder.setObjectName("btnOpenFolder")
        self.horizontalLayout_7.addWidget(self.btnOpenFolder)
        self.btnDeleteFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteFolder.setMinimumSize(QtCore.QSize(70, 0))
        self.btnDeleteFolder.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnDeleteFolder.setDefault(True)
        self.btnDeleteFolder.setFlat(True)
        self.btnDeleteFolder.setObjectName("btnDeleteFolder")
        self.horizontalLayout_7.addWidget(self.btnDeleteFolder)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 1, 1, 2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.rbFBX = QtWidgets.QRadioButton(self.centralwidget)
        self.rbFBX.setMaximumSize(QtCore.QSize(40, 16777215))
        self.rbFBX.setChecked(True)
        self.rbFBX.setObjectName("rbFBX")
        self.horizontalLayout_9.addWidget(self.rbFBX)
        self.rbObj = QtWidgets.QRadioButton(self.centralwidget)
        self.rbObj.setMaximumSize(QtCore.QSize(40, 16777215))
        self.rbObj.setObjectName("rbObj")
        self.horizontalLayout_9.addWidget(self.rbObj)
        self.rbSelf = QtWidgets.QRadioButton(self.centralwidget)
        self.rbSelf.setMaximumSize(QtCore.QSize(40, 16777215))
        self.rbSelf.setObjectName("rbSelf")
        self.horizontalLayout_9.addWidget(self.rbSelf)
        self.cbKeepID = QtWidgets.QCheckBox(self.centralwidget)
        self.cbKeepID.setEnabled(True)
        self.cbKeepID.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbKeepID.setStyleSheet("background-color: rgb(103, 77, 60);\n"
"color: rgb(255, 255, 255);")
        self.cbKeepID.setObjectName("cbKeepID")
        self.horizontalLayout_9.addWidget(self.cbKeepID)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.btnAddID = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddID.setMinimumSize(QtCore.QSize(70, 0))
        self.btnAddID.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnAddID.setObjectName("btnAddID")
        self.gridLayout.addWidget(self.btnAddID, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindowExporter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowExporter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 21))
        self.menubar.setObjectName("menubar")
        MainWindowExporter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowExporter)
        self.statusbar.setObjectName("statusbar")
        MainWindowExporter.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowExporter)
        QtCore.QMetaObject.connectSlotsByName(MainWindowExporter)

    def retranslateUi(self, MainWindowExporter):
        MainWindowExporter.setWindowTitle(QtWidgets.QApplication.translate("MainWindowExporter", "Exporter", None, -1))
        self.btnFixMaterial.setText(QtWidgets.QApplication.translate("MainWindowExporter", "FIX MAT", None, -1))
        self.cbBinary.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Bin", None, -1))
        self.cbKeepInstance.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Nếu tick chọn sẽ giữ Instance khi export file</span></p></body></html>", None, -1))
        self.cbKeepInstance.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Ins", None, -1))
        self.cbKeepVertexNormal.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Nếu tick chọn sẽ Lock Normal khi Import(Chỉ có tác dụng khi Import)<br/></span></p></body></html>", None, -1))
        self.cbKeepVertexNormal.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Nor", None, -1))
        self.cbKeepGroup.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Nếu tick chọn Sẽ tạo group khi import file vào scene với tên &quot;ZZZ_imported_group&quot;</span></p></body></html>", None, -1))
        self.cbKeepGroup.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Grp", None, -1))
        self.btnExport.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Export Standard</span></p></body></html>", None, -1))
        self.btnExport.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Export ", None, -1))
        self.btnImport.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Import Standard</span></p></body></html>", None, -1))
        self.btnImport.setText(QtWidgets.QApplication.translate("MainWindowExporter", " Import", None, -1))
        self.btnExportSP.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Export to Substance Painter", None, -1))
        self.btnExportSeparatePart.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Separate", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Current Folder", None, -1))
        self.btnExportHigh.setText(QtWidgets.QApplication.translate("MainWindowExporter", "HIGH", None, -1))
        self.btnExportLow.setText(QtWidgets.QApplication.translate("MainWindowExporter", "LOW", None, -1))
        self.btnExportWorking.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Export Working File</span></p></body></html>", None, -1))
        self.btnExportWorking.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Export W>", None, -1))
        self.btnImportWorking.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Import Working File</span></p></body></html>", None, -1))
        self.btnImportWorking.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Import W<", None, -1))
        self.btnOpenFolder.setText(QtWidgets.QApplication.translate("MainWindowExporter", "OPEN", None, -1))
        self.btnDeleteFolder.setText(QtWidgets.QApplication.translate("MainWindowExporter", "CLEAN  ", None, -1))
        self.rbFBX.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Export ra file định dạng .FBX</span></p></body></html>", None, -1))
        self.rbFBX.setText(QtWidgets.QApplication.translate("MainWindowExporter", "FBX", None, -1))
        self.rbObj.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Export ra file định dạng .OBJ</span></p></body></html>", None, -1))
        self.rbObj.setText(QtWidgets.QApplication.translate("MainWindowExporter", "OBJ", None, -1))
        self.rbSelf.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Export ra file định dạng theo Software đang sử dụng</span></p></body></html>", None, -1))
        self.rbSelf.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Self", None, -1))
        self.cbKeepID.setToolTip(QtWidgets.QApplication.translate("MainWindowExporter", "<html><head/><body><p><span style=\" font-size:10pt;\">Nếu tick chọn sẽ thêm suffix ID* vào tên Material khi Export(Chỉ dùng cho Multisub Material trong 3dsmax)</span></p></body></html>", None, -1))
        self.cbKeepID.setText(QtWidgets.QApplication.translate("MainWindowExporter", "ID", None, -1))
        self.btnAddID.setText(QtWidgets.QApplication.translate("MainWindowExporter", "Add ID", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowExporter = QtWidgets.QMainWindow()
    ui = Ui_MainWindowExporter()
    ui.setupUi(MainWindowExporter)
    MainWindowExporter.show()
    sys.exit(app.exec_())

