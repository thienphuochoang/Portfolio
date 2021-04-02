import os
import sys
import importlib
currentFilePath = os.path.dirname(os.path.abspath(__file__))
rootPath = "\\".join((currentFilePath.split("\\")[:-1]))
rootPath = rootPath.replace("\\","/")
sys.path.append(rootPath)

moduleImporterPath = 'general.modules_importer.modules_importer_function' # Don't change this
importerFunction = None

if moduleImporterPath in sys.modules:
	importerFunction = sys.modules[moduleImporterPath]
	try:
		importlib.reload(importerFunction)
	except:
		reload(importerFunction)
else:
	importerFunction = importlib.import_module(moduleImporterPath)

exportSBSARFunction = importerFunction.importModule('puzzle_substance_designer.sbsar_exporter.function.export_sbsar_function')



class LauncherFunction():
	def __init__(self):
		self.exportSBSARDict = {}
		self.satFilePath = rootPath + "/" + "modules" + "/" + "lib" + "/" + "site-packages" + "/" + "substance_automation_toolkit"
		#self.sbsarExportMainFilePath = rootPath + "/" + "puzzle_substance_designer" + "/" + "sbsar_exporter" + "/" + "controller" + "/" + "main.py"
		self.exportSBSARFunctionInstance = exportSBSARFunction.SDExportSbsarFunction()

	def getSBSCookerInstalledLocation(self):
		if os.path.exists(self.satFilePath):
			for file in os.listdir(self.satFilePath):
				if "sbscooker.exe" in file.lower():
					sbscookerEXEPath = self.satFilePath + "/" + "sbscooker.exe"
					return sbscookerEXEPath
		else:
			return False

	def getDisplayedIcon(self):
		displayIconFullPath = rootPath + "/" + "lib" + "/" + "icon" + "/" + "sbsar_icon.png"
		return displayIconFullPath

	def getSBSCommandLineInputList(self):
		inputSBSCommandLineList = self.exportSBSARFunctionInstance.exportSBSAR()
		return inputSBSCommandLineList

	def getExecuteCommandLine(self, sbscookerEXEPath):
		executeCommandLineList = []
		inputSBSCommandLineList = self.getSBSCommandLineInputList()
		for sbsCommandLineInput in inputSBSCommandLineList:
			
			sbsCommandLineInput.insert(0, sbscookerEXEPath)
			#executeCommandLine = [sbscookerEXEPath, sbsCommandLineInput]

			executeCommandLineList.append(sbsCommandLineInput)
		return executeCommandLineList

	def main(self):
		installedLocation = self.getSBSCookerInstalledLocation()
		displayedIcon = self.getDisplayedIcon()
		importedLibrary = ""
		commandLineList = self.getExecuteCommandLine(installedLocation)
		self.exportSBSARDict["Export substance designer library from SBS to SBSAR"] = [installedLocation, displayedIcon, commandLineList, importedLibrary, commandLineList]
		return self.exportSBSARDict
