# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/WIP_Portfolio/puzzle_maya/uv_tool/texel_density/ui/texel_density_ui.ui',
# licensing of 'D:/WIP_Portfolio/puzzle_maya/uv_tool/texel_density/ui/texel_density_ui.ui' applies.
#
# Created: Tue Jul 28 02:12:48 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 176)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnGet = QtWidgets.QPushButton(self.frame)
        self.btnGet.setObjectName("btnGet")
        self.horizontalLayout_6.addWidget(self.btnGet)
        self.spnTexelDensity = QtWidgets.QDoubleSpinBox(self.frame)
        self.spnTexelDensity.setDecimals(4)
        self.spnTexelDensity.setObjectName("spnTexelDensity")
        self.horizontalLayout_6.addWidget(self.spnTexelDensity)
        self.btnSet = QtWidgets.QPushButton(self.frame)
        self.btnSet.setObjectName("btnSet")
        self.horizontalLayout_6.addWidget(self.btnSet)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cbWidth = QtWidgets.QComboBox(self.frame_2)
        self.cbWidth.setObjectName("cbWidth")
        self.horizontalLayout_2.addWidget(self.cbWidth)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cbHeight = QtWidgets.QComboBox(self.frame_2)
        self.cbHeight.setObjectName("cbHeight")
        self.horizontalLayout_2.addWidget(self.cbHeight)
        self.cbConstraint = QtWidgets.QCheckBox(self.frame_2)
        self.cbConstraint.setText("")
        self.cbConstraint.setChecked(True)
        self.cbConstraint.setObjectName("cbConstraint")
        self.horizontalLayout_2.addWidget(self.cbConstraint)
        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAssignCheckerMaterial = QtWidgets.QPushButton(self.frame_3)
        self.btnAssignCheckerMaterial.setText("")
        self.btnAssignCheckerMaterial.setObjectName("btnAssignCheckerMaterial")
        self.horizontalLayout.addWidget(self.btnAssignCheckerMaterial)
        self.btnCycleCheckerMap = QtWidgets.QPushButton(self.frame_3)
        self.btnCycleCheckerMap.setText("")
        self.btnCycleCheckerMap.setObjectName("btnCycleCheckerMap")
        self.horizontalLayout.addWidget(self.btnCycleCheckerMap)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.spnTilingU = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.spnTilingU.setProperty("value", 1.0)
        self.spnTilingU.setObjectName("spnTilingU")
        self.horizontalLayout.addWidget(self.spnTilingU)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.spnTilingV = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.spnTilingV.setProperty("value", 1.0)
        self.spnTilingV.setObjectName("spnTilingV")
        self.horizontalLayout.addWidget(self.spnTilingV)
        self.btnReset = QtWidgets.QPushButton(self.frame_3)
        self.btnReset.setText("")
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout.addWidget(self.btnReset)
        self.gridLayout.addWidget(self.frame_3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Texel Density Tool", None, -1))
        self.btnGet.setText(QtWidgets.QApplication.translate("MainWindow", "Get", None, -1))
        self.btnSet.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Width:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Height:", None, -1))
        self.cbConstraint.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Constraints for Width and Height", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "U", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "V", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Texel Density\n"
" (Px/Unit)", None, -1))

