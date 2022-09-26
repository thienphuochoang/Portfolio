import os
import pysbs
import sys
from pysbs import context
from pysbs import sbsenum
from pysbs import sbsgenerator
import subprocess
import importlib
currentFilePath = os.path.dirname(os.path.abspath(__file__))
rootPath = currentFilePath.replace("\\","/")
rootPath = "/".join(rootPath.split("/")[:-3])
import maya.cmds as cmds 
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

mat_creation_function = importerFunction.importModule("puzzle_maya.sbsar_mat_creation.function.mat_creation_function")
exportSBSARFunction = importerFunction.importModule('puzzle_substance_designer.sbsar_exporter.function.export_sbsar_function')
sdLibrarySBSARExportFunction = importerFunction.importModule('launch.sd_library_sbsar_export_launcher')

class InputNodeFunction():
	def __init__(self, sbsDoc, aGraph, nodePath, posX, posY, posZ):
		self.sbsDoc = sbsDoc
		self.aGraph = aGraph
		self.nodePath = nodePath
		self.posX = posX
		self.posY = posY
		self.posZ = posZ


	def importBitmapNode(self, colorMode):
		importedNode = self.aGraph.createBitmapNode(aSBSDocument  = self.sbsDoc,
													aResourcePath = self.nodePath,
													aParameters   = {sbsenum.CompNodeParamEnum.COLOR_MODE: colorMode},
													aGUIPos	      = [self.posX, self.posY, self.posZ])
		return importedNode

	def createLevelNodeForBitmapNode(self):
		levelNodeForBitmapNode = self.aGraph.createCompFilterNode(aFilter	    = sbsenum.FilterEnum.LEVELS,
																  aGUIPos	    = [self.posX + 300, self.posY, self.posZ],
																  aInheritance  = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})

		return levelNodeForBitmapNode

	def connectBitmapNodeToLevelNode(self, importedBitmapNode, levelNodeForBitmapNode):
		self.aGraph.connectNodes(aLeftNode = importedBitmapNode, aRightNode = levelNodeForBitmapNode)

	def importMaterialNode(self):
		matNode = self.aGraph.createCompInstanceNodeFromPath(aSBSDocument 	 = self.sbsDoc,
															 aPath		 	 = self.nodePath,
															 aGUIPos	  	 = [self.posX, self.posY, self.posZ],
															 aInheritance 	 = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
		return matNode

	def connectLevelOfBitmapNodeToImportedMaterialNode(self, levelNodeOfBitmap, importedMaterialNode, pattern):
		try:
			self.aGraph.connectNodes(aLeftNode = levelNodeOfBitmap, aRightNode = importedMaterialNode, aRightNodeInput = "input" + "_" + pattern)
		except:
			pass

	def createMultiMaterialBlendNode(self, sbsDependencyLibraryPath, matAndColorIDDict):
		self.matAndColorIDDict = matAndColorIDDict
		self.sbsDependencyLibraryPath = sbsDependencyLibraryPath
		blendMaterialNode = self.aGraph.createCompInstanceNodeFromPath(aSBSDocument = self.sbsDoc,
																  	   aPath		= self.nodePath,
																       aParameters  = {'Materials':int(len(self.matAndColorIDDict)), 'ambient_occlusion': True, 'diffuse': False, 'specular': False, 'glossiness': False},
																       aGUIPos	    = [self.posX, self.posY, self.posZ],
																       aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
		return blendMaterialNode

	def setColorIDForMultiMaterialBlendNode(self, index, colorValue, multiMatBlendNode):
		if index > 1:
			redVal = colorValue[0]
			greenVal = colorValue[1]
			blueVal = colorValue[2]
			rgbVal = str(redVal) + " " + str(greenVal) + " " + str(blueVal)
			multiMatBlendNode.setParameterValue("Material_"+str(index)+"_Color", rgbVal)
			#print (multiMatBlendNode.getParameterValue("Material_"+str(index)+"_Color"))

	def connectMaterialNodeToMultiMaterialBlendNode(self, multiMatBlendNode, materialNode, index):
		# Connect material node to multi material blend
		self.aGraph.connectNodes(aLeftNode = materialNode, aRightNode = multiMatBlendNode, aLeftNodeOutput = "output_base_color", aRightNodeInput = "material"+str(index)+"_basecolor")

		try:
			self.aGraph.connectNodes(aLeftNode = materialNode, aRightNode = multiMatBlendNode, aLeftNodeOutput = "output_normal", aRightNodeInput = "material"+str(index)+"_normal")
		except:
			pass
		
		try:
			self.aGraph.connectNodes(aLeftNode = materialNode, aRightNode = multiMatBlendNode, aLeftNodeOutput = "output_metallic", aRightNodeInput = "material"+str(index)+"_metallic")
		except:
			pass
		
		try:
			self.aGraph.connectNodes(aLeftNode = materialNode, aRightNode = multiMatBlendNode, aLeftNodeOutput = "output_roughness", aRightNodeInput = "material"+str(index)+"_roughness")
		except:
			pass

		try:
			self.aGraph.connectNodes(aLeftNode = materialNode, aRightNode = multiMatBlendNode, aLeftNodeOutput = "output_height", aRightNodeInput = "material"+str(index)+"_height")
		except:
			pass

		try:
			self.aGraph.connectNodes(aLeftNode = materialNode, aRightNode = multiMatBlendNode, aLeftNodeOutput = "output_ambient_occlusion", aRightNodeInput = "material"+str(index)+"_ambientocclusion")
		except:
			pass
	def connectMultiMaterialBlendNodeToWeatherNode(self, multiMatBlendNode, weatherEffectNode):

		try:
			self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = weatherEffectNode, aLeftNodeOutput = "basecolor", aRightNodeInput = "input_base_color")
		except:
			pass

		try:
			self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = weatherEffectNode, aLeftNodeOutput = "Normal", aRightNodeInput = "input_normal")
		except:
			pass

		try:
			self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = weatherEffectNode, aLeftNodeOutput = "Roughness", aRightNodeInput = "input_roughness")
		except:
			pass

		try:
			self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = weatherEffectNode, aLeftNodeOutput = "Metallic", aRightNodeInput = "input_metallic")
		except:
			pass

		try:
			self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = weatherEffectNode, aLeftNodeOutput = "AmbientOcclusion", aRightNodeInput = "input_ambient_occlusion")
		except:
			pass

		try:
			self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = weatherEffectNode, aLeftNodeOutput = "Height", aRightNodeInput = "input_height")
		except:
			pass

	def connectPreviousWeatherNodeResultsToTheCurrentWeatherNode(self, previousWeatherNode, currentWeatherNode, inputNodeDict):
		allPreviousWeatherNodeDef = previousWeatherNode.getDefinition()
		allCurrentWeatherNodeDef = currentWeatherNode.getDefinition()
		if len(allPreviousWeatherNodeDef.getAllOutputIdentifiers()) > len(allCurrentWeatherNodeDef.getAllInputIdentifiers()):
			for output in allPreviousWeatherNodeDef.getAllOutputIdentifiers():
				replacedOutputName = output.replace("output_", "input_")
				for input in allCurrentWeatherNodeDef.getAllInputIdentifiers():
					if replacedOutputName == input:
						try:
							self.aGraph.connectNodes(aLeftNode = previousWeatherNode, aRightNode = currentWeatherNode, aLeftNodeOutput = output, aRightNodeInput = input)
						except:
							pass
		else:
			for input in allCurrentWeatherNodeDef.getAllInputIdentifiers():
				replacedInputName = input.replace("input_", "output_")
				for output in allPreviousWeatherNodeDef.getAllOutputIdentifiers():
					if replacedInputName == output:
						try:
							self.aGraph.connectNodes(aLeftNode = previousWeatherNode, aRightNode = currentWeatherNode, aLeftNodeOutput = output, aRightNodeInput = input)
						except:
							pass

	def createOutputNodesAndConnectLatestWeatherNodeToOutputNodes(self, latestWeatherNode):
		compOutputList = latestWeatherNode.mCompOutputs
		for output in compOutputList:
			aIdentifier = latestWeatherNode.getCompOutputIdentifier(output.mUID)
			if "output_base_color" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = aIdentifier,
														  aGUIPos	  = [self.posX, self.posY, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.BASECOLOR: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = latestWeatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			if "output_normal" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = aIdentifier,
														  aGUIPos	  = [self.posX, self.posY + 150, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.NORMAL: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = latestWeatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			if "output_metallic" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = aIdentifier,
														  aGUIPos	  = [self.posX, self.posY + 300, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.METALLIC: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = latestWeatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			if "output_roughness" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = aIdentifier,
														  aGUIPos	  = [self.posX, self.posY + 450, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.ROUGHNESS: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = latestWeatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			if "output_ambient_occlusion" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = aIdentifier,
														  aGUIPos	  = [self.posX, self.posY + 600, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.AMBIENT_OCCLUSION: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = latestWeatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)

	def connectLevelNodeToWeatherEffectNode(self, weatherEffectNode, multiMatBlendNode, inputNodeDict):
		for pattern, value in inputNodeDict.items():
			if pattern == "ambient_occlusion":
				try:
					self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = weatherEffectNode, aLeftNodeOutput = "AmbientOcclusion", aRightNodeInput = rightNodeInput)
				except:
					pass
			else:
				levelNodeOfBitmap = value[1]
				rightNodeInput = "input" + "_" + pattern
				try:
					self.aGraph.connectNodes(aLeftNode = levelNodeOfBitmap, aRightNode = weatherEffectNode, aRightNodeInput = rightNodeInput)
				except:
					pass
		return weatherEffectNode

	def createOutputNodesAndConnectMultiMatBlendNodeToOutputNode(self, multiMatBlendNode):
		compOutputList = multiMatBlendNode.mCompOutputs
		for output in compOutputList:
			aIdentifier = multiMatBlendNode.getCompOutputIdentifier(output.mUID)
			if "basecolor" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = "output_base_color",
														  aGUIPos	  = [self.posX, self.posY, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.BASECOLOR: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			if "Normal" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = "output_normal",
														  aGUIPos	  = [self.posX, self.posY + 150, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.NORMAL: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			if "Metallic" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = "output_metallic",
														  aGUIPos	  = [self.posX, self.posY + 300, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.METALLIC: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			if "Roughness" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = "output_roughness",
														  aGUIPos	  = [self.posX, self.posY + 450, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.ROUGHNESS: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			if "AmbientOcclusion" in aIdentifier:
				outputNode = self.aGraph.createOutputNode(aIdentifier = "output_ambient_occlusion",
														  aGUIPos	  = [self.posX, self.posY + 600, self.posZ],
														  aUsages	  = {sbsenum.UsageEnum.AMBIENT_OCCLUSION: {sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})
				self.aGraph.connectNodes(aLeftNode = multiMatBlendNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)

	def connectColorIDBitmapNodeToMultiMaterialBlendNode(self, colorIDBitmapNode, multiMatBlendNode):
		self.aGraph.connectNodes(aLeftNode = colorIDBitmapNode, aRightNode = multiMatBlendNode, aRightNodeInput = "Input_160")

	def getExposedMaterialParameter(self, node):
		nodeParameterDict = {}
		inputParameterDict = {}
		listOfInputParameters = node.getDefinition().getAllParameters()
		for parameter in listOfInputParameters:
			if (isinstance((parameter.getIdentifier()), int) == True) or (isinstance((parameter.getIdentifier()), float) == True):
				pass
			else:
				# Append input parameter to dictionary (identifier + type)
				if parameter.mType == 4:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.BUTTON_BOOL
				if parameter.mType == 16:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.SLIDER_INT1
				if parameter.mType == 32:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.SLIDER_INT2
				if parameter.mType == 64:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.SLIDER_INT3
				if parameter.mType == 128:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.SLIDER_INT4
				if parameter.mType == 256:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.SLIDER_FLOAT1
				if parameter.mType == 512:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.SLIDER_FLOAT2
				if parameter.mType == 1024:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.COLOR_FLOAT3
				if parameter.mType == 2048:
					inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.COLOR_FLOAT4
		nodeParameterDict[node] = inputParameterDict
		return nodeParameterDict

	def exposeImportedMaterialParameterToMainParameter(self, node, matName):
		nodeParameterDict = self.getExposedMaterialParameter(node)
		for importedNode, parameterDict in nodeParameterDict.items():
			pkgPath = importedNode.getCompInstance().mPath
			uniqueIdentifier = (pkgPath.split("pkg:///")[-1]).split("?")[0]
			for key, value in parameterDict.items():
				defaultNodeParameterValue = node.getParameterValue(aParameter = key)
				if matName != None:
					aGraphParameter = self.aGraph.addInputParameter(aIdentifier = matName + "_" + key, aWidget = value, aGroup = matName, aLabel = key, aDefaultValue = defaultNodeParameterValue)
					# Link graph parameter + weather node parameter
					aGraphFunction = node.setDynamicParameter(aParameter = key)
					aGraphFunction.setToInputParam(aParentGraph = self.aGraph, aInputParamIdentifier = matName + "_" + key)
				else:
					aGraphParameter = self.aGraph.addInputParameter(aIdentifier = uniqueIdentifier + "_" + key, aWidget = value, aGroup = uniqueIdentifier, aLabel = key, aDefaultValue = defaultNodeParameterValue)
					# Link graph parameter + weather node parameter
					aGraphFunction = node.setDynamicParameter(aParameter = key)
					aGraphFunction.setToInputParam(aParentGraph = self.aGraph, aInputParamIdentifier = uniqueIdentifier + "_" + key)



class PYSBSCreationWorkflowFunction():
	def __init__(self):
		self.matCreationFunctionInstance = mat_creation_function.MatCreationFunction()
		self.exportSBSARFunctionInstance = exportSBSARFunction.SDExportSbsarFunction()
		self.sdLibrarySBSARExportFunctionInstance = sdLibrarySBSARExportFunction.LauncherFunction()

	def setInputsForFileSBSCreation(self, cbbUseUpperSettings, leInputPath, leInputName, leOutputPath, leOutputName):
		if cbbUseUpperSettings.isChecked():
			leInputPath.setText(leOutputPath.text())
			leInputName.setText(leOutputName.text())

	# def getOriginalSDMatFromMesh(self):
	# 	assignedMatAndOriginalSDMatDict = {}
	# 	selectedMesh = self.matCreationFunctionInstance.getTransformGroupInScene()
	# 	assignedMatList = self.matCreationFunctionInstance.getSDShadersFromMesh(selectedMesh)
	# 	originalSDMatList = self.matCreationFunctionInstance.getOriginalSDMaterial(assignedMatList)

	# 	for i in range(0, len(assignedMatList)):
	# 		assignedMatAndOriginalSDMatDict[assignedMatList[i]] = originalSDMatList[i]

	# 	return assignedMatAndOriginalSDMatDict

	def getMatAndColorIDFromDict(self):
		matAndColorIDDict = self.matCreationFunctionInstance.getMatAndColorIDFromDict()
		return matAndColorIDDict

	def convertMapSizeInput(self, width, height):
		width = str(width)
		height = str(height)

		convertMapSizeDict = {"128": sbsenum.OutputSizeEnum.SIZE_128,
		"256": sbsenum.OutputSizeEnum.SIZE_256,
		"512": sbsenum.OutputSizeEnum.SIZE_512,
		"1024": sbsenum.OutputSizeEnum.SIZE_1024,
		"2048": sbsenum.OutputSizeEnum.SIZE_2048,
		"4096": sbsenum.OutputSizeEnum.SIZE_4096}

		convertedWidth = convertMapSizeDict[width]
		convertedHeight = convertMapSizeDict[height]

		return convertedWidth, convertedHeight

	def getInputsForFileSBSCreation(self, *args):
		self.inputPath = args[0]
		self.inputName = args[1]
		self.fileFormat = args[2]
		mapOutputSizeWidth = args[3]
		mapOutputSizeHeight = args[4]
		self.meshAndAssignedWeatherEffectsDict = args[5]
		self.convertedWidth, self.convertedHeight = self.convertMapSizeInput(mapOutputSizeWidth, mapOutputSizeHeight)

		self.colorIDKeyword = "color_id"
		self.ambientOcclusionKeyword = "ambient_occlusion"
		self.curvatureKeyword = "curvature"
		self.positionKeyword = "position"
		self.worldSpaceNormalsKeyword = "world_space_normals"
		self.normalKeyword = "normal"

		self.ColorID_Node_Path = self.inputPath + "\\" + self.inputName + "_" + self.colorIDKeyword + "." + self.fileFormat
		self.AmbientOcclusion_Node_Path = self.inputPath + "\\" + self.inputName + "_" + self.ambientOcclusionKeyword + "." + self.fileFormat
		self.Curvature_Node_Path = self.inputPath + "\\" + self.inputName + "_" + self.curvatureKeyword + "." + self.fileFormat
		self.Position_Node_Path = self.inputPath + "\\" + self.inputName + "_" + self.positionKeyword + "." + self.fileFormat
		self.WorldSpaceNormal_Node_Path = self.inputPath + "\\" + self.inputName + "_" + self.worldSpaceNormalsKeyword + "." + self.fileFormat
		self.Normal_Node_Path = self.inputPath + "\\" + self.inputName + "_" + self.normalKeyword + "." + self.fileFormat
		self.sbsDestination = self.inputPath + "\\" + self.inputName + "." + "sbs"
		self.sbsMaterialLibraryPath = rootPath + "\\" + "lib" + "\\" + "substance_designer_library" + "\\" + "materials"
		self.sbsWeatherLibraryPath = rootPath + "\\" + "lib" + "\\" + "substance_designer_library" + "\\" + "weather_effects"
		self.sbsDependencyLibraryPath = rootPath + "\\" + "lib" + "\\" + "substance_designer_library" + "\\" + "packages"

		# self.assignedMatList = self.getOriginalSDMatFromMesh()
		self.checkInputNodeDict = self.checkInputNodeExistance()

	def checkInputNodeExistance(self):
		checkNodeDict = {}

		if os.path.exists(self.ColorID_Node_Path):
			checkNodeDict[self.ColorID_Node_Path] = True
		else:
			checkNodeDict[self.ColorID_Node_Path] = False

		if os.path.exists(self.AmbientOcclusion_Node_Path):
			checkNodeDict[self.AmbientOcclusion_Node_Path] = True
		else:
			checkNodeDict[self.AmbientOcclusion_Node_Path] = False

		if os.path.exists(self.Curvature_Node_Path):
			checkNodeDict[self.Curvature_Node_Path] = True
		else:
			checkNodeDict[self.Curvature_Node_Path] = False

		if os.path.exists(self.Position_Node_Path):
			checkNodeDict[self.Position_Node_Path] = True
		else:
			checkNodeDict[self.Position_Node_Path] = False

		if os.path.exists(self.WorldSpaceNormal_Node_Path):
			checkNodeDict[self.WorldSpaceNormal_Node_Path] = True
		else:
			checkNodeDict[self.WorldSpaceNormal_Node_Path] = False

		if os.path.exists(self.Normal_Node_Path):
			checkNodeDict[self.Normal_Node_Path] = True
		else:
			checkNodeDict[self.Normal_Node_Path] = False

		return checkNodeDict

	def cookSBS(self, *args):
		self.getInputsForFileSBSCreation(*args)

		inputNodeDict = {}
		aContext = context.Context()

		startPosX = 0
		startPosY = 0
		startPosZ = 0


		# Create a new SBSDocument from scratch
		sbsDoc = sbsgenerator.createSBSDocument(aContext, aFileAbsPath = self.sbsDestination)

		# Create the graph
		temp = self.sbsDestination.split("\\")[-1]
		graphName = temp.split(".")[0]
		aGraph = sbsDoc.createGraph(aGraphIdentifier = graphName)
		aGraph.setDefaultParentSize(aWidth = self.convertedWidth, aHeight = self.convertedHeight)

		

		# Create Input Node
		inputNodePosCount = 0
		for nodePath, existChecked in self.checkInputNodeDict.items():
			if existChecked == True:
				outputNameAndPattern = (nodePath.split(".")[0]).split("\\")[-1]
				if ((self.inputName + "_" + self.ambientOcclusionKeyword) == outputNameAndPattern) or ((self.inputName + "_" + self.curvatureKeyword) == outputNameAndPattern):
					onlyPattern = outputNameAndPattern.replace(self.inputName + "_", "")

					inputNode = InputNodeFunction(sbsDoc, aGraph, nodePath, startPosX, startPosY + inputNodePosCount, startPosZ)
					importedBitmapNode = inputNode.importBitmapNode(False)
					

					# Create Level Node for Input Node
					levelNodeForBitmapNode = inputNode.createLevelNodeForBitmapNode()
					# Connect Input Node and Level Node
					inputNode.connectBitmapNodeToLevelNode(importedBitmapNode, levelNodeForBitmapNode)

					inputNodeDict[onlyPattern] = [importedBitmapNode, levelNodeForBitmapNode]
					inputNodePosCount = inputNodePosCount + 100

				else:
					onlyPattern = outputNameAndPattern.replace(self.inputName + "_", "")

					inputNode = InputNodeFunction(sbsDoc, aGraph, nodePath, startPosX, startPosY + inputNodePosCount, startPosZ)
					importedBitmapNode = inputNode.importBitmapNode(True)

					# Create Level Node for Input Node
					levelNodeForBitmapNode = inputNode.createLevelNodeForBitmapNode()
					# Connect Input Node and Level Node
					inputNode.connectBitmapNodeToLevelNode(importedBitmapNode, levelNodeForBitmapNode)

					inputNodeDict[onlyPattern] = [importedBitmapNode, levelNodeForBitmapNode]
					inputNodePosCount = inputNodePosCount + 100

		# Get Material color ID
		matAndColorIDDict = self.getMatAndColorIDFromDict()
		print (matAndColorIDDict)
		# Create multi-material blend node
		multiMaterialPath = self.sbsDependencyLibraryPath + "/multi_material_blend.sbs/multi_material_blend"
		inputNode = InputNodeFunction(sbsDoc, aGraph, multiMaterialPath, startPosX + 800, startPosY, startPosZ)
		multiMatBlendNode = inputNode.createMultiMaterialBlendNode(self.sbsDependencyLibraryPath, matAndColorIDDict)

		# Import material
		matPosCount = 200
		if len(matAndColorIDDict) > 0:
			index = 1
			for matName, colorVal in matAndColorIDDict.items():
				originalMatName = "_".join((matName.split("_")[:-1]))
				fullOriginalMatPath = self.sbsMaterialLibraryPath + "\\" + originalMatName + ".sbs"
				inputNode = InputNodeFunction(sbsDoc, aGraph, fullOriginalMatPath, startPosX + 500, startPosY + matPosCount, startPosZ)

				importedMaterialNode = inputNode.importMaterialNode()
				inputNode.exposeImportedMaterialParameterToMainParameter(importedMaterialNode, matName)
				matPosCount = matPosCount + 200
				# Connect material node to multi material blend node
				inputNode.connectMaterialNodeToMultiMaterialBlendNode(multiMatBlendNode, importedMaterialNode, index)
				# Set color ID for multi material blend node
				inputNode.setColorIDForMultiMaterialBlendNode(index, colorVal, multiMatBlendNode)
				
				for pattern, value in inputNodeDict.items():
					if pattern != "color_id":
						levelNodeOfBitmap = value[1]

						# Connect level's bitmap node to imported material node
						inputNode.connectLevelOfBitmapNodeToImportedMaterialNode(levelNodeOfBitmap, importedMaterialNode, pattern)
					else:
						colorIDBitmapNode = value[0]
						inputNode.connectColorIDBitmapNodeToMultiMaterialBlendNode(colorIDBitmapNode, multiMatBlendNode)
				index = index + 1


		# Import weather effect graph
		matPosCount = 200
		latestWeatherNode = None
		if len(self.meshAndAssignedWeatherEffectsDict) > 0:
			index = 0
			previousWeatherNode = None
			for mesh, weatherEffectFullPathList in self.meshAndAssignedWeatherEffectsDict.items():
				for eachWeather in weatherEffectFullPathList:
					inputNode = InputNodeFunction(sbsDoc, aGraph, eachWeather, startPosX + 1200, startPosY + matPosCount, startPosZ)
					importedWeatherEffectNode = inputNode.importMaterialNode()
					inputNode.exposeImportedMaterialParameterToMainParameter(importedWeatherEffectNode, None)

					matPosCount = matPosCount + 200
					# Connect multi material blend node to weather effect node
					if index == 0:
						inputNode.connectMultiMaterialBlendNodeToWeatherNode(multiMatBlendNode, importedWeatherEffectNode)

						#Connect input nodes to weather effect node
						previousWeatherNode = inputNode.connectLevelNodeToWeatherEffectNode(importedWeatherEffectNode, multiMatBlendNode, inputNodeDict)

						latestWeatherNode = importedWeatherEffectNode

					else:
						inputNode.connectPreviousWeatherNodeResultsToTheCurrentWeatherNode(previousWeatherNode, importedWeatherEffectNode, inputNodeDict)

						previousWeatherNode = inputNode.connectLevelNodeToWeatherEffectNode(importedWeatherEffectNode, multiMatBlendNode, inputNodeDict)

						latestWeatherNode = importedWeatherEffectNode


					index = index + 1
			# Create output nodes and connect latest weather node to 
			inputNode = InputNodeFunction(sbsDoc, aGraph, None, startPosX + 1600, startPosY, startPosZ)
			inputNode.createOutputNodesAndConnectLatestWeatherNodeToOutputNodes(latestWeatherNode)

		else:
			# In case there is no weather effect nodes, connect multi mat blend node to output nodes
			inputNode = InputNodeFunction(sbsDoc, aGraph, None, startPosX + 1600, startPosY, startPosZ)
			inputNode.createOutputNodesAndConnectMultiMatBlendNodeToOutputNode(multiMatBlendNode)





		sbsDoc.writeDoc()

		self.exportSBSAR()
		return self.sbsDestination

	def exportSBSAR(self):
		sbsFile = [self.sbsDestination]
		inputCommandLineList = self.exportSBSARFunctionInstance.exportSBSAR(sbsFile)
		installedLocation = self.sdLibrarySBSARExportFunctionInstance.getSBSCookerInstalledLocation()
		for eachCommandLine in inputCommandLineList:
			eachCommandLine.insert(0, installedLocation)
			subprocess.call(eachCommandLine)
# a = PYSBSCreationWorkflowFunction()
# a.cookSBS()