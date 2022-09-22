# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pivot_MainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PivotMainWindow(object):
    def setupUi(self, PivotMainWindow):
        if not PivotMainWindow.objectName():
            PivotMainWindow.setObjectName(u"PivotMainWindow")
        PivotMainWindow.resize(341, 143)
        PivotMainWindow.setMinimumSize(QSize(341, 143))
        PivotMainWindow.setMaximumSize(QSize(341, 143))
        self.centralwidget = QWidget(PivotMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSetupPivotUp0 = QPushButton(self.centralwidget)
        self.btnSetupPivotUp0.setObjectName(u"btnSetupPivotUp0")

        self.gridLayout.addWidget(self.btnSetupPivotUp0, 0, 2, 1, 1)

        self.gbX = QGroupBox(self.centralwidget)
        self.gbX.setObjectName(u"gbX")
        self.gbX.setAlignment(Qt.AlignCenter)
        self.gbX.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.gbX)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rbMinX = QRadioButton(self.gbX)
        self.rbMinX.setObjectName(u"rbMinX")

        self.verticalLayout.addWidget(self.rbMinX)

        self.rbCenterX = QRadioButton(self.gbX)
        self.rbCenterX.setObjectName(u"rbCenterX")
        self.rbCenterX.setChecked(True)

        self.verticalLayout.addWidget(self.rbCenterX)

        self.rbMaxX = QRadioButton(self.gbX)
        self.rbMaxX.setObjectName(u"rbMaxX")

        self.verticalLayout.addWidget(self.rbMaxX)


        self.gridLayout.addWidget(self.gbX, 1, 1, 1, 1)

        self.btnSetupPivot000 = QPushButton(self.centralwidget)
        self.btnSetupPivot000.setObjectName(u"btnSetupPivot000")

        self.gridLayout.addWidget(self.btnSetupPivot000, 0, 1, 1, 1)

        self.gbZ = QGroupBox(self.centralwidget)
        self.gbZ.setObjectName(u"gbZ")
        self.gbZ.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.gbZ)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rbMinZ = QRadioButton(self.gbZ)
        self.rbMinZ.setObjectName(u"rbMinZ")
        self.rbMinZ.setChecked(False)

        self.verticalLayout_3.addWidget(self.rbMinZ)

        self.rbCenterZ = QRadioButton(self.gbZ)
        self.rbCenterZ.setObjectName(u"rbCenterZ")
        self.rbCenterZ.setChecked(True)

        self.verticalLayout_3.addWidget(self.rbCenterZ)

        self.rbMaxZ = QRadioButton(self.gbZ)
        self.rbMaxZ.setObjectName(u"rbMaxZ")

        self.verticalLayout_3.addWidget(self.rbMaxZ)


        self.gridLayout.addWidget(self.gbZ, 1, 3, 1, 1)

        self.gbY = QGroupBox(self.centralwidget)
        self.gbY.setObjectName(u"gbY")
        self.gbY.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.gbY)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rbMinY = QRadioButton(self.gbY)
        self.rbMinY.setObjectName(u"rbMinY")
        self.rbMinY.setChecked(True)

        self.verticalLayout_2.addWidget(self.rbMinY)

        self.rbCenterY = QRadioButton(self.gbY)
        self.rbCenterY.setObjectName(u"rbCenterY")
        self.rbCenterY.setChecked(False)

        self.verticalLayout_2.addWidget(self.rbCenterY)

        self.rbMaxY = QRadioButton(self.gbY)
        self.rbMaxY.setObjectName(u"rbMaxY")

        self.verticalLayout_2.addWidget(self.rbMaxY)


        self.gridLayout.addWidget(self.gbY, 1, 2, 1, 1)

        self.btnSetupPivot = QPushButton(self.centralwidget)
        self.btnSetupPivot.setObjectName(u"btnSetupPivot")
        self.btnSetupPivot.setMaximumSize(QSize(55, 90))

        self.gridLayout.addWidget(self.btnSetupPivot, 1, 0, 1, 1)

        self.btnSetupPos000 = QPushButton(self.centralwidget)
        self.btnSetupPos000.setObjectName(u"btnSetupPos000")

        self.gridLayout.addWidget(self.btnSetupPos000, 0, 3, 1, 1)

        PivotMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PivotMainWindow)

        QMetaObject.connectSlotsByName(PivotMainWindow)
    # setupUi

    def retranslateUi(self, PivotMainWindow):
        PivotMainWindow.setWindowTitle(QCoreApplication.translate("PivotMainWindow", u"Pivot Main Window", None))
        self.btnSetupPivotUp0.setText(QCoreApplication.translate("PivotMainWindow", u"Up Pivot = 0", None))
        self.gbX.setTitle(QCoreApplication.translate("PivotMainWindow", u"X", None))
        self.rbMinX.setText(QCoreApplication.translate("PivotMainWindow", u"min", None))
        self.rbCenterX.setText(QCoreApplication.translate("PivotMainWindow", u"center", None))
        self.rbMaxX.setText(QCoreApplication.translate("PivotMainWindow", u"max", None))
        self.btnSetupPivot000.setText(QCoreApplication.translate("PivotMainWindow", u"Pivot = [0,0,0]", None))
        self.gbZ.setTitle(QCoreApplication.translate("PivotMainWindow", u"Z", None))
        self.rbMinZ.setText(QCoreApplication.translate("PivotMainWindow", u"min", None))
        self.rbCenterZ.setText(QCoreApplication.translate("PivotMainWindow", u"center", None))
        self.rbMaxZ.setText(QCoreApplication.translate("PivotMainWindow", u"max", None))
        self.gbY.setTitle(QCoreApplication.translate("PivotMainWindow", u"Y", None))
        self.rbMinY.setText(QCoreApplication.translate("PivotMainWindow", u"min", None))
        self.rbCenterY.setText(QCoreApplication.translate("PivotMainWindow", u"center", None))
        self.rbMaxY.setText(QCoreApplication.translate("PivotMainWindow", u"max", None))
        self.btnSetupPivot.setText(QCoreApplication.translate("PivotMainWindow", u"Pivot =", None))
        self.btnSetupPos000.setText(QCoreApplication.translate("PivotMainWindow", u"Pos = [0,0,0]", None))
    # retranslateUi

