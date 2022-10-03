try:
	from PySide2 import QtGui, QtCore, QtWidgets
	from PySide2.QtCore import QFile, QObject, QSize
	from PySide2.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QPushButton, QFileDialog, QStyleFactory, QMessageBox, QMainWindow, QDialog
except ImportError:
	from PySide import QtGui, QtCore
	from PySide.QtCore import QFile, QObject, QSize
	from PySide.QtGui import QWidget, QVBoxLayout, QSizePolicy, QPushButton, QFileDialog, QStyleFactory, QMessageBox, QMainWindow, QDialog
	from PySide.QtGui import QIcon
	import PySide.QtGui as QtWidgets

import sys
from functools import partial
import importlib
import pymxs
rt = pymxs.runtime
from qtmax import GetQMaxMainWindow
def import_file(str_module):
	"""import a module from string"""
	nameModule = importlib.import_module(str_module)
	try:
		importlib.reload(nameModule)
	except:
		reload(nameModule)
	return nameModule
	
#import Function____________________
eif = import_file(r"puzzle_max.exporter.function.exporter_function")
exporter_mainUI = import_file(r"lib.ui.Exporter_MainUI")

		
class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		#UIFile = QFile(ui_file)
		#UIFile.open(QFile.ReadOnly)
		#loader = QUiLoader()
		#self.window = loader.load(UIFile)
		#MaxPlus.AttachQWidgetToMax(self.window)
		self.window = exporter_mainUI.Ui_MainWindowExporter()
		self.window.setupUi(self)
		
		self.changeSelfRadioButtonText()
		self.setAddMatIDButtonVisibility()
		self.connectUI()
	
	def connectUI(self):
		self.window.btnExport.clicked.connect(lambda: eif.exportFileAndKeepID(self.queryKeepIDStatus(), self.queryRadioButtonStatus(), self.queryKeepVertexNormalStatus(), self.queryExportBinaryStatus(), self.queryKeepInstanceStatus()))
		self.window.btnImport.clicked.connect(lambda: eif.importFile(self.queryRadioButtonStatus(), self.queryKeepVertexNormalStatus(), self.queryKeepGroupStatus()))
		self.window.btnFixMaterial.clicked.connect(lambda: MatFixDialog())
		self.window.btnExportWorking.clicked.connect(lambda: eif.exportWorkingFiles(self.queryRadioButtonStatus(), self.queryKeepVertexNormalStatus(), self.queryExportBinaryStatus(), self.queryKeepInstanceStatus()))
		self.window.btnImportWorking.clicked.connect(lambda: eif.importWorkingFiles(self.queryRadioButtonStatus(), self.queryKeepVertexNormalStatus(), self.queryKeepGroupStatus()))
		self.window.btnExportHigh.clicked.connect(lambda: eif.exportHighPoly(self.queryKeepVertexNormalStatus()))
		self.window.btnExportLow.clicked.connect(lambda: eif.exportLowPoly(self.queryKeepVertexNormalStatus()))
		self.window.btnExportSeparatePart.clicked.connect(lambda: eif.exportSeparatePart(self.queryRadioButtonStatus(), self.queryKeepVertexNormalStatus()))
		self.window.btnOpenFolder.clicked.connect(partial(eif.openTempFolder))
		self.window.btnDeleteFolder.clicked.connect(partial(eif.deleteTempFolderContents))
		self.window.btnExportSP.clicked.connect(lambda: eif.exportToSubstancePainter(self.queryKeepVertexNormalStatus()))
		self.window.btnAddID.clicked.connect(lambda: eif.exportIgnoreScale(self.queryRadioButtonStatus(), self.queryKeepVertexNormalStatus(), self.queryExportBinaryStatus(), self.queryKeepInstanceStatus()))
		self.window.btnExportCurrentFolder.clicked.connect(lambda: eif.exportCurrentFolder())
		self.window.btnExportToUnity.clicked.connect(lambda: eif.exportToUnity())

	def changeSelfRadioButtonText(self):
		if rt.getFileVersion("$max/3dsmax.exe") != "":
			self.window.rbSelf.setText("Max")

			
	def setAddMatIDButtonVisibility(self):
		self.window.btnAddID.setText("Ignore Scale")
			
	def queryRadioButtonStatus(self):
		rbFBX = self.window.rbFBX.isChecked()
		rbObjStatus = self.window.rbObj.isChecked()
		rbSelfStatus = self.window.rbSelf.isChecked()
		if rbFBX:
			return "FBX"
		elif rbObjStatus:
			return "OBJ"
		elif rbSelfStatus:
			return "Self"

		
	def queryKeepIDStatus(self):
		cbKeepID = self.window.cbKeepID.isChecked()
		if cbKeepID:
			return "On"
		else:
			return "Off"

		
	def queryKeepVertexNormalStatus(self):
		cbKeepVertexNormal = self.window.cbKeepVertexNormal.isChecked()
		if cbKeepVertexNormal:
			return "On"
		else:
			return "Off"

			
	def queryExportBinaryStatus(self):
		cbBinary = self.window.cbBinary.isChecked()
		if cbBinary:
			return "On"
		else:
			return "Off"

			
	def queryKeepInstanceStatus(self):
		cbKeepInstance = self.window.cbKeepInstance.isChecked()
		if cbKeepInstance:
			return "On"
		else:
			return "Off"

			
	def queryKeepGroupStatus(self):
		cbKeepGroup = self.window.cbKeepGroup.isChecked()
		if cbKeepGroup:
			return "On"
		else:
			return "Off"
			
class MatFixDialog(QDialog):
	def __init__(self, parent=GetQMaxMainWindow()):
		super(MatFixDialog, self).__init__(parent)
		self.setWindowTitle("Fix Mat Dialog")
		self.fixMatbtn = QtWidgets.QPushButton("Fix Material ID")
		self.removeIDbtn = QtWidgets.QPushButton("Remove 'ID' Suffix")
		layout = QtWidgets.QHBoxLayout()
		layout.addWidget(self.fixMatbtn)
		layout.addWidget(self.removeIDbtn)
		self.setLayout(layout)
		self.fixMatbtn.clicked.connect(lambda: self.fixID())
		self.removeIDbtn.clicked.connect(lambda: self.removeIDSuffix())
		#MaxPlus.AttachQWidgetToMax(self)
		self.show()
	def fixID(self):
		eif.fixID()
	def removeIDSuffix(self):
		eif.removeIDSuffix()
		
try:
	openUI.close()
except:
	pass
	

openUI = MainWindow(GetQMaxMainWindow())
#MaxPlus.AttachQWidgetToMax(openUI)
openUI.show()
eif.createTempFolder()