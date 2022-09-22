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
pivot_function = importerFunction.importModule("puzzle_maya.pivot.function.pivot_function")
pivot_mainUI = importerFunction.importModule("lib.ui.Pivot_MainUI")

class PivotMainWindow(QtWidgets.QMainWindow, pivot_mainUI.Ui_PivotMainWindow):
	def __init__(self):
		super(PivotMainWindow, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.pivotFunctionInstance = pivot_function.PivotFunction()
		self.connectUI()

	def getComboBoxState(self, gbX, gbY, gbZ):
		stateList = self.pivotFunctionInstance.getComboBoxState(gbX, gbY, gbZ)
		return stateList

	def connectUI(self):
		self.btnSetupPivot.clicked.connect(lambda: self.setupPivot())
		self.btnSetupPivot000.clicked.connect(lambda: self.setupPivot000())
		self.btnSetupPivotUp0.clicked.connect(lambda: self.setupPivotUp0())
		self.btnSetupPos000.clicked.connect(lambda: self.setupPos000())

	def setupPivot(self):
		stateList = self.getComboBoxState(self.gbX, self.gbY, self.gbZ)
		self.pivotFunctionInstance.setupPivot(stateList[0], stateList[1], stateList[-1])

	def setupPivot000(self):
		self.pivotFunctionInstance.setupPivot000()

	def setupPivotUp0(self):
		self.pivotFunctionInstance.setupPivotUp0()

	def setupPos000(self):
		self.pivotFunctionInstance.setupPos000()

def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)


check_exist_window("PivotMainWindow")
winPivot = PivotMainWindow()
winPivot.show()







