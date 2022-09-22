# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sbsar_mat_creation_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SBSARMatCreationMainWindow(object):
    def setupUi(self, SBSARMatCreationMainWindow):
        if not SBSARMatCreationMainWindow.objectName():
            SBSARMatCreationMainWindow.setObjectName(u"SBSARMatCreationMainWindow")
        SBSARMatCreationMainWindow.resize(828, 810)
        self.centralwidget = QWidget(SBSARMatCreationMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(743, 530))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbBakingSettings = QLabel(self.centralwidget)
        self.lbBakingSettings.setObjectName(u"lbBakingSettings")
        font = QFont()
        font.setPointSize(15)
        self.lbBakingSettings.setFont(font)
        self.lbBakingSettings.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.lbBakingSettings.setFrameShape(QFrame.StyledPanel)
        self.lbBakingSettings.setFrameShadow(QFrame.Raised)
        self.lbBakingSettings.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbBakingSettings, 0, 0, 1, 2)

        self.twSwitchingTab = QTabWidget(self.centralwidget)
        self.twSwitchingTab.setObjectName(u"twSwitchingTab")
        self.bakingTab = QWidget()
        self.bakingTab.setObjectName(u"bakingTab")
        self.gridLayout_6 = QGridLayout(self.bakingTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbAntiAlias = QLabel(self.bakingTab)
        self.lbAntiAlias.setObjectName(u"lbAntiAlias")
        self.lbAntiAlias.setMinimumSize(QSize(50, 0))
        self.lbAntiAlias.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.lbAntiAlias)

        self.cbbAntiAlias = QComboBox(self.bakingTab)
        self.cbbAntiAlias.setObjectName(u"cbbAntiAlias")
        self.cbbAntiAlias.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.cbbAntiAlias)

        self.lbUvSet = QLabel(self.bakingTab)
        self.lbUvSet.setObjectName(u"lbUvSet")
        self.lbUvSet.setMinimumSize(QSize(50, 0))
        self.lbUvSet.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.lbUvSet)

        self.cbbUvSet = QComboBox(self.bakingTab)
        self.cbbUvSet.setObjectName(u"cbbUvSet")

        self.horizontalLayout_4.addWidget(self.cbbUvSet)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbInputPath = QLabel(self.bakingTab)
        self.lbInputPath.setObjectName(u"lbInputPath")

        self.gridLayout_4.addWidget(self.lbInputPath, 1, 0, 1, 1)

        self.leInputPath = QLineEdit(self.bakingTab)
        self.leInputPath.setObjectName(u"leInputPath")

        self.gridLayout_4.addWidget(self.leInputPath, 1, 1, 1, 1)

        self.cbbUseUpperSettings = QCheckBox(self.bakingTab)
        self.cbbUseUpperSettings.setObjectName(u"cbbUseUpperSettings")

        self.gridLayout_4.addWidget(self.cbbUseUpperSettings, 0, 0, 1, 2)

        self.lbInputName = QLabel(self.bakingTab)
        self.lbInputName.setObjectName(u"lbInputName")

        self.gridLayout_4.addWidget(self.lbInputName, 2, 0, 1, 1)

        self.leInputName = QLineEdit(self.bakingTab)
        self.leInputName.setObjectName(u"leInputName")

        self.gridLayout_4.addWidget(self.leInputName, 2, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 9, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 446, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 11, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbWidth = QLabel(self.bakingTab)
        self.lbWidth.setObjectName(u"lbWidth")
        self.lbWidth.setMinimumSize(QSize(50, 0))
        self.lbWidth.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.lbWidth)

        self.cbbWidth = QComboBox(self.bakingTab)
        self.cbbWidth.setObjectName(u"cbbWidth")
        self.cbbWidth.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.cbbWidth)

        self.lbHeight = QLabel(self.bakingTab)
        self.lbHeight.setObjectName(u"lbHeight")
        self.lbHeight.setMinimumSize(QSize(50, 0))
        self.lbHeight.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.lbHeight)

        self.cbbHeight = QComboBox(self.bakingTab)
        self.cbbHeight.setObjectName(u"cbbHeight")
        self.cbbHeight.setMinimumSize(QSize(0, 0))
        self.cbbHeight.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.cbbHeight)

        self.lbFormat = QLabel(self.bakingTab)
        self.lbFormat.setObjectName(u"lbFormat")
        self.lbFormat.setMinimumSize(QSize(50, 0))
        self.lbFormat.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.lbFormat)

        self.cbbFormat = QComboBox(self.bakingTab)
        self.cbbFormat.setObjectName(u"cbbFormat")

        self.horizontalLayout_3.addWidget(self.cbbFormat)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.leNormalMap = QLineEdit(self.bakingTab)
        self.leNormalMap.setObjectName(u"leNormalMap")

        self.horizontalLayout_9.addWidget(self.leNormalMap)

        self.btnBrowseNormalMap = QPushButton(self.bakingTab)
        self.btnBrowseNormalMap.setObjectName(u"btnBrowseNormalMap")

        self.horizontalLayout_9.addWidget(self.btnBrowseNormalMap)

        self.cbUseLowAsHigh = QCheckBox(self.bakingTab)
        self.cbUseLowAsHigh.setObjectName(u"cbUseLowAsHigh")
        self.cbUseLowAsHigh.setChecked(True)

        self.horizontalLayout_9.addWidget(self.cbUseLowAsHigh)


        self.gridLayout_6.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.btnBakeMeshMaps = QPushButton(self.bakingTab)
        self.btnBakeMeshMaps.setObjectName(u"btnBakeMeshMaps")

        self.gridLayout_6.addWidget(self.btnBakeMeshMaps, 7, 0, 1, 1)

        self.btnCreateFileSBS = QPushButton(self.bakingTab)
        self.btnCreateFileSBS.setObjectName(u"btnCreateFileSBS")

        self.gridLayout_6.addWidget(self.btnCreateFileSBS, 10, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbOutputPath = QLabel(self.bakingTab)
        self.lbOutputPath.setObjectName(u"lbOutputPath")

        self.horizontalLayout_7.addWidget(self.lbOutputPath)

        self.leOutputPath = QLineEdit(self.bakingTab)
        self.leOutputPath.setObjectName(u"leOutputPath")

        self.horizontalLayout_7.addWidget(self.leOutputPath)

        self.btnBrowse = QPushButton(self.bakingTab)
        self.btnBrowse.setObjectName(u"btnBrowse")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.btnBrowse)


        self.gridLayout_6.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbOutputName = QLabel(self.bakingTab)
        self.lbOutputName.setObjectName(u"lbOutputName")

        self.horizontalLayout_5.addWidget(self.lbOutputName)

        self.leOutputName = QLineEdit(self.bakingTab)
        self.leOutputName.setObjectName(u"leOutputName")

        self.horizontalLayout_5.addWidget(self.leOutputName)


        self.gridLayout_6.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gbPreBake = QGroupBox(self.bakingTab)
        self.gbPreBake.setObjectName(u"gbPreBake")
        self.gbPreBake.setFlat(False)
        self.gridLayout_7 = QGridLayout(self.gbPreBake)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lbNote = QLabel(self.gbPreBake)
        self.lbNote.setObjectName(u"lbNote")

        self.gridLayout_7.addWidget(self.lbNote, 0, 0, 1, 2)


        self.horizontalLayout_6.addWidget(self.gbPreBake)


        self.gridLayout_6.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cbbBakeAO = QCheckBox(self.bakingTab)
        self.cbbBakeAO.setObjectName(u"cbbBakeAO")

        self.horizontalLayout_8.addWidget(self.cbbBakeAO)

        self.cbbBakeCurvature = QCheckBox(self.bakingTab)
        self.cbbBakeCurvature.setObjectName(u"cbbBakeCurvature")

        self.horizontalLayout_8.addWidget(self.cbbBakeCurvature)

        self.cbbBakeWorldSpaceNormal = QCheckBox(self.bakingTab)
        self.cbbBakeWorldSpaceNormal.setObjectName(u"cbbBakeWorldSpaceNormal")

        self.horizontalLayout_8.addWidget(self.cbbBakeWorldSpaceNormal)

        self.cbbBakePosition = QCheckBox(self.bakingTab)
        self.cbbBakePosition.setObjectName(u"cbbBakePosition")

        self.horizontalLayout_8.addWidget(self.cbbBakePosition)

        self.cbbBakeColorID = QCheckBox(self.bakingTab)
        self.cbbBakeColorID.setObjectName(u"cbbBakeColorID")

        self.horizontalLayout_8.addWidget(self.cbbBakeColorID)


        self.gridLayout_6.addLayout(self.horizontalLayout_8, 6, 0, 1, 1)

        self.line = QFrame(self.bakingTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_6.addWidget(self.line, 8, 0, 1, 1)

        self.twSwitchingTab.addTab(self.bakingTab, "")
        self.materialCreationTab = QWidget()
        self.materialCreationTab.setObjectName(u"materialCreationTab")
        self.gridLayout_5 = QGridLayout(self.materialCreationTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.btnRefresh = QPushButton(self.materialCreationTab)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.btnRefresh, 1, 1, 1, 1)

        self.lwObjectSBSARMatList = QListWidget(self.materialCreationTab)
        self.lwObjectSBSARMatList.setObjectName(u"lwObjectSBSARMatList")
        self.lwObjectSBSARMatList.setMaximumSize(QSize(16777215, 16777215))
        self.lwObjectSBSARMatList.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.lwObjectSBSARMatList.setIconSize(QSize(128, 128))

        self.gridLayout_8.addWidget(self.lwObjectSBSARMatList, 1, 0, 1, 1)

        self.lwObjectSBSARWeatherEffectList = QListWidget(self.materialCreationTab)
        self.lwObjectSBSARWeatherEffectList.setObjectName(u"lwObjectSBSARWeatherEffectList")
        self.lwObjectSBSARWeatherEffectList.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.lwObjectSBSARWeatherEffectList.setIconSize(QSize(128, 128))
        self.lwObjectSBSARWeatherEffectList.setMovement(QListView.Static)
        self.lwObjectSBSARWeatherEffectList.setFlow(QListView.TopToBottom)
        self.lwObjectSBSARWeatherEffectList.setProperty("isWrapping", False)
        self.lwObjectSBSARWeatherEffectList.setResizeMode(QListView.Fixed)
        self.lwObjectSBSARWeatherEffectList.setViewMode(QListView.ListMode)

        self.gridLayout_8.addWidget(self.lwObjectSBSARWeatherEffectList, 1, 2, 1, 1)

        self.lbAssignedMaterials = QLabel(self.materialCreationTab)
        self.lbAssignedMaterials.setObjectName(u"lbAssignedMaterials")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbAssignedMaterials.setFont(font1)
        self.lbAssignedMaterials.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.lbAssignedMaterials.setFrameShape(QFrame.StyledPanel)
        self.lbAssignedMaterials.setFrameShadow(QFrame.Plain)
        self.lbAssignedMaterials.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lbAssignedMaterials, 0, 0, 1, 1)

        self.lbAssignedWeatherEffects = QLabel(self.materialCreationTab)
        self.lbAssignedWeatherEffects.setObjectName(u"lbAssignedWeatherEffects")
        self.lbAssignedWeatherEffects.setFont(font1)
        self.lbAssignedWeatherEffects.setStyleSheet(u"background-color: rgb(170, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.lbAssignedWeatherEffects.setFrameShape(QFrame.StyledPanel)
        self.lbAssignedWeatherEffects.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lbAssignedWeatherEffects, 0, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_8, 2, 0, 1, 2)

        self.gbMatLibrary = QGroupBox(self.materialCreationTab)
        self.gbMatLibrary.setObjectName(u"gbMatLibrary")
        font2 = QFont()
        font2.setPointSize(10)
        self.gbMatLibrary.setFont(font2)
        self.gbMatLibrary.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.gbMatLibrary)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.gbMaterials = QGroupBox(self.gbMatLibrary)
        self.gbMaterials.setObjectName(u"gbMaterials")
        self.gbMaterials.setAutoFillBackground(False)
        self.gbMaterials.setStyleSheet(u"")
        self.gbMaterials.setFlat(False)
        self.gbMaterials.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.gbMaterials)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cbbMaterials = QComboBox(self.gbMaterials)
        self.cbbMaterials.setObjectName(u"cbbMaterials")

        self.verticalLayout_2.addWidget(self.cbbMaterials)

        self.btnCreateMat = QPushButton(self.gbMaterials)
        self.btnCreateMat.setObjectName(u"btnCreateMat")
        self.btnCreateMat.setMinimumSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btnCreateMat)


        self.gridLayout_3.addWidget(self.gbMaterials, 3, 0, 1, 1)

        self.gbWeatherEffects = QGroupBox(self.gbMatLibrary)
        self.gbWeatherEffects.setObjectName(u"gbWeatherEffects")
        self.gridLayout = QGridLayout(self.gbWeatherEffects)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnAssignWeatherEffects = QPushButton(self.gbWeatherEffects)
        self.btnAssignWeatherEffects.setObjectName(u"btnAssignWeatherEffects")
        self.btnAssignWeatherEffects.setMinimumSize(QSize(50, 50))

        self.gridLayout.addWidget(self.btnAssignWeatherEffects, 1, 0, 1, 1)

        self.cbbWeatherEffects = QComboBox(self.gbWeatherEffects)
        self.cbbWeatherEffects.setObjectName(u"cbbWeatherEffects")

        self.gridLayout.addWidget(self.cbbWeatherEffects, 0, 0, 1, 1)

        self.btnRemoveWeatherEffects = QPushButton(self.gbWeatherEffects)
        self.btnRemoveWeatherEffects.setObjectName(u"btnRemoveWeatherEffects")
        self.btnRemoveWeatherEffects.setMinimumSize(QSize(50, 50))

        self.gridLayout.addWidget(self.btnRemoveWeatherEffects, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gbWeatherEffects, 4, 0, 1, 1)


        self.gridLayout_5.addWidget(self.gbMatLibrary, 0, 0, 1, 1)

        self.lwThumbnailMatShowing = QListWidget(self.materialCreationTab)
        self.lwThumbnailMatShowing.setObjectName(u"lwThumbnailMatShowing")
        self.lwThumbnailMatShowing.setDragDropMode(QAbstractItemView.DragDrop)
        self.lwThumbnailMatShowing.setIconSize(QSize(128, 128))
        self.lwThumbnailMatShowing.setResizeMode(QListView.Adjust)
        self.lwThumbnailMatShowing.setSpacing(0)
        self.lwThumbnailMatShowing.setViewMode(QListView.IconMode)

        self.gridLayout_5.addWidget(self.lwThumbnailMatShowing, 0, 1, 1, 1)

        self.lbAddedMaterials = QLabel(self.materialCreationTab)
        self.lbAddedMaterials.setObjectName(u"lbAddedMaterials")
        self.lbAddedMaterials.setFont(font)
        self.lbAddedMaterials.setStyleSheet(u"background-color: rgb(170, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.lbAddedMaterials.setFrameShape(QFrame.Box)
        self.lbAddedMaterials.setFrameShadow(QFrame.Raised)
        self.lbAddedMaterials.setLineWidth(2)
        self.lbAddedMaterials.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lbAddedMaterials, 1, 0, 1, 2)

        self.twSwitchingTab.addTab(self.materialCreationTab, "")

        self.gridLayout_2.addWidget(self.twSwitchingTab, 1, 0, 1, 2)

        SBSARMatCreationMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SBSARMatCreationMainWindow)

        self.twSwitchingTab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SBSARMatCreationMainWindow)
    # setupUi

    def retranslateUi(self, SBSARMatCreationMainWindow):
        SBSARMatCreationMainWindow.setWindowTitle(QCoreApplication.translate("SBSARMatCreationMainWindow", u"SBS Material Main Window", None))
        self.lbBakingSettings.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Substance Automation Tools", None))
        self.lbAntiAlias.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Anti-Alias", None))
        self.lbUvSet.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"UV Set", None))
        self.lbInputPath.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Input Path", None))
        self.cbbUseUpperSettings.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Use Upper Settings ?", None))
        self.lbInputName.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Input Name", None))
        self.lbWidth.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Width", None))
        self.lbHeight.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Height", None))
        self.lbFormat.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Format", None))
        self.leNormalMap.setPlaceholderText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Load Normal Map", None))
        self.btnBrowseNormalMap.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Browse", None))
        self.cbUseLowAsHigh.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Use Low As High?", None))
        self.btnBakeMeshMaps.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"CLICK TO BAKE SELECTION!!!", None))
        self.btnCreateFileSBS.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"CREATE FILE SBS !!!", None))
        self.lbOutputPath.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Output Path", None))
        self.btnBrowse.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Browse", None))
        self.lbOutputName.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Output Name", None))
        self.gbPreBake.setTitle(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Pre-Baking", None))
        self.lbNote.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"If you have a low and high poly. Please select bake normal. High poly meshes should be put in HighPoly group\n"
"low poly meshes should be put in LowPoly group", None))
        self.cbbBakeAO.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Bake AO", None))
        self.cbbBakeCurvature.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Bake Curvature", None))
        self.cbbBakeWorldSpaceNormal.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Bake World Space Normal", None))
        self.cbbBakePosition.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Bake Position", None))
        self.cbbBakeColorID.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Bake Color ID", None))
        self.twSwitchingTab.setTabText(self.twSwitchingTab.indexOf(self.bakingTab), QCoreApplication.translate("SBSARMatCreationMainWindow", u"Mesh Baking", None))
        self.btnRefresh.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Refresh", None))
        self.lbAssignedMaterials.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Assigned Materials", None))
        self.lbAssignedWeatherEffects.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Assigned Weather Effects", None))
        self.gbMatLibrary.setTitle(QCoreApplication.translate("SBSARMatCreationMainWindow", u"SUBSTANCE MATERIAL LIBRARY", None))
        self.gbMaterials.setTitle(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Materials", None))
        self.btnCreateMat.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Click to Create and\n"
" Assign To Selection", None))
        self.gbWeatherEffects.setTitle(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Weather Effects", None))
        self.btnAssignWeatherEffects.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Click to Add", None))
        self.btnRemoveWeatherEffects.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Click to Remove\n"
"From Selection", None))
        self.lbAddedMaterials.setText(QCoreApplication.translate("SBSARMatCreationMainWindow", u"Substance Materials Of Selected Objects", None))
        self.twSwitchingTab.setTabText(self.twSwitchingTab.indexOf(self.materialCreationTab), QCoreApplication.translate("SBSARMatCreationMainWindow", u"Material Creation", None))
    # retranslateUi

