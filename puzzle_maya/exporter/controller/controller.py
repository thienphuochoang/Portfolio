import sys
import os
from functools import partial
import importlib
try:
	from PySide2 import QtGui, QtCore, QtWidgets
	from PySide2 import __version__
	from PySide2.QtUiTools import QUiLoader
	from shiboken2 import wrapInstance
except ImportError:
	from PySide import QtGui, QtCore
	import PySide.QtGui as QtWidgets
	from PySide import __version__
	from PySide.QtUiTools import QUiLoader
	from shiboken import wrapInstance


import maya.OpenMayaUI as omui
import maya.mel as mel
import maya.cmds as cmds


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
exporter_func = importerFunction.importModule("puzzle_maya.exporter.function.exporter_function")
exporter_func.createTempFolder()
exporter_mainUI = importerFunction.importModule("lib.ui.Exporter_MainUI")

def import_add_id_ui():
	pass


class MainExporter(QtWidgets.QMainWindow, exporter_mainUI.Ui_MainWindowExporter):
	def __init__(self):
		super(MainExporter, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.changeSelfRadioButtonText()
		self.connectUI()
		self.disableWorkingFilesExportButtons()


	def connectUI(self):
		self.btnExport.clicked.connect(
			lambda: exporter_func.exportFile(
				self.queryRadioButtonStatus(), 
				self.queryCheckboxBinaryStatus(), 
				self.queryCheckboxInstanceStatus()))
		self.btnImport.clicked.connect(
			lambda: exporter_func.importFile(
				self.queryRadioButtonStatus(), 
				self.queryCheckboxLockNormalStatus(), 
				self.queryCheckboxGroup()))
		self.btnAddID.clicked.connect(lambda: import_add_id_ui())

		self.btnFixMaterial.clicked.connect(
			partial(exporter_func.replaceMaterials))
		self.btnExportWorking.clicked.connect(
			lambda: exporter_func.exportWorkingFiles(
				self.queryRadioButtonStatus(), 
				self.queryCheckboxBinaryStatus(), 
				self.queryCheckboxInstanceStatus()))
		self.btnImportWorking.clicked.connect(
			lambda: exporter_func.importWorkingFiles(
				self.queryRadioButtonStatus(), 
				self.queryCheckboxLockNormalStatus(), 
				self.queryCheckboxGroup()))
		self.btnExportHigh.clicked.connect(
			partial(exporter_func.exportHighPoly))
		self.btnExportLow.clicked.connect(
			partial(exporter_func.exportLowPoly))
		self.btnExportSeparatePart.clicked.connect(
			lambda: exporter_func.exportSeparatePart(
				self.queryRadioButtonStatus(), 
				self.queryCheckboxBinaryStatus(), 
				self.queryCheckboxInstanceStatus()))
		self.btnOpenFolder.clicked.connect(
			partial(exporter_func.openTempFolder))
		self.btnDeleteFolder.clicked.connect(
			partial(exporter_func.deleteTempFolderContents))
		self.btnExportSP.clicked.connect(
			partial(exporter_func.exportToSubstancePainter))
		self.btnExportCurrentFolder.clicked.connect(
			lambda: exporter_func.exportFileToCurrentFolder(
				self.queryRadioButtonStatus(), 
				self.queryCheckboxBinaryStatus(), 
				self.queryCheckboxInstanceStatus()))
		self.btnExportToUnity.clicked.connect(
			lambda: exporter_func.exportToUnity())

		
	def changeSelfRadioButtonText(self):
		self.rbSelf.setText("MA")


	def queryRadioButtonStatus(self):
		rbFBX = self.rbFBX.isChecked()
		rbObjStatus = self.rbObj.isChecked()
		rbSelfStatus = self.rbSelf.isChecked()
		if rbFBX:
			return "FBX"
		elif rbObjStatus:
			return "OBJ"
		elif rbSelfStatus:
			return "Self"

		
	def queryKeepIDStatus(self):
		cbKeepID = self.cbKeepID.isChecked()
		if cbKeepID:
			return "On"
		else:
			return "Off"

		
	def queryCheckboxBinaryStatus(self):
		cbBinaryStatus = self.cbBinary.isChecked()
		if cbBinaryStatus:
			return "false"
		else:
			return "true"


	def queryCheckboxInstanceStatus(self):
		cbKeepInstanceStatus = self.cbKeepInstance.isChecked()
		if cbKeepInstanceStatus:
			return "true"
		else:
			return "false"


	def queryCheckboxLockNormalStatus(self):
		cbKeepLockVertexNormalStatus = self.cbKeepVertexNormal.isChecked()
		if cbKeepLockVertexNormalStatus:
			return "false"
		else:
			return "true"


	def queryCheckboxGroup(self):
		cbKeepGroup = self.cbKeepGroup.isChecked()
		if cbKeepGroup:
			return "true"
		else:
			return "false"

	def disableWorkingFilesExportButtons(self):
		self.btnImportWorking.setEnabled(False)
		self.btnExportWorking.setEnabled(False)

def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)


#check_exist_window("ExporterAddID")
check_exist_window("MainWindowExporter")
winExporter = MainExporter()
winExporter.show()