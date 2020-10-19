import maya.cmds as cmds
import math
import os
import PySide2
from PySide2 import QtGui
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
rootDirectory = "/".join((currentFilePath.split("/")[:-4]))

checkerMapResources = rootDirectory + "/" + "lib" + "/" + "resource" + "/" + "checkers"
iconResources = rootDirectory + "/" + "lib" + "/" + "icon"
shaderLibrary = rootDirectory + "/" + "lib" + "/" + "shader_library"

checkerMapList = ["checker_map_256x256.png", "checker_map_512x512.png", "checker_map_1024x1024.png", "checker_map_2048x2048.png"]
shaderName = "puzzle_checker"
cycleCheckerCount = 0

class TexelDensityFunction():
	def __init__(self):
		self.MaterialObjOriginalDict = {}

	def getTexelDensity(self, mapWidth, mapHeight):
		if len(cmds.ls(sl = True)) > 0:
			# Convert selection to faces 
			previousSelection = cmds.ls(sl = True)
			selectionFaces = cmds.polyListComponentConversion(toFace = True)
			# Calculate area of faces
			areaGeo = cmds.polyEvaluate(selectionFaces, worldFaceArea = True)
			# Calculate area of UV
			areaUV = cmds.polyEvaluate(selectionFaces, uvFaceArea = True)
			area3DSum = 0.0
			area2DSum = 0.0
			for eachArea in areaGeo:
				area3DSum = area3DSum + eachArea
			for eachArea in areaUV:
				area2DSum = area2DSum  + eachArea

			textureArea = mapWidth * mapHeight
			usedAreaPixels = area2DSum * textureArea
			texelDensity = math.sqrt(usedAreaPixels/area3DSum)
			texelDensity = round(texelDensity, 4)
			cmds.select(previousSelection, replace = True)
			return texelDensity
		else:
			return False

	def setTexelDensity(self, texelDensityInput, mapWidth, mapHeight):
		if len(cmds.ls(sl = True)) > 0:
			# Convert selection to UVs 
			previousSelection = cmds.ls(sl = True)
			texelDensityCluster = self.getTexelDensity(mapWidth, mapHeight)
			cmds.select(cmds.polyListComponentConversion(toUV = True), replace = True)
			#calculate center
			x = cmds.ls(sl=True, flatten = True)
			u = 0
			v = 0
			for i in x:
				u += cmds.polyEditUV(i, query = True)[0]
				v += cmds.polyEditUV(i, query = True)[1]
			u = u/len(x)
			v = v/len(x)

			theDefinedRatio = texelDensityInput / texelDensityCluster
			cmds.polyEditUV(pivotU=u, pivotV=v, scaleU = theDefinedRatio, scaleV = theDefinedRatio)
			cmds.select(previousSelection, replace = True)
		else:
			return False

	def rememberCurrentMaterial(self, obj):
		theNodes = cmds.ls(obj, dag = True, s = True)
		shadeEng = cmds.listConnections(theNodes, type = "shadingEngine")
		materials = cmds.ls(cmds.listConnections(shadeEng), materials = True)
		if materials[0] != "{}_material".format(shaderName):
			return materials[0]
		else:
			return None

	def cycleCheckerMap(self, selectionList):
		if len(selectionList) > 0:
			global cycleCheckerCount
			try:
				file = checkerMapResources + "/" + checkerMapList[cycleCheckerCount]
			except:
				file = checkerMapResources + "/" + checkerMapList[0]
				cycleCheckerCount = 0
			cycleCheckerCount = cycleCheckerCount + 1

			for obj in selectionList:
				objMat = self.rememberCurrentMaterial(obj)
				if objMat != None:
					self.MaterialObjOriginalDict[obj] = objMat

			if not cmds.objExists("{}_fileNode".format(shaderName)):
				# Create a file texture node
				file_node=cmds.shadingNode("file", asTexture=True, name = "{}_fileNode".format(shaderName))
			else:
				cmds.select("{}_fileNode".format(shaderName))
				file_node = cmds.ls(sl = True)[0]

			# Set checker map to file texture node
			cmds.setAttr("{}_fileNode.fileTextureName".format(shaderName), file, type = "string")

			if not cmds.objExists("{}_uvNode".format(shaderName)):
				# Create a uv node
				uvNode = cmds.shadingNode("place2dTexture", asUtility=True, name="{}_uvNode".format(shaderName))
			else:
				cmds.select("{}_uvNode".format(shaderName))
				uvNode = cmds.ls(sl = True)[0]

			# Connect UV Node to file texture Node
			cmds.connectAttr("{}_uvNode.coverage".format(shaderName), "{}_fileNode.coverage".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.translateFrame".format(shaderName), "{}_fileNode.translateFrame".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.rotateFrame".format(shaderName), "{}_fileNode.rotateFrame".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.mirrorU".format(shaderName), "{}_fileNode.mirrorU".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.mirrorV".format(shaderName), "{}_fileNode.mirrorV".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.stagger".format(shaderName), "{}_fileNode.stagger".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.wrapU".format(shaderName), "{}_fileNode.wrapU".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.wrapV".format(shaderName), "{}_fileNode.wrapV".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.repeatUV".format(shaderName), "{}_fileNode.repeatUV".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.offset".format(shaderName), "{}_fileNode.offset".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.rotateUV".format(shaderName), "{}_fileNode.rotateUV".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.noiseUV".format(shaderName), "{}_fileNode.noiseUV".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.vertexUvOne".format(shaderName), "{}_fileNode.vertexUvOne".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.vertexUvTwo".format(shaderName), "{}_fileNode.vertexUvTwo".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.vertexUvThree".format(shaderName), "{}_fileNode.vertexUvThree".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.vertexCameraOne".format(shaderName), "{}_fileNode.vertexCameraOne".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.outUV".format(shaderName), "{}_fileNode.uv".format(shaderName), f = True)
			cmds.connectAttr("{}_uvNode.outUvFilterSize".format(shaderName), "{}_fileNode.uvFilterSize".format(shaderName), f = True)

			if not cmds.objExists("{}_material".format(shaderName)):
				# Create a blinn material
				sha = cmds.shadingNode('blinn', asShader=True, name="{}_material".format(shaderName))
			else:
				cmds.select("{}_material".format(shaderName))
				sha = cmds.ls(sl = True)[0]

			if not cmds.objExists("{}_sg".format(shaderName)):
				# Create a shading group
				sg = cmds.sets(empty=True, renderable=True, noSurfaceShader=True,  name="{}_sg".format(shaderName))
			else:
				cmds.select("{}_sg".format(shaderName))
			# Connect shading group to blinn material
			cmds.connectAttr("{}_material.outColor".format(shaderName), "{}_sg.surfaceShader".format(shaderName), f=True)
			# Connect material to file texture node
			cmds.connectAttr("{}_fileNode.outColor".format(shaderName), "{}_material.color".format(shaderName), f=True)
			# Assign shader to objects
			cmds.sets(selectionList, e=True, forceElement="{}_sg".format(shaderName))
			cmds.select(selectionList)
			return True
		else:
			return False

	def resetToOriginalMat(self):
		if len(self.MaterialObjOriginalDict) > 0:
			for obj, mat in self.MaterialObjOriginalDict.items():
				cmds.select(obj)
				cmds.hyperShade(assign = mat)

	def tilingCheckerMap(self, tilingUValue, tilingVValue):
		if cmds.objExists("{}_uvNode".format(shaderName)):
			cmds.setAttr("{}_uvNode.repeatU".format(shaderName), tilingUValue)
			cmds.setAttr("{}_uvNode.repeatV".format(shaderName), tilingVValue)

	def getCurrentCheckerMap(self):
		if cmds.objExists("{}_fileNode".format(shaderName)):
			texturePath = cmds.getAttr("{}_fileNode.fileTextureName".format(shaderName))
			return texturePath
		else:
			return None

	def checkDXPluginsAndViewport(self):
		renderingEngine = cmds.optionVar(query = "vp2RenderingEngine")
		if renderingEngine != "DirectX11":
			return False
		else:
			cmds.loadPlugin("dx11Shader", quiet = True )
			return True


	def assignCheckerMaterial(self, selectionList):
		if len(selectionList) > 0:
			pluginAndViewportCheckResult = self.checkDXPluginsAndViewport()
			if pluginAndViewportCheckResult == True:
				if not cmds.objExists("{}_shader".format(shaderName)):
					# Create a blinn material
					sha = cmds.shadingNode('dx11Shader', asShader=True, name="{}_shader".format(shaderName))
				if not cmds.objExists("{}_shader_sg".format(shaderName)):
					# Create a shading group
					sg = cmds.sets(empty=True, renderable=True, noSurfaceShader=True,  name="{}_shader_sg".format(shaderName))

				cmds.connectAttr("{}_shader.outColor".format(shaderName), "{}_shader_sg.surfaceShader".format(shaderName), f=True)
				texelDensityShaderPath = shaderLibrary + "/" + "Texel_Density.fx"
				cmds.setAttr("{}_shader.shader".format(shaderName), texelDensityShaderPath.replace("/","\\"), type = "string")
				cmds.sets(selectionList, e=True, forceElement="{}_shader_sg".format(shaderName))
				cmds.select(selectionList)
				return True
			else:
				return False
		else:
			return None


				#return True

	def setDefaultComboBoxValue(self, comboBox):
		comboBox.addItems(["128", "256", "512", "1024", "2048", "4096"])
		comboBox.setCurrentText("512")

	def setDefaultButtonIcon(self, btnCycleCheckerMap, btnReset, btnAssignCheckerMaterial):
		btnCycleCheckerMap.setIcon(QtGui.QIcon(iconResources + "/checker_icon.jpg"))
		btnReset.setIcon(QtGui.QIcon(iconResources + "/reset.jpg"))
		btnAssignCheckerMaterial.setIcon(QtGui.QIcon(iconResources + "/checker_material.jpg"))