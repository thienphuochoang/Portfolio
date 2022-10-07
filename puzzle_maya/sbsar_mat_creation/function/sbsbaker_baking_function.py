import os
import sys
import subprocess
import maya.mel as mel
import maya.cmds as cmds
import pymel.core as py
import PySide2
from PySide2 import QtWidgets, QtGui
import json
import pysbs
import importlib
from pysbs import context, substance, sbsenum, batchtools, sbsbakers
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


class SBSBakerBakingFunction():
	def __init__(self):
		pass

	def getFullOutputPath(self):
		outputPath = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder", "")
		return outputPath

	def getSATLocation(self):
		SATLocation = rootPath + "/" + "modules" + "/" + "Lib" + "/" + "site-packages" + "/" + "substance_automation_toolkit"
		#SATLocation = "D:/Substance_Designer/Adobe Substance 3D Designer"
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

	def exportFBXToBake(self, outputPath, outputName):
		fbxPath = outputPath + "/" + outputName
		print (fbxPath)
		exporter_func.exportFBX(fbxPath, createTempGroup = False, sg="true", sm="true", 
			ins="false", tri="false", tan="false", ascii="false")

	def convertResolution(self, resolution):
		convertDict = {"128": "7", "256": "8", "512": "9", "1024": "10", "2048": "11"}
		return convertDict.get(str(resolution))

	def disableNormalPathWhenCheckedUseLowAsHigh(self, useLowAsHighButtonStatus, normalPath, browseButton):
		if useLowAsHighButtonStatus == True:
			normalPath.setEnabled(False)
			browseButton.setEnabled(False)
		else:
			normalPath.setEnabled(True)
			browseButton.setEnabled(True)

	def browseNormalMap(self):
		normalMap, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", "")
		normalMap = normalMap.replace("/","\\")
		return normalMap

	def bakeSelectedMesh(self, *args):
		outputName = str(args[8])
		outputName = outputName.replace("\\","/")
		outputPath = str(args[-1])
		outputPath = outputPath.replace("\\","/")
		fbxPath = outputPath + "/" + outputName + ".fbx"
		widthResolution = self.convertResolution(args[1])
		heightResolution = self.convertResolution(args[2])
		resolution = widthResolution + "," + heightResolution
		uvSet = str(int(args[4]) - 1)
		quality = str(args[3])
		lowDefAsHigh = str(args[7]).lower()
		outputFormat = args[5]
		normalMap = args[6]

		self.SBSBakerLocation = self.getSBSBaker()
		if self.SBSBakerLocation != None:
			if len(cmds.ls(sl = True)) > 0:
				self.exportFBXToBake(outputPath, outputName)


				statusList = []
				#bakeNormalStatus = args[0][0]
				#statusList.append(bakeNormalStatus)

				bakeAOStatus = args[0][0]
				statusList.append(bakeAOStatus)

				bakeCurvatureStatus = args[0][1]
				statusList.append(bakeCurvatureStatus)

				bakeWorldSpaceNormalStatus = args[0][2]
				statusList.append(bakeWorldSpaceNormalStatus)

				bakePositionStatus = args[0][3]
				statusList.append(bakePositionStatus)

				bakeColorIDStatus = args[0][-1]
				statusList.append(bakeColorIDStatus)

				defaultBakingPresetPath = self.getDefaultBakingPreset()
				if defaultBakingPresetPath != None:
					latestPresetFilePath = self.removeBakerFromFileJson(statusList, defaultBakingPresetPath)
					
					self.editGeneralDataFromLatestPresetFile(latestPresetFilePath,
															fbxPath,
															outputName,
															outputPath,
															outputFormat,
															widthResolution,
															heightResolution,
															uvSet,
															quality,
															lowDefAsHigh)

					if bakeAOStatus == True:
						# self.editDataFromLatestPresetFile(latestPresetFilePath, "ambient_occlusion", "output-name", None, "{mesh}_ambient_occlusion")
						self.editDataFromLatestPresetFile(latestPresetFilePath, "ambient_occlusion", "parameters", "output-size", "width", int(widthResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "ambient_occlusion", "parameters", "output-size", "height", int(heightResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "ambient_occlusion", "parameters", "output-format", None, outputFormat)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "ambient_occlusion", "parameters", "antialiasing", None, int(quality))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "ambient_occlusion", "parameters", "ignore-backface-secondary", None, 0)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "ambient_occlusion", "parameters", "nb-second-rays", None, 64)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "ambient_occlusion", "parameters", "normal-format", None, 0)

					if bakeCurvatureStatus == True:
						# self.editDataFromLatestPresetFile(latestPresetFilePath, "curvature", "output-name", None, "{mesh}_curvature")
						self.editDataFromLatestPresetFile(latestPresetFilePath, "curvature", "parameters", "output-size", "width", int(widthResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "curvature", "parameters", "output-size", "height", int(heightResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "curvature", "parameters", "output-format", None, outputFormat)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "curvature", "parameters", "dilation-width", None, 4)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "curvature", "parameters", "details", None, 0.25)

					if bakeWorldSpaceNormalStatus == True:
						self.editDataFromLatestPresetFile(latestPresetFilePath, "world_space_normals", "parameters", "output-size", "width", int(widthResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "world_space_normals", "parameters", "output-size", "height", int(heightResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "world_space_normals", "parameters", "output-format", None, outputFormat)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "world_space_normals", "parameters", "dilation-width", None, 4)

					if bakePositionStatus == True:
						self.editDataFromLatestPresetFile(latestPresetFilePath, "position", "parameters", "output-size", "width", int(widthResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "position", "parameters", "output-size", "height", int(heightResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "position", "parameters", "output-format", None, outputFormat)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "position", "parameters", "antialiasing", None, int(quality))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "position", "parameters", "use-lowdef-as-highdef", None, bool(lowDefAsHigh))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "position", "parameters", "dilation-width", None, 4)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "position", "parameters", "mode", None, 0)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "position", "parameters", "normalization", None, 1)

					if bakeColorIDStatus == True:
						self.editDataFromLatestPresetFile(latestPresetFilePath, "color_id", "parameters", "output-size", "width", int(widthResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "color_id", "parameters", "output-size", "height", int(heightResolution))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "color_id", "parameters", "output-format", None, outputFormat)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "color_id", "parameters", "antialiasing", None, int(quality))
						self.editDataFromLatestPresetFile(latestPresetFilePath, "color_id", "parameters", "color-source", None, 1)
						self.editDataFromLatestPresetFile(latestPresetFilePath, "color_id", "parameters", "use-lowdef-as-highdef", None, bool(lowDefAsHigh))



					self.bakeFromFilePreset(latestPresetFilePath)
					self.renameBakedMaps(latestPresetFilePath)
			else:
				cmds.confirmDialog(title='Missing selection', message='Please select mesh to export', icon="critical")

	def getDefaultBakingPreset(self):
		defaultBakingPresetPath = rootPath + "/" + "lib" + "/" + "substance_designer_library" + "/" + "presets" + "/" + "default_baking_preset.json"
		if os.path.exists(defaultBakingPresetPath):
			return defaultBakingPresetPath
		else:
			cmds.confirmDialog(title='Missing default baking preset', message='Default baking preset is missing. Please check again.', icon="critical")
			return None

	def renameBakedMaps(self, latestPresetFilePath):
		fbxFileName = ""
		outputPath = ""
		outputFormat = ""
		with open(latestPresetFilePath, "r") as f:
			data = json.load(f)
			fbxPath = data["inputs"]
			fbxFileName = (fbxPath.split("/")[-1]).split(".")[0]
			outputPath = data["output-path"]
			outputFormat = data["output-format"]

		aoPath = outputPath + "/" + fbxFileName + "_ambient-occlusion-from-mesh" + "." + outputFormat
		newAoPath = outputPath + "/" + fbxFileName + "_ambient_occlusion" + "." + outputFormat
		if (os.path.exists(aoPath)):
			try:
				os.remove(newAoPath)
			except:
				print ("Remove old file: " + aoPath)
			os.rename(aoPath, newAoPath)

		colorIDPath = outputPath + "/" + fbxFileName + "_color-from-mesh" + "." + outputFormat
		newColorIDPath = outputPath + "/" + fbxFileName + "_color_id" + "." + outputFormat
		if (os.path.exists(colorIDPath)):
			try:
				os.remove(newColorIDPath)
			except:
				print ("Remove old file: " + newColorIDPath)
			os.rename(colorIDPath, newColorIDPath)

		curvaturePath = outputPath + "/" + fbxFileName + "_curvature-from-mesh-v2" + "." + outputFormat
		newCurvaturePath = outputPath + "/" + fbxFileName + "_curvature" + "." + outputFormat
		if (os.path.exists(curvaturePath)):
			try:
				os.remove(newCurvaturePath)
			except:
				print ("Remove old file: " + newCurvaturePath)
			os.rename(curvaturePath, newCurvaturePath)

		normalWorldSpacePath = outputPath + "/" + fbxFileName + "_normal-world-space" + "." + outputFormat
		newNormalWorldSpacePath = outputPath + "/" + fbxFileName + "_world_space_normals" + "." + outputFormat
		if (os.path.exists(normalWorldSpacePath)):
			try:
				os.remove(newNormalWorldSpacePath)
			except:
				print ("Remove old file: " + newNormalWorldSpacePath)
			os.rename(normalWorldSpacePath, newNormalWorldSpacePath)

		positionPath = outputPath + "/" + fbxFileName + "_position-from-mesh" + "." + outputFormat
		newPositionPath = outputPath + "/" + fbxFileName + "_position" + "." + outputFormat
		if (os.path.exists(positionPath)):
			try:
				os.remove(newPositionPath)
			except:
				print ("Remove old file: " + newPositionPath)
			os.rename(positionPath, newPositionPath)


	def removeBakerFromFileJson(self, statusList, defaultBakingPresetPath):
		latestPresetFilePath = rootPath + "/" + "lib" + "/" + "substance_designer_library" + "/" + "presets" + "/" + "latest_baking_preset.json"
		with open(defaultBakingPresetPath, "r") as f:
			data = json.load(f)
			#bakeNormalStatus = statusList[0]
			bakeAOStatus = statusList[0]
			bakeCurvatureStatus = statusList[1]
			bakeWorldSpaceNormalStatus = statusList[2]
			bakePositionStatus = statusList[3]
			bakeColorIDStatus = statusList[-1]



			if bakeAOStatus == False:
				try:
					del data['ambient_occlusion']
				except KeyError:
					print ("Cannot find ambient_occlusion key value in file json")

			if bakeCurvatureStatus == False:
				try:
					del data['curvature']
				except KeyError:
					print ("Cannot find curvature key value in file json")

			if bakeWorldSpaceNormalStatus == False:
				try:
					del data['world_space_normals']
				except KeyError:
					print ("Cannot find world_space_normals key value in file json")

			if bakePositionStatus == False:
				try:
					del data['position']
				except KeyError:
					print ("Cannot find position key value in file json")

			if bakeColorIDStatus == False:
				try:
					del data['color_id']
				except KeyError:
					print ("Cannot find color_id key value in file json")


			with open(latestPresetFilePath, "w") as latestFile:
				json.dump(data, latestFile, indent = 4)

			return latestPresetFilePath

	def editDataFromLatestPresetFile(self, *args):
		latestPresetFile = args[0]
		keyBaker = args[1]
		parameter = args[2]
		specifiedParameter = args[3]
		specifiedOutputSize = args[4]
		replacedData = args[-1]


		data = None
		with open(latestPresetFile, "r") as f:
			data = json.load(f)
			if keyBaker != None:
				if parameter != None:
					if specifiedOutputSize != None:
						data[keyBaker][parameter][specifiedParameter][specifiedOutputSize] = replacedData
					else:
						data[keyBaker][parameter][specifiedParameter] = replacedData
				else:
					data[keyBaker][specifiedParameter] = replacedData
			else:
				data[specifiedParameter] = replacedData
				
		with open(latestPresetFile, "w") as f:
			json.dump(data, f, indent = 4)

	def editGeneralDataFromLatestPresetFile(self, *args):
		latestPresetFilePath = args[0]
		fbxPath = args[1]
		outputName = args[2]
		outputPath = args[3]
		outputFormat = args[4]
		widthResolution = int(args[5])
		heightResolution = int(args[6])
		uvSet = int(args[7])
		antiAliasing = int(args[8])
		lowDefAsHigh = bool(args[9])

		self.editDataFromLatestPresetFile(latestPresetFilePath, None, None, "inputs", None, fbxPath)
		self.editDataFromLatestPresetFile(latestPresetFilePath, None, None, "output-path", None, outputPath)
		self.editDataFromLatestPresetFile(latestPresetFilePath, None, None, "output-format", None, outputFormat)
		#self.editDataFromLatestPresetFile(latestPresetFilePath, None, None, "output-size", "width", widthResolution)
		#self.editDataFromLatestPresetFile(latestPresetFilePath, None, None, "output-size", "height", heightResolution)
		self.editDataFromLatestPresetFile(latestPresetFilePath, None, None, "uv-set", None, uvSet)
		self.editDataFromLatestPresetFile(latestPresetFilePath, None, None, "subsampling", None, antiAliasing)
		self.editDataFromLatestPresetFile(latestPresetFilePath, None, None, "use-lowdef-as-highdef", None, lowDefAsHigh)

	def bakeFromFilePreset(self, latestPresetFile):
		subprocess.call([self.SBSBakerLocation,
						"run",
						"--json",
						latestPresetFile])


	# def bakeColorIDFromSBSBaker(self, *args):
	# 	fbxPath = args[0]
	# 	outputName = args[1]
	# 	pattern = args[2]
	# 	outputPath = args[3]
	# 	resolution = args[4]
	# 	uvSet = args[5]
	# 	quality = args[6]
	# 	lowAsHigh = args[7]
	# 	outputFormat = args[-1]


	# 	subprocess.call([self.SBSBakerLocation, 
	# 		"--verbose",
	# 		"color-from-mesh",
	# 		"--inputs", fbxPath,
	# 		"--output-name", outputName + "_" + pattern, 
	# 		"--output-path", outputPath,
	# 		"--output-size", resolution,
	# 		"--antialiasing", quality,
	# 		"--uv-set", uvSet,
	# 		"--output-format", outputFormat,
	# 		"--color-source", "1",
	# 		"--use-lowdef-as-highdef", lowAsHigh])				

	# def bakePositionFromSBSBaker(self, *args):
	# 	fbxPath = args[0]
	# 	outputName = args[1]
	# 	pattern = args[2]
	# 	outputPath = args[3]
	# 	resolution = args[4]
	# 	uvSet = args[5]
	# 	outputFormat = args[6]
	# 	quality = args[7]
	# 	lowAsHigh = args[-1]

	# 	subprocess.call([self.SBSBakerLocation, 
	# 		"--verbose",
	# 		"position-from-mesh",
	# 		"--inputs", fbxPath,
	# 		"--output-name", outputName + "_" + pattern, 
	# 		"--output-path", outputPath,
	# 		"--output-size", resolution,
	# 		"--antialiasing", quality,
	# 		"--uv-set", uvSet,
	# 		"--output-format", outputFormat,
	# 		"--use-lowdef-as-highdef", lowAsHigh,
	# 		"--dilation-width", "4",
	# 		"--mode", "0",
	# 		"--normalization", "1",
	# 		])

	# def bakeWorldSpaceNormalFromSBSBaker(self, *args):
	# 	fbxPath = args[0]
	# 	outputName = args[1]
	# 	pattern = args[2]
	# 	outputPath = args[3]
	# 	resolution = args[4]
	# 	uvSet = args[5]
	# 	outputFormat = args[6]
	# 	normalMap = args[-1]

	# 	subprocess.call([self.SBSBakerLocation, 
	# 		"--verbose",
	# 		"normal-world-space",
	# 		"--inputs", fbxPath,
	# 		"--output-name", outputName + "_" + pattern, 
	# 		"--output-path", outputPath,
	# 		"--output-size", resolution,
	# 		"--uv-set", uvSet,
	# 		"--output-format", outputFormat,
	# 		"--dilation-width", "4",
	# 		"--normal-format", "0",
	# 		"--normal", normalMap
	# 		])

	# def bakeCurvatureFromSBSBaker(self, *args):
	# 	fbxPath = args[0]
	# 	outputName = args[1]
	# 	pattern = args[2]
	# 	outputPath = args[3]
	# 	resolution = args[4]
	# 	uvSet = args[5]
	# 	outputFormat = args[-1]

	# 	subprocess.call([self.SBSBakerLocation, 
	# 		"--verbose",
	# 		"curvature",
	# 		"--inputs", fbxPath,
	# 		"--output-name", outputName + "_" + pattern, 
	# 		"--output-path", outputPath,
	# 		"--output-size", resolution,
	# 		"--uv-set", uvSet,
	# 		"--output-format", outputFormat,
	# 		"--dilation-width", "4",
	# 		"--details", "0.25"
	# 		])


	# def bakeAOFromSBSBaker(self, *args):
	# 	fbxPath = args[0]
	# 	outputName = args[1]
	# 	pattern = args[2]
	# 	outputPath = args[3]
	# 	resolution = args[4]
	# 	quality = args[5]
	# 	lowAsHigh = args[6]
	# 	uvSet = args[7]
	# 	outputFormat = args[8]
	# 	ignoreBackFace = args[9]
	# 	normalMap = args[-1]


	# 	subprocess.call([self.SBSBakerLocation, 
	# 		"--verbose",
	# 		"ambient-occlusion-from-mesh",
	# 		"--inputs", fbxPath,
	# 		"--output-name", outputName + "_" + pattern, 
	# 		"--output-path", outputPath,
	# 		"--output-size", resolution,
	# 		"--antialiasing", quality,
	# 		"--use-lowdef-as-highdef", lowAsHigh,
	# 		"--uv-set", uvSet,
	# 		"--output-format", outputFormat,
	# 		"--dilation-width", "4",
	# 		"--ignore-backface", ignoreBackFace,
	# 		"--ignore-backface-secondary", "0",
	# 		"--nb-second-rays", "64",
	# 		"--normal", normalMap,
	# 		"--normal-format", "0"], shell=False)



	''' To have a better normal map, I will use an external graph to bake a normal map '''


	def getSBSBakingNormalFile(self):
		sdNormalBakingFilePath = rootPath + "/" + "lib" + "/" + "substance_designer_library" + "/" + "functions" + "/" + "sd_normal_baking.sbs"
		if os.path.exists(sdNormalBakingFilePath):
			return True
		else:
			cmds.confirmDialog(title='Missing baking normal sbs file', message='Please check again', icon="critical")
			return False