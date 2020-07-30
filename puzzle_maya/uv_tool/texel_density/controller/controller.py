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
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)

from puzzle_maya.uv_tool.texel_density.function import texel_density_function as tdf
reload(tdf)
from puzzle_maya.uv_tool.texel_density.ui import texel_density_ui as tdu
reload(tdu)

class MainTexelDensity(QtWidgets.QMainWindow, tdu.Ui_TexelDensityMainWindow):
	def __init__(self):
		super(MainTexelDensity, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.texelDensityFunction = tdf.TexelDensityFunction()
		self.setupDefaultLayout()
		self.connectUI()

	def setupDefaultLayout(self):
		self.cbWidth.addItems(["128", "256", "512", "1024", "2048", "4096"])
		self.cbHeight.addItems(["128", "256", "512", "1024", "2048", "4096"])
		self.cbWidth.setCurrentText("512")
		self.cbHeight.setCurrentText("512")

	def connectUI(self):
		self.btnGet.clicked.connect(lambda: self.getTexelDensity(int(self.cbWidth.currentText()), int(self.cbHeight.currentText())))
		self.btnSet.clicked.connect(lambda: self.setTexelDensity(float(self.spnTexelDensity.text()),int(self.cbWidth.currentText()), int(self.cbHeight.currentText())))
		self.btnCycleCheckerMap.clicked.connect(lambda: self.cycleCheckerMap(cmds.ls(sl = True)))
		self.spnTilingU.valueChanged.connect(lambda: self.tilingCheckerMap(self.spnTilingU.text(), self.spnTilingV.text()))
		self.spnTilingV.valueChanged.connect(lambda: self.tilingCheckerMap(self.spnTilingU.text(), self.spnTilingV.text()))

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
		#self.btnCycleCheckerMap.setIcon(QtGui.QIcon('myImage.jpg'))
        #self.button.setIconSize(QtCore.QSize(24,24))


def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)

check_exist_window("TexelDensityMainWindow")
mainTexelDensityUI = MainTexelDensity()
mainTexelDensityUI.show()