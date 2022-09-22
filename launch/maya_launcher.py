import os
import sys
try:
	import winreg
except ImportError:
	import _winreg as winreg
import ctypes
from ctypes.wintypes import MAX_PATH

currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
rootPath = ("/".join(currentFilePath.split("/")[:-1]))
sys.path.append(rootPath)
class LauncherFunction():
	def __init__(self):
		self.mayaVersionList =   ["2013","2014","2015","2016","2017","2018","2019","2020","2021","2022"]
		self.externalModules = rootPath + "/" + "modules" + "/" + "Lib" + "/" + "site-packages"

	def saveRootPathToMayaEnvFile(self, mayaVersion):
		currentUserDocumentPath = None
		dll = ctypes.windll.shell32
		buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
		if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
			currentUserDocumentPath = buf.value
			currentUserDocumentPath = currentUserDocumentPath.replace("\\","/")
			mayaDocumentFolderPath = currentUserDocumentPath + "/" + "maya" + "/" + str(mayaVersion)
			print (mayaDocumentFolderPath)
			foundMayaEnvFileFlag = False
			for file in os.listdir(mayaDocumentFolderPath):
				if (file.lower()).endswith(".env"):
					foundMayaEnvFileFlag = True
					with open(mayaDocumentFolderPath + "/" + file, "a+") as f:
						datafile = f.readlines()
						foundPuzzleRootPathVar = False
						for line in datafile:
							if "PUZZLE_ROOT_PATH" in line:
								foundPuzzleRootPathVar = True		

						if foundPuzzleRootPathVar == False:
							f.write("\nPUZZLE_ROOT_PATH = " + rootPath + "")
							print ("Set PUZZLE_ROOT_PATH to Maya Environment File SUCCESSFULLY!!!")

			if foundMayaEnvFileFlag == False:
				with open(mayaDocumentFolderPath + "/" + file, "w") as f:
					f.write("\nPUZZLE_ROOT_PATH = " + rootPath + "")
					print ("Set PUZZLE_ROOT_PATH to Maya Environment File SUCCESSFULLY!!!")

		else:
			print ("Cannot find current computer user Documents folder")

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
		self.mayaLibrary = "puzzle_maya"
		return (self.mayaLibrary)

	def getOpenCommandLine(self, exeFilePath, mayaLibrary):
		#self.openingCommandLine = "\"" + exeFilePath + "\" -c" + ' python(\""import sys; sys.path.append('""+currentFilePath+""'); from '+mayaLibrary+' import startup; startup.main()\"")'
		#self.openingCommandLine = shlex.split(self.openingCommandLine)
		#self.openingCommandLine = subprocess.Popen([exeFilePath, "-c", "python(\"import sys; sys.path.append('"+currentFilePath+"'); from "+mayaLibrary+" import startup; startup.main()\")"])
		self.openingCommandLine = [exeFilePath, "-c", "python(\"import sys; sys.path.append('"+rootPath+"'); sys.path.append('"+self.externalModules+"'); from "+mayaLibrary+" import startup; startup.main()\")"]
		#b = exeFilePath + " -c " + "python(\"import sys; sys.path.append('"+currentFilePath+"'); from "+mayaLibrary+" import startup; startup.main()\")"
		#a = shlex.split(b)
		#print (a)
		return (self.openingCommandLine)

	def main(self):
		self.mayaInformationDict = {}
		for mayaVersion in self.mayaVersionList:
			mayaInstalledLocation = self.getInstalledLocationInRegistryEditor(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY, mayaVersion)
			if mayaInstalledLocation:
				self.saveRootPathToMayaEnvFile(mayaVersion)
				mayaDisplayedIcon = self.getDisplayIcon(mayaInstalledLocation)
				mayaExeFilePath = self.getExeFilePath(mayaInstalledLocation)
				mayaImportedLibrary = self.getLibrary()
				mayaOpeningCommandLine = self.getOpenCommandLine(mayaExeFilePath, mayaImportedLibrary)
				self.mayaInformationDict["Maya " + mayaVersion] = [mayaInstalledLocation, mayaDisplayedIcon, mayaExeFilePath, mayaImportedLibrary, mayaOpeningCommandLine]
		return self.mayaInformationDict