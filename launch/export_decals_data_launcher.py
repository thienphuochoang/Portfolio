import os
import subprocess
import sys

currentFilePath = os.path.dirname(os.path.abspath(__file__))
rootPath = "\\".join((currentFilePath.split("\\")[:-1]))
rootPath = rootPath.replace("\\","/")
sys.path.append(rootPath)

from launch import max_launcher
class LauncherFunction():
	def __init__(self):
		self.decalsPath = rootPath + "/" + "lib" + "/" + "resource" + "/" + "decals"
		self.iconPath = rootPath + "/" + "lib" + "/" + "icon"
		self.decalFilePathList = []

	def getLatestInstalledMaxVersion(self):
		maxVersionDataDict = max_launcher.LauncherFunction().main()
		latestVersion = 0
		if len(maxVersionDataDict):
			for maxYear, maxData in maxVersionDataDict.items():
				onlyYear = (maxYear.split(" ")[-1])
				if int(onlyYear) > int(latestVersion):
					latestVersion = onlyYear

			for maxYear, maxData in maxVersionDataDict.items():
				onlyYear = (maxYear.split(" ")[-1])
				if int(onlyYear) == int(latestVersion):
					return {maxYear: maxData}

	def getAllDecalMaxFiles(self):
		for file in os.listdir(self.decalsPath):
			if file.endswith(".max"):
				self.decalFilePathList.append((os.path.join(self.decalsPath, file)).replace("\\","/"))
		return list(set(self.decalFilePathList))

	def getDisplayIcon(self, maxInstalledLocation):
		self.decalIconName = "decals.jpg"
		iconDecalPath = self.iconPath + "/" + self.decalIconName
		return iconDecalPath

	def getExeFilePath(self, maxInstalledLocation):
		maxExeFilePath = maxInstalledLocation + "3dsmaxcmd.exe"
		if os.path.isfile(maxExeFilePath):
			return maxExeFilePath

	def executeCommandLine(self, exeFilePath, scriptPath, filePath):
		executeCommandLine = [exeFilePath, "-script", scriptPath, filePath]
		return executeCommandLine

	def getDecalExportDataFunctionFilePath(self):
		decalDataExportFunctionPath = rootPath + "/" + "puzzle_max" + "/" + "decal_tool" + "/" + "function" + "/" + "decal_data_export_function.py"
		return decalDataExportFunctionPath

	def getExportDataCommandLineList(self, installedLocation):
		allDecalMaxFiles = self.getAllDecalMaxFiles()
		listOfCommandLines = []
		for file in allDecalMaxFiles:
			exeFilePath = self.getExeFilePath(installedLocation)
			decalExportDataFilePath = self.getDecalExportDataFunctionFilePath()
			commandLine = self.executeCommandLine(exeFilePath, decalExportDataFilePath, file)
			listOfCommandLines.append(commandLine)
		return listOfCommandLines

	def main(self):
		maxDataDict = self.getLatestInstalledMaxVersion()
		self.exportDecalData = {}
		if maxDataDict:
			maxVersion = list(maxDataDict.keys())[0]
			installedLocation = maxDataDict[maxVersion][0]
			exeFilePath = self.getExeFilePath(installedLocation)
			displayedIcon = self.getDisplayIcon(installedLocation)
			commandLineList = self.getExportDataCommandLineList(installedLocation)
			importedLibrary = ""
			self.exportDecalData["Export Decals Data From Max"] = [installedLocation, displayedIcon, exeFilePath, importedLibrary, commandLineList]
			return self.exportDecalData
		

#a = LauncherFunction()
#print (a.main())
#convert()
#fixPy()

