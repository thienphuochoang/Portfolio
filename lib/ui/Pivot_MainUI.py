# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/WIP_Portfolio/lib/ui/Pivot_MainUI.ui',
# licensing of 'D:/WIP_Portfolio/lib/ui/Pivot_MainUI.ui' applies.
#
# Created: Thu Jun 17 00:36:02 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PivotMainWindow(object):
    def setupUi(self, PivotMainWindow):
        PivotMainWindow.setObjectName("PivotMainWindow")
        PivotMainWindow.resize(341, 143)
        PivotMainWindow.setMinimumSize(QtCore.QSize(341, 143))
        PivotMainWindow.setMaximumSize(QtCore.QSize(341, 143))
        self.centralwidget = QtWidgets.QWidget(PivotMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSetupPivotUp0 = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetupPivotUp0.setObjectName("btnSetupPivotUp0")
        self.gridLayout.addWidget(self.btnSetupPivotUp0, 0, 2, 1, 1)
        self.gbX = QtWidgets.QGroupBox(self.centralwidget)
        self.gbX.setAlignment(QtCore.Qt.AlignCenter)
        self.gbX.setFlat(False)
        self.gbX.setObjectName("gbX")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gbX)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbMinX = QtWidgets.QRadioButton(self.gbX)
        self.rbMinX.setObjectName("rbMinX")
        self.verticalLayout.addWidget(self.rbMinX)
        self.rbCenterX = QtWidgets.QRadioButton(self.gbX)
        self.rbCenterX.setChecked(True)
        self.rbCenterX.setObjectName("rbCenterX")
        self.verticalLayout.addWidget(self.rbCenterX)
        self.rbMaxX = QtWidgets.QRadioButton(self.gbX)
        self.rbMaxX.setObjectName("rbMaxX")
        self.verticalLayout.addWidget(self.rbMaxX)
        self.gridLayout.addWidget(self.gbX, 1, 1, 1, 1)
        self.btnSetupPivot000 = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetupPivot000.setObjectName("btnSetupPivot000")
        self.gridLayout.addWidget(self.btnSetupPivot000, 0, 1, 1, 1)
        self.gbZ = QtWidgets.QGroupBox(self.centralwidget)
        self.gbZ.setAlignment(QtCore.Qt.AlignCenter)
        self.gbZ.setObjectName("gbZ")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbZ)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rbMinZ = QtWidgets.QRadioButton(self.gbZ)
        self.rbMinZ.setChecked(False)
        self.rbMinZ.setObjectName("rbMinZ")
        self.verticalLayout_3.addWidget(self.rbMinZ)
        self.rbCenterZ = QtWidgets.QRadioButton(self.gbZ)
        self.rbCenterZ.setChecked(True)
        self.rbCenterZ.setObjectName("rbCenterZ")
        self.verticalLayout_3.addWidget(self.rbCenterZ)
        self.rbMaxZ = QtWidgets.QRadioButton(self.gbZ)
        self.rbMaxZ.setObjectName("rbMaxZ")
        self.verticalLayout_3.addWidget(self.rbMaxZ)
        self.gridLayout.addWidget(self.gbZ, 1, 3, 1, 1)
        self.gbY = QtWidgets.QGroupBox(self.centralwidget)
        self.gbY.setAlignment(QtCore.Qt.AlignCenter)
        self.gbY.setObjectName("gbY")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbY)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbMinY = QtWidgets.QRadioButton(self.gbY)
        self.rbMinY.setChecked(True)
        self.rbMinY.setObjectName("rbMinY")
        self.verticalLayout_2.addWidget(self.rbMinY)
        self.rbCenterY = QtWidgets.QRadioButton(self.gbY)
        self.rbCenterY.setChecked(False)
        self.rbCenterY.setObjectName("rbCenterY")
        self.verticalLayout_2.addWidget(self.rbCenterY)
        self.rbMaxY = QtWidgets.QRadioButton(self.gbY)
        self.rbMaxY.setObjectName("rbMaxY")
        self.verticalLayout_2.addWidget(self.rbMaxY)
        self.gridLayout.addWidget(self.gbY, 1, 2, 1, 1)
        self.btnSetupPivot = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetupPivot.setMaximumSize(QtCore.QSize(55, 90))
        self.btnSetupPivot.setObjectName("btnSetupPivot")
        self.gridLayout.addWidget(self.btnSetupPivot, 1, 0, 1, 1)
        self.btnSetupPos000 = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetupPos000.setObjectName("btnSetupPos000")
        self.gridLayout.addWidget(self.btnSetupPos000, 0, 3, 1, 1)
        PivotMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PivotMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PivotMainWindow)

    def retranslateUi(self, PivotMainWindow):
        PivotMainWindow.setWindowTitle(QtWidgets.QApplication.translate("PivotMainWindow", "Pivot Main Window", None, -1))
        self.btnSetupPivotUp0.setText(QtWidgets.QApplication.translate("PivotMainWindow", "Up Pivot = 0", None, -1))
        self.gbX.setTitle(QtWidgets.QApplication.translate("PivotMainWindow", "X", None, -1))
        self.rbMinX.setText(QtWidgets.QApplication.translate("PivotMainWindow", "min", None, -1))
        self.rbCenterX.setText(QtWidgets.QApplication.translate("PivotMainWindow", "center", None, -1))
        self.rbMaxX.setText(QtWidgets.QApplication.translate("PivotMainWindow", "max", None, -1))
        self.btnSetupPivot000.setText(QtWidgets.QApplication.translate("PivotMainWindow", "Pivot = [0,0,0]", None, -1))
        self.gbZ.setTitle(QtWidgets.QApplication.translate("PivotMainWindow", "Z", None, -1))
        self.rbMinZ.setText(QtWidgets.QApplication.translate("PivotMainWindow", "min", None, -1))
        self.rbCenterZ.setText(QtWidgets.QApplication.translate("PivotMainWindow", "center", None, -1))
        self.rbMaxZ.setText(QtWidgets.QApplication.translate("PivotMainWindow", "max", None, -1))
        self.gbY.setTitle(QtWidgets.QApplication.translate("PivotMainWindow", "Y", None, -1))
        self.rbMinY.setText(QtWidgets.QApplication.translate("PivotMainWindow", "min", None, -1))
        self.rbCenterY.setText(QtWidgets.QApplication.translate("PivotMainWindow", "center", None, -1))
        self.rbMaxY.setText(QtWidgets.QApplication.translate("PivotMainWindow", "max", None, -1))
        self.btnSetupPivot.setText(QtWidgets.QApplication.translate("PivotMainWindow", "Pivot =", None, -1))
        self.btnSetupPos000.setText(QtWidgets.QApplication.translate("PivotMainWindow", "Pos = [0,0,0]", None, -1))

