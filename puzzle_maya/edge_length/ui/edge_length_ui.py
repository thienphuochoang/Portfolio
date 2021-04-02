# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/WIP_Portfolio/puzzle_maya/edge_length/ui/edge_length_ui.ui',
# licensing of 'D:/WIP_Portfolio/puzzle_maya/edge_length/ui/edge_length_ui.ui' applies.
#
# Created: Wed Mar 10 23:32:31 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_EdgeLengthMainWindow(object):
    def setupUi(self, EdgeLengthMainWindow):
        EdgeLengthMainWindow.setObjectName("EdgeLengthMainWindow")
        EdgeLengthMainWindow.resize(296, 119)
        self.centralwidget = QtWidgets.QWidget(EdgeLengthMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSelectEdge = QtWidgets.QPushButton(self.frame)
        self.btnSelectEdge.setObjectName("btnSelectEdge")
        self.gridLayout.addWidget(self.btnSelectEdge, 0, 0, 1, 1)
        self.spnSelectedLength = QtWidgets.QDoubleSpinBox(self.frame)
        self.spnSelectedLength.setMaximum(10000000.0)
        self.spnSelectedLength.setObjectName("spnSelectedLength")
        self.gridLayout.addWidget(self.spnSelectedLength, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnSetLength = QtWidgets.QPushButton(self.frame_2)
        self.btnSetLength.setObjectName("btnSetLength")
        self.gridLayout_3.addWidget(self.btnSetLength, 0, 2, 1, 1)
        self.spnEdgeLength = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.spnEdgeLength.setMaximum(10000000.0)
        self.spnEdgeLength.setObjectName("spnEdgeLength")
        self.gridLayout_3.addWidget(self.spnEdgeLength, 0, 1, 1, 1)
        self.btnGetLength = QtWidgets.QPushButton(self.frame_2)
        self.btnGetLength.setObjectName("btnGetLength")
        self.gridLayout_3.addWidget(self.btnGetLength, 0, 0, 1, 1)
        self.rdbLeft = QtWidgets.QRadioButton(self.frame_2)
        self.rdbLeft.setChecked(True)
        self.rdbLeft.setObjectName("rdbLeft")
        self.gridLayout_3.addWidget(self.rdbLeft, 1, 0, 1, 1)
        self.rdbCenter = QtWidgets.QRadioButton(self.frame_2)
        self.rdbCenter.setObjectName("rdbCenter")
        self.gridLayout_3.addWidget(self.rdbCenter, 1, 1, 1, 1)
        self.rdbRight = QtWidgets.QRadioButton(self.frame_2)
        self.rdbRight.setObjectName("rdbRight")
        self.gridLayout_3.addWidget(self.rdbRight, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 4, 0, 1, 3)
        EdgeLengthMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EdgeLengthMainWindow)
        QtCore.QMetaObject.connectSlotsByName(EdgeLengthMainWindow)

    def retranslateUi(self, EdgeLengthMainWindow):
        EdgeLengthMainWindow.setWindowTitle(QtWidgets.QApplication.translate("EdgeLengthMainWindow", "Edge Length Main Window", None, -1))
        self.btnSelectEdge.setText(QtWidgets.QApplication.translate("EdgeLengthMainWindow", "Select Edge With Length <", None, -1))
        self.btnSetLength.setText(QtWidgets.QApplication.translate("EdgeLengthMainWindow", "Set Length", None, -1))
        self.btnGetLength.setText(QtWidgets.QApplication.translate("EdgeLengthMainWindow", "Get Length", None, -1))
        self.rdbLeft.setText(QtWidgets.QApplication.translate("EdgeLengthMainWindow", "left", None, -1))
        self.rdbCenter.setText(QtWidgets.QApplication.translate("EdgeLengthMainWindow", "center", None, -1))
        self.rdbRight.setText(QtWidgets.QApplication.translate("EdgeLengthMainWindow", "right", None, -1))

