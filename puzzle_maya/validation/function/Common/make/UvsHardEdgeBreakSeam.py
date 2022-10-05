description = ""
toolTips = "Hard edge must cut uv seam"


import maya.api.OpenMaya as om2
import maya.mel as mel
import maya.cmds as cmds
import itertools


# def getHardEdges(obj):
#     cmds.select(obj)
#     cmds.ConvertSelectionToEdges()
#     # cmds.polySelectConstraint(mode=0, dist=0)#off mode
#     cmds.polySelectConstraint(mode=3, t=0x8000, smoothness=1)
#     cmds.polySelectConstraint(mode=0, dist=0)  # off mode
#     mel.eval("resetPolySelectConstraint;")
#     hardEdges = cmds.ls(selection=True, flatten=True)
#     cmds.SelectToggleMode()  # convert to objects select mode
#     cmds.SelectToggleMode()  # convert to objects select mode
#     cmds.select(clear=True)
#     return hardEdges


# def getUVBorderEdges(obj):
#     cmds.select(obj)
#     cmds.ConvertSelectionToEdges()
#     cmds.SelectUVShell()
#     meshEdges = cmds.ls(sl=True, fl=True)  # list edges
#     uvBorderEdges = []
#     for edge in meshEdges:  # Filter through the mesh(s) edges.
#         # print edge
#         edgeUvs = cmds.ls(
#             cmds.polyListComponentConversion(edge, tuv=True), fl=True)
#         edgeFaces = cmds.ls(
#             cmds.polyListComponentConversion(edge, tf=True), fl=True)
#         # If an edge has more than two uvs, it is a uv border edge.
#         if len(edgeUvs) > 2:
#             uvBorderEdges.append(edge)
#         # If an edge has less than 2 faces, it is a border edge.
#         elif len(edgeFaces) < 2:
#             uvBorderEdges.append(edge)
#     cmds.SelectToggleMode()  # convert to objects select mode
#     cmds.SelectToggleMode()  # convert to objects select mode
#     cmds.select(clear=True)
#     return uvBorderEdges

# def getVertUVInfo(vertIn):
#     uArr = OM.MFloatArray()
#     vArr = OM.MFloatArray()
#     fIDs = OM.MIntArray()
#     uvIndices = OM.MIntArray()
#     uvSet = 'map1'
#     vertIn.getUVs(uArr, vArr, fIDs, uvSet)
#     vertIn.getUVIndices(uvIndices, uvSet)

#     print uArr, vArr, fIDs, uvIndices
#     return fIDs, uvIndices

def getDagPath(obj):
    """get mDagPath from objects name"""
    sel = om2.MSelectionList()
    sel.add(obj)
    mDag = sel.getDagPath(0)
    return mDag
    
def getHardEdges(obj):
    """get Hard edges of mesh"""
    listHE = []
    mDag = getDagPath(obj)#get MDagPath
    itEdges = om2.MItMeshEdge(mDag)
    nameObj = mDag.fullPathName()
    
    itEdges = om2.MItMeshEdge(mDag)  # created iterator Edges
    while not itEdges.isDone():
        edgeSM = itEdges.isSmooth
        edgeIndex = itEdges.index()
        if not edgeSM:
            edgeName = "{}.e[{}]".format(nameObj,  edgeIndex)
            listHE.append(edgeName)
        itEdges.next()
    return listHE
    
    
def getUVborderVertices(obj):
    """get UV vertices border of mesh"""
    listUVBV = []
    mDag = getDagPath(obj)#get MDagPath
    nameObj = mDag.fullPathName()
    itVert = om2.MItMeshVertex(mDag)
    
    while not itVert.isDone():
        vertID = itVert.index()
        uvID = set(itVert.getUVIndices())
        #If length uvID == 1 is index interior
        # print uvID
        nameVert = "{}.vtx[{}]".format(nameObj, vertID)
        if len(uvID) != 1:
            listUVBV.append(nameVert)
        
        itVert.next()
    # cmds.select(listUVBV)
    return listUVBV
    
        
def getUVBorderEdges(obj):
    """get UV edges border of mesh"""
    listUVBE = []
    listUVBV = getUVborderVertices(obj)
    mDag = getDagPath(obj)#get MDagPath
    nameObj = mDag.fullPathName()
    itEdges = om2.MItMeshEdge(mDag)
    # print mFnMesh.numEdges
    
    while not itEdges.isDone():
        edgeIndex = itEdges.index()
        nameEdge = "{}.e[{}]".format(nameObj, edgeIndex)
        # toEdge = itEdges.connectedToEdge(edgeIndex)
        # toFace = itEdges.connectedToFace(edgeIndex)
        # print itEdges.getConnectedFaces()#check border edge
        edgeBorder = itEdges.onBoundary()#True =  border edge
        # print itVert.getUVs()
        # print itVert.index()
        
        # print itEdges.count()
        # print mFnMesh.getEdgeVertices(edgeIndex)#  Returns a tuple containing [0,0]
        toVertA = itEdges.vertexId(0)
        toVertB = itEdges.vertexId(1)
        nameVertA = "{}.vtx[{}]".format(nameObj, toVertA)
        nameVertB = "{}.vtx[{}]".format(nameObj, toVertB)
        toVertices = [nameVertA, nameVertB] 
        #edgeUvs = cmds.ls(cmds.polyListComponentConversion(nameEdge, tuv=True), fl=True)

        # print  mFnMesh.getPolygonVerticesl(0)
        # itMesh.getUVIndexAndValue(12)
        
        # edgeFaces = cmds.ls(cmds.polyListComponentConversion(nameEdge, tf=True), fl=True)
        
        # If an edge has more than two uvs, it is a uv border edge.
        # if len(edgeUvs) > 2:
        #     ListUVBE.append(nameEdge)
        # # If an edge has less than 2 faces, it is a border edge.
        # elif len(edgeFaces) < 2:
        #     ListUVBE.append(nameEdge)
        # if set(toVertices).issubset(listUVBV):
        #     listUVBE.append(nameEdge)
        if edgeBorder:
            listUVBE.append(nameEdge)
            
        elif set(toVertices).issubset(listUVBV):
            listUVBE.append(nameEdge)
        
        # elif toVertices in listUVBV:
        #     listUVBE.append(nameEdge)
        
        itEdges.next()
    # cmds.select(ListUVBE)
    return listUVBE
    


# obj = "pCube1"
#_______Function Required_______#
def getDAGNode():
    """get element check"""
    #get transform of shape
    allSceneMeshes = cmds.filterExpand(cmds.ls(l=False, typ='transform'), sm=12)
    return allSceneMeshes

def result():
    bad = []
    good = ["UVs shell interior not has hard edge"]
    # allSceneMeshes = [cmds.listRelatives(m, parent=True, fullPath = True)[0]
    #           for m in cmds.ls(type='mesh', long=False)]
    allSceneMeshes = getDAGNode()
    for obj in allSceneMeshes:
        # print obj
        hardEdges = getHardEdges(obj)  # List hardedge from
        uvBorderEdges = getUVBorderEdges(obj)
        edgeIssuse = list(set(hardEdges) - set(uvBorderEdges))
        if edgeIssuse:
            bad.extend(edgeIssuse)
    # cmds.select(bad)
    if bad:
        return "bad", bad
    else:
        return "good", good
        


def doubleclick():
    pass
