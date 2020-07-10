import maya.cmds as cmds
import os
import json
class GlobalTransferAnimVariables:
	def __init__(self):
		currentFilePath = os.path.dirname(os.path.abspath(__file__))
		currentFilePath = currentFilePath.replace("\\","/")
		currentFilePath = ("/".join(currentFilePath.split("/")[:-1]))
		self.userScriptPath = currentFilePath
		self.animExportImportDLL = "animImportExport"
		self.jsonPath = self.userScriptPath + "/database"
		
GlobalTransferAnimVariables = GlobalTransferAnimVariables()
"""
def enableAnimPlugin():
	pluginName = None
	animExportImportDLL = "animImportExport"
	os = cmds.about(os=1)
	if os == 'win64':
		pluginName = '%s.mll' % (animExportImportDLL)
		
	if not cmds.pluginInfo(pluginName, q=True, l=True ):
		try:
			cmds.loadPlugin(pluginName, qt = True)
			cmds.info('Plug-in: %s loaded success!' %(pluginName))
		except: 
			print ('Plug-in: %s was not found in MAYA PLUGIN PATH!' %(pluginName))
	else:
		print ('Plug-in: %s loaded success!' %(pluginName))


def getAnimatedObjList():
	allTransforms = cmds.ls(type = "transform")
	allAnimatedObjs = []
	cmds.select(clear = True)
	for obj in allTransforms:
		numKeyframes = cmds.keyframe(obj, query = True, keyframeCount = True)
		if numKeyframes > 0:
			cmds.select(obj, add = True)
			allAnimatedObjs.append(obj)
			
	return allAnimatedObjs
	

	
def enableAnimPlugin():
	pluginName = None
	os = cmds.about(os=1)
	if os == 'win64':
		pluginName = '%s.mll' % (GlobalTransferAnimVariables.animExportImportDLL)
		
	if not cmds.pluginInfo(pluginName, q=True, l=True ):
		try:
			cmds.loadPlugin(pluginName, qt = True)
			cmds.info('Plug-in: %s loaded success!' %(pluginName))
		except: 
			print ('Plug-in: %s was not found in MAYA PLUGIN PATH!' %(pluginName))
	else:
		print ('Plug-in: %s loaded success!' %(pluginName))
		
def exportAnim():
	filePath = "C:/Users/phuochoang/Desktop/Tools/LEGO_Outsource/test.anim"
	cmds.file(filePath, force = True, type = "animExport", exportSelectedAnim = True)
	
def importAnim():
	filePath = "C:/Users/phuochoang/Desktop/Tools/LEGO_Outsource/test.anim"
	cmds.file(filePath, i = True, importFrameRate = True, importTimeRange = "override", type = "animExport")
	
def testExport():
	getAnimatedObjList()
	if cmds.ls(sl = True):
		exportAnim()
	else:
		print ("No animated objects in scene")
		
def printObjToFileTXT():
	file1 = open("C:/Users/phuochoang/Desktop/Tools/LEGO_Outsource/myfile.txt","w")
	getAnimatedObjList()
	if cmds.ls(sl = True):
		for obj in cmds.ls(sl = True, long = True):
			file1.write(obj + "\n")
	file1.close()
"""

class TransferTransformFunction:
	def __init__(self):
		pass
		
	
	def checkTransformDataFileExistance(self, jsonFilePath):
		if os.path.exists(jsonFilePath):
			os.remove(jsonFilePath)

	def getTransformDataFilePath(self):
		filepath = cmds.file(q=True, sn=True)
		filepath = (filepath.split("/")[-1]).split(".")[0] + ".json"
		return (GlobalTransferAnimVariables.jsonPath + "/" + filepath)
			
	def queryObjectTransformation(self, objectFullName):
		dataDict = {}
		translation = cmds.xform(objectFullName, query=True, worldSpace=True, matrix=True )
		#translation =  cmds.xform(objectFullName, query = True, worldSpace = True, rp = True)
		#rotation = cmds.xform(objectFullName, query = True, worldSpace = True, ro = True)
		#scalation = cmds.xform(objectFullName, query = True, worldSpace = True, sp = True)
		#dataDict[objectFullName] = translation, rotation, scalation
		dataDict[objectFullName] = translation
		return dataDict
		
	def printDataToJsonFile(self):
		self.allTransformData = []
		allTransforms = cmds.ls(type = "transform") #Get all transform groups in scene
		cmds.select(allTransforms) #Select all transform groups
		jsonFilePath = self.getTransformDataFilePath()
		if cmds.ls(sl = True):
			self.checkTransformDataFileExistance(jsonFilePath) #Remove old file data json if it is available
			for obj in cmds.ls(sl = True, long = True):
				tempDataDict = self.queryObjectTransformation(obj)
				self.allTransformData.append(tempDataDict)
			with open(jsonFilePath,"a") as f:
				try:
					json.dump(self.allTransformData, f, indent=4)
					cmds.confirmDialog(title = "Successful", message = "Export Transform Data Successfully!!!")
				except:
					cmds.confirmDialog(title = "Failed", message = "Export Transform Data Failed!!!")
					
		
	def unGroupToWorld(self, obj):
		if cmds.objExists(obj):
			cmds.select(obj)
			oldFullObjName = cmds.ls(sl = True, long = True)[0]
			try:
				cmds.parent(oldFullObjName, world = True)
			except:
				pass
			oldGroup = "|".join(oldFullObjName.split("|")[:-1])
			return oldGroup
		else:
			return False
				
	def readFileJson(self, jsonFilePath):
		missingObjects = []
		with open(jsonFilePath) as json_file:
			json_data = json.load(json_file)
			cmds.select(clear = True)
			for data in json_data:
				for obj, transform in data.iteritems():
					if cmds.objExists(obj):
						cmds.select(obj)
						cmds.xform( cmds.ls(sl = True)[0], worldSpace=True, matrix=transform)
					else:
						missingObjects.append(obj)
		if missingObjects:
			return missingObjects
		else:
			return True
						
	def applyTransformDataToTargetFile(targetFileName):
		pass
		
						#print transform
					#oldGroup = self.unGroupToWorld(obj)
					#if oldGroup != "" and oldGroup != False:
						#cmds.move(transform[0][0], transform[0][1], transform[0][2], cmds.ls(sl = True)[0], rpr = True)
						#cmds.rotate(transform[1][0], transform[1][1], transform[1][2], cmds.ls(sl = True)[0], ws = True, a = True)
						#cmds.scale(transform[2][0], transform[2][1], transform[2][2], cmds.ls(sl = True)[0], ws = True, a = True)
						#cmds.parent(cmds.ls(sl = True)[0], oldGroup)
					#elif oldGroup == "" and oldGroup != False:
						#cmds.move(transform[0][0], transform[0][1], transform[0][2], cmds.ls(sl = True)[0], rpr = True, ws = True)
						#cmds.rotate(transform[1][0], transform[1][1], transform[1][2], cmds.ls(sl = True)[0], ws = True, a = True)
						#cmds.scale(transform[2][0], transform[2][1], transform[2][2], cmds.ls(sl = True)[0], ws = True, a = True)
#ahihi = TransferTransformFunction()
#ahihi.readFileJson()
#ahihi.printDataToJsonFile()
#a = cmds.ls(type = "transform")
#cmds.select(a)a)