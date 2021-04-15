import os
import sys
import subprocess
import maya.mel as mel
import maya.cmds as cmds
import PySide2
from PySide2 import QtWidgets
currentFilePath = os.path.dirname(os.path.abspath(__file__))
rootPath = currentFilePath.replace("\\","/")
rootPath = "/".join(rootPath.split("/")[:-3])

moduleImporterPath = 'general.modules_importer.modules_importer_function'
importerFunction = None

if moduleImporterPath in sys.modules:
	importerFunction = sys.modules[moduleImporterPath]
	try:
		importlib.reload(importerFunction)
	except:
		reload(importerFunction)
else:
	importerFunction = importlib.import_module(moduleImporterPath)


exporter_func = importerFunction.importModule(r"puzzle_maya.exporter.function.exporter_function")

class MatCreationFunction():
	def __init__(self):
		pass

	def getSATLocation(self):
		SATLocation = rootPath + "/" + "modules" + "/" + "Lib" + "/" + "site-packages" + "/" + "substance_automation_toolkit"
		if os.path.exists(SATLocation):
			return SATLocation
		else:
			cmds.confirmDialog(title='Missing substance automation toolkit', message='Substance Automation Toolkit folder is not found. Please check again.', icon="critical")
			return None

	def getSBSBaker(self):
		SATLocation = self.getSATLocation()
		if SATLocation != None:
			SBSBakerLocation = SATLocation + "/" + "sbsbaker.exe"
			if os.path.exists(SBSBakerLocation):
				return SBSBakerLocation
			else:
				cmds.confirmDialog(title='Missing SBSBaker', message='sbsbaker.exe is not found. Please check again.', icon="critical")
				return None

	def exportFBXToBake(self, outputPath):
		fbxPath = self.outputPath
		exporter_func.exportFBX(fbxPath, createTempGroup = False, sg="true", sm="true", 
			ins="false", tri="false", tan="false", ascii="false")

	def convertResolution(self, resolution):
		convertDict = {"128": "7", "256": "8", "512": "9", "1024": "10", "2048": "11"}
		return convertDict.get(str(resolution))


	def bakeSelectedMesh(self, *args):
		fbxPath = self.outputPath + ".fbx"
		outputName = self.outputPath.split("\\")[-1]
		outputPath = self.outputPath.split("\\")[:-1]
		widthResolution = self.convertResolution(args[1])
		heightResolution = self.convertResolution(args[2])
		resolution = widthResolution + "," + heightResolution

		self.SBSBakerLocation = self.getSBSBaker()
		if self.SBSBakerLocation != None:
			self.exportFBXToBake(self.outputPath)
			if args[0][0] == True:
				self.bakeAOFromSBSBaker(fbxPath,
										outputName,
										"ambient_occlusion",
										self.outputPath,
										resolution,
										str(args[3]),
										str(args[-1]).lower(),
										str(int(args[4]) - 1),
										args[5],
										"false",
										args[6])

			if args[0][1] == True:
				self.bakeCurvatureFromSBSBaker(fbxPath,
										outputName,
										"curvature",
										self.outputPath,
										resolution,
										str(int(args[4]) - 1),
										args[5])

			if args[0][2] == True:
				self.bakeWorldSpaceNormalFromSBSBaker(fbxPath,
										outputName,
										"world_space_normal",
										self.outputPath,
										resolution,
										str(int(args[4]) - 1),
										args[5],
										args[6])

			if args[0][3] == True:
				self.bakePositionFromSBSBaker(fbxPath,
										outputName,
										"position",
										self.outputPath,
										resolution,
										str(int(args[4]) - 1),
										args[5],
										str(args[3]),
										str(args[-1]).lower())

			if args[0][-1] == True:
				self.bakeColorIDFromSBSBaker(fbxPath,
										outputName,
										"color_id",
										self.outputPath,
										resolution,
										str(int(args[4]) - 1),
										str(args[3]),
										str(args[-1]).lower(),
										args[5])

	def bakeColorIDFromSBSBaker(self, *args):
		fbxPath = args[0]
		outputName = args[1]
		pattern = args[2]
		outputPath = args[3]
		resolution = args[4]
		uvSet = args[5]
		quality = args[6]
		lowAsHigh = args[7]
		outputFormat = args[-1]


		subprocess.call([self.SBSBakerLocation, 
			"--verbose",
			"color-from-mesh",
			"--inputs", fbxPath,
			"--output-name", outputName + "_" + pattern, 
			"--output-path", outputPath,
			"--output-size", resolution,
			"--antialiasing", quality,
			"--uv-set", uvSet,
			"--output-format", outputFormat,
			"--color-source", "1",
			"--use-lowdef-as-highdef", lowAsHigh])				

	def bakePositionFromSBSBaker(self, *args):
		fbxPath = args[0]
		outputName = args[1]
		pattern = args[2]
		outputPath = args[3]
		resolution = args[4]
		uvSet = args[5]
		outputFormat = args[6]
		quality = args[7]
		lowAsHigh = args[-1]

		subprocess.call([self.SBSBakerLocation, 
			"--verbose",
			"position-from-mesh",
			"--inputs", fbxPath,
			"--output-name", outputName + "_" + pattern, 
			"--output-path", outputPath,
			"--output-size", resolution,
			"--antialiasing", quality,
			"--uv-set", uvSet,
			"--output-format", outputFormat,
			"--use-lowdef-as-highdef", lowAsHigh,
			"--dilation-width", "4",
			"--mode", "0",
			"--normalization", "1",
			])

	def bakeWorldSpaceNormalFromSBSBaker(self, *args):
		fbxPath = args[0]
		outputName = args[1]
		pattern = args[2]
		outputPath = args[3]
		resolution = args[4]
		uvSet = args[5]
		outputFormat = args[6]
		normalMap = args[-1]

		subprocess.call([self.SBSBakerLocation, 
			"--verbose",
			"normal-world-space",
			"--inputs", fbxPath,
			"--output-name", outputName + "_" + pattern, 
			"--output-path", outputPath,
			"--output-size", resolution,
			"--uv-set", uvSet,
			"--output-format", outputFormat,
			"--dilation-width", "4",
			"--normal-format", "0",
			"--normal", normalMap
			])

	def bakeCurvatureFromSBSBaker(self, *args):
		fbxPath = args[0]
		outputName = args[1]
		pattern = args[2]
		outputPath = args[3]
		resolution = args[4]
		uvSet = args[5]
		outputFormat = args[-1]

		subprocess.call([self.SBSBakerLocation, 
			"--verbose",
			"curvature",
			"--inputs", fbxPath,
			"--output-name", outputName + "_" + pattern, 
			"--output-path", outputPath,
			"--output-size", resolution,
			"--uv-set", uvSet,
			"--output-format", outputFormat,
			"--dilation-width", "4",
			"--details", "0.25"
			])


	def bakeAOFromSBSBaker(self, *args):
		fbxPath = args[0]
		outputName = args[1]
		pattern = args[2]
		outputPath = args[3]
		resolution = args[4]
		quality = args[5]
		lowAsHigh = args[6]
		uvSet = args[7]
		outputFormat = args[8]
		ignoreBackFace = args[9]
		normalMap = args[-1]


		subprocess.call([self.SBSBakerLocation, 
			"--verbose",
			"ambient-occlusion-from-mesh",
			"--inputs", fbxPath,
			"--output-name", outputName + "_" + pattern, 
			"--output-path", outputPath,
			"--output-size", resolution,
			"--antialiasing", quality,
			"--use-lowdef-as-highdef", lowAsHigh,
			"--uv-set", uvSet,
			"--output-format", outputFormat,
			"--dilation-width", "4",
			"--ignore-backface", ignoreBackFace,
			"--ignore-backface-secondary", "0",
			"--nb-second-rays", "64",
			"--normal", normalMap,
			"--normal-format", "0"], shell=False)

	def getFullOutputPath(self):
		self.outputPath, fileType = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "")

		if "." in self.outputPath:
			self.outputPath = self.outputPath.split(".")[0]

		return self.outputPath




# a = MatCreationFunction()
# a.bakeAOFromSBSBaker()