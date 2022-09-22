# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Validation_ItemCheck.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(401, 46)
        palette = QPalette()
        brush = QBrush(QColor(255, 6, 10, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnStatus = QPushButton(self.frame)
        self.btnStatus.setObjectName(u"btnStatus")
        self.btnStatus.setMaximumSize(QSize(20, 20))
        self.btnStatus.setStyleSheet(u"")
        self.btnStatus.setLocale(QLocale(QLocale.English, QLocale.Zimbabwe))
        self.btnStatus.setIconSize(QSize(20, 20))
        self.btnStatus.setCheckable(True)
        self.btnStatus.setChecked(True)
        self.btnStatus.setFlat(True)

        self.horizontalLayout.addWidget(self.btnStatus)

        self.btnResult = QPushButton(self.frame)
        self.btnResult.setObjectName(u"btnResult")
        self.btnResult.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnResult.sizePolicy().hasHeightForWidth())
        self.btnResult.setSizePolicy(sizePolicy)
        self.btnResult.setMinimumSize(QSize(4, 22))
        self.btnResult.setMaximumSize(QSize(4, 16777215))
        self.btnResult.setStyleSheet(u"QPushButton { \n"
"	background-color: grey;\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:checked { \n"
"    background-color: rgb(255, 0, 0); \n"
" }\n"
"\n"
"QPushButton:unchecked { \n"
"	background-color: rgb(0, 255, 0);\n"
" }")
        self.btnResult.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnResult)

        self.label = QPushButton(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);\n"
"Text-align:left;\n"
"")
        self.label.setFlat(True)

        self.horizontalLayout.addWidget(self.label)

        self.btnMaximize = QPushButton(self.frame)
        self.btnMaximize.setObjectName(u"btnMaximize")
        self.btnMaximize.setMaximumSize(QSize(20, 20))
        self.btnMaximize.setCheckable(True)

        self.horizontalLayout.addWidget(self.btnMaximize)

        self.btnCollapse = QPushButton(self.frame)
        self.btnCollapse.setObjectName(u"btnCollapse")
        self.btnCollapse.setMaximumSize(QSize(20, 20))
        self.btnCollapse.setStyleSheet(u"QPushButton:checked{background-color: rgb(85, 170, 255);}")
        self.btnCollapse.setIconSize(QSize(20, 20))
        self.btnCollapse.setCheckable(True)
        self.btnCollapse.setFlat(False)

        self.horizontalLayout.addWidget(self.btnCollapse)

        self.btnFix = QPushButton(self.frame)
        self.btnFix.setObjectName(u"btnFix")
        self.btnFix.setMaximumSize(QSize(20, 20))
        self.btnFix.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btnFix)

        self.btnDoc = QPushButton(self.frame)
        self.btnDoc.setObjectName(u"btnDoc")
        self.btnDoc.setMaximumSize(QSize(20, 20))
        self.btnDoc.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btnDoc)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btnStatus.setDefault(True)
        self.label.setDefault(False)
        self.btnCollapse.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnStatus.setText("")
        self.btnResult.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btnMaximize.setText("")
#if QT_CONFIG(tooltip)
        self.btnCollapse.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Collapse v\u00e0 uncollapse k\u1ebft qu\u1ea3 check</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnCollapse.setText("")
#if QT_CONFIG(tooltip)
        self.btnFix.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">T\u1ef1 \u0111\u1ed9ng fix l\u1ed7i:<br/>.N\u1ebfu kh\u00f4ng ch\u1ecdn th\u00ec s\u1ebd fixes t\u1ea5t c\u1ea3 ph\u1ea7n t\u1eed trong danh s\u00e1ch l\u1ed7i<br/>.N\u1ebfu ch\u1ecdn th\u00ec ch\u1ec9 fixes nh\u1eefng ph\u1ea7n t\u1eed \u0111\u01b0\u1ee3c ch\u1ecdn trong danh s\u00e1ch l\u1ed7i</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnFix.setText("")
#if QT_CONFIG(tooltip)
        self.btnDoc.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">M\u1edf document h\u01b0\u1edbng d\u1eabn</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnDoc.setText("")
    # retranslateUi

