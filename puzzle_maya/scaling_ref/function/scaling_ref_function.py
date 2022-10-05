import os
import maya.cmds as cmds
import maya.mel as mel
import importlib
rootPath = mel.eval('getenv("PUZZLE_ROOT_PATH")')

def import_file(str_module):
	"""import a module from string"""
	nameModule = importlib.import_module(str_module)
	try:
		reload(nameModule)
	except:
		importlib.reload(nameModule)
	return nameModule
	
#import Function____________________
exporter_func = import_file(r"puzzle_maya.exporter.function.exporter_function")

class ScalingRefFunction():
	def __init__(self):
		pass

	def updateRefFileComboBox(self, cbbRefFiles):
		cbbRefFiles.clear()
		self.fullReferenceFilePathList = []
		referenceFileList = []
		scalingRefFolderPath = rootPath + "/" + "lib" + "/" + "resource" + "/" + "scaling_reference"
		for file in os.listdir(scalingRefFolderPath):
			if (file.lower()).endswith(".fbx"):
				self.fullReferenceFilePathList.append(scalingRefFolderPath + "/" + file)
				referenceFileList.append(file.split(".")[0])
		cbbRefFiles.addItems(referenceFileList)

	def importRef(self, currentSelectedItem):
		for file in self.fullReferenceFilePathList:
			if currentSelectedItem in file:
				exporter_func.importFBX(file.split(".")[0], "true", "false")

	def openRefFolder(self):
		scalingRefFolderPath = rootPath + "/" + "lib" + "/" + "resource" + "/" + "scaling_reference"
		os.startfile(scalingRefFolderPath)