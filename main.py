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

currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
sys.path.append(currentFilePath)

import PySide2
from PySide2 import QtWidgets, QtGui
#from launch import maya_launcher, max_launcher
#importlib.reload(maya_launcher)
#importlib.reload(max_launcher)

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
	def __init__(self, itemName, icon, exeFilePath, library, parent = None):
		QtWidgets.QAction.__init__(self, parent)
		self.itemName = itemName
		self.icon = icon
		self.exeFilePath = exeFilePath
		self.library = library
		self.setText(self.itemName)
		self.setIcon(QtGui.QIcon(self.icon))
		self.triggered.connect(lambda: self.startSoftware(self.exeFilePath, self.library))

	def startSoftware(self, exeFilePath, library):
		try:
			subprocess.Popen([exeFilePath, "-c", "python(\"import sys; sys.path.append('"+currentFilePath+"'); from "+library+" import startup; startup.main()\")"])
		except:
			subprocess.Popen([exeFilePath])

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
	"""
	CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
	"""
	def __init__(self, icon, parent=None):
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
		self.setToolTip(r'Graphic Software Management Tools')
		self.menu = QtWidgets.QMenu(parent)
		"""
		Create menu depend on the SystemTrayItems.xml and optional user creations
		"""
		#self.readSystemTrayItemXML()
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
					newAction = SystemTrayItem(itemName , info[1], info[2], info[-1], self.menu)
					self.menu.addAction(newAction)
		self.menu.addSeparator()
		#mayaLauncherFunction = maya_launcher.MayaLauncherFunction(currentFilePath)
		#maxLauncherFunction = max_launcher.MaxLauncherFunction(currentFilePath)
		#mayaInfoDict = mayaLauncherFunction.getAllMayaVersionInfo()
		#maxInfoDict = maxLauncherFunction.getAllMaxVersionInfo()
		#for itemName, info in mayaInfoDict.items():
			#print (key, values)
			#newAction = SystemTrayItem(itemName , info[1], info[2], info[-1], self.menu)
			#self.menu.addAction(newAction)

		#for itemName, info in maxInfoDict.items():
			#print (key, values)
			#newAction = SystemTrayItem(itemName , info[1], info[2], info[-1], self.menu)
			#self.menu.addAction(newAction)

		#self.menu.addSeparator()

	
	# def getGraphicInstalledSoftware(self, hive, flag):
	# 	"""
	# 	Get all the installed softwares
	# 	"""
	# 	aReg = winreg.ConnectRegistry(None, hive)
	# 	aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
	# 						  0, winreg.KEY_READ | flag)

	# 	count_subkey = winreg.QueryInfoKey(aKey)[0]

	# 	software_list = []

	# 	for i in range(count_subkey):
	# 		software = {}
	# 		try:
	# 			asubkey_name = winreg.EnumKey(aKey, i)
	# 			asubkey = winreg.OpenKey(aKey, asubkey_name)
	# 			#aloadkey = winreg.
	# 			software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]
	# 			#software['key'] = winreg.OpenKey(aKey, asubkey_name, 0, winreg.KEY_SET_VALUE)
	# 			#try:
	# 			#	software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
	# 			#except EnvironmentError:
	# 			#	software['version'] = 'undefined'
	# 			try:
	# 				software['location'] = winreg.QueryValueEx(asubkey, "InstallLocation")[0]
	# 			except EnvironmentError:
	# 				software['location'] = 'undefined'
	# 				#print ("Cannot find Install Location key in regedit of " + software['name'])

	# 			software_list.append(software)
	# 		except EnvironmentError:
	# 			continue

	# 	return software_list

	# def readSystemTrayItemXML(self):
	# 	"""
	# 	Get the installed softwares, compare to the softwares in the SystemTrayItems.xml 
	# 	"""
	# 	tree = ET.parse(systemTrayItems)
	# 	root = tree.getroot()
	# 	software_list = self.getGraphicInstalledSoftware(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY)
	# 	for elem in root:
	# 		for subelem in elem:
	# 			for software in software_list:
	# 				if subelem.attrib["name"].lower() in software['name'].lower():
	# 					if software['location'] == 'undefined':
	# 						try:
	# 							software['location'] = subelem.attrib["install_location"] + "\\"
	# 							key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" + "\\" + software['name'], 0, winreg.KEY_ALL_ACCESS)
	# 							winreg.SetValueEx(key, 'InstallLocation', 0, winreg.REG_SZ, software['location'])
	# 						except:
	# 							print (subelem.attrib["name"])
	# 							print (software['location'])
	# 							print ("Cannot find install location in file xml")

	# 					if software['location'] != 'undefined' and software['location'] != '':
	# 						itemName = subelem.attrib["name"]
	# 						iconPath = currentFilePath + "\\" + subelem.attrib["icon"]
	# 						exeFilePath = software['location'] + subelem.attrib["exe_path"]
	# 						library = subelem.attrib["library"]
	# 						newAction = SystemTrayItem(itemName , iconPath, exeFilePath, library, self.menu)
	# 						self.menu.addAction(newAction)
	# 		self.menu.addSeparator()
	
if __name__ == '__main__':
	iconInstanceClass = GeneralIconManagement()
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	tray_icon = SystemTrayIcon(QtGui.QIcon(iconInstanceClass.mainIcon), w)
	tray_icon.show()
	tray_icon.showMessage('Graphic Software Management Tools', 'Hello ' + getpass.getuser() + '. Hope you have a great day!!!',QtGui.QIcon(iconInstanceClass.waveHandIcon))

	sys.exit(app.exec_())