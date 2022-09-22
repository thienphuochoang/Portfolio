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
unbevel_function = importerFunction.importModule("puzzle_maya.unbevel.function.unbevel_function")
#edge_length_mainUI = importerFunction.importModule("puzzle_maya.edge_length.ui.edge_length_ui")

def main():
	unbevelFunctionInstance = unbevel_function.UnbevelFunction()
	unbevelFunctionInstance.smartCollapsing()

main()