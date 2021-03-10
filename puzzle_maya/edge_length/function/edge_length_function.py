import maya.mel as mel
import maya.cmds as cmds
import math
import pymel.core.datatypes as dt
import maya.OpenMaya as om

class EdgeLengthFunction():
	def __init__(self):
		pass
		
	def getLength(self, edge):
		cmds.polyListComponentConversion(edge, tv = True)
		p = cmds.xform(edge, q = True, t = True, ws = True)
		length = math.sqrt(math.pow(p[0]-p[3],2) + math.pow(p[1]-p[4],2) + math.pow(p[2]-p[5],2))
		return float('%.3f' % length)

	def setEdgeLength(self, desLeg, direction):
		selEdge = cmds.ls(sl = True, fl = True)
		if direction == "left": 
			for i in range(0, len(selEdge),1):
				curLeg = self.getLength(selEdge[i])
				#toVert = cmds.polyListComponentConversion(selEdge[i], tv = True)
				cmds.select(selEdge[i])
				mel.eval("PolySelectConvert 3;")
				toVert = cmds.ls(sl = True, fl = True)
				vertPos1 = cmds.xform(toVert[0], q = True, ws = True, t = True)
				vertPos2 = cmds.xform(toVert[1], q = True, ws = True, t = True)

				vectorV1 = dt.Vector(vertPos1)
				vectorV2 = dt.Vector(vertPos2)
				
				direction = vectorV1 - vectorV2
				des = (direction/dt.length(direction))*(desLeg-curLeg)
				cmds.polyMoveVertex( toVert[0], t = des, ch = False)
				
		elif direction == "right":
			for i in range(0, len(selEdge),1):
				curLeg = self.getLength(selEdge[i])
				#toVert = cmds.polyListComponentConversion(selEdge[i], tv = True)
				cmds.select(selEdge[i])
				mel.eval("PolySelectConvert 3;")
				toVert = cmds.ls(sl = True, fl = True)
				vertPos1 = cmds.xform(toVert[0], q = True, ws = True, t = True)
				vertPos2 = cmds.xform(toVert[1], q = True, ws = True, t = True)

				vectorV1 = dt.Vector(vertPos1)
				vectorV2 = dt.Vector(vertPos2)
				
				direction = vectorV2 - vectorV1
				des = (direction/dt.length(direction))*(desLeg-curLeg)
				cmds.polyMoveVertex( toVert[1], t = des, ch = False)
				
		else:
			for i in range(0, len(selEdge),1):
				curLeg = self.getLength(selEdge[i])
				#toVert1 = cmds.polyListComponentConversion(selEdge[i], tv = True, internal = True)
				cmds.select(selEdge[i])
				mel.eval("PolySelectConvert 3;")
				toVert = cmds.ls(sl = True, fl = True)
				vertPos1 = cmds.xform(toVert[0], q = True, ws = True, t = True)
				vertPos2 = cmds.xform(toVert[1], q = True, ws = True, t = True)

				vectorV1 = dt.Vector(vertPos1)
				vectorV2 = dt.Vector(vertPos2)
				
				direction1 = vectorV1 - vectorV2
				direction2 = vectorV2 - vectorV1 
				
				des1 = ((direction1/dt.length(direction1))*(desLeg-curLeg))/2
				des2 = ((direction2/dt.length(direction2))*(desLeg-curLeg))/2
				
				cmds.polyMoveVertex( toVert[0], t = des1, ch = False)
				cmds.polyMoveVertex( toVert[1], t = des2, ch = False)
		mel.eval("DeleteAllHistory;")       
		mel.eval("PolySelectConvert 2;")        
		cmds.select(selEdge)

	def selEdge(self, value):
		sel = cmds.ls(sl = True, o = True)
		
		if len(sel) != 0:
			listToCheck = []
			results = []
			for s in sel:
				if cmds.objectType(s) == "mesh":
					listToCheck.append(cmds.listRelatives(s, p = True)[0])
				else:
					listToCheck.append(s)
					
			
			for obj in listToCheck:
				edgeCount = cmds.polyEvaluate(obj, e = True)
				cmds.select(obj + '.e[0:'+str(edgeCount)+']')
				edgeSel = cmds.ls(sl = True, fl = True)
				#edgeSel.remove(edgeSel[0])
				for edge in edgeSel:
					if self.getLength(edge) < value:
						results.append(edge)
			cmds.select(cl = True)
			for i in range(0, len(results),1):
				cmds.select(results[i], add = True)
		else:
			om.MGlobal.displayError("Select obj!")
		
	def lengthToField(self):
		sel = cmds.ls(sl = True, fl = True)
		if not sel or len(sel) > 1:
			om.MGlobal.displayError("Select one edge!")
			return None
		else:
			leg = self.getLength(sel[0])
			return leg
		
		
	def setLength(self, value, direction):
		
		if direction == "left":
			self.setEdgeLength(value, direction = "left")
		elif direction == "center":
			self.setEdgeLength(value, direction = "center")
		else:
			self.setEdgeLength(value, direction = "right")