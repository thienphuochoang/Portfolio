import sys
import os
import importlib
import PySide2
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide2 import QtGui, QtCore, QtWidgets
from shiboken2 import wrapInstance

# Create a maya Main window
mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)

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

tdf = importerFunction.importModule('puzzle_maya.uv_tool.texel_density.function.texel_density_function')
tdu = importerFunction.importModule('puzzle_maya.uv_tool.texel_density.ui.texel_density_ui')

class MainTexelDensity(QtWidgets.QMainWindow, tdu.Ui_TexelDensityMainWindow):
	def __init__(self):
		super(MainTexelDensity, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.texelDensityFunction = tdf.TexelDensityFunction()
		self.setupDefaultLayout()
		self.connectUI()

	def setupDefaultLayout(self):
		self.texelDensityFunction.setDefaultComboBoxValue(self.cbWidth)
		self.texelDensityFunction.setDefaultComboBoxValue(self.cbHeight)
		self.texelDensityFunction.setDefaultButtonIcon(self.btnCycleCheckerMap, self.btnReset, self.btnAssignCheckerMaterial)

	def connectUI(self):
		self.btnGet.clicked.connect(lambda: self.getTexelDensity(int(self.cbWidth.currentText()), int(self.cbHeight.currentText())))
		self.btnSet.clicked.connect(lambda: self.setTexelDensity(float(self.spnTexelDensity.text()),int(self.cbWidth.currentText()), int(self.cbHeight.currentText())))
		self.btnCycleCheckerMap.clicked.connect(lambda: self.cycleCheckerMap(cmds.ls(sl = True)))
		self.spnTilingU.valueChanged.connect(lambda: self.tilingCheckerMap(self.spnTilingU.text(), self.spnTilingV.text()))
		self.spnTilingV.valueChanged.connect(lambda: self.tilingCheckerMap(self.spnTilingU.text(), self.spnTilingV.text()))
		self.btnReset.clicked.connect(lambda: self.resetToOriginalMat())
		self.btnAssignCheckerMaterial.clicked.connect(lambda: self.assignCheckerMaterial(cmds.ls(sl = True)))

	def getTexelDensity(self, mapWidth, mapHeight):
		texelDensity = self.texelDensityFunction.getTexelDensity(mapWidth, mapHeight)
		if texelDensity != False:
			self.spnTexelDensity.setValue(texelDensity)
		else:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setWindowTitle("Error")
			msgBox.setText("Please select at least 1 faces")
			msgBox.exec_()

	def setTexelDensity(self, texelDensityInput, mapWidth, mapHeight):
		texelDensity = self.texelDensityFunction.setTexelDensity(texelDensityInput, mapWidth, mapHeight)
		if texelDensity == False:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setWindowTitle("Error")
			msgBox.setText("Please select at least 1 faces")
			msgBox.exec_()

	def resetToOriginalMat(self):
		self.texelDensityFunction.resetToOriginalMat()

	def cycleCheckerMap(self, selectionList):
		cycleCheckerMapResult = self.texelDensityFunction.cycleCheckerMap(selectionList)
		if cycleCheckerMapResult == False:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setWindowTitle("Error")
			msgBox.setText("Please select at least 1 object")
			msgBox.exec_()
		else:
			texturePath = self.texelDensityFunction.getCurrentCheckerMap()
			if texturePath != None:
				self.btnCycleCheckerMap.setIcon(QtGui.QIcon(texturePath))
				#self.btnCycleCheckerMap.setIconSize(QtCore.QSize(16,16))



	def tilingCheckerMap(self, tilingUValue, tilingVValue):
		self.texelDensityFunction.tilingCheckerMap(float(tilingUValue), float(tilingVValue))

	def assignCheckerMaterial(self, selectionList):
		checkerMaterialResult = self.texelDensityFunction.assignCheckerMaterial(selectionList)
		if checkerMaterialResult == None:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setWindowTitle("Error")
			msgBox.setText("Please select at least 1 object")
			msgBox.exec_()
		if checkerMaterialResult == False:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setWindowTitle("Error")
			msgBox.setText("Please set Rendering Engine to Direct X 11 then restart Maya")
			msgBox.exec_()

def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)

check_exist_window("TexelDensityMainWindow")
mainTexelDensityUI = MainTexelDensity()
mainTexelDensityUI.show()