# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/WIP_Portfolio/lib/ui/Validation_Addons.ui',
# licensing of 'D:/WIP_Portfolio/lib/ui/Validation_Addons.ui' applies.
#
# Created: Fri Nov  6 01:59:14 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 219)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnError = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnError.sizePolicy().hasHeightForWidth())
        self.btnError.setSizePolicy(sizePolicy)
        self.btnError.setMinimumSize(QtCore.QSize(0, 10))
        self.btnError.setMaximumSize(QtCore.QSize(12, 12))
        self.btnError.setStyleSheet("QPushButton { \n"
"   background-color: rgb(230, 0, 0);\n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(200, 0, 0); \n"
"}\n"
"\n"
"QPushButton:checked { \n"
"    background-color: rgb(255, 0, 0); \n"
" }\n"
"")
        self.btnError.setText("")
        self.btnError.setIconSize(QtCore.QSize(12, 12))
        self.btnError.setCheckable(True)
        self.btnError.setChecked(True)
        self.btnError.setObjectName("btnError")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btnError)
        self.horizontalLayout.addWidget(self.btnError)
        self.btnInfo = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInfo.sizePolicy().hasHeightForWidth())
        self.btnInfo.setSizePolicy(sizePolicy)
        self.btnInfo.setMinimumSize(QtCore.QSize(0, 10))
        self.btnInfo.setMaximumSize(QtCore.QSize(12, 12))
        self.btnInfo.setStyleSheet("QPushButton { \n"
"   background-color: rgb(0, 230, 0);\n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(0,200, 0); \n"
"}\n"
"\n"
"QPushButton:checked { \n"
"    background-color: rgb(0, 255, 0); \n"
" }\n"
"\n"
"")
        self.btnInfo.setText("")
        self.btnInfo.setCheckable(True)
        self.btnInfo.setFlat(False)
        self.btnInfo.setObjectName("btnInfo")
        self.buttonGroup.addButton(self.btnInfo)
        self.horizontalLayout.addWidget(self.btnInfo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setIconSize(QtCore.QSize(15, 15))
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setGridSize(QtCore.QSize(20, 20))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.btnError.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Hiển thị danh sách những phần tử sai</span></p></body></html>", None, -1))
        self.btnInfo.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Hiển thị danh sách những phần tử đúng</span></p></body></html>", None, -1))
        self.listWidget.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">01.Click chuột trái để chọn phần tử</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">02.Đè Shift để chon thêm phần tử</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">03.Double click chuột để chọn tất cả phần tử trùng tên trong danh sách</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">04.Ctrl+A để chọn hết tát cả phần tử trong danh sách</span></p></body></html>", None, -1))

