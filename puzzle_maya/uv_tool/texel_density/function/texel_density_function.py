import maya.api.OpenMaya as om
import maya.cmds as cmds
import math
systemUnitConvertDict = {"inch": 0.0254, "foot": 0.3048, "millimeter": 0.001, "centimeter": 0.01, "meter": 1.0, "yard": 1.0936}
class TexelDensityFunction():
	def __init__(self):
		pass

	def calculateUVArea(self):
		return cmds.polyEvaluate(uvFaceArea = True)

	def calculateFaceArea(self):
		return cmds.polyEvaluate(worldArea = True)

	def convertCurrentUnitSetupToMeter(self):
		currentUnitSetupName = cmds.currentUnit( query=True, fullName = True)
		return systemUnitConvertDict[currentUnitSetupName]

	def getTexelDensity(self, mapWidth, mapHeight):
		if cmds.ls(sl = True):
			selectionFaces = cmds.filterExpand(cmds.ls(sl = True),expand = False, selectionMask = 34 )
			# Calculate the uv's area
			areaUV = self.calculateUVArea()
			# Calculate the total texture area
			textureArea = mapWidth * mapHeight
			# Calculate the used area
			usedAreaPixels = areaUV * textureArea
			# Get current selection faces area
			areaGeometry = self.calculateFaceArea(selectionFaces)
			return usedAreaPixels
			# Calculate the texel density
			#texelDensity = math.sqrt(usedAreaPixels/areaGeometry)
			#return texelDensity
a = TexelDensityFunction()
b = a.getTexelDensity(512, 512)
print (b)
'''
fn GetTexelDensity w h =
(
	--Check the Modifier Class whether it is unwrap_uvw or not
	if classof (unwrapmod = modpanel.getcurrentobject()) == unwrap_uvw do
	(
		--Make an array of selected Faces
		if (faces = unwrapmod.getselectedfaces()).count > 0 do
		(
			-- Get some information about the selection
			unwrapmod.getarea faces &mX &mY &mWidth &mHeight &mAreaUVW &mAreaGeom

			-- Calculate the total texture area
-- 			textureArea = theMapSize^2
			textureArea = w*h
			-- Calculate the used area
			usedAreaPixels = mAreaUVW * textureArea

			-- Calculate the texel density
			texelDensity = sqrt (usedAreaPixels/mAreaGeom)
			-- break()
		)
	)
	texelDensity --return value
) --end of fuction
'''