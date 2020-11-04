import pymxs
import json
import os
import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
rt = pymxs.runtime
puzzleRootPath = rt.puzzleRootPath



class DecalImportFunction():
	def __init__(self):
		self.decalsFullPathList = []
		self.diffuseDecalPath = None
		self.decalResources = puzzleRootPath + "/" + "lib" + "/" + "resource" + "/" + "decals"

	def updateDecalsComboBox(self):
		decalList = []
		for file in os.listdir(self.decalResources):
			if file.endswith(".max"):
				decalMaxFile = file.split(".")[0]
				decalList.append(decalMaxFile)
				self.decalsFullPathList.append(os.path.join(self.decalResources, file).replace("\\","/"))

		return decalList

	def setImageForGraphicView(self, bitmapPath, graphicsView):
		pixmap = QtGui.QPixmap(bitmapPath)
		self.scene = QtWidgets.QGraphicsScene()
		self.scene.addPixmap(pixmap)
		graphicsView.setScene(self.scene)
		graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

	def showEvent(self, graphicsView):
		graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

	def showDecalImage(self, graphicsView, cbbDecal):
		currentSelectedDecal = cbbDecal.currentText()
		for decal in self.decalsFullPathList:
			if currentSelectedDecal.lower() in (decal.split("/")[-1]).lower():
				foundFlag = True
				self.diffuseDecalPath = self.decalResources + "/" + currentSelectedDecal + "_D" + ".tga"
				if os.path.isfile(self.diffuseDecalPath):
					self.setImageForGraphicView(self.diffuseDecalPath, graphicsView)
					break

	def getDataFromJsonFile(self):
		if self.diffuseDecalPath != None:
			decalDataFilePath = self.diffuseDecalPath.replace("_D.tga", ".json")
			decalMaxFilePath = self.diffuseDecalPath.replace("_D.tga", ".max")
			if os.path.isfile(decalDataFilePath) == True and os.path.isfile(decalMaxFilePath) == True:
				self.threedsmaxLocation = decalMaxFilePath
				with open(decalDataFilePath, 'rb') as file:
					data = json.load(file)
					return data
			else:
				rt.messageBox("Decal Data needs 2 available files: Json and Max. Please check again.")
				return None
		else:
			return None

	def getObjBoundingBoxData(self):
		decalDataDict = self.getDataFromJsonFile()
		if decalDataDict != None:
			objBoundingBox = {}
			for objectName, pointData in decalDataDict.items():
				objMax = pointData[0]
				objMin = pointData[-1]
	
				vertexList = []
				vertexList.append([objMin, objMin])
				vertexList.append([objMax, objMax])
				if objectName in objBoundingBox.keys():
					objBoundingBox[objectName].append(vertexList)
				else:
					objBoundingBox[objectName] = vertexList
			return objBoundingBox

	def analyzeDecalData(self, p):
		objectBoundingBox = self.getObjBoundingBoxData()
		if len(objectBoundingBox) > 0:
			minRowValue = 0
			maxRowValue = 608
			minColumnValue = 26
			maxColumnValue = 628
			largestX = 0
			largestY = 0
			# Convert pressed point to 0 -> 1 range
			newPy = float(p.y() / maxColumnValue) - 0.04
			newPx = float(p.x() / maxRowValue)
			newPx = round(newPx, 3)
			newPy = round(newPy, 3)

			# Get largestX and largestY from decal data
			for obj, vertexData in objectBoundingBox.items():
				for i in range(len(vertexData)):
					if vertexData[i][0][0] > largestX:
						largestX = vertexData[i][0][0]
					if -vertexData[i][-1][1] > largestY:
						largestY = -vertexData[i][-1][1]

			for obj, vertexData in objectBoundingBox.items():
				xList = []
				yList = []
				for i in range(len(vertexData)):
					convertedX = vertexData[i][0][0]/ largestX
					convertedY = -vertexData[i][-1][1] / largestY
					convertedX = round(convertedX, 3)
					convertedY = round(convertedY, 3)

					xList.append(convertedX)
					yList.append(convertedY)
				xList = list(set(xList))
				yList = list(set(yList))
				minX = None
				minY = None
				maxX = None
				maxY = None

				if xList[0] < xList[-1]:
					minX = xList[0]
					maxX = xList[-1]
				if xList[0] > xList[-1]:
					minX = xList[-1]
					maxX = xList[0]

				if yList[0] < yList[-1]:
					minY = yList[0]
					maxY = yList[-1]
				if yList[0] > yList[-1]:
					minY = yList[-1]
					maxY = yList[0]


				if newPx > minX and newPx < maxX:
					if newPy > minY and newPy < maxY:
						rt.mergeMAXFile(self.threedsmaxLocation, [obj], rt.Name("AutoRenameDups"), rt.Name("renameMtlDups"), rt.Name("select"))
						snapDecalMSFilePath = puzzleRootPath + "/" + "puzzle_max" + "/" + "decal_tool" + "/" + "function"
						snapDecalMSScriptFile = snapDecalMSFilePath + "/" + "decal_snap_function.ms"
						rt.filein(snapDecalMSScriptFile)