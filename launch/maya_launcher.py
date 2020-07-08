import os
import sys
try:
	import winreg
except ImportError:
	import _winreg as winreg
#import shlex

currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
currentFilePath = ("/".join(currentFilePath.split("/")[:-1]))
sys.path.append(currentFilePath)
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

	def getOpenCommandLine(self, exeFilePath, mayaLibrary):
		#self.openingCommandLine = "\"" + exeFilePath + "\" -c" + ' python(\""import sys; sys.path.append('""+currentFilePath+""'); from '+mayaLibrary+' import startup; startup.main()\"")'
		#self.openingCommandLine = shlex.split(self.openingCommandLine)
		#self.openingCommandLine = subprocess.Popen([exeFilePath, "-c", "python(\"import sys; sys.path.append('"+currentFilePath+"'); from "+mayaLibrary+" import startup; startup.main()\")"])
		self.openingCommandLine = [exeFilePath, "-c", "python(\"import sys; sys.path.append('"+currentFilePath+"'); from "+mayaLibrary+" import startup; startup.main()\")"]
		#b = exeFilePath + " -c " + "python(\"import sys; sys.path.append('"+currentFilePath+"'); from "+mayaLibrary+" import startup; startup.main()\")"
		#a = shlex.split(b)
		#print (a)
		return (self.openingCommandLine)

	def getAllVersionInfo(self):
		self.mayaInformationDict = {}
		for mayaVersion in self.mayaVersionList:
			mayaInstalledLocation = self.getInstalledLocationInRegistryEditor(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY, mayaVersion)
			if mayaInstalledLocation:
				mayaDisplayedIcon = self.getDisplayIcon(mayaInstalledLocation)
				mayaExeFilePath = self.getExeFilePath(mayaInstalledLocation)
				mayaImportedLibrary = self.getLibrary()
				mayaOpeningCommandLine = self.getOpenCommandLine(mayaExeFilePath, mayaImportedLibrary)
				self.mayaInformationDict["Maya " + mayaVersion] = [mayaInstalledLocation, mayaDisplayedIcon, mayaExeFilePath, mayaImportedLibrary, mayaOpeningCommandLine]
		return self.mayaInformationDict