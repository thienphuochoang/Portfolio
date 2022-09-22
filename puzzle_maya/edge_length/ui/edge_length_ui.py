# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edge_length_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EdgeLengthMainWindow(object):
    def setupUi(self, EdgeLengthMainWindow):
        if not EdgeLengthMainWindow.objectName():
            EdgeLengthMainWindow.setObjectName(u"EdgeLengthMainWindow")
        EdgeLengthMainWindow.resize(296, 119)
        self.centralwidget = QWidget(EdgeLengthMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.btnSelectEdge = QPushButton(self.frame)
        self.btnSelectEdge.setObjectName(u"btnSelectEdge")

        self.gridLayout.addWidget(self.btnSelectEdge, 0, 0, 1, 1)

        self.spnSelectedLength = QDoubleSpinBox(self.frame)
        self.spnSelectedLength.setObjectName(u"spnSelectedLength")
        self.spnSelectedLength.setMaximum(10000000.000000000000000)

        self.gridLayout.addWidget(self.spnSelectedLength, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnSetLength = QPushButton(self.frame_2)
        self.btnSetLength.setObjectName(u"btnSetLength")

        self.gridLayout_3.addWidget(self.btnSetLength, 0, 2, 1, 1)

        self.spnEdgeLength = QDoubleSpinBox(self.frame_2)
        self.spnEdgeLength.setObjectName(u"spnEdgeLength")
        self.spnEdgeLength.setMaximum(10000000.000000000000000)

        self.gridLayout_3.addWidget(self.spnEdgeLength, 0, 1, 1, 1)

        self.btnGetLength = QPushButton(self.frame_2)
        self.btnGetLength.setObjectName(u"btnGetLength")

        self.gridLayout_3.addWidget(self.btnGetLength, 0, 0, 1, 1)

        self.rdbLeft = QRadioButton(self.frame_2)
        self.rdbLeft.setObjectName(u"rdbLeft")
        self.rdbLeft.setChecked(True)

        self.gridLayout_3.addWidget(self.rdbLeft, 1, 0, 1, 1)

        self.rdbCenter = QRadioButton(self.frame_2)
        self.rdbCenter.setObjectName(u"rdbCenter")

        self.gridLayout_3.addWidget(self.rdbCenter, 1, 1, 1, 1)

        self.rdbRight = QRadioButton(self.frame_2)
        self.rdbRight.setObjectName(u"rdbRight")

        self.gridLayout_3.addWidget(self.rdbRight, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 4, 0, 1, 3)

        EdgeLengthMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EdgeLengthMainWindow)

        QMetaObject.connectSlotsByName(EdgeLengthMainWindow)
    # setupUi

    def retranslateUi(self, EdgeLengthMainWindow):
        EdgeLengthMainWindow.setWindowTitle(QCoreApplication.translate("EdgeLengthMainWindow", u"Edge Length Main Window", None))
        self.btnSelectEdge.setText(QCoreApplication.translate("EdgeLengthMainWindow", u"Select Edge With Length <", None))
        self.btnSetLength.setText(QCoreApplication.translate("EdgeLengthMainWindow", u"Set Length", None))
        self.btnGetLength.setText(QCoreApplication.translate("EdgeLengthMainWindow", u"Get Length", None))
        self.rdbLeft.setText(QCoreApplication.translate("EdgeLengthMainWindow", u"left", None))
        self.rdbCenter.setText(QCoreApplication.translate("EdgeLengthMainWindow", u"center", None))
        self.rdbRight.setText(QCoreApplication.translate("EdgeLengthMainWindow", u"right", None))
    # retranslateUi

