import sys
import os
import PySide2
import importlib
from PySide2 import QtWidgets
from qtmax import GetQMaxMainWindow
#sys.path.append(r"D:\WIP_Portfolio")

# snapDecalMSFilePath = "/".join(currentFilePath.split("/")[:-1]) + "/" + "function"
# snapDecalMSScriptFile = snapDecalMSFilePath + "/" + "decal_snap_function.ms"
# rt.filein(snapDecalMSScriptFile)

def import_file(str_module):
	"""import a module from string"""
	nameModule = importlib.import_module(str_module)
	try:
		importlib.reload(nameModule)
	except:
		reload(nameModule)
	return nameModule
	
#import Function____________________
ui = import_file("lib.ui.DecalSnapUI")
decalFunctionFile = import_file("puzzle_max.decal_tool.function.decal_import_function")

class SnapDecalMainWindow(QtWidgets.QMainWindow, ui.Ui_MainWindow):
	def __init__(self, parent=None):
		super(SnapDecalMainWindow, self).__init__(parent)
		# Show UI
		self.setupUi(self)

		# Create a decal function class instance from decal_import_function file
		self.decalFunctionInstance = decalFunctionFile.DecalImportFunction()

		self.diffuseDecalPath = None
		self.decalsFullPathList = []
		self.updateDecalsComboBox()
		self.showDecalImage()
		self.cbbDecal.currentTextChanged.connect(lambda: self.showDecalImage())

	def showEvent(self, event):
		self.decalFunctionInstance.showEvent(self.graphicsView)

	def updateDecalsComboBox(self):
		decalList = self.decalFunctionInstance.updateDecalsComboBox()
		self.cbbDecal.clear()
		self.cbbDecal.addItems(sorted(decalList))
		
	def showDecalImage(self):
		self.decalFunctionInstance.showDecalImage(self.graphicsView, self.cbbDecal)
		self.objBoundingBox = self.decalFunctionInstance.getObjBoundingBoxData()

	def mousePressEvent(self, event):
		p = event.localPos()
		self.decalFunctionInstance.analyzeDecalData(p)

try:
	window.close()
except:
	pass
window = SnapDecalMainWindow(GetQMaxMainWindow())
window.show()
