import maya.cmds as cmds
import math

class TexelDensityFunction():
	def __init__(self):
		pass

	def getTexelDensity(self, mapWidth, mapHeight):
		if len(cmds.ls(sl = True)) > 0:
			# Convert selection to faces 
			selectionFaces = cmds.ls(sl = True)
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
			return texelDensity
		else:
			return False

	def setTexelDensity(self, mapWidth, mapHeight):
		pass
#a = TexelDensityFunction()
#b = a.getTexelDensity(512, 512)
#print (b)
