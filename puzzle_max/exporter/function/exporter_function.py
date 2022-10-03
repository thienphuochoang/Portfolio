from functools import partial
import os
import pymxs
import sys
import shutil
rt = pymxs.runtime

importConvertToCmDict = {
						"millimeters": 10.0, 
						"centimeters": 1.0, 
						"decimeters": 0.1, 
						"meters": 0.01, 
						"kilometers": 0.00001, 
						"inches": 0.3937008, 
						"feet": 0.0328084, 
						"yards": 0.0109361, 
						"miles": 0.0000062}
exportConvertToCmDict = {
						"millimeters": 0.1, 
						"centimeters": 1.0,
						"meters": 100.0,
						"kilometers": 100000.0, 
						"inches": 2.54, 
						"feet": 30.48, 
						"miles": 160934.4}

#importConvertToCmScaleFactor = importConvertToCmDict[currentUnitSetup]

def exportIgnoreScale(Status, keepVertexNormalStatus, exportBinaryStatus, keepInstanceStatus):
	if keepVertexNormalStatus == "Off":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
		
	if exportBinaryStatus == "On":
		exportBinaryStatus = False
	else:
		exportBinaryStatus = True
		
	if keepInstanceStatus == "On":
		keepInstanceStatus = True
	else:
		keepInstanceStatus = False
		
	#currentUnitSetup = str(rt.units.SystemType)
	#exportConvertToCmScaleFactor = exportConvertToCmDict[currentUnitSetup]
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
	if Status == "FBX":
		fbx = "C:/Temp_Exporter/temp.fbx"
		rt.FBXExporterSetParam("SmoothingGroups",True)
		rt.FBXExporterSetParam("PreserveEdgeOrientation",False)
		rt.FBXExporterSetParam("Preserveinstances", keepInstanceStatus)
		rt.FBXExporterSetParam("Animation",False)
		rt.FBXExporterSetParam("ShowWarnings",True)
		rt.FBXExporterSetParam("UpAxis","Y")
		#rt.FBXExporterSetParam("ConvertUnit", "cm")
		#MaxPlus.Core.EvalMAXScript("FBXExporterSetParam "ConvertUnit" "cm'")
		rt.FBXExporterSetParam("ScaleFactor", 1.0)
		rt.FBXExporterSetParam("ASCII", exportBinaryStatus)
		rt.FBXExporterSetParam("FileVersion","FBX201400")
		rt.exportFile(fbx, rt.Name("noPrompt"), selectedOnly = True, using = rt.FBXEXP)
		#MaxPlus.Core.EvalMAXScript("exportfile \"" + fbx + "\" #noPrompt selectedOnly:True using:FBXEXP")
		#MaxPlus.Core.EvalMAXScript("mergeMaxFile \"" + scene + "\" #(\"MaterialTemplate\",\"MaterialTemplate_Phys\" , \"MaterialTemplate_Proxy\")  #deleteOldDups #useMergedMtlDups quite:true")
	elif Status == "OBJ":
		obj = "C:/Temp_Exporter/temp.obj"
		theINI = rt.objimp.getIniName()
		rt.setINISetting(theINI, "General","UseLogging","1")
		rt.setINISetting(theINI, "Geometry","FlipZyAxis","1")
		rt.setINISetting(theINI, "Geometry", "ExportHiddenObjects", "1")
		rt.setINISetting(theINI, "Geometry", "FaceType", "1")
		rt.setINISetting(theINI, "Geometry", "Normals", "1")
		rt.setINISetting(theINI, "Geometry", "TextureCoords", "1")
		rt.setINISetting(theINI, "Geometry", "SmoothingGroups", "1")
		rt.setINISetting(theINI, "Geometry", "ObjScale", "1.0")
		rt.setINISetting(theINI, "Material", "UseMaterial", "1")
		rt.setINISetting(theINI, "Material", "CreateMatLibrary", "0")
		rt.setINISetting(theINI, "Material", "ForceBlackAmbient", "0")
		rt.setINISetting(theINI, "Output", "RelativeIndex", "0")
		rt.setINISetting(theINI, "Output", "Target", "0")
		rt.setINISetting(theINI, "Output", "Precision", "4")
		rt.setINISetting(theINI, "Optimize", "optVertex", "0")
		rt.setINISetting(theINI, "Optimize", "optNormals", "1")
		rt.setINISetting(theINI, "Optimize", "optTextureCoords", "1")
		rt.exportFile(obj, rt.Name("noPrompt"), selectedOnly = True, using = rt.ObjExp)
		#MaxPlus.Core.EvalMAXScript("exportfile \"" + obj + "\" #noPrompt selectedOnly:True using:ObjExp")
	elif Status == "Self":
		max = "C:/Temp_Exporter/temp.max"
		rt.saveNodes(rt.selection, max, quiet = True)
		#MaxPlus.Core.EvalMAXScript("saveNodes selection \"" + max + "\" quiet:True")
		#rt.saveNodes("selection","C:\\Temp\\temp_max.max","quiet:True")
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
	
def exportCurrentFolder():
	if (rt.maxfilename != "" and rt.maxfilepath != ""):
		currentUnitSetup = str(rt.units.SystemType)
		exportConvertToCmScaleFactor = exportConvertToCmDict[currentUnitSetup]
		rt.units.SystemType = rt.Name("centimeters")
		#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
		
		filename = rt.maxfilename.replace(".max",".fbx")
		destination = rt.maxfilepath + filename
		destination = destination.replace("\\","/")
		#print destination
		rt.FBXExporterSetParam("SmoothingGroups",True)
		rt.FBXExporterSetParam("PreserveEdgeOrientation",False)
		rt.FBXExporterSetParam("Animation",False)
		rt.FBXExporterSetParam("ShowWarnings",True)
		rt.FBXExporterSetParam("UpAxis","Y")
		rt.FBXExporterSetParam("ConvertUnit", "cm")
		#MaxPlus.Core.EvalMAXScript("FBXExporterSetParam "ConvertUnit" "cm'")
		rt.FBXExporterSetParam("ScaleFactor", exportConvertToCmScaleFactor)
		rt.FBXExporterSetParam("ASCII", True)
		rt.FBXExporterSetParam("FileVersion","FBX201400")
		rt.exportFile(destination, rt.Name("noPrompt"), selectedOnly = True, using = rt.FBXEXP)
		#MaxPlus.Core.EvalMAXScript("exportfile \"" + destination.replace("\\","/") + "\" #noPrompt selectedOnly:True using:FBXEXP")
		rt.units.SystemType = rt.Name(currentUnitSetup)
		#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
	else:
		rt.messageBox("Please save your file first before exporting")
	
def exportFile(Status, keepVertexNormalStatus, exportBinaryStatus, keepInstanceStatus):
	if keepVertexNormalStatus == "Off":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
		
	if exportBinaryStatus == "On":
		exportBinaryStatus = False
	else:
		exportBinaryStatus = True
		
	if keepInstanceStatus == "On":
		keepInstanceStatus = True
	else:
		keepInstanceStatus = False
		
	currentUnitSetup = str(rt.units.SystemType)
	exportConvertToCmScaleFactor = exportConvertToCmDict[currentUnitSetup]
	rt.units.SystemType = rt.Name("centimeters")
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
	if Status == "FBX":
		fbx = "C:/Temp_Exporter/temp.fbx"
		rt.FBXExporterSetParam("SmoothingGroups",True)
		rt.FBXExporterSetParam("PreserveEdgeOrientation",False)
		rt.FBXExporterSetParam("Preserveinstances", keepInstanceStatus)
		rt.FBXExporterSetParam("Animation",False)
		rt.FBXExporterSetParam("ShowWarnings",True)
		rt.FBXExporterSetParam("UpAxis","Y")
		rt.FBXExporterSetParam("ConvertUnit", "cm")
		#MaxPlus.Core.EvalMAXScript("FBXExporterSetParam "ConvertUnit" "cm'")
		rt.FBXExporterSetParam("ScaleFactor", exportConvertToCmScaleFactor)
		rt.FBXExporterSetParam("ASCII", exportBinaryStatus)
		rt.FBXExporterSetParam("FileVersion","FBX201400")
		rt.exportFile(fbx, rt.Name("noPrompt"), selectedOnly = True, using = rt.FBXEXP)
		#MaxPlus.Core.EvalMAXScript("exportfile \"" + fbx + "\" #noPrompt selectedOnly:True using:FBXEXP")
		#MaxPlus.Core.EvalMAXScript("mergeMaxFile \"" + scene + "\" #(\"MaterialTemplate\",\"MaterialTemplate_Phys\" , \"MaterialTemplate_Proxy\")  #deleteOldDups #useMergedMtlDups quite:true")
	elif Status == "OBJ":
		obj = "C:/Temp_Exporter/temp.obj"
		theINI = rt.objimp.getIniName()
		rt.setINISetting(theINI, "General","UseLogging","1")
		rt.setINISetting(theINI, "Geometry","FlipZyAxis","1")
		rt.setINISetting(theINI, "Geometry", "ExportHiddenObjects", "1")
		rt.setINISetting(theINI, "Geometry", "FaceType", "1")
		rt.setINISetting(theINI, "Geometry", "Normals", "1")
		rt.setINISetting(theINI, "Geometry", "TextureCoords", "1")
		rt.setINISetting(theINI, "Geometry", "SmoothingGroups", "1")
		rt.setINISetting(theINI, "Geometry", "ObjScale", "1.0")
		rt.setINISetting(theINI, "Material", "UseMaterial", "1")
		rt.setINISetting(theINI, "Material", "CreateMatLibrary", "0")
		rt.setINISetting(theINI, "Material", "ForceBlackAmbient", "0")
		rt.setINISetting(theINI, "Output", "RelativeIndex", "0")
		rt.setINISetting(theINI, "Output", "Target", "0")
		rt.setINISetting(theINI, "Output", "Precision", "4")
		rt.setINISetting(theINI, "Optimize", "optVertex", "0")
		rt.setINISetting(theINI, "Optimize", "optNormals", "1")
		rt.setINISetting(theINI, "Optimize", "optTextureCoords", "1")
		rt.exportFile(obj, rt.Name("noPrompt"), selectedOnly = True, using = rt.ObjExp)
		#MaxPlus.Core.EvalMAXScript("exportfile \"" + obj + "\" #noPrompt selectedOnly:True using:ObjExp")
	elif Status == "Self":
		max = "C:/Temp_Exporter/temp.max"
		rt.saveNodes(rt.selection, max, quiet = True)
		#MaxPlus.Core.EvalMAXScript("saveNodes selection \"" + max + "\" quiet:True")
		#rt.saveNodes("selection","C:\\Temp\\temp_max.max","quiet:True")
	rt.units.SystemType = rt.Name(currentUnitSetup)
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
	
def importFile(Status, keepVertexNormalStatus, queryKeepGroupStatus):
	if keepVertexNormalStatus == "Off":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
		
	if queryKeepGroupStatus == "On":
		queryKeepGroupStatus = True
	else:
		queryKeepGroupStatus = False
	
	currentUnitSetup = str(rt.units.SystemType)
	importConvertToCmScaleFactor = importConvertToCmDict[currentUnitSetup]
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
	if Status == "FBX" and queryKeepGroupStatus == True:
		fbx = "C:/Temp_Exporter/temp.fbx"
		rt.FBXImporterSetParam("Mode", "#create")
		rt.FBXImporterSetParam("SmoothingGroups", keepVertexNormalStatus)
		rt.FBXImporterSetParam("UpAxis", "Z")
		#rt.FBXImporterSetParam("ScaleConversion", True)
		rt.FBXExporterSetParam("GenerateLog", True)
		rt.FBXImporterSetParam("ConvertUnit", "cm")
		rt.FBXImporterSetParam("ScaleFactor", importConvertToCmScaleFactor / rt.units.SystemScale)
		#rt.FBXImporterSetParam("ScaleConversion", True)
		rt.importFile(fbx, rt.Name("noPrompt"))
		#MaxPlus.Core.EvalMAXScript("importfile \"" + fbx + "\" #noPrompt")
		
		#Delete temp export group
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
				
		rt.group(rt.selection, name = "ZZZ_ImportedGroup")
		
	elif Status == "FBX" and queryKeepGroupStatus == False:
		fbx = "C:/Temp_Exporter/temp.fbx"
		rt.FBXImporterSetParam("Mode", "#create")
		rt.FBXImporterSetParam("SmoothingGroups", keepVertexNormalStatus)
		rt.FBXImporterSetParam("UpAxis", "Z")
		#rt.FBXImporterSetParam("ScaleConversion", True)
		rt.FBXExporterSetParam("GenerateLog", True)
		rt.FBXImporterSetParam("ConvertUnit", "cm")
		rt.FBXImporterSetParam("ScaleFactor", importConvertToCmScaleFactor / rt.units.SystemScale)
		#rt.FBXImporterSetParam("ScaleConversion", True)
		rt.importFile(fbx, rt.Name("noPrompt"))
		#MaxPlus.Core.EvalMAXScript("importfile \"" + fbx + "\" #noPrompt")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
	
	elif Status == "OBJ" and queryKeepGroupStatus == True:
		obj = "C:/Temp_Exporter/temp.obj"
		rt.importFile(obj, rt.Name("noPrompt"))
		#MaxPlus.Core.EvalMAXScript("importfile \"" + obj + "\" #noPrompt")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
		rt.group(rt.selection, name = "ZZZ_ImportedGroup")
		
	elif Status == "OBJ" and queryKeepGroupStatus == False:
		obj = "C:/Temp_Exporter/temp.obj"
		rt.importFile(obj, rt.Name("noPrompt"))
		#MaxPlus.Core.EvalMAXScript("importfile \"" + obj + "\" #noPrompt")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
		
	elif Status == "Self" and queryKeepGroupStatus == True:
		max = "C:/Temp_Exporter/temp.max"
		rt.mergeMaxFile(max, rt.Name("promptDups"), rt.Name("promptMtlDups"))
		#MaxPlus.Core.EvalMAXScript("mergeMAXFile \"" + max + "\" #promptDups #promptMtlDups")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
		rt.group(rt.selection, name = "ZZZ_ImportedGroup")
		
	elif Status == "Self" and queryKeepGroupStatus == False:
		max = "C:/Temp_Exporter/temp.max"
		rt.mergeMaxFile(max, rt.Name("promptDups"), rt.Name("promptMtlDups"))
		#MaxPlus.Core.EvalMAXScript("mergeMAXFile \"" + max + "\" #promptDups #promptMtlDups")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)

	rt.units.SystemType = rt.Name(currentUnitSetup)
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
def addIDSuffix():
	for obj in rt.selection:
		mat = obj.mat
		if rt.classOf(mat) == rt.Multimaterial:
			for numMat in range(0,int(mat.numsubs)):
				if mat[numMat] != rt.undefined:
					currentName = mat[numMat].name
					newName = currentName + "_ID" + str(numMat+1)
					checkAlreadyHadIDSuffix = newName.split("_")
					if checkAlreadyHadIDSuffix[-1] != checkAlreadyHadIDSuffix[-2]:
						mat[numMat].name = newName
		else:
			rt.messageBox("Chuc nang nay chi danh cho Multi-Sub Material")
		
def removeIDSuffix():
	for obj in rt.selection:
		mat = obj.mat
		if rt.classOf(mat) == rt.Multimaterial:
			for numMat in range(0,int(mat.numsubs)):
				if mat[numMat] != rt.undefined:
					currentName = mat[numMat].name
					checkAlreadyHadIDSuffix = currentName.split("_")
					if "ID" in checkAlreadyHadIDSuffix[-1]:
						mat[numMat].name = "_".join(checkAlreadyHadIDSuffix[:-1])
		else:
			currentName = mat.name
			checkAlreadyHadIDSuffix = currentName.split("_")
			if "ID" in checkAlreadyHadIDSuffix[-1]:
				mat.name = "_".join(checkAlreadyHadIDSuffix[:-1])
			
def exportFileAndKeepID(cbKeepID, Status, keepVertexNormalStatus, exportBinaryStatus, keepInstanceStatus):
	if cbKeepID == "On":
		addIDSuffix()
		exportFile(Status, keepVertexNormalStatus, exportBinaryStatus, keepInstanceStatus)
		removeIDSuffix()
	else:
		exportFile(Status, keepVertexNormalStatus, exportBinaryStatus, keepInstanceStatus)

def fixID():
	needToFixList = []
	materialList = []
	for obj in rt.selection:
		needToFixList.append(obj)

	for obj in needToFixList:
		rt.deselect(rt.selection) 
		rt.select(obj)
		finalList = []
		mat = obj.mat
		if rt.classOf(mat) == rt.MultiMaterial:
			numFaces = rt.polyop.getNumFaces(obj)
			for face in range(1,numFaces+1):
				currentPolygonMaterialID = rt.polyop.getFaceMatID(obj, face)
				try:
					materialName = obj.material[currentPolygonMaterialID-1]
				except:
					pass
				tempList = []
				tempList.append(str(face))
				tempList.append(materialName)
				finalList.append(tempList)
			for i in finalList:
				matName = i[-1].name
				matID = matName.split("ID")[-1]
				#rt.polyop.setFaceMatID(obj,i[0],matID)
				rt.polyop.setFaceMatID(rt.selection[0], i[0], matID)
				#MaxPlus.Core.EvalMAXScript("polyop.setFaceMatID $ {} {}".format(i[0],matID))
		else:
			matName = mat.name
			matID = matName.split("ID")[-1]
			numFaces = rt.polyop.getNumFaces(obj)
			for face in range(1,numFaces+1):
				rt.polyop.setFaceMatID(rt.selection[0], str(face), matID)
				#MaxPlus.Core.EvalMAXScript("polyop.setFaceMatID $ {} {}".format(str(face),matID))
			
	for obj in needToFixList:
		rt.deselect(rt.selection)
		rt.select(obj)
		mat = obj.mat
		if rt.classOf(mat) == rt.MultiMaterial:
			numMat = 0
			rt.meditMaterials[8] = (rt.selection[0]).material
			#MaxPlus.Core.EvalMAXScript("meditMaterials[8] = $.material")
			for i in mat.materialList:
				currentName = i.name
				temp = currentName.split("_")
				temp2 = temp[-1].split("ID")
				position = int(temp2[-1])
				rt.meditMaterials[8].materialIDList[numMat] = position
				#MaxPlus.Core.EvalMAXScript("meditMaterials[8].materialIDList[{}] = {}".format(numMat,position))
				numMat = numMat + 1
	#removeIDSuffix()

def exportToUnity():
	exportCurrentFolder()

				
def exportWorkingFiles(Status, keepVertexNormalStatus, exportBinaryStatus, keepInstanceStatus):
	if keepVertexNormalStatus == "Off":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
		
	if exportBinaryStatus == "On":
		exportBinaryStatus = False
	else:
		exportBinaryStatus = True
		
	if keepInstanceStatus == "On":
		keepInstanceStatus = True
	else:
		keepInstanceStatus = False
		
	currentUnitSetup = str(rt.units.SystemType)
	exportConvertToCmScaleFactor = exportConvertToCmDict[currentUnitSetup]
	rt.units.SystemType = rt.Name("centimeters")
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
	if Status == "FBX":
		fbx = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.fbx"
		rt.FBXExporterSetParam("SmoothingGroups",True)
		rt.FBXExporterSetParam("PreserveEdgeOrientation",True)
		rt.FBXExporterSetParam("Preserveinstances", keepInstanceStatus)
		rt.FBXExporterSetParam("Animation",False)
		rt.FBXExporterSetParam("ShowWarnings",True)
		rt.FBXExporterSetParam("UpAxis","Y")
		rt.FBXExporterSetParam("ConvertUnit","cm")
		rt.FBXExporterSetParam("ScaleFactor",exportConvertToCmScaleFactor)
		rt.FBXExporterSetParam("ASCII", exportBinaryStatus)
		rt.FBXExporterSetParam("FileVersion","FBX201400")
		rt.exportFile(fbx, rt.Name("noPrompt"), selectedOnly = True, using = rt.FBXEXP)
		#MaxPlus.Core.EvalMAXScript("exportfile \"" + fbx + "\" #noPrompt selectedOnly:True using:FBXEXP")
		#MaxPlus.Core.EvalMAXScript("mergeMaxFile \"" + scene + "\" #(\"MaterialTemplate\",\"MaterialTemplate_Phys\" , \"MaterialTemplate_Proxy\")  #deleteOldDups #useMergedMtlDups quite:true")
	elif Status == "OBJ":
		obj = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.obj"
		theINI = rt.objimp.getIniName()
		rt.setINISetting(theINI, "General","UseLogging","1")
		rt.setINISetting(theINI, "Geometry","FlipZyAxis","1")
		rt.setINISetting(theINI, "Geometry", "ExportHiddenObjects", "1")
		rt.setINISetting(theINI, "Geometry", "FaceType", "1")
		rt.setINISetting(theINI, "Geometry", "Normals", "1")
		rt.setINISetting(theINI, "Geometry", "TextureCoords", "1")
		rt.setINISetting(theINI, "Geometry", "SmoothingGroups", "1")
		rt.setINISetting(theINI, "Geometry", "ObjScale", str(exportConvertToCmScaleFactor))
		rt.setINISetting(theINI, "Material", "UseMaterial", "1")
		rt.setINISetting(theINI, "Material", "CreateMatLibrary", "0")
		rt.setINISetting(theINI, "Material", "ForceBlackAmbient", "0")
		rt.setINISetting(theINI, "Output", "RelativeIndex", "0")
		rt.setINISetting(theINI, "Output", "Target", "0")
		rt.setINISetting(theINI, "Output", "Precision", "4")
		rt.setINISetting(theINI, "Optimize", "optVertex", "0")
		rt.setINISetting(theINI, "Optimize", "optNormals", "1")
		rt.setINISetting(theINI, "Optimize", "optTextureCoords", "1")
		rt.exportFile(obj, rt.Name("noPrompt"), selectedOnly = True, using = rt.ObjExp)
		#MaxPlus.Core.EvalMAXScript("exportfile \"" + obj + "\" #noPrompt selectedOnly:True using:ObjExp")
	elif Status == "Self":
		max = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.max"
		rt.saveNodes(rt.selection, max, quiet = True)
		#MaxPlus.Core.EvalMAXScript("saveNodes selection \"" + max + "\" quiet:True")
		#rt.saveNodes("selection","C:\\Temp\\temp_max.max","quiet:True")
	rt.units.SystemType = rt.Name(currentUnitSetup)
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
			
def importWorkingFiles(Status, keepVertexNormalStatus, queryKeepGroupStatus):
	if keepVertexNormalStatus == "Off":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
		
	if queryKeepGroupStatus == "On":
		queryKeepGroupStatus = True
	else:
		queryKeepGroupStatus = False
	
	currentUnitSetup = str(rt.units.SystemType)
	importConvertToCmScaleFactor = importConvertToCmDict[currentUnitSetup]
	if Status == "FBX" and queryKeepGroupStatus == True:
		fbx = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.fbx"
		rt.FBXImporterSetParam("Mode", "#create")
		rt.FBXImporterSetParam("SmoothingGroups", keepVertexNormalStatus)
		rt.FBXImporterSetParam("UpAxis", "Z")
		rt.FBXImporterSetParam("ConvertUnit", "cm")
		rt.FBXExporterSetParam("GenerateLog", True)
		rt.FBXImporterSetParam("ScaleFactor", importConvertToCmScaleFactor / rt.units.SystemScale)
		rt.importFile(fbx, rt.Name("noPrompt"))
		#MaxPlus.Core.EvalMAXScript("importfile \"" + fbx + "\" #noPrompt")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
		rt.group(rt.selection, name = "ZZZ_ImportedGroup")
	elif Status == "FBX" and queryKeepGroupStatus == False:
		fbx = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.fbx"
		rt.FBXImporterSetParam("Mode", "#create")
		rt.FBXImporterSetParam("SmoothingGroups", keepVertexNormalStatus)
		rt.FBXImporterSetParam("UpAxis", "Z")
		rt.FBXImporterSetParam("ConvertUnit", "cm")
		rt.FBXExporterSetParam("GenerateLog", True)
		rt.FBXImporterSetParam("ScaleFactor", importConvertToCmScaleFactor / rt.units.SystemScale)
		rt.importFile(fbx, rt.Name("noPrompt"))
		#MaxPlus.Core.EvalMAXScript("importfile \"" + fbx + "\" #noPrompt")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
	
	elif Status == "OBJ" and queryKeepGroupStatus == True:
		obj = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.obj"
		rt.importFile(obj, rt.Name("noPrompt"))
		#MaxPlus.Core.EvalMAXScript("importfile \"" + obj + "\" #noPrompt")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
		rt.group(rt.selection, name = "ZZZ_ImportedGroup")
		
	elif Status == "OBJ" and queryKeepGroupStatus == False:
		obj = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.obj"
		rt.importFile(obj, rt.Name("noPrompt"))
		#MaxPlus.Core.EvalMAXScript("importfile \"" + obj + "\" #noPrompt")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
		
	elif Status == "Self" and queryKeepGroupStatus == True:
		max = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.max"
		rt.mergeMaxFile(max, rt.Name("promptDups"), rt.Name("promptMtlDups"))
		#MaxPlus.Core.EvalMAXScript("mergeMAXFile \"" + max + "\" #promptDups #promptMtlDups")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
		rt.group(rt.selection, name = "ZZZ_ImportedGroup")
		
	elif Status == "Self" and queryKeepGroupStatus == False:
		max = "//glassegg.com/GROUPS/SHARE/PhuocHoang/EnvWorkingFiles/temp.max"
		rt.mergeMaxFile(max, rt.Name("promptDups"), rt.Name("promptMtlDups"))
		#MaxPlus.Core.EvalMAXScript("mergeMAXFile \"" + max + "\" #promptDups #promptMtlDups")
		for obj in rt.selection:
			if "tempExportGroup" in obj.name:
				rt.delete(obj)
	rt.units.SystemType = rt.Name(currentUnitSetup)
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")

def exportLowPoly(keepVertexNormalStatus):
	if keepVertexNormalStatus == "Off":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
		
	currentUnitSetup = str(rt.units.SystemType)
	exportConvertToCmScaleFactor = exportConvertToCmDict[currentUnitSetup]
	rt.units.SystemType = rt.Name("centimeters")
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
	fbx = "C:/Temp_Exporter/temp_lowpoly.fbx"
	rt.FBXExporterSetParam("SmoothingGroups",True)
	rt.FBXExporterSetParam("PreserveEdgeOrientation",False)
	rt.FBXExporterSetParam("Animation",False)
	rt.FBXExporterSetParam("ShowWarnings",True)
	rt.FBXExporterSetParam("UpAxis","Y")
	rt.FBXExporterSetParam("ConvertUnit","cm")
	rt.FBXExporterSetParam("ScaleFactor",exportConvertToCmScaleFactor)
	rt.FBXExporterSetParam("ASCII", False)
	rt.FBXExporterSetParam("FileVersion","FBX201400")
	rt.exportFile(fbx, rt.Name("noPrompt"), selectedOnly = True, using = rt.FBXEXP)
	#MaxPlus.Core.EvalMAXScript("exportfile \"" + fbx + "\" #noPrompt selectedOnly:True using:FBXEXP")
	rt.units.SystemType = rt.Name(currentUnitSetup)
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
	
def exportHighPoly(keepVertexNormalStatus):
	if keepVertexNormalStatus == "On":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
		
	currentUnitSetup = str(rt.units.SystemType)
	exportConvertToCmScaleFactor = exportConvertToCmDict[currentUnitSetup]
	rt.units.SystemType = rt.Name("centimeters")
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
	fbx = "C:/Temp_Exporter/temp_highpoly.fbx"
	for obj in rt.selection:
		rt.collapseStack(obj)
		#MaxPlus.Core.EvalMAXScript("collapseStack $")
	rt.FBXExporterSetParam("SmoothingGroups",True)
	rt.FBXExporterSetParam("PreserveEdgeOrientation",True)
	rt.FBXExporterSetParam("ASCII",False)
	rt.FBXExporterSetParam("SmoothMeshExport",True)
	rt.FBXExporterSetParam("Animation",False)
	rt.FBXExporterSetParam("ShowWarnings",True)
	rt.FBXExporterSetParam("UpAxis","Y")
	rt.FBXExporterSetParam("ConvertUnit","cm")
	rt.FBXExporterSetParam("ScaleFactor",exportConvertToCmScaleFactor)
	rt.FBXExporterSetParam("ASCII", False)
	rt.FBXExporterSetParam("FileVersion","FBX201400")
	rt.exportFile(fbx, rt.Name("noPrompt"), selectedOnly = True, using = rt.FBXEXP)
	#MaxPlus.Core.EvalMAXScript("exportfile \"" + fbx + "\" #noPrompt selectedOnly:True using:FBXEXP")
	rt.units.SystemType = rt.Name(currentUnitSetup)
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
	
def exportSeparatePart(Status, keepVertexNormalStatus):
	if keepVertexNormalStatus == "Off":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
	currentUnitSetup = str(rt.units.SystemType)
	exportConvertToCmScaleFactor = exportConvertToCmDict[currentUnitSetup]
	rt.units.SystemType = rt.Name("centimeters")
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
	if Status == "FBX":
		selectedObj = rt.selection
		for obj in list(selectedObj):
			rt.select(obj)
			fbx = "C:/Temp_Exporter/" + obj.name + ".fbx"
			rt.FBXExporterSetParam("SmoothingGroups",True)
			rt.FBXExporterSetParam("PreserveEdgeOrientation",False)
			rt.FBXExporterSetParam("Animation",False)
			rt.FBXExporterSetParam("ShowWarnings",True)
			rt.FBXExporterSetParam("UpAxis","Y")
			rt.FBXExporterSetParam("ConvertUnit","cm")
			rt.FBXExporterSetParam("ScaleFactor",exportConvertToCmScaleFactor)
			rt.FBXExporterSetParam("ASCII", True)
			rt.FBXExporterSetParam("FileVersion","FBX201400")
			rt.exportFile(fbx, rt.Name("noPrompt"), selectedOnly = True, using = rt.FBXEXP)
			#MaxPlus.Core.EvalMAXScript("exportfile \"" + fbx + "\" #noPrompt selectedOnly:True using:FBXEXP")
			rt.clearSelection()
			#MaxPlus.Core.EvalMAXScript("max select none")
	elif Status == "OBJ":
		selectedObj = rt.selection
		for obje in list(selectedObj):
			rt.select(obje)
			obj = "C:/Temp_Exporter/" + obje.name + ".obj"
			theINI = rt.objimp.getIniName()
			rt.setINISetting(theINI, "General","UseLogging","1")
			rt.setINISetting(theINI, "Geometry","FlipZyAxis","1")
			rt.setINISetting(theINI, "Geometry", "ExportHiddenObjects", "1")
			rt.setINISetting(theINI, "Geometry", "FaceType", "1")
			rt.setINISetting(theINI, "Geometry", "Normals", "1")
			rt.setINISetting(theINI, "Geometry", "TextureCoords", "1")
			rt.setINISetting(theINI, "Geometry", "SmoothingGroups", "1")
			rt.setINISetting(theINI, "Geometry", "ObjScale", str(exportConvertToCmScaleFactor))
			rt.setINISetting(theINI, "Material", "UseMaterial", "1")
			rt.setINISetting(theINI, "Material", "CreateMatLibrary", "0")
			rt.setINISetting(theINI, "Material", "ForceBlackAmbient", "0")
			rt.setINISetting(theINI, "Output", "RelativeIndex", "0")
			rt.setINISetting(theINI, "Output", "Target", "0")
			rt.setINISetting(theINI, "Output", "Precision", "4")
			rt.setINISetting(theINI, "Optimize", "optVertex", "0")
			rt.setINISetting(theINI, "Optimize", "optNormals", "1")
			rt.setINISetting(theINI, "Optimize", "optTextureCoords", "1")
			rt.exportFile(obj, rt.Name("noPrompt"), selectedOnly = True, using = rt.ObjExp)
			#MaxPlus.Core.EvalMAXScript("exportfile \"" + obj + "\" #noPrompt selectedOnly:True using:ObjExp")
			rt.clearSelection()
			#MaxPlus.Core.EvalMAXScript("max select none")
	elif Status == "Self":
		selectedObj = rt.selection
		for obj in list(selectedObj):
			rt.select(obj)
			max = "C:/Temp_Exporter/" + obj.name + ".max"
			rt.saveNodes(rt.selection, max, quiet = True)
			#MaxPlus.Core.EvalMAXScript("saveNodes selection \"" + max + "\" quiet:True")
			rt.clearSelection()
			#MaxPlus.Core.EvalMAXScript("max select none")
	rt.units.SystemType = rt.Name(currentUnitSetup)
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
		
def openTempFolder():
	os.startfile('C:/Temp_Exporter')
				
def deleteTempFolderContents():
	folder = 'C:/Temp_Exporter'
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print(e)
	
def exportToSubstancePainter(keepVertexNormalStatus):
	if keepVertexNormalStatus == "Off":
		keepVertexNormalStatus = True
	else:
		keepVertexNormalStatus = False
		
	currentUnitSetup = str(rt.units.SystemType)
	exportConvertToCmScaleFactor = exportConvertToCmDict[currentUnitSetup]
	rt.units.SystemType = rt.Name("centimeters")
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #centimeters")
	fbx = "C:/Temp_Exporter/temp_SubstancePainter.fbx"
	rt.FBXExporterSetParam("SmoothingGroups",True)
	rt.FBXExporterSetParam("PreserveEdgeOrientation",True)
	rt.FBXExporterSetParam("TangentSpaceExport",True)
	#rt.FBXExporterSetParam("ColladaTriangulate",True)
	rt.FBXExporterSetParam("Animation",False)
	rt.FBXExporterSetParam("ShowWarnings",True)
	rt.FBXExporterSetParam("UpAxis","Y")
	rt.FBXExporterSetParam("ConvertUnit","cm")
	rt.FBXExporterSetParam("ScaleFactor",exportConvertToCmScaleFactor)
	rt.FBXExporterSetParam("ASCII", True)
	rt.FBXExporterSetParam("FileVersion","FBX201400")
	rt.exportFile(fbx, rt.Name("noPrompt"), selectedOnly = True, using = rt.FBXEXP)
	#MaxPlus.Core.EvalMAXScript("exportfile \"" + fbx + "\" #noPrompt selectedOnly:True using:FBXEXP")
	rt.units.SystemType = rt.Name(currentUnitSetup)
	#MaxPlus.Core.EvalMAXScript("units.SystemType = #"+currentUnitSetup+"")
	
def createTempFolder():
	directoryPath = "C:\\Temp_Exporter"
	if os.path.exists(directoryPath) == False:
		os.mkdir(directoryPath)