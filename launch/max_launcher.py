import os
import sys
try:
	import winreg
except ImportError:
	import _winreg as winreg
#import shlex

currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
rootPath = ("/".join(currentFilePath.split("/")[:-1]))
sys.path.append(rootPath)
class LauncherFunction():
	def __init__(self):
		self.maxVersionDict =   {"19.0": "2017","20.0": "2018","21.0": "2019","22.0": "2020","23.0": "2021", "24.0": "2022"}

	def getInstalledLocationInRegistryEditor(self, hive, flag, version):
		aReg = winreg.ConnectRegistry(None, hive)
		keyPath = r"SOFTWARE\Autodesk\3dsMax" + "\\" + version
		try:
			aKey = winreg.OpenKey(aReg, keyPath, 0, winreg.KEY_READ | flag)
			maxInstalledLocation, null = winreg.QueryValueEx(aKey, r"Installdir")
			maxInstalledLocation = maxInstalledLocation.replace("\\","/")
			return maxInstalledLocation
		except FileNotFoundError:
			pass

	def getDisplayIcon(self, maxInstalledLocation):
		self.maxIconName = "icon_main"
		iconMaxPath = maxInstalledLocation + "icons"
		for file in os.listdir(iconMaxPath):
			if self.maxIconName in file.lower():
				displayIconFullPath = iconMaxPath + "/" + file
				return displayIconFullPath

	def getExeFilePath(self, maxInstalledLocation):
		maxExeFilePath = maxInstalledLocation + "3dsmax.exe"
		if os.path.isfile(maxExeFilePath):
			return maxExeFilePath

	def getLibrary(self):
		self.maxLibrary = "puzzle_max"
		return (self.maxLibrary)

	def getOpenCommandLine(self, exeFilePath, maxLibrary):
		#self.openingCommandLine = "\"" + exeFilePath + "\" -c" + ' python(\""import sys; sys.path.append('""+currentFilePath+""'); from '+mayaLibrary+' import startup; startup.main()\"")'
		#self.openingCommandLine = shlex.split(self.openingCommandLine)
		#self.openingCommandLine = subprocess.Popen([exeFilePath, "-c", "python(\"import sys; sys.path.append('"+currentFilePath+"'); from "+mayaLibrary+" import startup; startup.main()\")"])
		startupCommandLine = rootPath + "/" + self.maxLibrary + "/" + "startup.py"
		self.openingCommandLine = [exeFilePath, '-U', 'PythonHost', startupCommandLine]
		#b = exeFilePath + " -u PythonHost " + "\"'"+startupCommandLine+"'\""
		#a = shlex.split(b)
		#print (a)
		return (self.openingCommandLine)

	def main(self):
		self.maxInformationDict = {}
		for maxVersion, maxYearVersion in self.maxVersionDict.items():
			maxInstalledLocation = self.getInstalledLocationInRegistryEditor(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY, maxVersion)
			if maxInstalledLocation:
				maxDisplayedIcon = self.getDisplayIcon(maxInstalledLocation)
				maxExeFilePath = self.getExeFilePath(maxInstalledLocation)
				maxImportedLibrary = self.getLibrary()
				maxOpeningCommandLine = self.getOpenCommandLine(maxExeFilePath, maxImportedLibrary)
				self.maxInformationDict["3DSMax " + maxYearVersion] = [maxInstalledLocation, maxDisplayedIcon, maxExeFilePath, maxImportedLibrary, maxOpeningCommandLine]
		return self.maxInformationDict