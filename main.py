import os
import sys
import getpass
import importlib
import subprocess
import xml.etree.ElementTree as ET
try:
	import winreg
except ImportError:
	import _winreg as winreg
import shlex
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
sys.path.append(currentFilePath)

import PySide2
from PySide2 import QtWidgets, QtGui

def importModulesFromLaunchFolder():
	importModuleList = []
	for file in os.listdir(currentFilePath + "/launch"):
		if file.endswith(".py") and "__init__" not in file:
			importModule = file.replace(".py","")
			importedModule = importlib.import_module("launch." + importModule)
			importModuleList.append(importedModule)
	return importModuleList

class GeneralIconManagement():
	def __init__(self):
		self.mainIcon = currentFilePath + "/icon/SystemTray.png"
		self.exitIcon = currentFilePath + "/icon/exit.jpg"
		self.waveHandIcon = currentFilePath + "/icon/wavehand.png"

class SystemTrayItem(QtWidgets.QAction):
	def __init__(self, itemName, icon, exeFilePath, library, commandLine, parent = None):
		QtWidgets.QAction.__init__(self, parent)
		self.itemName = itemName
		self.icon = icon
		self.exeFilePath = exeFilePath
		self.library = library
		self.commandLine = commandLine
		print (self.commandLine)
		self.setText(self.itemName)
		self.setIcon(QtGui.QIcon(self.icon))
		self.triggered.connect(lambda: self.startSoftware())

	def startSoftware(self):
		try:
			subprocess.Popen(self.commandLine)
		except:
			subprocess.Popen(self.exeFilePath)

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
	"""
	CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
	"""
	def __init__(self, icon, parent=None):
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
		self.setToolTip(r'Graphic Software Management Tools')
		self.menu = QtWidgets.QMenu(parent)

		self.importAllSoftwareFunction()
		self.exit = self.menu.addAction("Exit")
		self.exit.triggered.connect(lambda: sys.exit())
		self.exit.setIcon(QtGui.QIcon(iconInstanceClass.exitIcon))
		
		self.menu.addSeparator()
		self.setContextMenu(self.menu)

	def importAllSoftwareFunction(self):
		modulesList = importModulesFromLaunchFolder()
		for module in modulesList:
			moduleFunction = module.LauncherFunction()
			moduleInformation = moduleFunction.getAllVersionInfo()
			if moduleInformation:
				for itemName, info in moduleInformation.items():
					newAction = SystemTrayItem(itemName , info[1], info[2], info[3], info[-1], self.menu)
					self.menu.addAction(newAction)
		self.menu.addSeparator()
	
if __name__ == '__main__':
	iconInstanceClass = GeneralIconManagement()
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	tray_icon = SystemTrayIcon(QtGui.QIcon(iconInstanceClass.mainIcon), w)
	tray_icon.show()
	tray_icon.showMessage('Graphic Software Management Tools', 'Hello ' + getpass.getuser() + '. Hope you have a great day!!!',QtGui.QIcon(iconInstanceClass.waveHandIcon))

	sys.exit(app.exec_())