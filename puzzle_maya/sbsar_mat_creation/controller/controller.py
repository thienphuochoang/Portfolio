import importlib
import PySide2
from PySide2 import QtGui, QtCore, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds
import sys

mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)  # create a maya Main window

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
mat_creation_mainUI = importerFunction.importModule("puzzle_maya.sbsar_mat_creation.ui.sbsar_mat_creation_ui")

class sbsarMatCreationMainWindow(QtWidgets.QMainWindow, mat_creation_mainUI.Ui_SBSARMatCreationMainWindow):
	def __init__(self):
		super(sbsarMatCreationMainWindow, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.matCreationFunctionInstance = mat_creation_function.MatCreationFunction()
		self.connectUI()
		self.addResolutionComboBox()
		self.addFormatComboBox()
		self.addAntiAliasComboBox()
		self.addUvSetComboBox()

	def connectUI(self):
		self.btnBrowse.clicked.connect(lambda: self.setOutputPath())
		self.btnBakeMeshMaps.clicked.connect(lambda: self.bakeSelectedMesh(self.queryBakeTypeStatus(),
											self.cbbWidth.currentText(),
											self.cbbHeight.currentText(),
											self.cbbAntiAlias.currentIndex(),
											self.cbbUvSet.currentText(),
											self.cbbFormat.currentText(),
											self.leNormalMap.text(),
											self.cbUseLowAsHigh.isChecked()))

	def getFullOutputPath(self):
		fullOutputPath = self.matCreationFunctionInstance.getFullOutputPath()
		return fullOutputPath

	def setOutputPath(self):
		fullOutputPath = self.getFullOutputPath()
		self.leOutputPath.setText(fullOutputPath.replace("/","\\"))

	def queryBakeTypeStatus(self):
		statusList = []
		isBakeAO = self.cbbBakeAO.isChecked()
		isBakeCurvature = self.cbbBakeCurvature.isChecked()
		isBakeWorldSpaceNormal = self.cbbBakeWorldSpaceNormal.isChecked()
		isBakePosition = self.cbbBakePosition.isChecked()
		isBakeColorID = self.cbbBakeColorID.isChecked()
		statusList.append(isBakeAO)
		statusList.append(isBakeCurvature)
		statusList.append(isBakeWorldSpaceNormal)
		statusList.append(isBakePosition)
		statusList.append(isBakeColorID)
		return statusList

	def exportFBXForInput(self):
		self.matCreationFunctionInstance.exportFBXForInput()

	def bakeSelectedMesh(self, *args):
		if self.leOutputPath.text() != "":
			self.matCreationFunctionInstance.bakeSelectedMesh(*args)
		else:
			cmds.confirmDialog(title='Missing Output Path', message='Output path is empty. Please check again.', icon="critical")

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

def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)


check_exist_window("SBSARMatCreationMainWindow")
winMat = sbsarMatCreationMainWindow()
winMat.show()







