import sys
import os
import importlib
try:
	import maya.cmds as cmds
	from PySide2 import QtGui, QtCore, QtWidgets
	from PySide2.QtUiTools import QUiLoader
	import maya.OpenMayaUI as omui
	from shiboken2 import wrapInstance
except:
	pass
	
mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)

class GlobalMainVariables:
	def __init__(self):
		currentFilePath = os.path.dirname(os.path.abspath(__file__))
		currentFilePath = currentFilePath.replace("\\","/")
		currentFilePath = ("/".join(currentFilePath.split("/")[:-1]))
		self.mainPath = currentFilePath
		self.mainUIPath = self.mainPath + "/ui/TransferTransformation_UI.ui"
		self.mainFunctionPath = self.mainPath + "/function"
		
GlobalMainVariables = GlobalMainVariables()
sys.path.append(GlobalMainVariables.mainPath)
from puzzle_maya.transfer_transformation.function import Transfer_Transformation_Data as ttd

from puzzle_maya.transfer_transformation.function import MayaProcessHook as mph2
importlib.reload(mph2)
from puzzle_maya.transfer_transformation.function import socket_startup as ss
importlib.reload(ss)
from puzzle_maya.transfer_transformation.ui import TransferTransformation_UI as tt_ui
importlib.reload(tt_ui)

class MainTransferTransform(QtWidgets.QMainWindow, tt_ui.Ui_MainWindow):
	def __init__(self):
		super(MainTransferTransform, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.transferTransformFunction = ttd.TransferTransformFunction()
		self.transferTransformGlobalVariables = ttd.GlobalTransferAnimVariables
		self.PortFunction = mph2.PortFunction()
		self.socketStartup = ss.HookMainFunction()
		self.connectUI()
		self.updateTransformationDataToListWidget()
		self.checkPortStatus()
		#self.closeEvent = doSomething
		
	def closeEvent(self, event):
		#super(MainTransferTransform, self).closeEvent(event)
		self.socketStartup.shutdownSocket()

	def connectUI(self):
		self.btnExportTransformData.clicked.connect(lambda: self.printDataToJsonFile())
		self.btnImportTransformData.clicked.connect(lambda: self.readFileJson())
		self.btnOpenPort.clicked.connect(lambda: self.openOrClosePort())
		self.btnStartServerHook.clicked.connect(lambda: self.startHook())
		self.btnDeleteTransformationData.clicked.connect(lambda: self.deleteSelectedTransformationData())
		self.btnUpdateSelectionTransformation.clicked.connect(lambda: self.updateTransformationThroughButton())
		
	def updateTransformationDataToListWidget(self):
		self.listTransformationData.clear()
		self.allJsonFile = []
		for jsonFile in os.listdir(self.transferTransformGlobalVariables.jsonPath):
			if os.path.isfile(self.transferTransformGlobalVariables.jsonPath + "/" + jsonFile) and ".json" in jsonFile:
				self.allJsonFile.append(jsonFile)
		self.listTransformationData.addItems(self.allJsonFile)
		
	def checkPortStatus(self):
		if self.PortFunction.checkPortStatus():
			self.setOpenPortStatus()
		else:
			self.setClosePortStatus()
								 
		
	def printDataToJsonFile(self):
		self.transferTransformFunction.printDataToJsonFile()
		self.updateTransformationDataToListWidget()
		
	def readFileJson(self):
		combinedMissingObjects = []
		for jsonFile in self.listTransformationData.selectedItems():
			fullJsonFilePath = self.transferTransformGlobalVariables.jsonPath + "/" + jsonFile.text()
			missingObject = self.transferTransformFunction.readFileJson(fullJsonFilePath)
			if missingObject != True:
				combinedMissingObjects = combinedMissingObjects + missingObject
		if combinedMissingObjects:
			self.listMissingObjects.clear()
			self.listMissingObjects.addItems(combinedMissingObjects)
		else:
			self.listMissingObjects.clear()
		
	def updateTransformationThroughButton(self):
		if self.status:
			self.socketStartup.updateTransformationThroughButtonFunction()
		
	def startHook(self):
		self.status = self.socketStartup.startHook()
		if self.status:
			self.setStartHookStatus()
		
		
	def setOpenPortStatus(self):
		self.btnOpenPort.setStyleSheet("background-color: rgb(0, 186, 0);\nborder-width:0 px;")
		self.btnOpenPort.setText("Port status: OPENING!")

	def setClosePortStatus(self):
		self.btnOpenPort.setStyleSheet("background-color: rgb(186, 0, 0);\nborder-width:0 px;")
		self.btnOpenPort.setText("Port status: CLOSING!") 	   
			
	def openOrClosePort(self):
		if self.PortFunction.checkPortStatus():
			self.PortFunction.closePort()
			self.setClosePortStatus()
		else:
			self.PortFunction.openPort()
			self.setOpenPortStatus()
			
	def checkStartHookStatus(self):
		if self.btnStartServerHook.isEnabled() == True:
			return True
		else:
			return False
	
	def setStartHookStatus(self):
		self.btnStartServerHook.setStyleSheet("background-color: rgb(186, 0, 0);\nborder-width:0 px;")
		self.btnStartServerHook.setText("This Maya is chosen for main working!")
		self.btnStartServerHook.setEnabled(False)
		self.btnOpenPort.setEnabled(False)
			
	def deleteSelectedTransformationData(self):
		for jsonFile in self.listTransformationData.selectedItems():
			fullJsonFilePath = self.transferTransformGlobalVariables.jsonPath + "/" + jsonFile.text()
			os.remove(fullJsonFilePath)
		self.updateTransformationDataToListWidget()

def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)


#check_exist_window("ExporterAddID")
check_exist_window("MainWindow")
mainTransferTransform = MainTransferTransform()
mainTransferTransform.show()