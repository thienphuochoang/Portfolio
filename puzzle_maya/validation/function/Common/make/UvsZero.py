description = "Check UnmappedFaces and AreUVZero"
toolTips = ""

import maya.api.OpenMaya as om2
import maya.cmds as cmds
import maya.mel as mel


#_______Function Required_______#      
def result():
    bad = []
    good = ["No Unmapped Faces!"]
    
    allNodeMesh = om2.MItDependencyNodes(om2.MFn.kMesh) # query all node Mesh
    while not allNodeMesh.isDone():
        mObject = allNodeMesh.thisNode() # points MObject
        # mFnMesh = om2.MFnMesh(mObject) # assigned MObject into MFnMesh
        mFnDagNode = om2.MFnDagNode(mObject)
        nameMesh = mFnDagNode.fullPathName().split("|")[-1]
        iterFaces = om2.MItMeshPolygon(mObject)

        while not iterFaces.isDone():
            area = iterFaces.getUVArea("map1")
            # print area
            # if iterFaces.zeroUVArea("map1") :
            # if not iterFaces.hasUVs("map1") :
            # if not iterFaces.hasUVs("map1") :
            if area < 2.98023223877e-08:
                facesError = "{}.f[{}]".format(nameMesh, iterFaces.index())
                bad.append(facesError)
            iterFaces.next(None)
        allNodeMesh.next()
    
    if bad:
        return "bad", bad
    else:
        return "good", good

def doubleclick():
    pass
