# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Validation_Addons.ui'
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
        MainWindow.resize(420, 219)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnError = QPushButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.btnError)
        self.btnError.setObjectName(u"btnError")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnError.sizePolicy().hasHeightForWidth())
        self.btnError.setSizePolicy(sizePolicy)
        self.btnError.setMinimumSize(QSize(0, 10))
        self.btnError.setMaximumSize(QSize(12, 12))
        self.btnError.setStyleSheet(u"QPushButton { \n"
"   background-color: rgb(230, 0, 0);\n"
"	border: 0px;\n"
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
        self.btnError.setIconSize(QSize(12, 12))
        self.btnError.setCheckable(True)
        self.btnError.setChecked(True)

        self.horizontalLayout.addWidget(self.btnError)

        self.btnInfo = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.btnInfo)
        self.btnInfo.setObjectName(u"btnInfo")
        sizePolicy.setHeightForWidth(self.btnInfo.sizePolicy().hasHeightForWidth())
        self.btnInfo.setSizePolicy(sizePolicy)
        self.btnInfo.setMinimumSize(QSize(0, 10))
        self.btnInfo.setMaximumSize(QSize(12, 12))
        self.btnInfo.setStyleSheet(u"QPushButton { \n"
"   background-color: rgb(0, 230, 0);\n"
"	border: 0px;\n"
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
        self.btnInfo.setCheckable(True)
        self.btnInfo.setFlat(False)

        self.horizontalLayout.addWidget(self.btnInfo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 200))
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setIconSize(QSize(15, 15))
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setGridSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.listWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.btnError.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Hi\u1ec3n th\u1ecb danh s\u00e1ch nh\u1eefng ph\u1ea7n t\u1eed sai</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnError.setText("")
#if QT_CONFIG(tooltip)
        self.btnInfo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Hi\u1ec3n th\u1ecb danh s\u00e1ch nh\u1eefng ph\u1ea7n t\u1eed \u0111\u00fang</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnInfo.setText("")
#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">01.Click chu\u1ed9t tr\u00e1i \u0111\u1ec3 ch\u1ecdn ph\u1ea7n t\u1eed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">02.\u0110\u00e8 Shift \u0111\u1ec3 chon th\u00eam ph\u1ea7n t\u1eed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">03.Double click chu\u1ed9t \u0111\u1ec3 ch\u1ecdn t\u1ea5t "
                        "c\u1ea3 ph\u1ea7n t\u1eed tr\u00f9ng t\u00ean trong danh s\u00e1ch</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">04.Ctrl+A \u0111\u1ec3 ch\u1ecdn h\u1ebft t\u00e1t c\u1ea3 ph\u1ea7n t\u1eed trong danh s\u00e1ch</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

