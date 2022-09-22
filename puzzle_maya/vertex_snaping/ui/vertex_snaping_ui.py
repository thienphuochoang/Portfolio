# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vertex_snaping_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VertexSnapingMainWindow(object):
    def setupUi(self, VertexSnapingMainWindow):
        if not VertexSnapingMainWindow.objectName():
            VertexSnapingMainWindow.setObjectName(u"VertexSnapingMainWindow")
        VertexSnapingMainWindow.resize(206, 74)
        self.centralwidget = QWidget(VertexSnapingMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spnThreshold = QDoubleSpinBox(self.centralwidget)
        self.spnThreshold.setObjectName(u"spnThreshold")
        self.spnThreshold.setMaximum(100000000.000000000000000)
        self.spnThreshold.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.spnThreshold, 0, 1, 1, 1)

        self.thresholdLabel = QLabel(self.centralwidget)
        self.thresholdLabel.setObjectName(u"thresholdLabel")
        self.thresholdLabel.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.thresholdLabel, 0, 0, 1, 1)

        self.btnMergeToCenter = QPushButton(self.centralwidget)
        self.btnMergeToCenter.setObjectName(u"btnMergeToCenter")

        self.gridLayout_2.addWidget(self.btnMergeToCenter, 1, 1, 1, 1)

        self.btnSnapToClosestVertex = QPushButton(self.centralwidget)
        self.btnSnapToClosestVertex.setObjectName(u"btnSnapToClosestVertex")

        self.gridLayout_2.addWidget(self.btnSnapToClosestVertex, 1, 0, 1, 1)

        VertexSnapingMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(VertexSnapingMainWindow)

        QMetaObject.connectSlotsByName(VertexSnapingMainWindow)
    # setupUi

    def retranslateUi(self, VertexSnapingMainWindow):
        VertexSnapingMainWindow.setWindowTitle(QCoreApplication.translate("VertexSnapingMainWindow", u"Vertex Snaping Main Window", None))
        self.thresholdLabel.setText(QCoreApplication.translate("VertexSnapingMainWindow", u"Threshold", None))
        self.btnMergeToCenter.setText(QCoreApplication.translate("VertexSnapingMainWindow", u"Merge To Center", None))
        self.btnSnapToClosestVertex.setText(QCoreApplication.translate("VertexSnapingMainWindow", u"Snap To Closest", None))
    # retranslateUi

