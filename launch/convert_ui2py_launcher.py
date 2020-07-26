import os
import subprocess
import sys
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = "\\".join((currentFilePath.split("\\")[:-1]))

class LauncherFunction():
	def __init__(self):
		self.pyside2uic = currentFilePath + "\\" + "modules" + "\\" + "Scripts" + "\\" + "pyside2-uic.exe"
		#self.pyside2uic = "C:\\Python37\\Scripts\\pyside2-uic.exe"
		self.fileType = r".ui"
		self.convertUIInformationDict = {}

	def getDisplayIcon(self):
		displayIconFullPath = currentFilePath + "\\" + "lib" + "\\" + "icon" + "\\" + "convert.png"
		return displayIconFullPath

	def searchFile(self, startdir, typeFile):
		assert os.path.isdir(startdir)
		listUI = []
		for cur_path, directories, files in os.walk(startdir):
			for f in files:
				# print(f)
				if f.endswith(typeFile):
					listUI.append(os.path.join(startdir, cur_path, f))
		# print(listUI)
		return listUI
		

	def ui2py(self, uiFile):
		"""Convert file .ui to file .py"""
		pyFile = uiFile[:-3]
		pyFile = pyFile + (".py")

		pyFile = "".join(pyFile)
		uiFile = "".join(uiFile)
		executeCommandLine = [self.pyside2uic.replace("\\","/"), uiFile.replace("\\","/"), "-o", pyFile.replace("\\","/")]
		return executeCommandLine
		#subprocess.call([self.pyside2uic, "-x" ,uiFile, "-o", pyFile])
		#print(uiFile, "has been converted to", pyFile, "\n")

	def convert(self):
		uis = self.searchFile(currentFilePath, self.fileType)
		#uis = [r"D:\WIP_Portfolio\puzzle_maya\uv_tool\texel_density\ui\texel_density_ui.ui"]
		listOfCommandLines = []
		for ui in uis:
			commandLine = self.ui2py(ui)
			listOfCommandLines.append(commandLine)
		return listOfCommandLines

	def main(self):
		installedLocation = ""
		displayedIcon = self.getDisplayIcon()
		importedLibrary = ""
		commandLineList = self.convert()
		self.convertUIInformationDict["Convert UI -> Python"] = [installedLocation, displayedIcon, commandLineList, importedLibrary, commandLineList]
		return self.convertUIInformationDict
		


#convert()
#fixPy()

