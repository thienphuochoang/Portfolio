# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/WIP_Portfolio/puzzle_maya/sbsar_mat_creation/ui/assigned_sbsar_mat_object_ui.ui',
# licensing of 'D:/WIP_Portfolio/puzzle_maya/sbsar_mat_creation/ui/assigned_sbsar_mat_object_ui.ui' applies.
#
# Created: Thu Jun 17 00:36:04 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_widgetAssignedMat(object):
    def setupUi(self, widgetAssignedMat):
        widgetAssignedMat.setObjectName("widgetAssignedMat")
        widgetAssignedMat.resize(308, 91)
        self.horizontalLayout = QtWidgets.QHBoxLayout(widgetAssignedMat)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbObjectName = QtWidgets.QLabel(widgetAssignedMat)
        self.lbObjectName.setObjectName("lbObjectName")
        self.horizontalLayout.addWidget(self.lbObjectName)
        self.lwAssignedSBSARMat = QtWidgets.QListWidget(widgetAssignedMat)
        self.lwAssignedSBSARMat.setIconSize(QtCore.QSize(64, 64))
        self.lwAssignedSBSARMat.setResizeMode(QtWidgets.QListView.Adjust)
        self.lwAssignedSBSARMat.setViewMode(QtWidgets.QListView.IconMode)
        self.lwAssignedSBSARMat.setObjectName("lwAssignedSBSARMat")
        self.horizontalLayout.addWidget(self.lwAssignedSBSARMat)

        self.retranslateUi(widgetAssignedMat)
        QtCore.QMetaObject.connectSlotsByName(widgetAssignedMat)

    def retranslateUi(self, widgetAssignedMat):
        widgetAssignedMat.setWindowTitle(QtWidgets.QApplication.translate("widgetAssignedMat", "Form", None, -1))
        self.lbObjectName.setText(QtWidgets.QApplication.translate("widgetAssignedMat", "Asset Name", None, -1))

