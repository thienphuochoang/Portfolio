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
vertex_snaping_function = importerFunction.importModule("puzzle_maya.vertex_snaping.function.vertex_snaping_function")
vertex_snaping_mainUI = importerFunction.importModule("puzzle_maya.vertex_snaping.ui.vertex_snaping_ui")

class VertexSnapingMainWindow(QtWidgets.QMainWindow, vertex_snaping_mainUI.Ui_VertexSnapingMainWindow):
	def __init__(self):
		super(VertexSnapingMainWindow, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.vertexSnapingFunctionInstance = vertex_snaping_function.VertexSnapingFunction()
		self.connectUI()

	def mergeVertexToCenter(self, eps):
		self.vertexSnapingFunctionInstance.mergeVertexToCenter(eps)

	def snapSelectedVertexToClosestOne(self, eps):
		self.vertexSnapingFunctionInstance.snapSelectedVertexToClosestOne(eps)

	def connectUI(self):
		self.btnMergeToCenter.clicked.connect(lambda: self.mergeVertexToCenter(self.spnThreshold.value()))
		self.btnSnapToClosestVertex.clicked.connect(lambda: self.snapSelectedVertexToClosestOne(self.spnThreshold.value()))


def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)


check_exist_window("VertexSnapingMainWindow")
winVertexSnaping = VertexSnapingMainWindow()
winVertexSnaping.show()