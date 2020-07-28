import maya.cmds as cmds
import math

class TexelDensityFunction():
	def __init__(self):
		pass

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
