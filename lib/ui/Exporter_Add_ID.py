# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Exporter_Add_ID.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ExporterAddID(object):
    def setupUi(self, ExporterAddID):
        if not ExporterAddID.objectName():
            ExporterAddID.setObjectName(u"ExporterAddID")
        ExporterAddID.resize(476, 292)
        self.centralwidget = QWidget(ExporterAddID)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 278, 229))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lvMaterials = QListView(self.scrollAreaWidgetContents)
        self.lvMaterials.setObjectName(u"lvMaterials")
        self.lvMaterials.setMinimumSize(QSize(260, 0))

        self.gridLayout_4.addWidget(self.lvMaterials, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnSetID = QPushButton(self.centralwidget)
        self.btnSetID.setObjectName(u"btnSetID")

        self.gridLayout.addWidget(self.btnSetID, 0, 0, 1, 1)

        self.sbSetID = QSpinBox(self.centralwidget)
        self.sbSetID.setObjectName(u"sbSetID")
        self.sbSetID.setMinimumSize(QSize(50, 0))
        self.sbSetID.setMinimum(1)
        self.sbSetID.setValue(1)

        self.gridLayout.addWidget(self.sbSetID, 0, 1, 1, 1)

        self.btnSelectID = QPushButton(self.centralwidget)
        self.btnSelectID.setObjectName(u"btnSelectID")

        self.gridLayout.addWidget(self.btnSelectID, 1, 0, 1, 1)

        self.sbSelectID = QSpinBox(self.centralwidget)
        self.sbSelectID.setObjectName(u"sbSelectID")
        self.sbSelectID.setMinimumSize(QSize(80, 0))
        self.sbSelectID.setMinimum(1)
        self.sbSelectID.setValue(1)

        self.gridLayout.addWidget(self.sbSelectID, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setMinimumSize(QSize(0, 22))
        self.btn6.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn6, 0, 5, 1, 1)

        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setMinimumSize(QSize(0, 22))
        self.btn9.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn9, 1, 1, 1, 1)

        self.btn12 = QPushButton(self.centralwidget)
        self.btn12.setObjectName(u"btn12")
        self.btn12.setMinimumSize(QSize(0, 22))
        self.btn12.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn12, 1, 4, 1, 1)

        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(0, 22))
        self.btn1.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn1, 0, 0, 1, 1)

        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(0, 22))
        self.btn2.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn2, 0, 1, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(0, 22))
        self.btn3.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn3, 0, 2, 1, 1)

        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(0, 22))
        self.btn5.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn5, 0, 4, 1, 1)

        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setMinimumSize(QSize(0, 22))
        self.btn7.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn7, 0, 6, 1, 1)

        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setMinimumSize(QSize(0, 22))
        self.btn8.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn8, 1, 0, 1, 1)

        self.btn13 = QPushButton(self.centralwidget)
        self.btn13.setObjectName(u"btn13")
        self.btn13.setMinimumSize(QSize(0, 22))
        self.btn13.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn13, 1, 5, 1, 1)

        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(0, 22))
        self.btn4.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn4, 0, 3, 1, 1)

        self.btn24 = QPushButton(self.centralwidget)
        self.btn24.setObjectName(u"btn24")
        self.btn24.setMinimumSize(QSize(0, 22))
        self.btn24.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn24, 3, 2, 1, 1)

        self.btn30 = QPushButton(self.centralwidget)
        self.btn30.setObjectName(u"btn30")
        self.btn30.setMinimumSize(QSize(0, 22))
        self.btn30.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn30, 4, 1, 1, 1)

        self.btn27 = QPushButton(self.centralwidget)
        self.btn27.setObjectName(u"btn27")
        self.btn27.setMinimumSize(QSize(0, 22))
        self.btn27.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn27, 3, 5, 1, 1)

        self.btn39 = QPushButton(self.centralwidget)
        self.btn39.setObjectName(u"btn39")
        self.btn39.setMinimumSize(QSize(0, 22))
        self.btn39.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn39, 5, 3, 1, 1)

        self.btn31 = QPushButton(self.centralwidget)
        self.btn31.setObjectName(u"btn31")
        self.btn31.setMinimumSize(QSize(0, 22))
        self.btn31.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn31, 4, 2, 1, 1)

        self.btn28 = QPushButton(self.centralwidget)
        self.btn28.setObjectName(u"btn28")
        self.btn28.setMinimumSize(QSize(0, 22))
        self.btn28.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn28, 3, 6, 1, 1)

        self.btn38 = QPushButton(self.centralwidget)
        self.btn38.setObjectName(u"btn38")
        self.btn38.setMinimumSize(QSize(0, 22))
        self.btn38.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn38, 5, 2, 1, 1)

        self.btn21 = QPushButton(self.centralwidget)
        self.btn21.setObjectName(u"btn21")
        self.btn21.setMinimumSize(QSize(0, 22))
        self.btn21.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn21, 2, 6, 1, 1)

        self.btn20 = QPushButton(self.centralwidget)
        self.btn20.setObjectName(u"btn20")
        self.btn20.setMinimumSize(QSize(0, 22))
        self.btn20.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn20, 2, 5, 1, 1)

        self.btn35 = QPushButton(self.centralwidget)
        self.btn35.setObjectName(u"btn35")
        self.btn35.setMinimumSize(QSize(0, 22))
        self.btn35.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn35, 4, 6, 1, 1)

        self.btn19 = QPushButton(self.centralwidget)
        self.btn19.setObjectName(u"btn19")
        self.btn19.setMinimumSize(QSize(0, 22))
        self.btn19.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn19, 2, 4, 1, 1)

        self.btn36 = QPushButton(self.centralwidget)
        self.btn36.setObjectName(u"btn36")
        self.btn36.setMinimumSize(QSize(0, 22))
        self.btn36.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn36, 5, 0, 1, 1)

        self.btn34 = QPushButton(self.centralwidget)
        self.btn34.setObjectName(u"btn34")
        self.btn34.setMinimumSize(QSize(0, 22))
        self.btn34.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn34, 4, 5, 1, 1)

        self.btn26 = QPushButton(self.centralwidget)
        self.btn26.setObjectName(u"btn26")
        self.btn26.setMinimumSize(QSize(0, 22))
        self.btn26.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn26, 3, 4, 1, 1)

        self.btn37 = QPushButton(self.centralwidget)
        self.btn37.setObjectName(u"btn37")
        self.btn37.setMinimumSize(QSize(0, 22))
        self.btn37.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn37, 5, 1, 1, 1)

        self.btn41 = QPushButton(self.centralwidget)
        self.btn41.setObjectName(u"btn41")
        self.btn41.setMinimumSize(QSize(0, 22))
        self.btn41.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn41, 5, 5, 1, 1)

        self.btn40 = QPushButton(self.centralwidget)
        self.btn40.setObjectName(u"btn40")
        self.btn40.setMinimumSize(QSize(0, 22))
        self.btn40.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn40, 5, 4, 1, 1)

        self.btn42 = QPushButton(self.centralwidget)
        self.btn42.setObjectName(u"btn42")
        self.btn42.setMinimumSize(QSize(0, 22))
        self.btn42.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn42, 5, 6, 1, 1)

        self.btn17 = QPushButton(self.centralwidget)
        self.btn17.setObjectName(u"btn17")
        self.btn17.setMinimumSize(QSize(0, 22))
        self.btn17.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn17, 2, 2, 1, 1)

        self.btn16 = QPushButton(self.centralwidget)
        self.btn16.setObjectName(u"btn16")
        self.btn16.setMinimumSize(QSize(0, 22))
        self.btn16.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn16, 2, 1, 1, 1)

        self.btn14 = QPushButton(self.centralwidget)
        self.btn14.setObjectName(u"btn14")
        self.btn14.setMinimumSize(QSize(0, 22))
        self.btn14.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn14, 1, 6, 1, 1)

        self.btn15 = QPushButton(self.centralwidget)
        self.btn15.setObjectName(u"btn15")
        self.btn15.setMinimumSize(QSize(0, 22))
        self.btn15.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn15, 2, 0, 1, 1)

        self.btn25 = QPushButton(self.centralwidget)
        self.btn25.setObjectName(u"btn25")
        self.btn25.setMinimumSize(QSize(0, 22))
        self.btn25.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn25, 3, 3, 1, 1)

        self.btn32 = QPushButton(self.centralwidget)
        self.btn32.setObjectName(u"btn32")
        self.btn32.setMinimumSize(QSize(0, 22))
        self.btn32.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn32, 4, 3, 1, 1)

        self.btn18 = QPushButton(self.centralwidget)
        self.btn18.setObjectName(u"btn18")
        self.btn18.setMinimumSize(QSize(0, 22))
        self.btn18.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn18, 2, 3, 1, 1)

        self.btn29 = QPushButton(self.centralwidget)
        self.btn29.setObjectName(u"btn29")
        self.btn29.setMinimumSize(QSize(0, 22))
        self.btn29.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn29, 4, 0, 1, 1)

        self.btn33 = QPushButton(self.centralwidget)
        self.btn33.setObjectName(u"btn33")
        self.btn33.setMinimumSize(QSize(0, 22))
        self.btn33.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn33, 4, 4, 1, 1)

        self.btn10 = QPushButton(self.centralwidget)
        self.btn10.setObjectName(u"btn10")
        self.btn10.setMinimumSize(QSize(0, 22))
        self.btn10.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn10, 1, 2, 1, 1)

        self.btn11 = QPushButton(self.centralwidget)
        self.btn11.setObjectName(u"btn11")
        self.btn11.setMinimumSize(QSize(0, 22))
        self.btn11.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn11, 1, 3, 1, 1)

        self.btn23 = QPushButton(self.centralwidget)
        self.btn23.setObjectName(u"btn23")
        self.btn23.setMinimumSize(QSize(0, 22))
        self.btn23.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn23, 3, 1, 1, 1)

        self.btn22 = QPushButton(self.centralwidget)
        self.btn22.setObjectName(u"btn22")
        self.btn22.setMinimumSize(QSize(0, 22))
        self.btn22.setMaximumSize(QSize(22, 16777215))

        self.gridLayout_2.addWidget(self.btn22, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.btnRemoveID = QPushButton(self.centralwidget)
        self.btnRemoveID.setObjectName(u"btnRemoveID")

        self.gridLayout_3.addWidget(self.btnRemoveID, 2, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        ExporterAddID.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ExporterAddID)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 476, 21))
        ExporterAddID.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ExporterAddID)
        self.statusbar.setObjectName(u"statusbar")
        ExporterAddID.setStatusBar(self.statusbar)

        self.retranslateUi(ExporterAddID)

        QMetaObject.connectSlotsByName(ExporterAddID)
    # setupUi

    def retranslateUi(self, ExporterAddID):
        ExporterAddID.setWindowTitle(QCoreApplication.translate("ExporterAddID", u"Exporter Add ID", None))
        self.btnSetID.setText(QCoreApplication.translate("ExporterAddID", u"Set ID", None))
        self.btnSelectID.setText(QCoreApplication.translate("ExporterAddID", u"Select ID", None))
        self.btn6.setText(QCoreApplication.translate("ExporterAddID", u"6", None))
        self.btn9.setText(QCoreApplication.translate("ExporterAddID", u"9", None))
        self.btn12.setText(QCoreApplication.translate("ExporterAddID", u"12", None))
        self.btn1.setText(QCoreApplication.translate("ExporterAddID", u"1", None))
        self.btn2.setText(QCoreApplication.translate("ExporterAddID", u"2", None))
        self.btn3.setText(QCoreApplication.translate("ExporterAddID", u"3", None))
        self.btn5.setText(QCoreApplication.translate("ExporterAddID", u"5", None))
        self.btn7.setText(QCoreApplication.translate("ExporterAddID", u"7", None))
        self.btn8.setText(QCoreApplication.translate("ExporterAddID", u"8", None))
        self.btn13.setText(QCoreApplication.translate("ExporterAddID", u"13", None))
        self.btn4.setText(QCoreApplication.translate("ExporterAddID", u"4", None))
        self.btn24.setText(QCoreApplication.translate("ExporterAddID", u"24", None))
        self.btn30.setText(QCoreApplication.translate("ExporterAddID", u"30", None))
        self.btn27.setText(QCoreApplication.translate("ExporterAddID", u"27", None))
        self.btn39.setText(QCoreApplication.translate("ExporterAddID", u"39", None))
        self.btn31.setText(QCoreApplication.translate("ExporterAddID", u"31", None))
        self.btn28.setText(QCoreApplication.translate("ExporterAddID", u"28", None))
        self.btn38.setText(QCoreApplication.translate("ExporterAddID", u"38", None))
        self.btn21.setText(QCoreApplication.translate("ExporterAddID", u"21", None))
        self.btn20.setText(QCoreApplication.translate("ExporterAddID", u"20", None))
        self.btn35.setText(QCoreApplication.translate("ExporterAddID", u"35", None))
        self.btn19.setText(QCoreApplication.translate("ExporterAddID", u"19", None))
        self.btn36.setText(QCoreApplication.translate("ExporterAddID", u"36", None))
        self.btn34.setText(QCoreApplication.translate("ExporterAddID", u"34", None))
        self.btn26.setText(QCoreApplication.translate("ExporterAddID", u"26", None))
        self.btn37.setText(QCoreApplication.translate("ExporterAddID", u"37", None))
        self.btn41.setText(QCoreApplication.translate("ExporterAddID", u"41", None))
        self.btn40.setText(QCoreApplication.translate("ExporterAddID", u"40", None))
        self.btn42.setText(QCoreApplication.translate("ExporterAddID", u"42", None))
        self.btn17.setText(QCoreApplication.translate("ExporterAddID", u"17", None))
        self.btn16.setText(QCoreApplication.translate("ExporterAddID", u"16", None))
        self.btn14.setText(QCoreApplication.translate("ExporterAddID", u"14", None))
        self.btn15.setText(QCoreApplication.translate("ExporterAddID", u"15", None))
        self.btn25.setText(QCoreApplication.translate("ExporterAddID", u"25", None))
        self.btn32.setText(QCoreApplication.translate("ExporterAddID", u"32", None))
        self.btn18.setText(QCoreApplication.translate("ExporterAddID", u"18", None))
        self.btn29.setText(QCoreApplication.translate("ExporterAddID", u"29", None))
        self.btn33.setText(QCoreApplication.translate("ExporterAddID", u"33", None))
        self.btn10.setText(QCoreApplication.translate("ExporterAddID", u"10", None))
        self.btn11.setText(QCoreApplication.translate("ExporterAddID", u"11", None))
        self.btn23.setText(QCoreApplication.translate("ExporterAddID", u"23", None))
        self.btn22.setText(QCoreApplication.translate("ExporterAddID", u"22", None))
        self.btnRemoveID.setText(QCoreApplication.translate("ExporterAddID", u"Remove ID Selected", None))
    # retranslateUi

