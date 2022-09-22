import maya.mel as mel
import maya.cmds as cmds
import math
class VertexSnapingFunction():
	def __init__(self):
		pass

	def calculateLengthBetweenTwoVertexes(self, x1Pos, x2Pos):
		xLength = math.pow(x2Pos[0] - x1Pos[0], 2)
		yLength = math.pow(x2Pos[1] - x1Pos[1], 2)
		zLength = math.pow(x2Pos[2] - x1Pos[2], 2)
		length = math.sqrt(xLength + yLength + zLength)
		return length

	def getVertexIndexBasedOnPosition(self, selectedObj, selectedVtPos, flag):

		inloc = None
		if flag == 1:
			inloc = cmds.spaceLocator(name = "FirstPointLocaltor")[0]
		else:
			inloc = cmds.spaceLocator(name = "SecondPointLocaltor")[0]

		
		cpom = cmds.createNode('closestPointOnMesh')

		pos = selectedVtPos.strip('][').split(', ') 
		cmds.move(pos[0], pos[1], pos[2], inloc)
		shape = cmds.listRelatives(selectedObj, s=True, f=True)[0]
		cmds.connectAttr('%s.worldMesh' % shape, '%s.inMesh' % cpom)
		cmds.connectAttr('%s.worldMatrix' % shape, '%s.inputMatrix' % cpom)
		cmds.connectAttr('%s.translate' % inloc, '%s.inPosition' % cpom)
		
		vtxIndx = cmds.getAttr(cpom + ".closestVertexIndex")

		cmds.delete(cpom)
		cmds.delete(inloc)

		return vtxIndx

	def findTwoClosestVertex(self, eps):
		vtSelDict = {}
		vtSrcDict = {}
		
		#Get selected vertex and position
		vtSel = cmds.ls(l = True, fl = True, sl = True)
		for vt in vtSel:
			vtPos = cmds.xform(vt, q = True, ws = True, t = True)
			vtSelDict[vt] = vtPos
		
		# Get selected Object's all vertex
		objSel = cmds.ls(l = True, hilite = True)
		cmds.select(cl = True)
		cmds.select(objSel[0])
		mel.eval("ConvertSelectionToVertices ;")
		vtSrc = cmds.ls(l = True, fl = True, sl = True)
		for vt in vtSrc:
			vtPos = cmds.xform(vt, q = True, ws = True, t = True)
			vtSrcDict[vt] = vtPos
			
		cmds.select(cl = True)
		
		neededToMergeVertexDict = {}
		

		for eachVTSel, eachVTSelPos in vtSelDict.items():
			shortestLength = 0
			pickedVt = None
			count = 0
			for eachVTSrc, eachVTSrcPos in vtSrcDict.items():
				# Calculate length between 2 vertex (selected vertex and other object's vertex)
				length = self.calculateLengthBetweenTwoVertexes(eachVTSelPos, eachVTSrcPos)

				# Get closest vertex
				if count == 0:
					shortestLength = length
					pickedVt = eachVTSrc
					count = count + 1
				else:
					if length < shortestLength:
						shortestLength = length
						pickedVt = eachVTSrc
					
			if (shortestLength < eps):
				desPos = cmds.xform(pickedVt, q = True, ws = True, t = True)
				neededToMergeVertexDict[repr(eachVTSelPos)] = repr(desPos)

		return neededToMergeVertexDict, objSel[0]

			

	def mergeVertexToCenter(self, eps):
		neededToMergeVertexDict, selectedObj = self.findTwoClosestVertex(eps)
		# Depend on position, get object vertex and merge the closest one 
		for vtSelPos, vtDesPos in neededToMergeVertexDict.items():

			vtxIndx1 = self.getVertexIndexBasedOnPosition(selectedObj, vtSelPos, 1)

			vtxIndx2 = self.getVertexIndexBasedOnPosition(selectedObj, vtDesPos, 2)
			
			cmds.select(cl = True)
			cmds.select(selectedObj + ".vtx[" + str(vtxIndx1) + "]")
			cmds.select(selectedObj + ".vtx[" + str(vtxIndx2) + "]", add = True)

			mel.eval("polyMergeToCenter")

	def snapSelectedVertexToClosestOne(self, eps):
		neededToMergeVertexDict, selectedObj = self.findTwoClosestVertex(eps)
		# Depend on position, get object vertex and merge the closest one 
		for vtSelPos, vtDesPos in neededToMergeVertexDict.items():

			vtxIndx1 = self.getVertexIndexBasedOnPosition(selectedObj, vtSelPos, 1)

			vtxIndx2 = self.getVertexIndexBasedOnPosition(selectedObj, vtDesPos, 2)
			

			selectedVtx = selectedObj + ".vtx[" + str(vtxIndx1) + "]"
			desVtx = selectedObj + ".vtx[" + str(vtxIndx2) + "]"

			finalPos = vtDesPos.strip('][').split(', ')

			cmds.xform(selectedVtx, ws = True, t = [finalPos[0], finalPos[1], finalPos[2]])
