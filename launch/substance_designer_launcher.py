import os
try:
	import winreg
except ImportError:
	import _winreg as winreg

class LauncherFunction():
	def __init__(self):
		self.sdFindingKeyword = "Substance Designer"

	def getInstalledLocationInRegistryEditor(self, hive, flag):
		installAndVersionDict = {}
		aReg = winreg.ConnectRegistry(None, hive)
		keyPath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
		aKey = winreg.OpenKey(aReg, keyPath, 0, winreg.KEY_READ | flag)
		count_subkey = winreg.QueryInfoKey(aKey)[0]
		for i in range(count_subkey):
			try:
				asubkey_name = winreg.EnumKey(aKey, i)
				asubkey = winreg.OpenKey(aKey, asubkey_name)
				subkeyDisplayName = (winreg.QueryValueEx(asubkey, "DisplayName")[0])
				if self.sdFindingKeyword.lower() in subkeyDisplayName.lower():
					sdInstalledLocation = (winreg.QueryValueEx(asubkey, "InstallLocation")[0])
					sdInstalledLocation = sdInstalledLocation.replace("\\","/")
					sdVersion = (winreg.QueryValueEx(asubkey, "DisplayVersion")[0])
					installAndVersionDict[sdInstalledLocation] = sdVersion
			except EnvironmentError:
				pass
		return installAndVersionDict
	
	def getDisplayIcon(self, sdInstalledLocation):
		self.sdIconName = "sbs.ico"
		iconSDPath = sdInstalledLocation + "resources/icons"
		for file in os.listdir(iconSDPath):
			if self.sdIconName in file.lower():
				displayIconFullPath = iconSDPath + "/" + file
				return displayIconFullPath

	def getExeFilePath(self, sdInstalledLocation):
		sdExeFilePath = sdInstalledLocation + "Substance Designer.exe"
		if os.path.isfile(sdExeFilePath):
			return sdExeFilePath

	def getLibrary(self):
		self.sdLibrary = "htp_substance_designer"
		return (self.sdLibrary)

	def main(self):
		self.sdInformationDict = {}
		installAndVersionDict = self.getInstalledLocationInRegistryEditor(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY)
		if installAndVersionDict:
			for sdInstalledLocation, sdVersion in installAndVersionDict.items():
				sdDisplayedIcon = self.getDisplayIcon(sdInstalledLocation)
				sdExeFilePath = self.getExeFilePath(sdInstalledLocation)
				sdImportedLibrary = self.getLibrary()
				self.sdInformationDict["Substance Designer " + sdVersion] = [sdInstalledLocation, sdDisplayedIcon, sdExeFilePath, sdImportedLibrary]
		return self.sdInformationDict