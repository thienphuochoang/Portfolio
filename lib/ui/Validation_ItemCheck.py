# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/WIP_Portfolio/lib/ui/Validation_ItemCheck.ui',
# licensing of 'D:/WIP_Portfolio/lib/ui/Validation_ItemCheck.ui' applies.
#
# Created: Tue Oct 20 01:43:40 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(398, 22)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 6, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 6, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 6, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStatus = QtWidgets.QPushButton(self.frame)
        self.btnStatus.setMaximumSize(QtCore.QSize(20, 20))
        self.btnStatus.setStyleSheet("")
        self.btnStatus.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Zimbabwe))
        self.btnStatus.setText("")
        self.btnStatus.setIconSize(QtCore.QSize(20, 20))
        self.btnStatus.setCheckable(True)
        self.btnStatus.setChecked(True)
        self.btnStatus.setDefault(True)
        self.btnStatus.setFlat(True)
        self.btnStatus.setObjectName("btnStatus")
        self.horizontalLayout.addWidget(self.btnStatus)
        self.btnResult = QtWidgets.QPushButton(self.frame)
        self.btnResult.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnResult.sizePolicy().hasHeightForWidth())
        self.btnResult.setSizePolicy(sizePolicy)
        self.btnResult.setMinimumSize(QtCore.QSize(4, 22))
        self.btnResult.setMaximumSize(QtCore.QSize(4, 16777215))
        self.btnResult.setStyleSheet("QPushButton { \n"
"    background-color: grey;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:checked { \n"
"    background-color: rgb(255, 0, 0); \n"
" }\n"
"\n"
"QPushButton:unchecked { \n"
"    background-color: rgb(0, 255, 0);\n"
" }")
        self.btnResult.setText("")
        self.btnResult.setCheckable(True)
        self.btnResult.setObjectName("btnResult")
        self.horizontalLayout.addWidget(self.btnResult)
        self.label = QtWidgets.QPushButton(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"color: rgb(255, 255, 255);\n"
"Text-align:left;\n"
"")
        self.label.setDefault(False)
        self.label.setFlat(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btnMaximize = QtWidgets.QPushButton(self.frame)
        self.btnMaximize.setMaximumSize(QtCore.QSize(20, 20))
        self.btnMaximize.setText("")
        self.btnMaximize.setCheckable(True)
        self.btnMaximize.setObjectName("btnMaximize")
        self.horizontalLayout.addWidget(self.btnMaximize)
        self.btnCollapse = QtWidgets.QPushButton(self.frame)
        self.btnCollapse.setMaximumSize(QtCore.QSize(20, 20))
        self.btnCollapse.setStyleSheet("QPushButton:checked{background-color: rgb(85, 170, 255);}")
        self.btnCollapse.setText("")
        self.btnCollapse.setIconSize(QtCore.QSize(20, 20))
        self.btnCollapse.setCheckable(True)
        self.btnCollapse.setDefault(True)
        self.btnCollapse.setFlat(False)
        self.btnCollapse.setObjectName("btnCollapse")
        self.horizontalLayout.addWidget(self.btnCollapse)
        self.btnFix = QtWidgets.QPushButton(self.frame)
        self.btnFix.setMaximumSize(QtCore.QSize(20, 20))
        self.btnFix.setText("")
        self.btnFix.setIconSize(QtCore.QSize(20, 20))
        self.btnFix.setObjectName("btnFix")
        self.horizontalLayout.addWidget(self.btnFix)
        self.btnDoc = QtWidgets.QPushButton(self.frame)
        self.btnDoc.setMaximumSize(QtCore.QSize(20, 20))
        self.btnDoc.setText("")
        self.btnDoc.setIconSize(QtCore.QSize(18, 18))
        self.btnDoc.setObjectName("btnDoc")
        self.horizontalLayout.addWidget(self.btnDoc)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.btnCollapse.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Collapse và uncollapse kết quả check</span></p></body></html>", None, -1))
        self.btnFix.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Tự động fix lỗi:<br/>.Nếu không chọn thì sẽ fixes tất cả phần tử trong danh sách lỗi<br/>.Nếu chọn thì chỉ fixes những phần tử được chọn trong danh sách lỗi</span></p></body></html>", None, -1))
        self.btnDoc.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Mở document hướng dẫn</span></p></body></html>", None, -1))

