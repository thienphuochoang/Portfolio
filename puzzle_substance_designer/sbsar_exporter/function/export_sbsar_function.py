import os
import pysbs
# from pysbs.batchtools import thumbnail
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
rootDirectory = "/".join((currentFilePath.split("/")[:-3]))

class SDExportSbsarFunction():
	def __init__(self):
		self.sdLibraryPath = rootDirectory + "/" + "lib" + "/" + "substance_designer_library"
		self.materialsFilePath = self.sdLibraryPath + "/" + "materials"
		# self.satFilePath = rootDirectory + "/" + "lib" + "/" + "site-packages" + "/" + "substance_automation_toolkit"
		# self.sbscookerFilePath = self.satFilePath + "/" + "sbscooker.exe"

	def getMaterialList(self):
		sbsFileList = []
		for file in os.listdir(self.materialsFilePath):
			if file.endswith(".sbs"):
				filePath = os.path.join(self.materialsFilePath, file)
				filePath = filePath.replace("\\","/")
				sbsFileList.append(filePath)

		return sbsFileList

	def exportSBSAR(self, sbsFileList):
		inputCommandLineList = []
		for file in sbsFileList:
			fileNameWithoutSuffix = (file.split("/")[-1]).split(".")[0]
			outputPath = ("/").join((file.split("/")[:-1]))
			executeCommandLine = ["--inputs", file, "--output-name", fileNameWithoutSuffix, "--output-path", outputPath]
			inputCommandLineList.append(executeCommandLine)

		return inputCommandLineList

	def getMaterialListAndExportSBSAR(self):
		sbsFileList = self.getMaterialList()
		inputCommandLineList = self.exportSBSAR(sbsFileList)
		return inputCommandLineList
# SDExportSbsarFunctionInstance = SDExportSbsarFunction()
# inputCommandLineList = SDExportSbsarFunctionInstance.exportSBSAR()