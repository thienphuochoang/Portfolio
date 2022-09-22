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
edge_length_function = importerFunction.importModule("puzzle_maya.edge_length.function.edge_length_function")
edge_length_mainUI = importerFunction.importModule("puzzle_maya.edge_length.ui.edge_length_ui")

class EdgeLengthMainWindow(QtWidgets.QMainWindow, edge_length_mainUI.Ui_EdgeLengthMainWindow):
	def __init__(self):
		super(EdgeLengthMainWindow, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.edgeLengthFunctionInstance = edge_length_function.EdgeLengthFunction()
		self.connectUI()

	def selEdge(self, value):
		self.edgeLengthFunctionInstance.selEdge(value)

	def lengthToField(self):
		leg = self.edgeLengthFunctionInstance.lengthToField()
		if leg != None:
			self.spnEdgeLength.setValue(leg)

	def setLength(self, value):
		if self.rdbLeft.isChecked() == True:
			self.edgeLengthFunctionInstance.setLength(value, self.rdbLeft.text())
		elif self.rdbCenter.isChecked() == True:
			self.edgeLengthFunctionInstance.setLength(value, self.rdbCenter.text())
		elif self.rdbRight.isChecked() == True:
			self.edgeLengthFunctionInstance.setLength(value, self.rdbRight.text())

	def connectUI(self):
		self.btnSelectEdge.clicked.connect(lambda: self.selEdge(self.spnSelectedLength.value()))
		self.btnGetLength.clicked.connect(lambda: self.lengthToField())
		self.btnSetLength.clicked.connect(lambda: self.setLength(self.spnEdgeLength.value()))


def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)


check_exist_window("EdgeLengthMainWindow")
winEdgeLength = EdgeLengthMainWindow()
winEdgeLength.show()