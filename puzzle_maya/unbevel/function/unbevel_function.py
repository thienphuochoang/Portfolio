import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
import pymel.core.datatypes as dt
import math
import itertools  

Unit_UIWidth = 200
windowID = "TestUnBevel"


class UnbevelFunction():
	def lineIntersect(self, A, B, C, D):
		'''
		Description:
			Find an intersect point between two line (AB, CD)
			
		Args:
			 A, B ,C ,D: (Vector3) present for point in R3 space
			 
		Returns:
			Intersect point: (Vector3) if two lines are crossed to each other.
			0: if two line aren't crossed.
			
		'''
		a = B - A
		b = D - C
		c = C - A
		cross1 = a.cross(b)
		cross2 = c.cross(b)
		if cross1.length() > 0.001 and abs(cross1.dot(c)) < 0.0001:
			intersectPoint = A + a* cross2.dot(cross1)/math.pow(cross1.length(),2)
			return intersectPoint
		else:
			return 0



	def linePlaneIntersection(self, C, NormalFace, A, B):
		'''
		Description:
			Find an intersect point between line (AB) and a Plane (C, NormalFace)
			
		Args:
			 A, B ,C: (Vector3) present for point in R3 space
			 NormalFace: (Vector3) present for Vector in R3 space
			 
		Returns:
			Intersect point: (Vector3) if line and Plane are Intersect at one point.
			0: if line does not intersect Plane or line lies in the plane
			
		'''
		u = A- B
		w = B - C
		
		D = NormalFace.dot(u)
		N = -NormalFace.dot(w)
		if D != 0:  
			sI = N/D
			intersectPoint = B + sI*u
			#I =dt.Point(I)
			return intersectPoint
		else:
			return 0



	def lineIntersectForBevelEdges(self, A, B, C, D):
		'''

		Description:
			Find an intersect point between two line (AB, CD)
			
		Args:
			 A, B ,C ,D: (Vector3) present for point in R3 space
			 
		Returns:
			Intersect point: (Vector3) if two lines are not parallel

		'''
		a = B - A
		b = D - C
		c = C - A
		cross1 = a.cross(b)
		cross2 = c.cross(b)
		intersectPoint = A + a* cross2.dot(cross1)/math.pow(cross1.length(),2)
		return intersectPoint

	def twoEdgesIntersect(self, edgesSel):
		'''
		edgesSel is list of 2 edges Selected
		'''
		# get two point on the first edges
		vertSet = cmds.polyListComponentConversion(edgesSel[0], tv = True)
		vertSet = cmds.ls(vertSet, fl = True)
		pointA = pm.pointPosition(vertSet[0])
		pointB = pm.pointPosition(vertSet[1])
		# get two point on the second edges
		vertSet1 = cmds.polyListComponentConversion(edgesSel[1], tv = True)
		vertSet1 = cmds.ls(vertSet1, fl = True)
		pointC = pm.pointPosition(vertSet1[0])
		pointD = pm.pointPosition(vertSet1[1])
		# get the intersect Point base on 4 point
		intersectPoint = self.lineIntersect(pointA, pointB, pointC, pointD)
		#cmds.curve( p=[pointA,intersectPoint] )
		return intersectPoint




	def queryFaceNormal(self, FaceSel):   
		normalInfo= cmds.polyInfo(FaceSel, fn=True)
		normalInfo = normalInfo[0].replace("\n","").split(" ")
		FaceNormal = [float(normalInfo[-3]), float(normalInfo[-2]), float(normalInfo[-1])]
		return FaceNormal


	def getConnectedEdges(self):
		#if not cmds.selectType(q = True, e = True):   
		selectedEdges = cmds.ls(sl = True, fl = True)
		unconnectedSelectedEdges = list()
		#currentEdge = selectedEdges[0]
		while len(selectedEdges) > 0:
			unconnectedSelectedEdges.append(list())
			unconnectedSelectedEdges[len(unconnectedSelectedEdges) - 1].append(selectedEdges[0])
			selectedEdges.remove(selectedEdges[0])
			i = 0
			while i < len(unconnectedSelectedEdges[len(unconnectedSelectedEdges) - 1]):
				i += 1
				verts = cmds.polyListComponentConversion(unconnectedSelectedEdges[len(unconnectedSelectedEdges) - 1], tv = True)
				neigborEdges = cmds.polyListComponentConversion(verts, te = True)
				#cmds.select(neigborEdges)
				neigborEdges = cmds.ls(neigborEdges, fl = True)
				for e in neigborEdges:
					if e in selectedEdges:
						selectedEdges.remove(e)
						unconnectedSelectedEdges[len(unconnectedSelectedEdges) - 1].append(e)
		return unconnectedSelectedEdges 



	def getConnectedEdgesV2(self):
		'''
			Get edges set
		'''
		edgeSets = self.getConnectedEdges()
		outlist = list()
		for setEdgesConnected in edgeSets:
			cmds.select(setEdgesConnected)
			mel.eval('PolySelectTraverse 5;')
			edges = cmds.ls(sl = True, fl = True)
			outlist.append(edges)
		return outlist

	def getEdgeConnectToHardEdges(self, currentEdgeSel, *arg):
		#currentEdgeSel = cmds.ls(sl = True, fl = True)
		vertSel = cmds.ls(cmds.polyListComponentConversion(currentEdgeSel, tv = True), fl=True)
		vertToEdges = cmds.ls(cmds.polyListComponentConversion(vertSel, te = True), fl=True)
		faceSel = cmds.ls(cmds.polyListComponentConversion(currentEdgeSel, tf = True), fl=True)
		faceToEdges = cmds.ls(cmds.polyListComponentConversion(faceSel, te = True), fl=True)
		listHardEdges = [i for i in faceToEdges if i in vertToEdges and i not in currentEdgeSel]
		cmds.select(listHardEdges)
		#cmds.polySoftEdge( a=0 )
		#print listHardEdges
		return listHardEdges


	def smartCollapsing(self, *arg):          
		print ('--execute ---')
		currentEdgeSel = cmds.ls(sl = True, fl = True)
		#Check Selection is edge
		currentEdgeSel =  cmds.filterExpand(sm=32)
		if currentEdgeSel:
			currentVertSel = cmds.ls(cmds.polyListComponentConversion(currentEdgeSel, tv = True), fl=True)
			edgeSets = self.getConnectedEdgesV2()
			vertMerge=[]
			listHardEdges =[]
			for setEdgesConnected in edgeSets:
				#try:
					verts = list()
					endVerts = list()
					midleVerts = list()
					intersectPoint = 0
					for e in setEdgesConnected:
						for vertStr in cmds.polyListComponentConversion(e, tv = True):
							cmds.select(vertStr)
							for v in cmds.ls(sl = True, fl = True):
								verts.append(v)
								# filter verts to separate endverts and midle
					
					for v in verts:
						if verts.count(v) > 1:
							midleVerts.append(v)
						else:
							endVerts.append(v)
					# get end edges
					edges = cmds.polyListComponentConversion(endVerts, te = True)
					execEdges = list()
					cmds.select(edges)
					for e in cmds.ls(sl = True, fl = True):
						if e in setEdgesConnected:
							execEdges.append(e)
					cmds.select(execEdges)
					
					edgesExpand = [e for e in execEdges if e not in currentEdgeSel]
					edgeOld = [e for e in execEdges if e in currentEdgeSel] 
					#print  edgesExpand
					#twoEdges
					if len(edgesExpand) == 2:
						#print 'th1'
						'''
						there are only two edges at the end
						'''
						# get two point on the first edges
						vertSet = cmds.polyListComponentConversion(execEdges[0], tv = True)
						#cmds.select(vertSet)
						vertSet = cmds.ls(vertSet, fl = True)
						pointA = pm.pointPosition(vertSet[0])
						pointB = pm.pointPosition(vertSet[1])
						# get two point on the second edges
						vertSet = cmds.polyListComponentConversion(execEdges[1], tv = True)
						#cmds.select(vertSet)
						vertSet = cmds.ls(vertSet, fl = True)
						pointC = pm.pointPosition(vertSet[0])
						pointD = pm.pointPosition(vertSet[1])
						# get the intersect Point base on 4 point
						intersectPoint = self.lineIntersectForBevelEdges(pointA, pointB, pointC, pointD)
						if intersectPoint == 0:            
							vertexOfEdgesExpand0 = cmds.polyListComponentConversion(edgesExpand[0], tv = True)
							#print edgesExpand[0]
							allEdgesConectedEdgesExpand0 = cmds.ls(cmds.polyListComponentConversion(vertexOfEdgesExpand0, te = True), fl = True)
							edgeOld = [i for i in currentEdgeSel if i in allEdgesConectedEdgesExpand0 ]
							execEdges = [edgeOld[0], edgesExpand[1]]      
							edgesExpand.remove(edgesExpand[0])
						else:
							setEdgeOld = [e for e in setEdgesConnected if e in currentEdgeSel]
							listHardEdges += self.getEdgeConnectToHardEdges(setEdgeOld)
							
							for v in midleVerts:
								pm.move(v, intersectPoint)
								if v not in vertMerge:
									vertMerge.append(v)

					if len(edgesExpand) == 1:
						#print 'th2'                  
						'''
						 In execEdges have one edgeOld of currentEdgeSel
						'''
						# Use edgeOld and vertexOld to find Face to Intersect
						vertexOld = cmds.ls(cmds.polyListComponentConversion(edgeOld, tv = True), fl=True)
						vertexOfFace = [v for v in vertexOld if v not in midleVerts]
						listFace_1 = cmds.ls(cmds.polyListComponentConversion(vertexOfFace, fv =True, tf = True), fl=True)
						listFace_2 = cmds.ls(cmds.polyListComponentConversion(edgeOld, fe =True, tf = True), fl=True)
						faceToIntersect = [f for f in listFace_1 if f not in listFace_2]    
						NormalFaceIntersect =[]
						allIntersectPoint = []
						#Find Normal of face To Intersect
						if faceToIntersect:
							trianCmd=cmds.polyTriangulate(faceToIntersect)
							trianFace =cmds.ls(sl=True, fl=True)
							for face in trianFace:
								listVert = cmds.ls(cmds.polyListComponentConversion( face, ff=True, tv=True), fl = True)
								if vertexOfFace[0] in listVert:
									NormalFaceIntersect.append(self.queryFaceNormal(face))
							cmds.delete(trianCmd)                
							#print NormalFaceIntersect
							for i in range(0, len(NormalFaceIntersect)):
								# get two point of edgeToIntersect
								edgeToIntersect = [e for e in execEdges if e not in edgeOld]
								vertSet = cmds.polyListComponentConversion(edgeToIntersect[0], tv = True)
								cmds.select(vertSet)
								vertSet = cmds.ls(sl = True, fl = True)
								pointA = pm.pointPosition(vertSet[0])
								pointB = pm.pointPosition(vertSet[1])
								# Get Point and Normal of FaceIntersect
								pointC = pm.pointPosition(vertexOfFace[0])
								NormalFace = dt.Point( NormalFaceIntersect[i])
								intersectPoint = self.linePlaneIntersection(pointC, NormalFace, pointA, pointB)
								allIntersectPoint.append(intersectPoint)
			
							if allIntersectPoint:
								listLengthToEndVertsAndMidVerts = [(i - pm.pointPosition(endVerts[0])).length() + (i - pm.pointPosition(endVerts[1])).length() for i in allIntersectPoint]
								minLength = min(listLengthToEndVertsAndMidVerts)
								threshold = 7*(pm.pointPosition(endVerts[1]) - pm.pointPosition(endVerts[0])).length()
								print (minLength, threshold)
								if minLength < threshold:
									indexIPoint = listLengthToEndVertsAndMidVerts.index(minLength)
									intersectPoint = allIntersectPoint[indexIPoint]                
								else:
									intersectPoint = 0
			
							if intersectPoint:
								setEdgeOld = [e for e in setEdgesConnected if e in currentEdgeSel]
								listHardEdges += self.getEdgeConnectToHardEdges(setEdgeOld)
								midleVerts.append(vertexOfFace[0])
								for v in midleVerts:
									pm.move(v, intersectPoint)
									if v not in vertMerge:
										vertMerge.append(v)

					if len(edgesExpand) == 0:
					   # print 'th3'
						vertexSel = cmds.polyListComponentConversion(setEdgesConnected, tv = True)
						allEdgesConected = cmds.ls(cmds.polyListComponentConversion(vertexSel, te = True), fl = True)
						edgesToIntersect = [e for e in allEdgesConected if e not in setEdgesConnected]
						cmds.select(edgesToIntersect)
						edgesToIntersect1 = [i for i in edgesToIntersect if endVerts[0] in cmds.ls(cmds.polyListComponentConversion(i, tv = True), fl = True) and endVerts[1] not in cmds.ls(cmds.polyListComponentConversion(i, tv = True), fl = True)]
						edgesToIntersect2 = [i for i in edgesToIntersect if endVerts[1] in cmds.ls(cmds.polyListComponentConversion(i, tv = True), fl = True) and endVerts[0] not in cmds.ls(cmds.polyListComponentConversion(i, tv = True), fl = True)] 
						#cmds.select(edgesToIntersect1)
						#cmds.select(edgesToIntersect2)
						allPairEdges = list(itertools.product(edgesToIntersect1, edgesToIntersect2))
						allIntersectPoint = [self.twoEdgesIntersect(i) for i in allPairEdges if self.twoEdgesIntersect(i) != 0]

						if allIntersectPoint:
							listLengthToEndVertsAndMidVerts = [(i - pm.pointPosition(endVerts[0])).length() + (i - pm.pointPosition(endVerts[1])).length() for i in allIntersectPoint]
							minLength = min(listLengthToEndVertsAndMidVerts)
							threshold = 7*(pm.pointPosition(endVerts[1]) - pm.pointPosition(endVerts[0])).length()
							#print minLength, threshold
							if minLength < threshold:
								indexIPoint = listLengthToEndVertsAndMidVerts.index(minLength)
								intersectPoint = allIntersectPoint[indexIPoint]                
							else:
								intersectPoint = 0
						if intersectPoint:
							setEdgeOld = [e for e in setEdgesConnected if e in currentEdgeSel]
							listHardEdges += self.getEdgeConnectToHardEdges(setEdgeOld)
							allVert = midleVerts + endVerts
							for v in allVert:
								pm.move(v, intersectPoint)                
								if v not in vertMerge:
									vertMerge.append(v)
			
			if listHardEdges:
				cmds.select(listHardEdges)
				cmds.polySoftEdge( a=0 )
			if vertMerge:
				cmds.select(vertMerge) 
				cmds.polyMergeVertex(vertMerge, d = 0.001)  
				#print vertMerge
		else:
			cmds.confirmDialog(title='Confirm', m="Plaease Select Edge ring to unbevel")