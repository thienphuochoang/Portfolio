import os
import pysbs
from pysbs.batchtools import thumbnail
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
rootDirectory = "/".join((currentFilePath.split("/")[:-3]))

class SDThumbnailRenderingFunction():
	def __init__(self):
		self.sdLibraryPath = rootDirectory + "/" + "lib" + "/" + "substance_designer_library"
		self.materialsFilePath = self.sdLibraryPath + "/" + "materials"

	def getMaterialList(self):
		sbsFileList = []
		for file in os.listdir(self.materialsFilePath):
			if file.endswith(".sbs"):
				filePath = os.path.join(self.materialsFilePath, file)
				filePath = filePath.replace("\\","/")
				sbsFileList.append(filePath)

		return sbsFileList

	def generateSBSThumbnail(self):
		sbsFileList = self.getMaterialList()
		for file in sbsFileList:
			fileNameWithoutSuffix = (file.split("/")[-1]).split(".")[0]

			thumbnailPath = thumbnail.generate(aInput = file, aOutputPath = self.materialsFilePath + "/" + fileNameWithoutSuffix + ".png")

thumbnailRenderingFunctionInstance = SDThumbnailRenderingFunction()
thumbnailRenderingFunctionInstance.generateSBSThumbnail()