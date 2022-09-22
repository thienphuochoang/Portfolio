# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'texel_density_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TexelDensityMainWindow(object):
    def setupUi(self, TexelDensityMainWindow):
        if not TexelDensityMainWindow.objectName():
            TexelDensityMainWindow.setObjectName(u"TexelDensityMainWindow")
        TexelDensityMainWindow.resize(368, 98)
        self.centralwidget = QWidget(TexelDensityMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnGet = QPushButton(self.frame)
        self.btnGet.setObjectName(u"btnGet")

        self.horizontalLayout_6.addWidget(self.btnGet)

        self.spnTexelDensity = QDoubleSpinBox(self.frame)
        self.spnTexelDensity.setObjectName(u"spnTexelDensity")
        self.spnTexelDensity.setDecimals(4)
        self.spnTexelDensity.setMaximum(100000.000000000000000)

        self.horizontalLayout_6.addWidget(self.spnTexelDensity)

        self.btnSet = QPushButton(self.frame)
        self.btnSet.setObjectName(u"btnSet")

        self.horizontalLayout_6.addWidget(self.btnSet)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cbWidth = QComboBox(self.frame_2)
        self.cbWidth.setObjectName(u"cbWidth")

        self.horizontalLayout_2.addWidget(self.cbWidth)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.cbHeight = QComboBox(self.frame_2)
        self.cbHeight.setObjectName(u"cbHeight")

        self.horizontalLayout_2.addWidget(self.cbHeight)

        self.cbConstraint = QCheckBox(self.frame_2)
        self.cbConstraint.setObjectName(u"cbConstraint")
        self.cbConstraint.setChecked(True)

        self.horizontalLayout_2.addWidget(self.cbConstraint)


        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnAssignCheckerMaterial = QPushButton(self.frame_3)
        self.btnAssignCheckerMaterial.setObjectName(u"btnAssignCheckerMaterial")
        self.btnAssignCheckerMaterial.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.btnAssignCheckerMaterial)

        self.btnCycleCheckerMap = QPushButton(self.frame_3)
        self.btnCycleCheckerMap.setObjectName(u"btnCycleCheckerMap")
        self.btnCycleCheckerMap.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.btnCycleCheckerMap)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.spnTilingU = QDoubleSpinBox(self.frame_3)
        self.spnTilingU.setObjectName(u"spnTilingU")
        self.spnTilingU.setMaximum(1000.000000000000000)
        self.spnTilingU.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.spnTilingU)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.spnTilingV = QDoubleSpinBox(self.frame_3)
        self.spnTilingV.setObjectName(u"spnTilingV")
        self.spnTilingV.setMaximum(1000.000000000000000)
        self.spnTilingV.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.spnTilingV)

        self.btnReset = QPushButton(self.frame_3)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.btnReset)


        self.gridLayout.addWidget(self.frame_3, 2, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 3, 1)

        TexelDensityMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TexelDensityMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        TexelDensityMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TexelDensityMainWindow)

        QMetaObject.connectSlotsByName(TexelDensityMainWindow)
    # setupUi

    def retranslateUi(self, TexelDensityMainWindow):
        TexelDensityMainWindow.setWindowTitle(QCoreApplication.translate("TexelDensityMainWindow", u"Texel Density Tool", None))
        self.btnGet.setText(QCoreApplication.translate("TexelDensityMainWindow", u"Get", None))
        self.btnSet.setText(QCoreApplication.translate("TexelDensityMainWindow", u"Set", None))
        self.label_2.setText(QCoreApplication.translate("TexelDensityMainWindow", u"Width:", None))
        self.label_3.setText(QCoreApplication.translate("TexelDensityMainWindow", u"Height:", None))
#if QT_CONFIG(tooltip)
        self.cbConstraint.setToolTip(QCoreApplication.translate("TexelDensityMainWindow", u"Constraints for Width and Height", None))
#endif // QT_CONFIG(tooltip)
        self.cbConstraint.setText("")
        self.btnAssignCheckerMaterial.setText("")
        self.btnCycleCheckerMap.setText("")
        self.label_4.setText(QCoreApplication.translate("TexelDensityMainWindow", u"U", None))
        self.label_5.setText(QCoreApplication.translate("TexelDensityMainWindow", u"V", None))
        self.btnReset.setText("")
        self.label.setText(QCoreApplication.translate("TexelDensityMainWindow", u"Texel Density\n"
" (Px/Unit)", None))
    # retranslateUi

