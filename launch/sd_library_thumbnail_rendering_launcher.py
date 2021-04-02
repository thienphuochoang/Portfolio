import os
import sys

currentFilePath = os.path.dirname(os.path.abspath(__file__))
rootPath = "\\".join((currentFilePath.split("\\")[:-1]))
rootPath = rootPath.replace("\\","/")
sys.path.append(rootPath)


class LauncherFunction():
	def __init__(self):
		self.generateSDThumbnailDict = {}
		self.pythonLocationPath = rootPath + "/" + "modules" + "/" + "Scripts"
		self.thumbnailRenderingMainFilePath = rootPath + "/" + "puzzle_substance_designer" + "/" + "thumbnail_rendering" + "/" + "controller" + "/" + "main.py"

	def getPythonInstalledLocation(self):
		if os.path.exists(self.pythonLocationPath):
			for file in os.listdir(self.pythonLocationPath):
				if "python.exe" in file.lower():
					pythonEXEPath = self.pythonLocationPath + "/" + "python.exe"
					return pythonEXEPath
		else:
			return False

	def getDisplayedIcon(self):
		displayIconFullPath = rootPath + "/" + "lib" + "/" + "icon" + "/" + "default_sd_thumbnail_rendering_icon.png"
		return displayIconFullPath


	def getExecuteCommandLine(self, pythonEXEPath, mainThumbnailRenderingFilePath):
		executeCommandLine = [pythonEXEPath, mainThumbnailRenderingFilePath]
		return executeCommandLine

	def main(self):
		installedLocation = self.getPythonInstalledLocation()
		displayedIcon = self.getDisplayedIcon()
		importedLibrary = ""
		commandLineList = self.getExecuteCommandLine(installedLocation, self.thumbnailRenderingMainFilePath)
		self.generateSDThumbnailDict["Generate substance designer library thumbnail"] = [installedLocation, displayedIcon, commandLineList, importedLibrary, commandLineList]
		return self.generateSDThumbnailDict