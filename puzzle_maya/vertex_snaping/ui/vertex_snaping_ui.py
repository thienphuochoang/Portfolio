# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/WIP_Portfolio/puzzle_maya/vertex_snaping/ui/vertex_snaping_ui.ui',
# licensing of 'D:/WIP_Portfolio/puzzle_maya/vertex_snaping/ui/vertex_snaping_ui.ui' applies.
#
# Created: Wed Mar 10 21:58:59 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_VertexSnapingMainWindow(object):
    def setupUi(self, VertexSnapingMainWindow):
        VertexSnapingMainWindow.setObjectName("VertexSnapingMainWindow")
        VertexSnapingMainWindow.resize(206, 74)
        self.centralwidget = QtWidgets.QWidget(VertexSnapingMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spnThreshold = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spnThreshold.setMaximum(100000000.0)
        self.spnThreshold.setProperty("value", 1.0)
        self.spnThreshold.setObjectName("spnThreshold")
        self.gridLayout_2.addWidget(self.spnThreshold, 0, 1, 1, 1)
        self.thresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.thresholdLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.gridLayout_2.addWidget(self.thresholdLabel, 0, 0, 1, 1)
        self.btnMergeToCenter = QtWidgets.QPushButton(self.centralwidget)
        self.btnMergeToCenter.setObjectName("btnMergeToCenter")
        self.gridLayout_2.addWidget(self.btnMergeToCenter, 1, 1, 1, 1)
        self.btnSnapToClosestVertex = QtWidgets.QPushButton(self.centralwidget)
        self.btnSnapToClosestVertex.setObjectName("btnSnapToClosestVertex")
        self.gridLayout_2.addWidget(self.btnSnapToClosestVertex, 1, 0, 1, 1)
        VertexSnapingMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(VertexSnapingMainWindow)
        QtCore.QMetaObject.connectSlotsByName(VertexSnapingMainWindow)

    def retranslateUi(self, VertexSnapingMainWindow):
        VertexSnapingMainWindow.setWindowTitle(QtWidgets.QApplication.translate("VertexSnapingMainWindow", "Vertex Snaping Main Window", None, -1))
        self.thresholdLabel.setText(QtWidgets.QApplication.translate("VertexSnapingMainWindow", "Threshold", None, -1))
        self.btnMergeToCenter.setText(QtWidgets.QApplication.translate("VertexSnapingMainWindow", "Merge To Center", None, -1))
        self.btnSnapToClosestVertex.setText(QtWidgets.QApplication.translate("VertexSnapingMainWindow", "Snap To Closest", None, -1))

