# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assigned_sbsar_mat_object_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_widgetAssignedMat(object):
    def setupUi(self, widgetAssignedMat):
        if not widgetAssignedMat.objectName():
            widgetAssignedMat.setObjectName(u"widgetAssignedMat")
        widgetAssignedMat.resize(308, 91)
        self.horizontalLayout = QHBoxLayout(widgetAssignedMat)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbObjectName = QLabel(widgetAssignedMat)
        self.lbObjectName.setObjectName(u"lbObjectName")

        self.horizontalLayout.addWidget(self.lbObjectName)

        self.lwAssignedSBSARMat = QListWidget(widgetAssignedMat)
        self.lwAssignedSBSARMat.setObjectName(u"lwAssignedSBSARMat")
        self.lwAssignedSBSARMat.setIconSize(QSize(64, 64))
        self.lwAssignedSBSARMat.setResizeMode(QListView.Adjust)
        self.lwAssignedSBSARMat.setViewMode(QListView.IconMode)

        self.horizontalLayout.addWidget(self.lwAssignedSBSARMat)


        self.retranslateUi(widgetAssignedMat)

        QMetaObject.connectSlotsByName(widgetAssignedMat)
    # setupUi

    def retranslateUi(self, widgetAssignedMat):
        widgetAssignedMat.setWindowTitle(QCoreApplication.translate("widgetAssignedMat", u"Form", None))
        self.lbObjectName.setText(QCoreApplication.translate("widgetAssignedMat", u"Asset Name", None))
    # retranslateUi

