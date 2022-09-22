# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Validation_MainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindowValidation(object):
    def setupUi(self, MainWindowValidation):
        if not MainWindowValidation.objectName():
            MainWindowValidation.setObjectName(u"MainWindowValidation")
        MainWindowValidation.resize(409, 862)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowValidation.sizePolicy().hasHeightForWidth())
        MainWindowValidation.setSizePolicy(sizePolicy)
        MainWindowValidation.setMinimumSize(QSize(100, 0))
        self.actionShader_Library = QAction(MainWindowValidation)
        self.actionShader_Library.setObjectName(u"actionShader_Library")
        self.actionBaking_AO = QAction(MainWindowValidation)
        self.actionBaking_AO.setObjectName(u"actionBaking_AO")
        self.action = QAction(MainWindowValidation)
        self.action.setObjectName(u"action")
        self.actionOpen_Preset_Folder = QAction(MainWindowValidation)
        self.actionOpen_Preset_Folder.setObjectName(u"actionOpen_Preset_Folder")
        self.actionAdd_And_Save_Preset = QAction(MainWindowValidation)
        self.actionAdd_And_Save_Preset.setObjectName(u"actionAdd_And_Save_Preset")
        self.centralwidget = QWidget(MainWindowValidation)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 20))
        self.frame.setMaximumSize(QSize(16777215, 75))
        self.frame.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbTitle = QLabel(self.frame)
        self.lbTitle.setObjectName(u"lbTitle")
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(14)
        self.lbTitle.setFont(font)
        self.lbTitle.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbTitle, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 401, 676))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalSpacer = QSpacerItem(17, 700, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 15))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.lbValidationResult = QLabel(self.centralwidget)
        self.lbValidationResult.setObjectName(u"lbValidationResult")
        self.lbValidationResult.setLayoutDirection(Qt.LeftToRight)
        self.lbValidationResult.setAutoFillBackground(False)
        self.lbValidationResult.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbValidationResult)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnSwapCheckUncheckAll = QPushButton(self.centralwidget)
        self.btnSwapCheckUncheckAll.setObjectName(u"btnSwapCheckUncheckAll")
        self.btnSwapCheckUncheckAll.setMinimumSize(QSize(0, 35))
        self.btnSwapCheckUncheckAll.setStyleSheet(u"")
        self.btnSwapCheckUncheckAll.setCheckable(False)
        self.btnSwapCheckUncheckAll.setChecked(False)
        self.btnSwapCheckUncheckAll.setFlat(False)

        self.gridLayout.addWidget(self.btnSwapCheckUncheckAll, 0, 1, 1, 1)

        self.btnShowError = QPushButton(self.centralwidget)
        self.btnShowError.setObjectName(u"btnShowError")
        self.btnShowError.setMinimumSize(QSize(0, 33))
        self.btnShowError.setMaximumSize(QSize(10, 33))
        self.btnShowError.setStyleSheet(u"QPushButton { \n"
"   background-color: rgb(255, 0, 0);\n"
"	border: 0px;\n"
"}\n"
"")
        self.btnShowError.setCheckable(True)
        self.btnShowError.setFlat(False)

        self.gridLayout.addWidget(self.btnShowError, 0, 5, 1, 1)

        self.btnValidate = QPushButton(self.centralwidget)
        self.btnValidate.setObjectName(u"btnValidate")
        self.btnValidate.setMinimumSize(QSize(0, 45))

        self.gridLayout.addWidget(self.btnValidate, 0, 2, 1, 1)

        self.btnUncollapseAll = QPushButton(self.centralwidget)
        self.btnUncollapseAll.setObjectName(u"btnUncollapseAll")
        self.btnUncollapseAll.setMinimumSize(QSize(30, 35))
        self.btnUncollapseAll.setCheckable(True)
        self.btnUncollapseAll.setFlat(False)

        self.gridLayout.addWidget(self.btnUncollapseAll, 0, 4, 1, 1)

        self.btnResetAll = QPushButton(self.centralwidget)
        self.btnResetAll.setObjectName(u"btnResetAll")
        self.btnResetAll.setMinimumSize(QSize(0, 33))
        self.btnResetAll.setMaximumSize(QSize(10, 33))
        self.btnResetAll.setStyleSheet(u"QPushButton { \n"
"   background-color: grey;\n"
"	border: 0px;\n"
"}\n"
"")
        self.btnResetAll.setFlat(False)

        self.gridLayout.addWidget(self.btnResetAll, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        MainWindowValidation.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindowValidation)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 409, 29))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPreset = QMenu(self.menuBar)
        self.menuPreset.setObjectName(u"menuPreset")
        MainWindowValidation.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPreset.menuAction())
        self.menuFile.addAction(self.actionAdd_And_Save_Preset)
        self.menuFile.addAction(self.actionOpen_Preset_Folder)
        self.menuFile.addSeparator()

        self.retranslateUi(MainWindowValidation)

        self.btnUncollapseAll.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindowValidation)
    # setupUi

    def retranslateUi(self, MainWindowValidation):
        MainWindowValidation.setWindowTitle(QCoreApplication.translate("MainWindowValidation", u"Validation Main Window", None))
        self.actionShader_Library.setText(QCoreApplication.translate("MainWindowValidation", u"Shader Library", None))
        self.actionBaking_AO.setText(QCoreApplication.translate("MainWindowValidation", u"Rigging Vehicle", None))
        self.action.setText(QCoreApplication.translate("MainWindowValidation", u"Add New...", None))
        self.actionOpen_Preset_Folder.setText(QCoreApplication.translate("MainWindowValidation", u"Open Preset Folder", None))
        self.actionAdd_And_Save_Preset.setText(QCoreApplication.translate("MainWindowValidation", u"Create New/ Save Preset", None))
        self.lbTitle.setText(QCoreApplication.translate("MainWindowValidation", u"Validation", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindowValidation", u"%p%", None))
        self.lbValidationResult.setText(QCoreApplication.translate("MainWindowValidation", u"Validation Result !", None))
        self.btnSwapCheckUncheckAll.setText(QCoreApplication.translate("MainWindowValidation", u"Check\n"
"Uncheck", None))
#if QT_CONFIG(tooltip)
        self.btnShowError.setToolTip(QCoreApplication.translate("MainWindowValidation", u"<html><head/><body><p><span style=\" font-size:10pt;\">Hi\u1ec3n th\u1ecb t\u1ea5t c\u1ea3 danh s\u00e1ch ph\u1ea7n t\u1eed c\u1ee7a nh\u1eefng m\u1ee5c sai</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnShowError.setText("")
#if QT_CONFIG(tooltip)
        self.btnValidate.setToolTip(QCoreApplication.translate("MainWindowValidation", u"<html><head/><body><p><span style=\" font-size:10pt;\">T\u1ef1 \u0111\u1ed9ng ch\u1ea1y tu\u1ea7n t\u1ef1 t\u1eeb tr\u00ean xu\u1ed1ng d\u01b0\u1edbi t\u1ea5t c\u1ea3 c\u00e1c m\u1ee5c check l\u1ed7i</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnValidate.setText(QCoreApplication.translate("MainWindowValidation", u"Validate", None))
        self.btnUncollapseAll.setText(QCoreApplication.translate("MainWindowValidation", u"Collapse\n"
"Uncollapse", None))
#if QT_CONFIG(tooltip)
        self.btnResetAll.setToolTip(QCoreApplication.translate("MainWindowValidation", u"<html><head/><body><p><span style=\" font-size:10pt;\">Hi\u1ec3n th\u1ecb t\u1ea5t c\u1ea3 danh s\u00e1ch ph\u1ea7n t\u1eed c\u1ee7a nh\u1eefng m\u1ee5c \u0111\u00fang</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnResetAll.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindowValidation", u"File", None))
        self.menuPreset.setTitle(QCoreApplication.translate("MainWindowValidation", u"Load Preset", None))
    # retranslateUi

