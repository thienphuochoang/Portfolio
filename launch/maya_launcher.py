import os
try:
	import winreg
except ImportError:
	import _winreg as winreg

class LauncherFunction():
	def __init__(self):
		self.mayaVersionList =   ["2013","2014","2015","2016","2017","2018","2019","2020","2021"]

	def getInstalledLocationInRegistryEditor(self, hive, flag, version):
		aReg = winreg.ConnectRegistry(None, hive)
		keyPath = r"SOFTWARE\Autodesk\Maya" + "\\" + version + "\\" + r"Setup\InstallPath"
		try:
			aKey = winreg.OpenKey(aReg, keyPath, 0, winreg.KEY_READ | flag)
			mayaInstalledLocation, null = winreg.QueryValueEx(aKey, r"MAYA_INSTALL_LOCATION")
			mayaInstalledLocation = mayaInstalledLocation.replace("\\","/")
			return mayaInstalledLocation
		except FileNotFoundError:
			pass

	def getDisplayIcon(self, mayaInstalledLocation):
		self.mayaIconName = "mayaico"
		iconMayaPath = mayaInstalledLocation + "icons"
		for file in os.listdir(iconMayaPath):
			if self.mayaIconName in file.lower():
				displayIconFullPath = iconMayaPath + "/" + file
				return displayIconFullPath

	def getExeFilePath(self, mayaInstalledLocation):
		mayaExeFilePath = mayaInstalledLocation + "bin/maya.exe"
		if os.path.isfile(mayaExeFilePath):
			return mayaExeFilePath

	def getLibrary(self):
		self.mayaLibrary = "htp_maya"
		return (self.mayaLibrary)

	def getAllVersionInfo(self):
		self.mayaInformationDict = {}
		for mayaVersion in self.mayaVersionList:
			mayaInstalledLocation = self.getInstalledLocationInRegistryEditor(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY, mayaVersion)
			if mayaInstalledLocation:
				mayaDisplayedIcon = self.getDisplayIcon(mayaInstalledLocation)
				mayaExeFilePath = self.getExeFilePath(mayaInstalledLocation)
				mayaImportedLibrary = self.getLibrary()
				self.mayaInformationDict["Maya " + mayaVersion] = [mayaInstalledLocation, mayaDisplayedIcon, mayaExeFilePath, mayaImportedLibrary]
		return self.mayaInformationDict