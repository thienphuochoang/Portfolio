import importlib
import PySide2
from PySide2 import QtGui, QtCore, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds


mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)  # create a maya Main window


def import_file(str_module):
	"""import a module from string"""
	nameModule = importlib.import_module(str_module)
	try:
		reload(nameModule)
	except:
		importlib.reload(nameModule)
	return nameModule
	
#import Function____________________
scaling_ref_function = import_file(r"puzzle_maya.scaling_ref.function.scaling_ref_function")
scaling_ref_mainUI = import_file(r"lib.ui.Scaling_Reference_MainUI")

class MainScalingRef(QtWidgets.QMainWindow, scaling_ref_mainUI.Ui_Scaling_Reference_MainWindow):
	def __init__(self):
		super(MainScalingRef, self).__init__(parent=mayaMainWindow)
		self.setupUi(self)
		self.ScalingRefFunctionInstance = scaling_ref_function.ScalingRefFunction()
		self.connectUI()

	def connectUI(self):
		self.updateRefFileComboBox(self.cbbRefFiles)
		self.btnImportRef.clicked.connect(lambda: self.importRef(self.cbbRefFiles.currentText()))
		self.btnOpenRefFolder.clicked.connect(lambda: self.openRefFolder())

	def updateRefFileComboBox(self, cbbRefFiles):
		self.ScalingRefFunctionInstance.updateRefFileComboBox(cbbRefFiles)

	def importRef(self, currentSelectedItem):
		self.ScalingRefFunctionInstance.importRef(currentSelectedItem)

	def openRefFolder(self):
		self.ScalingRefFunctionInstance.openRefFolder()

	

def check_exist_window(name_window):
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)


check_exist_window("Scaling_Reference_MainWindow")
winScalingRef = MainScalingRef()
winScalingRef.show()







