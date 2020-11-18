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
rootPath = currentFilePath.replace("\\","/")
sys.path.append(rootPath)
import PySide2
from PySide2 import QtWidgets, QtGui

def importModulesFromLaunchFolder():
	importModuleList = []
	for file in os.listdir(rootPath + "/launch"):
		if file.endswith(".py") and "__init__" not in file:
			importModule = file.replace(".py","")
			try:
				importedModule = importlib.import_module("launch." + importModule)
				importModuleList.append(importedModule)
			except:
				print (importModule + "is not installed")
			
				
	return importModuleList

class GeneralIconManagement():
	def __init__(self):
		self.mainIcon = rootPath + "/lib/icon/SystemTray.png"
		self.exitIcon = rootPath + "/lib/icon/exit.jpg"
		self.waveHandIcon = rootPath + "/lib/icon/welcome.jpg"

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
		if type(self.commandLine[0]) is list:
			try:
				for eachCommandLine in self.commandLine:
					subprocess.call(eachCommandLine)
				resultBox = QtWidgets.QMessageBox()
				resultBox.setWindowTitle(self.itemName + " Result")
				resultBox.setText(self.itemName + " progress is finished.")
				resultBox.exec()

			except:
				for eachCommandLine in self.exeFilePath:
					subprocess.call(eachCommandLine)
				resultBox = QtWidgets.QMessageBox()
				resultBox.setWindowTitle(self.itemName + " Result")
				resultBox.setText(self.itemName + " progress is finished.")
				resultBox.exec()
		else:
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
		self.setToolTip(r'PUZZLE Tool Collection')
		self.menu = QtWidgets.QMenu(parent)

		self.importAllSoftwareFunction()
		self.menu.addSeparator()

		self.exit = self.menu.addAction("Exit")
		self.exit.triggered.connect(lambda: sys.exit())
		self.exit.setIcon(QtGui.QIcon(iconInstanceClass.exitIcon))
		
		self.menu.addSeparator()
		self.setContextMenu(self.menu)

		self.activated.connect(self.showMenuOnTrigger)

	def showMenuOnTrigger(self, reason):
		if reason == QtWidgets.QSystemTrayIcon.Trigger:
			self.contextMenu().popup(QtGui.QCursor.pos())

	def importAllSoftwareFunction(self):
		modulesList = importModulesFromLaunchFolder()
		for module in modulesList:
			try:
				moduleFunction = module.LauncherFunction()
				moduleInformation = moduleFunction.main()
				if moduleInformation:
					for itemName, info in moduleInformation.items():
						newAction = SystemTrayItem(itemName , info[1], info[2], info[3], info[-1], self.menu)
						self.menu.addAction(newAction)
			except:
				print (str(module) + "is not installed")
		self.menu.addSeparator()

if __name__ == '__main__':
	iconInstanceClass = GeneralIconManagement()
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	tray_icon = SystemTrayIcon(QtGui.QIcon(iconInstanceClass.mainIcon), w)
	tray_icon.show()
	tray_icon.showMessage('PUZZLE Tool Collection', 'Hello ' + getpass.getuser() + '. Hope you have a great day!!!',QtGui.QIcon(iconInstanceClass.waveHandIcon))

	sys.exit(app.exec_())