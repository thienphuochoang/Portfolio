import os
import sys
import subprocess
import maya.mel as mel
import maya.cmds as cmds
import pymel.core as py
import PySide2
from PySide2 import QtWidgets, QtGui
import random
import colorsys
import re
import importlib
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

exporter_function = importerFunction.importModule("puzzle_maya.exporter.function.exporter_function")

# -------------------------------------------------------------------------------------
# Need to fix the asynchronous of the stingray PBS



class MatCreationFunction():
	def __init__(self):
		self.puzzleOpaqueShaderAttributeList = ["uv_scale", 
		"uv_offset", 
		"BaseColor_Map", 
		"Normal_Map", 
		"Metallic_Map", 
		"Roughness_Map", 
		"AO_Map", 
		"Emissive_Map", 
		"BaseColor", 
		"AO_Intensity", 
		"Normal_Intensity", 
		"Metallic", 
		"Roughness", 
		"Emissive"]

	def getSDLibraryLocation(self):
		sdLibrary = rootPath + "/" + "lib" + "/" + "substance_designer_library"
		if os.path.exists(sdLibrary):
			return sdLibrary
		else:
			cmds.confirmDialog(title='Missing substance designer library', message='Substance Library folder is not found. Please check again.', icon="critical")
			return None

	def getShaderFXPath(self):
		shaderFXPath = rootPath + "/" + "lib" + "/" + "shader_library" + "/" + "puzzle_standard_opaque_shader.sfx"
		return shaderFXPath

	def updateItemsInListWidgets(self, currentSelectedMaterialType):
		self.thumbnailList = []
		self.sbsLibraryList = []
		sdLibrary = self.getSDLibraryLocation()
		if sdLibrary != None:
			selectedFolder = sdLibrary + "/" + currentSelectedMaterialType
			for subdir, dirs, files in os.walk(selectedFolder):
				for file in files:
					if (file.lower()).endswith(".png"):
						self.thumbnailList.append((os.path.join(subdir, file)).replace("\\","/"))
					if (file.lower()).endswith(".sbsar"):
						self.sbsLibraryList.append((os.path.join(subdir, file)).replace("\\","/"))
		return self.thumbnailList

	def showImageInListWidget(self, currentSelectedMaterialType, thumbnailListWidget):
		self.materialListWidgetItemDict = {}
		thumbnailListWidget.clear()
		thumbnailList = self.updateItemsInListWidgets(currentSelectedMaterialType)
		for thumbnailPath in thumbnailList:
			item = QtWidgets.QListWidgetItem()
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(thumbnailPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			item.setIcon(icon)
			item.setText((thumbnailPath.split("/")[-1]).split(".")[0])
			thumbnailListWidget.addItem(item)
			self.materialListWidgetItemDict[str(item)] = (thumbnailPath.split("/")[-1]).split(".")[0]

	def checkMayaSubstancePluginAvailable(self):
		count = 0
		neededLoadPluginList = ["substancemaya", "substanceworkflow", "Substance"]
		loadedPlugins = cmds.pluginInfo(query=True, listPlugins=True)
		for plugin in loadedPlugins:
			for needLoadPlugin in neededLoadPluginList:
				if needLoadPlugin.lower() == plugin.lower():
					isLoaded = cmds.pluginInfo(plugin, query=True, loaded=True )
					if isLoaded == True:
						count = count + 1

		if count == len(neededLoadPluginList):
			return True
		else:
			cmds.confirmDialog(title='Missing substance plugins', message='Please check these plugins are available:\nsubstancemaya, substanceworkflow, Substance', icon="critical")
			return False

	def getTransformGroupInScene(self):
		currentSelection = cmds.ls(sl=True, long = True, transforms = True)
		allChildrenSelection = cmds.listRelatives(allDescendents = True, fullPath = True, type = "shape")
		cmds.select(allChildrenSelection)
		self.correctSelection = cmds.listRelatives(parent = True, fullPath = True, type = "transform")
		cmds.select(self.correctSelection)
		return self.correctSelection

	def addWeatherEffectsToComboBox(self):
		sdLibrary = self.getSDLibraryLocation()
		weatherEffectList = []
		if sdLibrary != None:
			weatherEffectFolder = sdLibrary + "/" + "weather_effects"
			for file in os.listdir(weatherEffectFolder):
				if ".sbs" in file.lower():
					weatherEffectList.append(file.split(".")[0])
					#print ((os.path.join(weatherEffectFolder, file)).replace("\\","/"))
		return weatherEffectList


	def createStingrayPBRShader(self, materialName, shaderFXPath):
		#loadedStingrayPBRShaderName = "MAT_puzzle_standard_opaque"
		if cmds.objExists('restoreTechniqueNode_' + materialName):
			cmds.scriptNode('restoreTechniqueNode_' + materialName, ea = True)
			cmds.delete('restoreTechniqueNode_' + materialName)

		#shaderMayaFilePath = rootPath + "/" + "lib" + "/" + "resource" + "/" + "shader_file" + "/" + "maya_shaders_file"
		#exporter_function.importMA(shaderMayaFilePath, "false")
		#PBRShader = cmds.select(loadedStingrayPBRShaderName)
		PBRShader = py.shadingNode('StingrayPBS', asShader = True, name = materialName)
		if shaderFXPath:
			py.shaderfx(sfxnode = PBRShader, loadGraph = shaderFXPath)
		

		SGS = py.sets(renderable = True, name = materialName + '_SG')
		py.connectAttr(PBRShader + '.outColor', SGS + '.surfaceShader', force = True)
		# cmds.select(materialName)
		# confirmButton = cmds.confirmDialog(title='Confirm', message='Please press OK to continue.')
		# if (confirmButton == "Confirm"):
		# 	cmds.select(materialName)
		return PBRShader, SGS

	def createSubstanceNode(self, substanceName , sbsarFile, fileFormat, width, height):
		'''
			Create utility node and substance
		'''
		utility = cmds.shadingNode('place2dTexture', asUtility = True, name = 'place2dTexture')
		substance = cmds.shadingNode('substanceNode', asTexture = True, name = substanceName)

		'''
		Set resolution
		'''
		cmds.substanceSetLockResolution(False)
		cmds.substanceSetGlobalWidth(int(width))
		cmds.substanceSetGlobalHeight(int(height))

		'''
		Set file format
		'''
		if fileFormat == "png":
			cmds.substanceSetBakeType(0)
		elif fileFormat == "tga":
			cmds.substanceSetBakeType(1)

		'''
			load package substance
		'''
		
		cmds.substanceNodeLoadSubstance(substance, sbsarFile)

		'''
			connect utility and substance
		'''
		cmds.connectAttr(utility + '.outUV', substance + '.uvCoord')
		cmds.connectAttr(utility + '.outUvFilterSize', substance + '.uvFilterSize')
		cmds.select(substance)
		return substance

	def createTexture2DSubstance(self, substanceNode, pbrShader):
		try:
			mel.eval("SubstanceOutputHandleActivate "+substanceNode+" "'output_base_color'" "'1'";")
		except:
			pass

		try:
			mel.eval("SubstanceOutputHandleActivate "+substanceNode+" "'output_normal'" "'1'";")
		except:
			pass

		try:
			mel.eval("SubstanceOutputHandleActivate "+substanceNode+" "'output_roughness'" "'1'";")
		except:
			pass

		try:
			mel.eval("SubstanceOutputHandleActivate "+substanceNode+" "'output_metallic'" "'1'";")
		except:
			pass

		try:
			mel.eval("SubstanceOutputHandleActivate "+substanceNode+" "'output_ambient_occlusion'" "'1'";")
		except:
			pass

		self.getSubstanceOutputNode(substanceNode, pbrShader)

	def connectSubstanceOutputNodeToStingrayPBS(self, outputNode, pbrShader, outputType):
		fileNodeList = cmds.listConnections(outputNode, type = 'file')
		fileNode = fileNodeList[0]
		if outputType == 'baseColor':
			cmds.connectAttr(fileNode + ".outColor", pbrShader + ".TEX_BaseColor_Map")
			cmds.setAttr(pbrShader + ".use_color_map", 1)

		if outputType == 'normal':
			cmds.connectAttr(fileNode + ".outColor", pbrShader + ".TEX_Normal_Map")
			cmds.setAttr(pbrShader + ".use_normal_map", 1)

		if outputType == 'metallic':
			cmds.connectAttr(fileNode + ".outColor", pbrShader + ".TEX_Metallic_Map")
			cmds.setAttr(pbrShader + ".use_metallic_map", 1)

		if outputType == 'roughness':
			cmds.connectAttr(fileNode + ".outColor", pbrShader + ".TEX_Roughness_Map")
			cmds.setAttr(pbrShader + ".use_roughness_map", 1)

		if outputType == 'ambientOcclusion':
			cmds.connectAttr(fileNode + ".outColor", pbrShader + ".TEX_AO_Map")
			cmds.setAttr(pbrShader + ".use_ao_map", 1)



	def getSubstanceOutputNode(self, substance, pbrShader):
		output_count = cmds.substanceNodeGetOutputCount(substance)
		for i in range(0, output_count):
			if cmds.substanceNodeGetOutputUsage(substance, i) == 'baseColor':
				output_node = cmds.substanceNodeGetOutputNodeName(substance, i)
				self.connectSubstanceOutputNodeToStingrayPBS(output_node, pbrShader, 'baseColor')
			elif cmds.substanceNodeGetOutputUsage(substance, i) == 'roughness':
				output_node = cmds.substanceNodeGetOutputNodeName(substance, i)
				self.connectSubstanceOutputNodeToStingrayPBS(output_node, pbrShader, 'roughness')
			elif cmds.substanceNodeGetOutputUsage(substance, i) == 'metallic':
				output_node = cmds.substanceNodeGetOutputNodeName(substance, i)
				self.connectSubstanceOutputNodeToStingrayPBS(output_node, pbrShader, 'metallic')
			elif cmds.substanceNodeGetOutputUsage(substance, i) == 'normal':
				output_node = cmds.substanceNodeGetOutputNodeName(substance, i)
				self.connectSubstanceOutputNodeToStingrayPBS(output_node, pbrShader, 'normal')
			elif cmds.substanceNodeGetOutputUsage(substance, i) == 'ambientOcclusion':
				output_node = cmds.substanceNodeGetOutputNodeName(substance, i)
				self.connectSubstanceOutputNodeToStingrayPBS(output_node, pbrShader, 'ambientOcclusion')



	def createSubstanceNodeAndAssignToStingRayPBS(self, sbsFile, fileFormat, width, height):
		shaderFXPath = self.getShaderFXPath()
		sbsarFile = sbsFile.replace(".sbs", ".sbsar")
		fileNameWithoutSuffix = (sbsarFile.split("\\")[-1]).split(".")[0]
		substanceNodeName = fileNameWithoutSuffix + "_substance"
		stingrayMatName = "MAT_" + fileNameWithoutSuffix
		mel.eval('HypershadeWindow;')
		
		self.substanceNode = self.createSubstanceNode(substanceNodeName, sbsarFile, fileFormat, width, height)
		self.pbrShader, sgGroup = self.createStingrayPBRShader(stingrayMatName, shaderFXPath)
		self.createTexture2DSubstance(self.substanceNode, self.pbrShader)
		self.assignMatToSelection(self.correctSelection, self.pbrShader)


	def connectNodeAndMat(self):
		self.createTexture2DSubstance(self.substanceNode, self.pbrShader)
		self.assignMatToSelection(self.correctSelection, self.pbrShader)

	def createLambertForColorIDBaking(self, matName):
		rndH = random.uniform(0.0, 1.0)
		rndS = random.uniform(0.0, 1.0)
		rndV = random.uniform(0.0, 1.0)
		rndColor = colorsys.hsv_to_rgb(rndH, rndS, rndV)

		count = 1
		matNameWithCount = matName + "_" + str(count)
		while cmds.objExists(matNameWithCount):
			matNameWithCount = matName + "_" + str(count + 1)
			count = count + 1
		else:
			cmds.shadingNode("lambert", asShader = True, name = matNameWithCount)
			cmds.sets(renderable = True, noSurfaceShader = True, empty = True, name = matNameWithCount + "_SG")
			cmds.connectAttr(matNameWithCount + ".outColor", matNameWithCount + "_SG" + ".surfaceShader", force = True)
			cmds.setAttr(matNameWithCount + ".color", rndColor[0], rndColor[1], rndColor[2], type='double3')
			return matNameWithCount

	def assignMatToSelection(self, sel, matName):
		for obj in sel:
			cmds.select(obj)
			faces = cmds.polyListComponentConversion(obj, tf=True )
			cmds.sets(e = True, forceElement = matName + "_SG")

	def setMatInListWidget(self, imageList, lwAssignedSBSARMat):
		lwAssignedSBSARMat.clear()
		for image in imageList:
			item = QtWidgets.QListWidgetItem()
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			item.setIcon(icon)
			lwAssignedSBSARMat.addItem(item)

	def getSDShadersFromMesh(self, mesh = None): 
		# get shader from nodes
		shapeNode = cmds.listRelatives(mesh, c = True, f = True)[0]
		shadingGroup = cmds.listConnections(shapeNode, t = 'shadingEngine')
		if not shadingGroup:
			return
		shaders = list()
		for sg in shadingGroup:
			if cmds.connectionInfo(sg + '.surfaceShader', sfd = True):
				shader = cmds.connectionInfo(sg + '.surfaceShader', sfd = True).split('.')[0]
				#if "sd_" in shader.lower():
				shaders.append(shader)
		return list(set(shaders))

	def getAttributeFromShader(self, shaderName, attributeName, isStingrayShader = True):
		if (isStingrayShader):
			try:
				return cmds.getAttr(shaderName + "." + attributeName)
			except ValueError:
				fileNode = cmds.listConnections(shaderName + ".TEX_" + attributeName, type='file')
				if (fileNode != None):
					return cmds.getAttr(fileNode[0], fileNode[0] + ".fileTextureName")
				return ""

	def getColorFromMat(self, matName):
		matColor = cmds.getAttr(matName + ".color")
		return matColor[0]

	def getShaderAndMeshDataDict(self):
		shaderAndMeshDict = {}
		thumbnailAndMeshDict = {}
		allShapesInScene = cmds.ls( type='geometryShape', showType=True, long = True )
		for shape in allShapesInScene:
			if "|" in shape:
				shaderList = []
				assignedMatList = []
				transformNode = "|".join(shape.split("|")[:-1])
				shaderList = self.getSDShadersFromMesh(transformNode)
				shaderAndMeshDict[transformNode] = shaderList
				if shaderList:
					for shader in shaderList:
						originalShaderName = "_".join(shader.split("_")[:-1])
						for thumbnailPath in self.thumbnailList:
							if originalShaderName.lower() == (thumbnailPath.lower().split("/")[-1]).split(".")[0]:
								assignedMatList.append(thumbnailPath)
					thumbnailAndMeshDict[transformNode] = list(set(assignedMatList))

		return shaderAndMeshDict, thumbnailAndMeshDict

	def getOriginalSDMaterial(self, sdMaterialList):
		originalMatList = []
		for mat in sdMaterialList:
			originalShaderName = "_".join(mat.split("_")[:-1])
			originalMatList.append(originalShaderName)
		return originalMatList

	def getCurrentSelectedWeatherEffects(self, cbbWeatherEffects):
		return str(cbbWeatherEffects.currentText())

	def refreshMatInListWidget(self, lwObjectSBSARMatList, AssignedSBSARMatObjectClass):
		shaderAndMeshDataDict, thumbnailAndMeshDict = self.getShaderAndMeshDataDict()
		if shaderAndMeshDataDict:
			for mesh, thumbnail in thumbnailAndMeshDict.items():
				item = QtWidgets.QListWidgetItem()
				widget = AssignedSBSARMatObjectClass()
				widget.changeAssetName(mesh.split("|")[-1])
				widget.setMatInListWidget(thumbnail, widget.lwAssignedSBSARMat)
				lwObjectSBSARMatList.addItem(item)
				item.setSizeHint(widget.minimumSizeHint())
				lwObjectSBSARMatList.setItemWidget(item, widget)

	def refreshWeatherMatInListWidget(self, lwObjectSBSARWeatherEffectList, AssignedSBSARMatObjectClass):
		meshAndWeatherThumbnailDict = self.getWeatherEffectThumbnailFromMaterialDirectory()
		if meshAndWeatherThumbnailDict:
			for mesh, thumbnail in meshAndWeatherThumbnailDict.items():
				item = QtWidgets.QListWidgetItem()
				widget = AssignedSBSARMatObjectClass()
				widget.changeAssetName(mesh.split("|")[-1])
				widget.setMatInListWidget(thumbnail, widget.lwAssignedSBSARMat)
				lwObjectSBSARWeatherEffectList.addItem(item)
				item.setSizeHint(widget.minimumSizeHint())
				lwObjectSBSARWeatherEffectList.setItemWidget(item, widget)

	def addWeatherEffectsToSelectedMeshExtraAttributes(self, mesh, selectedWeatherEffect):
		extraAddtributeName = "weather_effects"
		alreadyAddedFlag = False

		userDefinedAttributeList = cmds.listAttr( mesh, userDefined = True )
		if userDefinedAttributeList:
			for attr in userDefinedAttributeList:
				if extraAddtributeName in attr:
					alreadyAddedFlag = True

		if alreadyAddedFlag == False:
			cmds.addAttr(mesh, ln = extraAddtributeName, dt = "string")
			cmds.setAttr(mesh + "." + extraAddtributeName, e = True, keyable = True)

		addedData = cmds.getAttr(mesh + "." + extraAddtributeName)
		if not addedData:
			cmds.setAttr(mesh + "." + extraAddtributeName, selectedWeatherEffect, type = "string")
		else:
			foundFlag = False
			temp = addedData.split(", ")
			for i in temp:
				if selectedWeatherEffect.lower() == i.lower():
					foundFlag = True
			if foundFlag == False:
				addedData = addedData + ", " + selectedWeatherEffect
				cmds.setAttr(mesh + "." + extraAddtributeName, addedData, type = "string")
		return addedData

	def refreshWeatherEffectsInListWidget(self, cbbWeatherEffects):
		transformNodes = self.getTransformGroupInScene()
		for node in transformNodes:
			selectedWeatherEffect = self.getCurrentSelectedWeatherEffects(cbbWeatherEffects)
			self.addWeatherEffectsToSelectedMeshExtraAttributes(node, selectedWeatherEffect)

	def getAssignedWeatherEffects(self, mesh):
		extraAddtributeName = "weather_effects"
		alreadyAddedFlag = False
		addedData = None
		userDefinedAttributeList = cmds.listAttr( mesh, userDefined = True )
		if userDefinedAttributeList:
			for attr in userDefinedAttributeList:
				if extraAddtributeName in attr:
					alreadyAddedFlag = True

		if alreadyAddedFlag == True:
			addedData = cmds.getAttr(mesh + "." + extraAddtributeName)

		sdLibrary = self.getSDLibraryLocation()
		assignedWeatherList = []
		if sdLibrary != None:
			weatherEffectFolder = sdLibrary + "/" + "weather_effects"
			try:
				splitedWeatherEffectList = addedData.split(", ")
				for assignedWeather in splitedWeatherEffectList:
					for file in os.listdir(weatherEffectFolder):
						if ".sbs" in file.lower():
							if assignedWeather.lower() in file.lower():
								assignedWeatherList.append(weatherEffectFolder + "/" + file)
			except:
				pass

		return assignedWeatherList


	def createMat(self, currentSelectedMaterial):
		checkedPluginInfoFlag = self.checkMayaSubstancePluginAvailable()
		if checkedPluginInfoFlag == True:
			matName = self.materialListWidgetItemDict[str(currentSelectedMaterial[0])]
			for sbsarFile in self.sbsLibraryList:
				if matName.lower() == ((sbsarFile.lower()).split("/")[-1]).split(".")[0]:
					sel = cmds.ls(sl = True, long = True)
					if sel:
						newCreatedMat= self.createLambertForColorIDBaking(matName)
						self.assignMatToSelection(sel, newCreatedMat)

						# mel.eval('HypershadeWindow;')
						# shaderFXPath = self.getShaderFXPath()
						# sbsarFile = sbsFile.replace(".sbs", ".sbsar")
						# fileNameWithoutSuffix = (sbsarFile.split("\\")[-1]).split(".")[0]
						# substanceNodeName = fileNameWithoutSuffix + "_substance"
						# stingrayMatName = "MAT_" + fileNameWithoutSuffix
						
						# self.pbrShader, sgGroup = self.createStingrayPBRShader(stingrayMatName, shaderFXPath)






					else:
						cmds.confirmDialog(title='Missing Selection', message='Please select at least 1 object or faces', icon="critical")
					#self.createStingrayPBRShader("MAT_" + matName, None)
					#self.createSubstanceNode("substance_" + matName, sbsarFile)

	def getMatAndColorIDFromDict(self):
		matAndColorIDDict = {}
		selectedMesh = self.getTransformGroupInScene()
		assignedShaderList = self.getSDShadersFromMesh(mesh = selectedMesh)
		print (assignedShaderList)
		for mat in assignedShaderList:
			matColor = self.getColorFromMat(mat)
			matAndColorIDDict[mat] = matColor

		return matAndColorIDDict

	def getAllAssignedWeatherEffectsFromSelection(self):
		meshAndAssignedWeatherEffectsDict = {}
		transformNodes = self.getTransformGroupInScene()
		for node in transformNodes:
			assignedWeatherEffectList = self.getAssignedWeatherEffects(node)
			if len(assignedWeatherEffectList) > 0:
				meshAndAssignedWeatherEffectsDict[node] = assignedWeatherEffectList
		return meshAndAssignedWeatherEffectsDict

	def getAllAssignedWeatherEffectsFromScene(self):
		meshAndAssignedWeatherEffectsDict = {}
		allShapesInScene = cmds.ls( type='geometryShape', showType=True, long = True )
		for shape in allShapesInScene:
			if "|" in shape:
				shaderList = []
				assignedMatList = []
				transformNode = "|".join(shape.split("|")[:-1])
				assignedWeatherEffectList = self.getAssignedWeatherEffects(transformNode)
				if len(assignedWeatherEffectList) > 0:
					meshAndAssignedWeatherEffectsDict[transformNode] = assignedWeatherEffectList

		return meshAndAssignedWeatherEffectsDict

	def getWeatherEffectThumbnailFromMaterialDirectory(self):
		meshAndWeatherThumbnailDict = {}
		meshAndAssignedWeatherEffectsDict = self.getAllAssignedWeatherEffectsFromScene()
		for mesh, weatherEffectFullPathList in meshAndAssignedWeatherEffectsDict.items():
			weatherThumbnailList = []
			for eachWeather in weatherEffectFullPathList:
				if "_weather_effects" in eachWeather.lower():
					eachWeather = eachWeather.replace("_weather_effects", "")
					if "/weather_effects" in eachWeather.lower():
						eachWeather = eachWeather.replace("/weather_effects", "/materials")
						if ".sbs" in eachWeather.lower():
							weatherEffectThumbnailFullPath = eachWeather.replace(".sbs", ".png")
							weatherThumbnailList.append(weatherEffectThumbnailFullPath)
			meshAndWeatherThumbnailDict[mesh] = weatherThumbnailList

		return meshAndWeatherThumbnailDict

	def removeWeatherEffectFromMesh(self, mesh, cbbWeatherEffects):
		currentWeatherEffect = self.getCurrentSelectedWeatherEffects(cbbWeatherEffects)
		extraAddtributeName = "weather_effects"
		alreadyAddedFlag = False

		userDefinedAttributeList = cmds.listAttr( mesh, userDefined = True )
		if userDefinedAttributeList:
			for attr in userDefinedAttributeList:
				if extraAddtributeName in attr:
					alreadyAddedFlag = True

		if alreadyAddedFlag == True:
			addedData = cmds.getAttr(mesh + "." + extraAddtributeName)
			newAddedData = ""
			splitedWeatherEffectList = addedData.split(", ")
			i = 0
			for weather in splitedWeatherEffectList:
				if currentWeatherEffect == weather:
					splitedWeatherEffectList.remove(weather)
			for i in range(0, len(splitedWeatherEffectList)):
				if i == 0:
					newAddedData = newAddedData + splitedWeatherEffectList[i]
				else:
					newAddedData = newAddedData + ", " + splitedWeatherEffectList[i]
				i = i + 1
			if not newAddedData:
				cmds.deleteAttr(mesh + "." + extraAddtributeName, at = extraAddtributeName)
			else:
				cmds.setAttr(mesh + "." + extraAddtributeName, newAddedData, type = "string")

	def removeWeatherEffectFromSelection(self, cbbWeatherEffects):
		selectedMesh = self.getTransformGroupInScene()
		for mesh in selectedMesh:
			self.removeWeatherEffectFromMesh(mesh, cbbWeatherEffects)