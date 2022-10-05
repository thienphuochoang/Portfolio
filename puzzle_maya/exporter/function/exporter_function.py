from functools import partial
import os
import sys
import maya.OpenMayaUI as omui
import maya.mel as mel
import maya.cmds as cmds
import json
import importlib

exportImportPath = r"C:/Temp_Exporter/temp"
exportImportUnityPath = "C:/Temp_Exporter/temp_unity"
exportImportWorkingPath = r"//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp"
exportSubstancePainterPath = r"C:/Temp_Exporter/temp_SubstancePainter"
exportImportHighPath = r"C:/Temp_Exporter/temp_highpoly"
exportImportLowPath = r"C:/Temp_Exporter/temp_lowpoly"
unityExportFilePath = "C:/Temp_Exporter/temp_unity.json"


# convertUnitSetupDict = {"millimeter": 10.0,
#                         "centimeter": 1.0,
#                         "meter": 0.01,
#                         "inch": 0.3937008,
#                         "foot": 0.0328084,
#                         "yard": 0.0109361}


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

def changeSceneUnitToCm():
	global currentSceneUnit
	currentSceneUnit = cmds.currentUnit(q=True, linear=True)
	if currentSceneUnit != "cm":
		cmds.currentUnit(linear="cm")


def checkSelectionMesh():
	selCurrent = cmds.ls(selection = True)
	if selCurrent == []:
		cmds.confirmDialog(title='Warning', message='Chon Mesh de Export', 
			button=['Yes'], icon="critical")
		return False
	else:
		return True
	
def groupTemp():
	#cmds.undoInfo(openChunk = True)
	objList = []
	if cmds.ls(sl = True):
		for obj in cmds.ls(sl = True, long = True):
			objList.append(obj)
			
		if not cmds.objExists("tempExportGroup"):
			cmds.group(name = "tempExportGroup", world = True, empty = True)
			
			for obj in objList:
				groupObj = "|".join(obj.split("|")[:-1])
				newGroup = "tempExportGroup" + groupObj
				destination = "|"
				tempList = newGroup.split("|")
				for i in tempList:
					destination = destination + i + "|"
					finalDes = ""
					if cmds.objExists(destination):
						finalDes = destination
					else:
						cmds.group(name = i, empty = True, parent=('|').join(destination.split('|')[:-2]))
						finalDes = destination
						
					try:
						cmds.parent(obj, newGroup)
					except:
						pass
			cmds.select("tempExportGroup")

def moveToOriginalGroup():
	nonExistingOriginalGroupList = {}
	for obj in cmds.listRelatives("tempExportGroup", allDescendents = True, fullPath = True, type = "transform"):
		originalGroup = "|" + "|".join(obj.split("|")[2:])
		if not cmds.objExists(originalGroup):
			parentGroup = "|".join(originalGroup.split("|")[:-1])
			nonExistingOriginalGroupList[obj] = parentGroup
	for tempGroup, originalGroup in nonExistingOriginalGroupList.items():
		if originalGroup == "":
			cmds.select(tempGroup)
			cmds.parent(tempGroup, world = True)
		else:
			try:
				cmds.parent(tempGroup, originalGroup)
			except:
				print ("tempGroup: " + tempGroup)
				print ("originalGroup: " + originalGroup)
		#cmds.parent(tempGroup, originalGroup)
		#if cmds.objExists(originalGroup):
			#childrenOfSubGroup = cmds.listRelatives(obj, children = True, fullPath = True, type = "transform")
			#print obj
			#print childrenOfSubGroup
			#print originalGroup
			#cmds.parent(childrenOfSubGroup, originalGroup)
		#else:
			#subGroup = "|".join(originalGroup.split("|")[:-1])
			#if not subGroup:
				#cmds.select(obj)
				#cmds.parent(obj, world = True)
			#else:
				#pass
				
	cmds.delete("tempExportGroup")

def ungroupTempGroup():
	if cmds.objExists("tempExportGroup"):
		try:
			if cmds.listRelatives("tempExportGroup", parent = True):
				for tempGroupParent in cmds.listRelatives("tempExportGroup", parent = True):
					if "ZZZ_ImportedGroup" in tempGroupParent:
						cmds.select(cmds.listRelatives("tempExportGroup", children = True, fullPath = True, type = "transform"))
						cmds.parent(cmds.ls(selection = True), tempGroupParent)
						cmds.delete("tempExportGroup")
			else:
				cmds.select(cmds.listRelatives("tempExportGroup", children = True, fullPath = True, type = "transform"))
				cmds.parent(cmds.ls(selection = True), world = True)
				cmds.delete("tempExportGroup")
		except:
			pass

def exportFBX(filePath, createTempGroup, sg="false", sm="false", ins="false", tri="false", tan="false",  ascii="true"):
	global currentSceneUnit
	unlockNormals =False
	currentSel=cmds.ls(sl=True, l=True)
	checkSelectedMesh = checkSelectionMesh()
	if checkSelectedMesh == True:
		if createTempGroup == True: 
			groupTemp()
			# Change current scene unit to cm
			changeSceneUnitToCm()
			#Geomytry
			mel.eval('FBXExportSmoothingGroups -v {};'.format(sg))     #Smoothing Groups
			mel.eval('FBXExportHardEdges -v false;')   #Split per-vertex Normals
			mel.eval('FBXExportTangents -v {};'.format(tan))     #Tangents and Binormals
			mel.eval('FBXExportSmoothMesh -v {};'.format(sm)) #Smooth Mesh
			mel.eval('FBXExportInstances -v {};'.format(ins)) #Preserve Instances
			mel.eval('FBXExportReferencedAssetsContent -v true;') 
			mel.eval('FBXExportTriangulate -v {};'.format(tri))  # Triangulate
			#Animation
			mel.eval('FBXExportAnimationOnly -v false;')
			mel.eval('FBXExportApplyConstantKeyReducer -v false;')
			mel.eval('FBXExportBakeComplexAnimation -v false;')
			mel.eval('FBXExportBakeResampleAnimation -v false;')
			mel.eval('FBXExportCacheFile -v false; ')
			mel.eval('FBXExportConstraints -v false;')
			mel.eval('FBXExportShapes -v false;')
			mel.eval('FBXExportSkins -v false;')
			mel.eval('FBXExportUseSceneName -v false; ')
			#Camera
			mel.eval('FBXExportCameras -v false;')
			mel.eval('FBXExportLights -v false;')
			mel.eval('FBXExportEmbeddedTextures -v false;')
		
			#Unit
			mel.eval('FBXExportConvertUnitString "cm";')
			mel.eval('FBXExportUpAxis "y";')
			mel.eval('FBXExportScaleFactor 1.0;')       #Scale Factor
			#FBX File Format 
			mel.eval('FBXExportInAscii -v {};'.format(ascii))    # Type        
			mel.eval('FBXExportFileVersion "FBX201400";') # Version
			mel.eval('FBXExportShowUI -v false;')
			mel.eval('FBXExportGenerateLog -v false;')
			#Export
		
			mel.eval('FBXExport -file "{}.fbx" -s ;'.format(filePath) )
			
			# revert current scene unit
			print (currentSceneUnit)
			cmds.currentUnit(linear = currentSceneUnit )
			
			#cmds.select(currentSel)
			moveToOriginalGroup()
		elif createTempGroup == False:
			#groupTemp()
			# Change current scene unit to cm
			changeSceneUnitToCm()
			#Geomytry
			mel.eval('FBXExportSmoothingGroups -v {};'.format(sg))     #Smoothing Groups
			mel.eval('FBXExportHardEdges -v false;')   #Split per-vertex Normals
			mel.eval('FBXExportTangents -v {};'.format(tan))     #Tangents and Binormals
			mel.eval('FBXExportSmoothMesh -v {};'.format(sm)) #Smooth Mesh
			mel.eval('FBXExportInstances -v {};'.format(ins)) #Preserve Instances
			mel.eval('FBXExportReferencedAssetsContent -v true;') 
			mel.eval('FBXExportTriangulate -v {};'.format(tri))  # Triangulate
			#Animation
			mel.eval('FBXExportAnimationOnly -v false;')
			mel.eval('FBXExportApplyConstantKeyReducer -v false;')
			mel.eval('FBXExportBakeComplexAnimation -v false;')
			mel.eval('FBXExportBakeResampleAnimation -v false;')
			mel.eval('FBXExportCacheFile -v false; ')
			mel.eval('FBXExportConstraints -v false;')
			mel.eval('FBXExportShapes -v false;')
			mel.eval('FBXExportSkins -v false;')
			mel.eval('FBXExportUseSceneName -v false; ')
			#Camera
			mel.eval('FBXExportCameras -v false;')
			mel.eval('FBXExportLights -v false;')
			mel.eval('FBXExportEmbeddedTextures -v false;')
		
			#Unit
			mel.eval('FBXExportConvertUnitString "cm";')
			mel.eval('FBXExportUpAxis "y";')
			mel.eval('FBXExportScaleFactor 1.0;')       #Scale Factor
			#FBX File Format 
			mel.eval('FBXExportInAscii -v {};'.format(ascii))    # Type        
			mel.eval('FBXExportFileVersion "FBX201400";') # Version
			mel.eval('FBXExportShowUI -v false;')
			mel.eval('FBXExportGenerateLog -v false;')
			#Export
		
			mel.eval('FBXExport -file "{}.fbx" -s ;'.format(filePath) )
			
			# revert current scene unit
			print (currentSceneUnit)
			cmds.currentUnit(linear = currentSceneUnit )
			
			#cmds.select(currentSel)
			#moveToOriginalGroup()
			

def importFBX(filePath, unlockNormals, keepGroup):
	global currentSceneUnit
	if os.path.exists(filePath + ".fbx"):
		# unlockNormals = "true"
		changeSceneUnitToCm()
		#Geomytry
		mel.eval('FBXImportMode -v add;')
		mel.eval('FBXImportHardEdges  -v false;')
		mel.eval('FBXImportUpAxis  "y";')
		mel.eval('FBXImportConvertUnitString  "cm";')
		mel.eval('FBXImportScaleFactor  1.0;')
		mel.eval('FBXImportUnlockNormals -v {};'.format(unlockNormals))
		mel.eval('FBXImportGenerateLog  -v false;')
		mel.eval('FBXImportShowUI -v false;')
		mel.eval('FBXImportCameras  -v true;')
		
		
		
		tempNamespace = "ZZZ"
		while cmds.namespace(exists=tempNamespace):
			tempNamespace += "Z"
		cmds.namespace(add = tempNamespace)
		mel.eval('file -import -type "FBX" -mergeNamespacesOnClash true \
			-namespace ":{}" -options "v=0" -pr "{}.fbx";'.format(tempNamespace, filePath))
		
		# mel.eval('file -import -type "FBX" -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":{}" -options "v=0" -pr -importFrameRate true -importTimeRange "override" "{}.fbx";'.format(tempNamespace, filePath))
		# mel.eval('FBXImport -file "{}.fbx";'.format(filePath) )
		renameMeshandMaterialsImported(tempNamespace, keepGroup)
		#Remove namespace
		cmds.namespace( rm=tempNamespace , mnr = True, f = True)
		# revert current scene unit
		cmds.currentUnit(linear = currentSceneUnit )
		ungroupTempGroup()


def exportMA(filePath):
	currentSel=cmds.ls(sl=True, l=True)
	checkSelectedMesh = checkSelectionMesh()
	if checkSelectedMesh == True:
		mel.eval( 'file -force -options "v=0;" -typ "mayaAscii" -es "{}.ma";'.format(filePath) )
		cmds.select(currentSel)


def importMA(filePath, keepGroup):
	tempNamespace = "ZZZ"
	while cmds.namespace( exists = tempNamespace ):
		tempNamespace += "Z"
	cmds.namespace(add = tempNamespace)
	mel.eval('file -import -type "mayaAscii" -ra true -mergeNamespacesOnClash true \
		-namespace ":{}" -options "v=0;"  -pr "{}.ma";'.format(tempNamespace, filePath))
	renameMeshandMaterialsImported(tempNamespace, keepGroup)
	#Remove namespace
	cmds.namespace( rm=tempNamespace , mnr = True, f = True)


def exportOBJ(filePath):
	currentSel=cmds.ls(sl=True, l=True)
	checkSelectedMesh = checkSelectionMesh()
	if checkSelectedMesh == True:
		mel.eval('DeleteHistory;') 
		# file -force -options "groups=1;ptgroups=1;materials=0;smoothing=1;normals=1" -typ "OBJexport" -pr -es "C:/TempFBX/aaa.obj";
		mel.eval('file -force -options "groups=1;ptgroups=1;materials=0;smoothing=1;normals=1" \
			-typ "OBJexport" -pr -es "{}.obj";'.format(filePath)) 
		cmds.select(currentSel)


def importOBJ(filePath):
	mel.eval('FBXImportUnlockNormals -v true;')
	mel.eval('FBXImportMode -v add;')
	mel.eval('FBXImport -f "{}.obj" -t ;'.format(filePath))


def exportFile(Status, cbBinary, cbKeepInstance):
	# print Status
	if Status == "FBX":
		exportFBX(exportImportPath, createTempGroup = True, sg="true", sm="true", 
			ins=cbKeepInstance, tri="false", tan="false", ascii=cbBinary)

	elif Status == "OBJ":
		exportOBJ(exportImportPath)

	elif Status == "Self":
		exportMA(exportImportPath)

def exportToUnity():
	currentSel=cmds.ls(sl=True)
	checkSelectedMesh = checkSelectionMesh()
	if checkSelectedMesh == True:
		exportFBX(exportImportUnityPath, createTempGroup = False, sg="true", sm="true", 
				ins="false", tri="false", tan="false", ascii="true")
		exportModelSettingsFile(currentSel[0])

def exportModelSettingsFile(modelName):
	matCreationFunctionInstance = mat_creation_function.MatCreationFunction()
	data = {}
	assignedMatList = []
	data["Model_Name"] = modelName
	materialList = matCreationFunctionInstance.getSDShadersFromMesh(modelName)
	for mat in materialList:
		eachMatAttrDict = {}
		# Get shader type
		shaderPath = matCreationFunctionInstance.getShaderFXPath()
		shaderPathWithoutSuffix = (shaderPath.split("/")[-1]).split(".")[0]
		# Add material name attribute
		eachMatAttrDict["material_name"] = mat
		# Add material type attribute
		eachMatAttrDict["material_type"] = shaderPathWithoutSuffix
		# Get all attributes from StingrayPBR Shader
		for attr in matCreationFunctionInstance.puzzleOpaqueShaderAttributeList:
			value = matCreationFunctionInstance.getAttributeFromShader(mat, attr, isStingrayShader = True)
			eachMatAttrDict[str(attr)] = str(value)
		assignedMatList.append(eachMatAttrDict)
	data["Materials"] = assignedMatList
	with open(unityExportFilePath, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)

def exportFileToCurrentFolder(Status, cbBinary, cbKeepInstance):
	filepath = cmds.file(q=True, sn=True)
	if filepath != "":
		temp = filepath.split(".")
		if Status == "FBX":
			exportedFilePath = temp[0]
			exportFBX(exportedFilePath, createTempGroup = True, sg="true", sm="true", 
				ins=cbKeepInstance, tri="false", tan="false", ascii=cbBinary)

		elif Status == "OBJ":
			exportedFilePath = temp[0]
			exportOBJ(exportedFilePath)

		elif Status == "Self":
			exportedFilePath = temp[0]
			exportMA(exportedFilePath)
	else:
		cmds.confirmDialog(title = "Error", message = "Please save file first before export")

def importFile(Status, unlockNormals, keepGroup):
	currentSel=cmds.ls(sl=True, l=True)
	if Status == "FBX":
		importFBX(exportImportPath, unlockNormals, keepGroup)
	
	elif Status == "OBJ":
		importOBJ(exportImportPath)
		
	elif Status == "Self":
		importMA(exportImportPath, keepGroup)
	cmds.select(currentSel)


def exportWorkingFiles(Status, cbBinary, cbKeepInstance):
	# print cbBinary, cbKeepInstance
	if Status == "FBX":
		exportFBX(exportImportWorkingPath, createTempGroup = True, sg="true", sm="true",
				  ins=cbKeepInstance, tri="false", tan="false", ascii=cbBinary)
	elif Status == "OBJ":
		exportOBJ(exportImportWorkingPath)
	elif Status == "Self":
		exportMA(exportImportWorkingPath)

			
def importWorkingFiles(Status, unlockNormals, keepGroup):
	currentSel=cmds.ls(sl=True, l=True)
	if Status == "FBX":
		importFBX(exportImportWorkingPath, unlockNormals, keepGroup)

	elif Status == "OBJ":
		importOBJ(exportImportWorkingPath)

	elif Status == "Self":
		importMA(exportImportWorkingPath, keepGroup)
	cmds.select(currentSel)


def exportToSubstancePainter():
	currentSel = cmds.ls(sl=True, l=True)
	dupSel = cmds.duplicate(returnRootsOnly=True)  
	cmds.Triangulate()
	cmds.select(dupSel)
	exportFBX(exportSubstancePainterPath, createTempGroup = False, sg="false", sm="true",
		ins="true", tri="false", tan="true", ascii="true")
	cmds.delete(dupSel)
	cmds.select(currentSel)


def exportLowPoly():
	exportFBX(exportImportLowPath, createTempGroup = False, sg="true", sm="true",
			  ins="true", tri="false", tan="false", ascii="true")


def exportHighPoly():
	exportFBX(exportImportHighPath, createTempGroup = False, sg="true", sm="false",
			  ins="false", tri="false", tan="false", ascii="false")


def exportSeparatePart(Status, cbBinary, cbKeepInstance):
	if Status == "FBX":
		selectedObjList = cmds.ls(sl=True, l =True)
		listShortName = cmds.ls(sl=True)
		for i in range(0,len(selectedObjList)):
			if cmds.listRelatives(selectedObjList[i], s = True):
				cmds.select(selectedObjList[i])
				objName = listShortName[i].replace("|","_")
				if objName.startswith("_"):
					objName = objName.replace("_","")
				# print listGroupName
				fbxPath = "C:/Temp_Exporter/" + objName
				exportFBX( fbxPath, createTempGroup = False, sg="true", sm = "true", ins = cbKeepInstance, 
					tri = "false", tan="false", ascii = cbBinary)
		cmds.select(selectedObjList)

	elif Status == "OBJ":
		selectedObjList = cmds.ls(sl=True, l =True)
		listShortName = cmds.ls(sl=True)
		for i in range(0,len(selectedObjList)):
			if cmds.listRelatives(selectedObjList[i], s = True):
				cmds.select(selectedObjList[i])
				objName = listShortName[i].replace("|","_")
				if objName.startswith("_"):
					objName = objName.replace("_","")
				fbxPath = "C:/Temp_Exporter/" + objName
			exportOBJ(fbxPath)
		cmds.select(selectedObjList)

	elif Status == "Self":
		selectedObjList = cmds.ls(sl=True, l =True)
		listShortName = cmds.ls(sl=True)
		for i in range(0,len(selectedObjList)):
			if cmds.listRelatives(selectedObjList[i], s = True):
				cmds.select(selectedObjList[i])
				objName = listShortName[i].replace("|","_")
				if objName.startswith("_"):
					objName = objName.replace("_","")
				fbxPath = "C:/Temp_Exporter/" + objName
			exportMA(fbxPath)
		cmds.select(selectedObjList)



def openTempFolder():
	os.startfile('C:/Temp_Exporter')


def deleteTempFolderContents():
	folder = 'C:/Temp_Exporter'
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path): shutil.rmtree(file_path)
		except Exception as e:
			print(e)


def createTempFolder():
	directoryPath = r"C:/Temp_Exporter"
	if os.path.exists(directoryPath) == False:
		os.mkdir(directoryPath)


def replaceMaterials(*arg):
	confirmA = cmds.confirmDialog(icon="warning", title="Fix Materials", 
		button=["Origin Mat", "Imported Mat", "Remove ID, ZZZ"],
		message="What Materials you want to use?",
		defaultButton="Origin Mat", cancelButton="Imported Mat", dismissString="No")
	currentSel=cmds.ls(sl=True, l=True)
	listAllMaterials = sorted(cmds.ls(mat=True))
	# listMaterialsImported = []
	# print listAllMaterials
	if confirmA == "Remove ID, ZZZ":
		for mat in listAllMaterials:
			sufix  = ""
			prefix = ""
			if  "ID" in mat.split("_")[-1]:
				sufix = "_" + mat.split("_")[-1]
			if mat.split("_")[0]:
				if "ZZZ" in mat.split("_")[0]:
					prefix = mat.split("_")[0] + "_"
			if sufix or prefix:
				matOrigin = mat
				matOrigin = matOrigin.replace(sufix,"")
				matOrigin = matOrigin.replace(prefix,"")
				cmds.rename(mat, matOrigin)
		return
	for mat in listAllMaterials:
		sufix  = ""
		prefix = ""
		if mat.split("_")[-1]:
			if "ID" in mat.split("_")[-1]:
				sufix = "_" + mat.split("_")[-1]
		if mat.split("_")[0]:
			if "ZZZ" in mat.split("_")[0]:
				prefix = mat.split("_")[0] + "_"
		if sufix or prefix:
			matOrigin = mat
			matOrigin = matOrigin.replace(sufix,"")
			matOrigin = matOrigin.replace(prefix,"")
			# print mat, matSel, "\n"
			if matOrigin in listAllMaterials:
				cmds.ShowAll()
				if confirmA == "Origin Mat":
					cmds.hyperShade(objects=mat)
					assignMaterialToSelectedMesh(["lambert1"])
					assignMaterialToSelectedMesh([matOrigin])
					cmds.delete(mat)
				if confirmA == "Imported Mat":
					cmds.hyperShade(objects=matOrigin)
					assignMaterialToSelectedMesh(["lambert1"])
					assignMaterialToSelectedMesh([mat])
					cmds.delete(matOrigin)
					cmds.rename(mat, matOrigin)
			else:
				cmds.rename(mat, matOrigin)
	cmds.select(currentSel)


def assignMaterialToSelectedMesh(materialSelected, *arg):
	# print materialSelected[0]
	if materialSelected != None and len(materialSelected) == 1:
		if cmds.listConnections(materialSelected,type='shadingEngine') != None:
			shadingEngine=cmds.listConnections(materialSelected,type='shadingEngine')[0]
			cmds.sets(e=True, forceElement=shadingEngine)
		else:
			cmds.hyperShade(assign=materialSelected[0])
			cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=materialSelected[0]+'SG')
			shadingEngine=cmds.listConnections(materialSelected,type='shadingEngine')[0]
			print ('Create shading group: ' + shadingEngine)
			cmds.sets(e=True, forceElement=shadingEngine)           
	else:
		print ('Choose one material')



def renameMeshandMaterialsImported(namespace, keepGroup):
	namespace = namespace +":"
	if keepGroup == "true":
		#Group all imported mesh
		newImportedGroup = "ZZZ_ImportedGroup"
		# if not cmds.objExists('ZZZ_ImportedGroup'):
		while cmds.objExists(newImportedGroup):
			if newImportedGroup.replace("ZZZ_ImportedGroup","").isdigit():
				newNum = int(newImportedGroup.replace("ZZZ_ImportedGroup","")) +1
				newImportedGroup = "ZZZ_ImportedGroup" + str(newNum)
			else:
				newImportedGroup = "ZZZ_ImportedGroup" + str(1)
		cmds.group( n = newImportedGroup ,em =True)

		importedRootTransform =[]
		for g in cmds.ls(tr = True, l = True):
			if not cmds.listRelatives(g, p = True) and namespace in g:
				print (g)
				importedRootTransform.append(g)

		for g in importedRootTransform:
				cmds.parent(g, newImportedGroup )
	#Rename Materials
	for mat in cmds.ls(mat=True):
		if namespace in mat:
			if mat.replace(namespace, "") in cmds.ls(mat=True) and mat.replace(namespace, "") != "lambert1":
				newName = "ZZZImported_" + mat.replace(namespace, "")
				while newName in cmds.ls(mat=True):
					newName = "z" + newName
				cmds.rename(mat, namespace + newName)
			if mat.replace(namespace, "") == "lambert1":
				cmds.hyperShade(objects=mat)
				assignMaterialToSelectedMesh(["lambert1"])
				cmds.delete(mat)

