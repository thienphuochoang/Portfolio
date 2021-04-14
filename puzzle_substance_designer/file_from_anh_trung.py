import sys
sys.path.append(r"Z:\Substances\Pysbs-2019.1.2")
import pysbs
from pysbs import python_helpers
from pysbs import context
from pysbs import sbsenum
from pysbs import sbsgenerator
from pysbs import sbscommon
from pysbs import substance, sbsarchive
from pysbs import sbslibrary
from pysbs.api_decorators import doc_source_code

Bakers = ['ColorID', 'AmbientOcclusion', 'WorldSpaceNormal','Position']

def cookSBS(*args, **kwargs):
	destination = kwargs['destination']
	colorIDNodePath = kwargs['colorIDNodePath']
	AmbientOcclusion_Node_Path = kwargs['AmbientOcclusion_Node_Path']
	Normal_Node_Path = kwargs['Normal_Node_Path']
	Position_Node_Path = kwargs['Position_Node_Path']
	WorldSpaceNormal_Node_Path = kwargs['WorldSpaceNormal_Node_Path']
	substancePath = kwargs['substancePath']
	MaterialNameAndColorDict = kwargs['MaterialNameAndColorDict']
	SBSDependencyPath =kwargs['SBSDependencyPath']

	aContext = context.Context()

	startPos = [48, 48, 0]
	xOffset  = [192, 0, 0]
	xOffset2 = [384, 0, 0]
	yOffset  = [0, 192, 0]

	# Create a new SBSDocument from scratch
	sbsDoc = sbsgenerator.createSBSDocument(aContext,
							aFileAbsPath = destination)
	

	# Create the graph
	temp = destination.split("/")
	graphName = temp[-1].split(".")[0]
	aGraph = sbsDoc.createGraph(aGraphIdentifier = graphName)
	
	weatherPath = ""
	for path, subdirs, files in os.walk(substancePath):
		checkWeatherFilePath = (path + "\\SUBS_Weather.sbs")
		if (os.path.isfile (checkWeatherFilePath) and "autosave" not in checkWeatherFilePath):
			weatherPath = checkWeatherFilePath
	# Create Instance Node
	weatherNode = aGraph.createCompInstanceNodeFromPath(aSBSDocument = sbsDoc,
														aPath		= weatherPath + "/SUBS_Weather",
														aGUIPos	  = startPos,
														aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	blendMaterialNode = aGraph.createCompInstanceNodeFromPath(aSBSDocument = sbsDoc,
															  aPath		= SBSDependencyPath + "/multi_material_blend.sbs/multi_material_blend",
															  aParameters  = {'Materials':int(len(MaterialNameAndColorDict)), 'ambient_occlusion': True},
															  aGUIPos	  = [-148,0,0],
															  aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	rgbamergeNode = aGraph.createCompInstanceNodeFromPath(aSBSDocument = sbsDoc,
														  aPath		= SBSDependencyPath + "/rgba_merge.sbs/rgba_merge",
														  aGUIPos	  = [-50,150,0],
														  aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})

	colorIDNode = aGraph.createBitmapNode(aSBSDocument  = sbsDoc,
										  aResourcePath = colorIDNodePath,
										  aGUIPos		= [-300,0,0])
	
	curvatureBlendNode = aGraph.createCompInstanceNodeFromPath(aSBSDocument = sbsDoc,
															   aPath		= SBSDependencyPath + "/curvature.sbs/curvature",
															   aParameters  = {"normal_format": 1},
															   aGUIPos		= [-148,300,0],
															   aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	normalCurvatureBlendNode = aGraph.createCompInstanceNodeFromPath(aSBSDocument = sbsDoc,
																     aPath		  = SBSDependencyPath + "/curvature.sbs/curvature",
																     aParameters  = {"normal_format": 1},
																     aGUIPos	  = [-180,300,0],
																     aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	normalCombineNode = aGraph.createCompInstanceNodeFromPath(aSBSDocument = sbsDoc,
														      aPath		   = SBSDependencyPath + "/normal_combine.sbs/normal_combine",
														      aParameters  = {"blend_quality": 2},
														      aGUIPos	   = [-230,300,0],
														      aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	blendNode = aGraph.createCompFilterNode(aFilter 	 = sbsenum.FilterEnum.BLEND,
											aParameters  = {sbsenum.CompNodeParamEnum.BLENDING_MODE : sbsenum.BlendBlendingModeEnum.OVERLAY},
											aGUIPos		 = [-148,500,0],
											aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	AmbientOcclusion_LevelNode 		= aGraph.createCompFilterNode(aFilter	= sbsenum.FilterEnum.LEVELS,
																  aGUIPos	= [-50,250,0],
																  aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	Curvature_LevelNode 			= aGraph.createCompFilterNode(aFilter	= sbsenum.FilterEnum.LEVELS,
																  aGUIPos	= [-50,350,0],
																  aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	Position_LevelNode 				= aGraph.createCompFilterNode(aFilter	= sbsenum.FilterEnum.LEVELS,
																  aGUIPos	= [-50,450,0],
																  aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	WorldSpaceNormal_LevelNode 		= aGraph.createCompFilterNode(aFilter	= sbsenum.FilterEnum.LEVELS,
																  aGUIPos	= [-50,550,0],
																  aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
	
	# Create Input Node
	
	AmbientOcclusion_Node   = aGraph.createBitmapNode(aSBSDocument  = sbsDoc,
													  aResourcePath = AmbientOcclusion_Node_Path,
													  aParameters   = {sbsenum.CompNodeParamEnum.COLOR_MODE:False},
													  aGUIPos		= [-200,250,0])
	
	Normal_Node		  = aGraph.createBitmapNode(aSBSDocument	= sbsDoc,
												aResourcePath   = Normal_Node_Path,
												aParameters		= {sbsenum.CompNodeParamEnum.COLOR_MODE:True},
												aGUIPos			= [-200,350,0])
	
	Position_Node		   = aGraph.createBitmapNode(aSBSDocument   = sbsDoc,
													 aResourcePath  = Position_Node_Path,
													 aParameters	= {sbsenum.CompNodeParamEnum.COLOR_MODE:True},
													 aGUIPos		= [-200,450,0])
	
	WorldSpaceNormal_Node   = aGraph.createBitmapNode(aSBSDocument  = sbsDoc,
													 aResourcePath  = WorldSpaceNormal_Node_Path,
													 aParameters	= {sbsenum.CompNodeParamEnum.COLOR_MODE:True},
													 aGUIPos		= [-200,550,0])
	
	# Connect input node to level node
	aGraph.connectNodes(aLeftNode = Normal_Node, aRightNode = normalCurvatureBlendNode)
	aGraph.connectNodes(aLeftNode = AmbientOcclusion_Node, aRightNode = AmbientOcclusion_LevelNode)
	aGraph.connectNodes(aLeftNode = normalCurvatureBlendNode, aRightNode = Curvature_LevelNode)
	aGraph.connectNodes(aLeftNode = Position_Node, aRightNode = Position_LevelNode)
	aGraph.connectNodes(aLeftNode = WorldSpaceNormal_Node, aRightNode = WorldSpaceNormal_LevelNode)
	
	# Connect level node to Weather Node
	aGraph.connectNodes(aLeftNode = AmbientOcclusion_LevelNode, aRightNode = weatherNode, aRightNodeInput = "AmbientOcclusion")
	aGraph.connectNodes(aLeftNode = Curvature_LevelNode, aRightNode = weatherNode, aRightNodeInput = "Curvature")
	aGraph.connectNodes(aLeftNode = Position_LevelNode, aRightNode = weatherNode, aRightNodeInput = "Position")
	aGraph.connectNodes(aLeftNode = WorldSpaceNormal_LevelNode, aRightNode = weatherNode, aRightNodeInput = "WorldSpaceNormal")

	
	# Load material SBS file
	index = 1
	for key, value in MaterialNameAndColorDict.iteritems():
		print key, value
		tempList = key.split("_")
		if len(tempList) > 2:
			del tempList[2:]
		else:
			pass
		fileName = ("_").join(tempList[:2])
		for path, subdirs, files in os.walk(substancePath):
			checkFilePath = (path + "\\" + fileName + ".sbs")
			if (os.path.isfile (checkFilePath) and "autosave" not in checkFilePath):
				materialNode = aGraph.createCompInstanceNodeFromPath(aSBSDocument = sbsDoc,
																	 aPath		= checkFilePath +"/"+fileName,
																	 aGUIPos	  = [-400,0,0],
																	 aInheritance = {sbsenum.CompNodeParamEnum.OUTPUT_SIZE:sbsenum.ParamInheritanceEnum.PARENT})
		

				# Connect material node to multi material blend
				aGraph.connectNodes(aLeftNode = materialNode, aRightNode = blendMaterialNode, aLeftNodeOutput = "BaseColor", aRightNodeInput = "material"+str(index)+"_basecolor")
				aGraph.connectNodes(aLeftNode = materialNode, aRightNode = blendMaterialNode, aLeftNodeOutput = "Normal", aRightNodeInput = "material"+str(index)+"_normal")
				aGraph.connectNodes(aLeftNode = materialNode, aRightNode = blendMaterialNode, aLeftNodeOutput = "Metallic", aRightNodeInput = "material"+str(index)+"_metallic")
				aGraph.connectNodes(aLeftNode = materialNode, aRightNode = blendMaterialNode, aLeftNodeOutput = "Roughness", aRightNodeInput = "material"+str(index)+"_roughness")
				aGraph.connectNodes(aLeftNode = materialNode, aRightNode = blendMaterialNode, aLeftNodeOutput = "AmbientOcclusion", aRightNodeInput = "material"+str(index)+"_ambientocclusion")
				
				# Change material node color
				if index == 1:
					pass
				else:
					blendMaterialNode.setParameterValue("Material_"+str(index)+"_Color",value)
				# Check if inputs are available in material node
				allNodes = materialNode.getDefinition()
				if allNodes.mInputs:
					for input in allNodes.getAllInputIdentifiers():
						# Connect input node to input node of material node
						if "AmbientOcclusion" in input:
							aGraph.connectNodes(aLeftNode = AmbientOcclusion_LevelNode, aRightNode = materialNode, aRightNodeInput = "AmbientOcclusion")
						if "WorldSpaceNormal" in input:
							aGraph.connectNodes(aLeftNode = WorldSpaceNormal_LevelNode, aRightNode = materialNode, aRightNodeInput = "WorldSpaceNormal")
						if "Curvature" in input:
							aGraph.connectNodes(aLeftNode = Curvature_LevelNode, aRightNode = materialNode, aRightNodeInput = "Curvature")
						if "Position" in input:
							aGraph.connectNodes(aLeftNode = Position_LevelNode, aRightNode = materialNode, aRightNodeInput = "Position")
				index = index + 1
				
				# Get all input parameter of material node
				inputParameterDict = {}
				ListOfInputParameters = materialNode.getDefinition().getAllParameters()
				for parameter in ListOfInputParameters:
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
							
				groupName = key	 
				# Create Graph Parameter
				for key, value in inputParameterDict.items():
					materialParameterValue = materialNode.getParameterValue(aParameter = key)
					aGraphParameter = aGraph.addInputParameter(aIdentifier = groupName + "_" + key,aWidget = value, aGroup = groupName, aLabel = key, aDefaultValue = materialParameterValue)
					# Link graph parameter + material node parameter
					aGraphFunction = materialNode.setDynamicParameter(aParameter = key)
					aGraphFunction.setToInputParam(aParentGraph = aGraph, aInputParamIdentifier = groupName + "_" + key)
			
	# Connect Multi Material Blend to Weather Node
	aGraph.connectNodes(aLeftNode = blendMaterialNode, aRightNode = weatherNode, aLeftNodeOutput = "basecolor", aRightNodeInput = "BaseColor")
	aGraph.connectNodes(aLeftNode = blendMaterialNode, aRightNode = weatherNode, aLeftNodeOutput = "Normal", aRightNodeInput = "Normal")
	aGraph.connectNodes(aLeftNode = blendMaterialNode, aRightNode = weatherNode, aLeftNodeOutput = "Roughness", aRightNodeInput = "Roughness")
	aGraph.connectNodes(aLeftNode = blendMaterialNode, aRightNode = weatherNode, aLeftNodeOutput = "Metallic", aRightNodeInput = "Metallic")
		
	# Create Output Node + Connect Output Node to Weather Node
	compOutputList = weatherNode.mCompOutputs
	for output in compOutputList:
		aIdentifier = weatherNode.getCompOutputIdentifier(output.mUID)

		if "Normal" in aIdentifier:
			outputNode = aGraph.createOutputNode(aIdentifier = aIdentifier,
												 aGUIPos	 = [384,100,0],
												 aUsages	 = {sbsenum.UsageEnum.NORMAL: sbsenum.ComponentsEnum.RGBA})   
			
			aGraph.connectNodes(aLeftNode = weatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
							
		if "BaseColor" in aIdentifier:
			outputNode = aGraph.createOutputNode(aIdentifier = aIdentifier,
												 aGUIPos	 = [384,500,0],
												 aUsages	 = {sbsenum.UsageEnum.BASECOLOR: sbsenum.ComponentsEnum.RGBA})
			
			aGraph.connectNodes(aLeftNode = weatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
		
		if "Metallic" in aIdentifier:
			outputNode = aGraph.createOutputNode(aIdentifier = aIdentifier,
												 aGUIPos	 = [384,600,0],
												 aUsages	 = {sbsenum.UsageEnum.METALLIC: sbsenum.ComponentsEnum.RGBA})
			
			aGraph.connectNodes(aLeftNode = weatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
			
		if "Roughness" in aIdentifier:
			outputNode = aGraph.createOutputNode(aIdentifier = aIdentifier,
												 aGUIPos	 = [384,700,0],
												 aUsages	 = {sbsenum.UsageEnum.ROUGHNESS: sbsenum.ComponentsEnum.RGBA})
			
			aGraph.connectNodes(aLeftNode = weatherNode, aRightNode = outputNode, aLeftNodeOutput = aIdentifier)
		
		
	
	
	# Connect Color ID Node to Color ID of Multi Material Blend
	aGraph.connectNodes(aLeftNode = colorIDNode, aRightNode = blendMaterialNode, aRightNodeInput = "Input_160")
	
	# Get all input parameter of weather node
	inputParameterDict = {}
	ListOfInputParameters = weatherNode.getDefinition().getAllParameters()
	for parameter in ListOfInputParameters:
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
				inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.SLIDER_FLOAT3
			if parameter.mType == 2048:
				inputParameterDict[parameter.mParameter] = sbsenum.WidgetEnum.SLIDER_FLOAT4
	
	# Create Graph Parameter
	for key, value in inputParameterDict.items():
		weatherParameterValue = weatherNode.getParameterValue(aParameter = key)
		aGraphParameter = aGraph.addInputParameter(aIdentifier = "GlobalEffect_" + key,aWidget = value, aGroup = "GlobalEffect", aLabel = key, aDefaultValue = weatherParameterValue)
		# Link graph parameter + weather node parameter
		aGraphFunction = weatherNode.setDynamicParameter(aParameter = key)
		aGraphFunction.setToInputParam(aParentGraph = aGraph, aInputParamIdentifier = "GlobalEffect_" + key)
	
	# Create Ambient Occlusion output node and connect to multi material blend node
	ambientOutputNode = aGraph.createOutputNode(aIdentifier = "AmbientOcclusion",
												aGUIPos	 = [384,400,0],
												aUsages	 = {sbsenum.UsageEnum.AMBIENT_OCCLUSION: sbsenum.ComponentsEnum.RGBA})
	
	aGraph.connectNodes(aLeftNode = blendMaterialNode, aRightNode = ambientOutputNode, aLeftNodeOutput = "AmbientOcclusion")
	
	
	# Connect blendMaterialNode to curvatureBlendNode
	aGraph.connectNodes(aLeftNode = blendMaterialNode, aRightNode = curvatureBlendNode, aLeftNodeOutput = "Normal")
	
	# Connect curvatureBlendNode to blendNode
	aGraph.connectNodes(aLeftNode = curvatureBlendNode, aRightNode = blendNode, aRightNodeInput = "source")
	
	# Connect Curvature_LevelNode to blendNode
	aGraph.connectNodes(aLeftNode = Curvature_LevelNode, aRightNode = blendNode, aRightNodeInput = "destination")
	
	# Connect blendNode to weatherNode
	aGraph.connectNodes(aLeftNode = blendNode, aRightNode = weatherNode, aRightNodeInput = "Curvature")
	
	# Create Export RGB Merge output node
	rgbaoutputNode = aGraph.createOutputNode(aIdentifier = "Export",
											 aGUIPos	 = [484,100,0],
											 aUsages	 = {sbsenum.UsageEnum.ANY: sbsenum.ComponentsEnum.RGBA})
	
	# Connect Ambient Occlusion from Multi material blend to rgba merge node
	aGraph.connectNodes(aLeftNode = blendMaterialNode, aRightNode = rgbamergeNode, aLeftNodeOutput = "AmbientOcclusion", aRightNodeInput = "B")
	
	# Connect weather node to rgba merge node
	aGraph.connectNodes(aLeftNode = weatherNode, aRightNode = rgbamergeNode, aLeftNodeOutput = "Metallic", aRightNodeInput = "R")
	aGraph.connectNodes(aLeftNode = weatherNode, aRightNode = rgbamergeNode, aLeftNodeOutput = "Roughness", aRightNodeInput = "G")
	
	# Connect rgba merge node to Export RGB Merge output node
	aGraph.connectNodes(aLeftNode = rgbamergeNode, aRightNode = rgbaoutputNode)
	
	# Connect Normal_Node to normalCombineNode
	aGraph.connectNodes(aLeftNode = Normal_Node, aRightNode = normalCombineNode, aRightNodeInput = "Input")
	
	# Connect blendMaterialNode to normalCombineNode
	aGraph.connectNodes(aLeftNode = blendMaterialNode, aRightNode = normalCombineNode, aLeftNodeOutput = "Normal", aRightNodeInput = "Input_1")
	
	# Connect normalCombineNode to weatherNode
	aGraph.connectNodes(aLeftNode = normalCombineNode, aRightNode = weatherNode, aRightNodeInput = "Normal")
	
	sbsDoc.writeDoc()
	return destination
	

