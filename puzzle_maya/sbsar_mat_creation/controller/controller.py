import importlib
import PySide2
from PySide2 import QtGui, QtCore, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import sys

mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)  # create a maya Main window

moduleImporterPath = 'general.modules_importer.modules_importer_function'
importerFunction = None

if moduleImporterPath in sys.modules:
	importerFunction = sys.modules[moduleImporterPath]
	try:
		importlib.reload(importerFunction)
	except:
		reload(importerFunction)
else:
	importerFunction = importlib.import_module(moduleImporterPath)
	
#import Function____________________
mat_creation_function = importerFunction.importModule("puzzle_maya.sbsar_mat_creation.function.mat_creation_function")
sbsbaker_baking_function = importerFunction.importModule("puzzle_maya.sbsar_mat_creation.function.sbsbaker_baking_function")
mat_creation_mainUI = importerFunction.importModule("puzzle_maya.sbsar_mat_creation.ui.sbsar_mat_creation_ui")
assigned_sbsar_mat_object_mainUI = importerFunction.importModule("puzzle_maya.sbsar_mat_creation.ui.assigned_sbsar_mat_object_ui")
pysbs_creation_workflow_function = importerFunction.importModule("puzzle_maya.sbsar_mat_creation.function.pysbs_creation_workflow_function")

class AssignedSBSARMatObjectMainWindow(QtWidgets.QWidget, assigned_sbsar_mat_object_mainUI.Ui_widgetAssignedMat):
	def __init__(self):
		super(AssignedSBSARMatObjectMainWindow, self).__init__(parent = None)
		self.setupUi(self)
		self.matCreationFunctionInstance = mat_creation_function.MatCreationFunction()
		self.disabledDragFunction()
		

	def changeAssetName(self, meshName):
		self.lbObjectName.setText(meshName)

	def setMatInListWidget(self, imageList, lwAssignedSBSARMat):
		self.matCreationFunctionInstance.setMatInListWidget(imageList, lwAssignedSBSARMat)

	def disabledDragFunction(self):
		self.lwAssignedSBSARMat.setDragEnabled(False)

class sbsarMatCreationMainWindow(QtWidgets.QMainWindow, mat_creation_mainUI.Ui_SBSARMatCreationMainWindow):
	def __init__(self):
		super(sbsarMatCreationMainWindow, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.matCreationFunctionInstance = mat_creation_function.MatCreationFunction()
		self.sbsbakerBakingFunctionInstance = sbsbaker_baking_function.SBSBakerBakingFunction()
		self.pysbsCreationWorkflowFunctionInstance = pysbs_creation_workflow_function.PYSBSCreationWorkflowFunction()

		# Add function into button
		self.connectUI()

		
		# Add data into combo box and setup default settings
		self.disableDragAndDropModeForListWidget()
		self.addResolutionComboBox()
		self.addFormatComboBox()
		self.addAntiAliasComboBox()
		self.addUvSetComboBox()
		self.addMaterialTypesToComboBox()
		self.addWeatherEffectsToComboBox()
		self.refreshMatInListWidget(self.lwObjectSBSARMatList, AssignedSBSARMatObjectMainWindow)
		self.refreshWeatherMatInListWidget(self.lwObjectSBSARWeatherEffectList, AssignedSBSARMatObjectMainWindow)
		self.disableNormalPathWhenCheckedUseLowAsHigh(self.cbUseLowAsHigh.isChecked(), self.leNormalMap, self.btnBrowseNormalMap)



	def connectUI(self):
		self.btnBrowse.clicked.connect(lambda: self.setOutputPath())

		self.btnBakeMeshMaps.clicked.connect(lambda: self.bakeSelectedMesh(self.queryBakeTypeStatus(),
											self.cbbWidth.currentText(),
											self.cbbHeight.currentText(),
											self.cbbAntiAlias.currentIndex(),
											self.cbbUvSet.currentText(),
											self.cbbFormat.currentText(),
											self.leNormalMap.text(),
											self.cbUseLowAsHigh.isChecked(),
											self.leOutputName.text(),
											self.leOutputPath.text()))

		self.cbUseLowAsHigh.stateChanged.connect(lambda: self.disableNormalPathWhenCheckedUseLowAsHigh(self.cbUseLowAsHigh.isChecked(), 
												self.leNormalMap,
												self.btnBrowseNormalMap))

		self.btnBrowseNormalMap.clicked.connect(lambda: self.browseNormalMap())

		self.cbbMaterials.currentIndexChanged.connect(lambda: self.showImageInListWidget(self.cbbMaterials.currentText(),
													self.lwThumbnailMatShowing))

		self.btnCreateMat.clicked.connect(lambda: self.createMat(self.lwThumbnailMatShowing.selectedItems()))

		self.btnAssignWeatherEffects.clicked.connect(lambda: self.refreshWeatherEffectsInListWidget(self.cbbWeatherEffects))

		self.btnRefresh.clicked.connect(lambda: self.refreshBothMatInListWidget(self.lwObjectSBSARMatList, AssignedSBSARMatObjectMainWindow, self.lwObjectSBSARWeatherEffectList))

		self.cbbUseUpperSettings.stateChanged.connect(lambda: self.setInputsForFileSBSCreation(self.cbbUseUpperSettings,
														self.leInputPath,
														self.leInputName,
														self.leOutputPath,
														self.leOutputName))

		self.btnCreateFileSBS.clicked.connect(lambda: self.cookSBSAndCreateSubstanceNodeAndAssignToStingRayPBS(self.leInputPath.text(),
												self.leInputName.text(),
												self.cbbFormat.currentText(),
												self.cbbWidth.currentText(),
												self.cbbHeight.currentText(),
												self.getAllAssignedWeatherEffectsFromSelection()))

		self.btnRemoveWeatherEffects.clicked.connect(lambda: self.removeWeatherEffectFromMesh(self.cbbWeatherEffects, self.lwObjectSBSARWeatherEffectList, AssignedSBSARMatObjectMainWindow))

		self.btnConnectSubstanceNodeAndMaterial.clicked.connect(lambda: self.connectNodeAndMat())

	def getFullOutputPath(self):
		fullOutputPath = self.sbsbakerBakingFunctionInstance.getFullOutputPath()
		return fullOutputPath

	def setOutputPath(self):
		fullOutputPath = self.getFullOutputPath()
		self.leOutputPath.setText(fullOutputPath.replace("/","\\"))

	def queryBakeTypeStatus(self):
		statusList = []
		#isBakeNormal = self.cbbBakeNormal.isChecked()
		isBakeAO = self.cbbBakeAO.isChecked()
		isBakeCurvature = self.cbbBakeCurvature.isChecked()
		isBakeWorldSpaceNormal = self.cbbBakeWorldSpaceNormal.isChecked()
		isBakePosition = self.cbbBakePosition.isChecked()
		isBakeColorID = self.cbbBakeColorID.isChecked()
		#statusList.append(isBakeNormal)
		statusList.append(isBakeAO)
		statusList.append(isBakeCurvature)
		statusList.append(isBakeWorldSpaceNormal)
		statusList.append(isBakePosition)
		statusList.append(isBakeColorID)
		return statusList

	def bakeSelectedMesh(self, *args):
		if self.leOutputPath.text() != "" and self.leOutputName.text() != "":
			self.sbsbakerBakingFunctionInstance.bakeSelectedMesh(*args)
		else:
			cmds.confirmDialog(title='Missing Output', message='Output path or output name is empty. Please check again.', icon="critical")

	def setInputsForFileSBSCreation(self, cbbUseUpperSettings, leInputPath, leInputName, leOutputPath, leOutputName):
		self.pysbsCreationWorkflowFunctionInstance.setInputsForFileSBSCreation(cbbUseUpperSettings, leInputPath, leInputName, leOutputPath, leOutputName)

	def disableDragAndDropModeForListWidget(self):
		self.lwThumbnailMatShowing.setDragEnabled(False)
		self.lwObjectSBSARMatList.setDragEnabled(False)
		self.lwObjectSBSARWeatherEffectList.setDragEnabled(False)

	def addResolutionComboBox(self):
		resolutionList = ["128","256","512","1024","2048","4096"]
		self.cbbWidth.addItems(resolutionList)
		self.cbbHeight.addItems(resolutionList)
		self.cbbWidth.setCurrentText("1024")
		self.cbbHeight.setCurrentText("1024")

	def addFormatComboBox(self):
		formatList = ["png", "tga", "jpg", "tif", "dds"]
		self.cbbFormat.addItems(formatList)

	def addAntiAliasComboBox(self):
		antiAliasList = ['None', 'Subsampling 2x2', 'Subsampling 4x4', 'Subsampling 8x8']
		self.cbbAntiAlias.addItems(antiAliasList)
		self.cbbAntiAlias.setCurrentText('Subsampling 8x8')

	def addUvSetComboBox(self):
		uvSetList = ["1", "2", "3", "4", "5"]
		self.cbbUvSet.addItems(uvSetList)

	def disableNormalPathWhenCheckedUseLowAsHigh(self, useLowAsHighButtonStatus, normalPath, browseButton):
		self.sbsbakerBakingFunctionInstance.disableNormalPathWhenCheckedUseLowAsHigh(useLowAsHighButtonStatus, normalPath, browseButton)

	def browseNormalMap(self):
		normalPath = self.sbsbakerBakingFunctionInstance.browseNormalMap()
		self.leNormalMap.setText(normalPath)

	def addMaterialTypesToComboBox(self):
		materialTypesList = ["materials"]
		self.cbbMaterials.addItems(materialTypesList)

	def showImageInListWidget(self, currentSelectedMaterialType, thumbnailListWidget):
		self.matCreationFunctionInstance.showImageInListWidget(currentSelectedMaterialType, thumbnailListWidget)

	def addWeatherEffectsToComboBox(self):
		weatherEffectItemList = self.matCreationFunctionInstance.addWeatherEffectsToComboBox()
		self.cbbWeatherEffects.addItems(weatherEffectItemList)

	def createMat(self, currentSelectedMaterial):
		self.matCreationFunctionInstance.createMat(currentSelectedMaterial)
		self.refreshMatInListWidget(self.lwObjectSBSARMatList, AssignedSBSARMatObjectMainWindow)

	def connectNodeAndMat(self):
		self.matCreationFunctionInstance.connectNodeAndMat()

	def refreshMatInListWidget(self, lwObjectSBSARMatList, sbsarMatObjectClass):
		self.lwObjectSBSARMatList.clear()
		self.matCreationFunctionInstance.refreshMatInListWidget(lwObjectSBSARMatList, sbsarMatObjectClass)

	def refreshWeatherMatInListWidget(self, lwObjectSBSARWeatherEffectList, sbsarMatObjectClass):
		self.lwObjectSBSARWeatherEffectList.clear()
		self.matCreationFunctionInstance.refreshWeatherMatInListWidget(lwObjectSBSARWeatherEffectList, sbsarMatObjectClass)

	def refreshBothMatInListWidget(self, lwObjectSBSARMatList, sbsarMatObjectClass, lwObjectSBSARWeatherEffectList):
		self.refreshMatInListWidget(lwObjectSBSARMatList, sbsarMatObjectClass)
		self.refreshWeatherMatInListWidget(lwObjectSBSARWeatherEffectList, sbsarMatObjectClass)

	def refreshWeatherEffectsInListWidget(self, cbbWeatherEffects):
		self.matCreationFunctionInstance.refreshWeatherEffectsInListWidget(cbbWeatherEffects)
		self.refreshWeatherMatInListWidget(self.lwObjectSBSARWeatherEffectList, AssignedSBSARMatObjectMainWindow)

	def cookSBS(self, *args):
		self.pysbsCreationWorkflowFunctionInstance.getInputsForFileSBSCreation(*args)
		sbsDestination = self.pysbsCreationWorkflowFunctionInstance.cookSBS(*args)
		return sbsDestination

	def createSubstanceNodeAndAssignToStingRayPBS(self, sbsDestination, fileFormat, width, height):
		self.matCreationFunctionInstance.createSubstanceNodeAndAssignToStingRayPBS(sbsDestination, fileFormat, width, height)

	def cookSBSAndCreateSubstanceNodeAndAssignToStingRayPBS(self, *args):
		sbsDestination = self.cookSBS(*args)
		fileFormat = args[2]
		width = args[3]
		height = args[4]
		self.createSubstanceNodeAndAssignToStingRayPBS(sbsDestination, fileFormat, width, height)

	def getAllAssignedWeatherEffectsFromSelection(self):
		meshAndAssignedWeatherEffectsDict = self.matCreationFunctionInstance.getAllAssignedWeatherEffectsFromSelection()
		return meshAndAssignedWeatherEffectsDict

	def removeWeatherEffectFromMesh(self, cbbWeatherEffects, lwObjectSBSARWeatherEffectList, sbsarMatObjectClass):
		self.matCreationFunctionInstance.removeWeatherEffectFromSelection(cbbWeatherEffects)
		self.refreshWeatherMatInListWidget(lwObjectSBSARWeatherEffectList, sbsarMatObjectClass)


def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)


check_exist_window("SBSARMatCreationMainWindow")
winMat = sbsarMatCreationMainWindow()
winMat.show()







