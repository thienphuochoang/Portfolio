import sys
import pymxs
import os
import PySide2
import importlib
from PySide2 import QtCore, QtWidgets, QtGui
from qtmax import GetQMaxMainWindow
rt = pymxs.runtime

currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")

sys.path.append(r"D:\WIP_Portfolio")

snapDecalMSFilePath = "/".join(currentFilePath.split("/")[:-1]) + "/" + "function"
snapDecalMSScriptFile = snapDecalMSFilePath + "/" + "decal_snap_function.ms"
rt.filein(snapDecalMSScriptFile)

decalResources = "/".join(currentFilePath.split("/")[:-3]) + "/" + "lib" + "/" + "resource" + "/" + "decals"

def import_file(str_module):
	"""import a module from string"""
	nameModule = importlib.import_module(str_module)
	try:
		importlib.reload(nameModule)
	except:
		reload(nameModule)
	return nameModule
	
#import Function____________________
ui = import_file("lib.ui.DecalSnapUI")

class SnapDecalMainWindow(QtWidgets.QMainWindow, ui.Ui_MainWindow):
	def __init__(self, parent=None):
		super(SnapDecalMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.decalsFullPathList = []
		#self.updateBiomesComboBox()
		self.updateDecalsComboBox()
		#self.showSwatchTintImage()
		self.showDecalImage()
		self.cbbDecal.currentTextChanged.connect(lambda: self.showDecalImage())
		#self.cbbBiomes.currentTextChanged.connect(lambda: self.updateDecalsComboBox())
	
	def setImageForGraphicView(self, bitmapPath):
		self.pixmap = QtGui.QPixmap(bitmapPath)

		self.scene = QtWidgets.QGraphicsScene()

		self.scene.addPixmap(self.pixmap)

		
		self.graphicsView.setScene(self.scene)
		self.graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

		

	def showEvent(self, event):
		self.graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

		

	def updateDecalsComboBox(self):
		decalList = []
		for file in os.listdir(decalResources):
			if file.endswith(".max"):
				decalMaxFile = file.split(".")[0]
				decalList.append(decalMaxFile)
				self.decalsFullPathList.append(os.path.join(decalResources, file).replace("\\","/"))

		self.cbbDecal.clear()
		self.cbbDecal.addItems(sorted(decalList))
			#print "decalFolder"
		#self.biomesFullPathList + "/" + "Decals"

	# def getDataFromDecalDataDumpFile(self, texFileName):
	# 	foundFlag = False
	# 	for f in os.listdir(dumpFilesPath):
	# 		if (f.split(".")[0]).lower() in texFileName.lower():
	# 			foundFlag = True
	# 			fullDumpFilePath = os.path.join(dumpFilesPath, f)
	# 			with open(fullDumpFilePath, 'rb') as file:
	# 				data = pickle.load(file)
	# 				for objectGeneralData in data.iteritems():
	# 					for eachData in objectGeneralData:
	# 						if type(eachData) is list:
	# 							return eachData
	# 	if foundFlag == False:
	# 		rt.messageBox("Khong tim thay du lieu decal tuong ung trong file Dump. Vui long lien he Tech")


	# def getDataFromMSFile(self):
	# 	threedsmaxDecalFilePath = decalMaxFilesPath + "/" + self.cbbBiomes.currentText() + "/" + "Decals"
	# 	threedsmaxDecalFilePath = threedsmaxDecalFilePath.replace("\\", "/")
	# 	textureFile = (self.cbbDecal.currentText()).split(".")[0]
	# 	foundFlag = False
	# 	if os.path.exists(threedsmaxDecalFilePath):
	# 		for folder in os.listdir(threedsmaxDecalFilePath):
	# 			if folder.lower() in textureFile.lower():
	# 				objectNameAndPointDataList = self.getDataFromDecalDataDumpFile(folder)
	# 				foundFlag = True
	# 				threedsmaxLocation = "/" + "3dsMax" + "/" + folder + ".max"
	# 				threedsmaxLocation = os.path.join(threedsmaxDecalFilePath, folder) + threedsmaxLocation
	# 				threedsmaxLocation = threedsmaxLocation.replace("\\","/")
	# 				objBoundingBox = {}
	# 				for eachObjectNameAndPointData in objectNameAndPointDataList:
	# 					for objectName, pointData in eachObjectNameAndPointData.iteritems():

	# 						if "Model".lower() not in objectName.lower():
	# 							objMax = pointData["max"]
	# 							objMin = pointData["min"]
								
	# 							vertexList = []
	# 							vertexList.append([objMin[0], objMin[1]])
	# 							vertexList.append([objMax[0], objMax[1]])
	# 							if objectName in objBoundingBox.keys():
	# 								objBoundingBox[objectName].append(vertexList)
	# 							else:
	# 								objBoundingBox[objectName] = vertexList
	# 							#a = rt.getObjectBoundingBox(objectName, objMax, objMin)
	# 							#print a


	# 							#print threedsmaxLocation
	# 							#dataList = rt.getObjectBoundingBox(threedsmaxLocation)
	# 							#dataList = list(dataList)

	# 				return objBoundingBox, threedsmaxLocation
					
	# 		if foundFlag == False:
	# 			rt.messageBox("Khong tim thay file 3DSMax tuong ung voi decal trong working files")
	# 	else:
	# 		rt.messageBox("Khong tim thay folder asset tuong ung voi decal trong working files")

		
	def showDecalImage(self):
		self.foundFlag = False
		currentSelectedDecal = self.cbbDecal.currentText()
		for decal in self.decalsFullPathList:
			if currentSelectedDecal.lower() in (decal.split("/")[-1]).lower():
				self.foundFlag = True
				diffuseDecalPath = decalResources + "/" + currentSelectedDecal + "_D" + ".tga"
				self.setImageForGraphicView(diffuseDecalPath)
				print (diffuseDecalPath)
				break
			else:
				continue
		if self.foundFlag == False:
			pass
			#self.setImageForGraphicView(BITMAP)
			

		
		
	
	# def mousePressEvent(self, event):
	# 	p = event.localPos()

	# 	objectBoundingBox, threedsmaxLocation = self.getDataFromMSFile()
	# 	print (objectBoundingBox)
	# 	print (threedsmaxLocation)
		
	# 	if objectBoundingBox and threedsmaxLocation:
	# 		minRowValue = 0
	# 		maxRowValue = 608
	# 		minColumnValue = 26
	# 		maxColumnValue = 628
	# 		largestX = 0
	# 		largestY = 0
	# 		# Convert pressed point to 0 -> 1 range
	# 		newPy = float(p.y() / maxColumnValue) - 0.04
	# 		newPx = float(p.x() / maxRowValue)
	# 		newPx = round(newPx, 3)
	# 		newPy = round(newPy, 3)
	# 		for obj, vertexData in objectBoundingBox.iteritems():
	# 			for i in range(len(vertexData)):
	# 				if vertexData[i][0] > largestX:
	# 					largestX = vertexData[i][0]
	# 				if -vertexData[i][-1] > largestY:
	# 					largestY = -vertexData[i][-1]

	# 		for obj, vertexData in objectBoundingBox.iteritems():
	# 			xList = []
	# 			yList = []
	# 			for i in range(len(vertexData)):
	# 				convertedX = vertexData[i][0] / largestX
	# 				convertedY = -vertexData[i][-1] / largestY
	# 				convertedX = round(convertedX, 3)
	# 				convertedY = round(convertedY, 3)

	# 				xList.append(convertedX)
	# 				yList.append(convertedY)
	# 			xList = list(set(xList))
	# 			yList = list(set(yList))
	# 			minX = None
	# 			minY = None
	# 			maxX = None
	# 			maxY = None

	# 			if xList[0] < xList[-1]:
	# 				minX = xList[0]
	# 				maxX = xList[-1]
	# 			if xList[0] > xList[-1]:
	# 				minX = xList[-1]
	# 				maxX = xList[0]

	# 			if yList[0] < yList[-1]:
	# 				minY = yList[0]
	# 				maxY = yList[-1]
	# 			if yList[0] > yList[-1]:
	# 				minY = yList[-1]
	# 				maxY = yList[0]


	# 			if newPx > minX and newPx < maxX:
	# 				if newPy > minY and newPy < maxY:
	# 					rt.mergeMAXFile(threedsmaxLocation, [obj], rt.Name("AutoRenameDups"), rt.Name("renameMtlDups"), rt.Name("select"))
	# 					MaxPlus.Core.EvalMAXScript("startTool AlignToSurface")

window = SnapDecalMainWindow(GetQMaxMainWindow())
window.show()
