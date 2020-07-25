import os
try:
	import winreg
except ImportError:
	import _winreg as winreg

class LauncherFunction():
	def __init__(self):
		pass

	def getInstalledLocationInRegistryEditor(self, hive, flag):
		installAndVersionDict = {}
		aReg = winreg.ConnectRegistry(None, hive)
		keyPath = r"SOFTWARE\Side Effects Software"
		aKey = winreg.OpenKey(aReg, keyPath, 0, winreg.KEY_READ | flag)
		count_subkey = winreg.QueryInfoKey(aKey)[0]
		for i in range(count_subkey):
			try:
				asubkey_name = winreg.EnumKey(aKey, i)
				asubkey = winreg.OpenKey(aKey, asubkey_name)
				houdiniInstalledLocation = (winreg.QueryValueEx(asubkey, "InstallPath")[0])
				houdiniInstalledLocation = houdiniInstalledLocation.replace("\\","/")
				houdiniVersion = (winreg.QueryValueEx(asubkey, "Version")[0])
				installAndVersionDict[houdiniInstalledLocation] = houdiniVersion
				#return (houdiniInstalledLocation, houdiniVersion)
			except EnvironmentError:
				pass
		return installAndVersionDict
	
	def getDisplayIcon(self, houdiniInstalledLocation):
		self.houdiniIconName = "minimizedicon.png"
		iconHoudiniPath = houdiniInstalledLocation + "/houdini/pic"
		for file in os.listdir(iconHoudiniPath):
			if self.houdiniIconName in file.lower():
				displayIconFullPath = iconHoudiniPath + "/" + file
				return displayIconFullPath

	def getExeFilePath(self, houdiniInstalledLocation):
		houdiniExeFilePath = houdiniInstalledLocation + "/bin/houdinifx.exe"
		if os.path.isfile(houdiniExeFilePath):
			return houdiniExeFilePath

	def getLibrary(self):
		self.houdiniLibrary = "htp_houdini"
		return (self.houdiniLibrary)

	def main(self):
		self.houdiniInformationDict = {}
		installAndVersionDict = self.getInstalledLocationInRegistryEditor(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY)
		if installAndVersionDict:
			for houdiniInstalledLocation, houdiniVersion in installAndVersionDict.items():
				houdiniDisplayedIcon = self.getDisplayIcon(houdiniInstalledLocation)
				houdiniExeFilePath = self.getExeFilePath(houdiniInstalledLocation)
				houdiniImportedLibrary = self.getLibrary()
				self.houdiniInformationDict["Houdini FX " + houdiniVersion] = [houdiniInstalledLocation, houdiniDisplayedIcon, houdiniExeFilePath, houdiniImportedLibrary]
		return self.houdiniInformationDict
