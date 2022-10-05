import os
import maya.api.OpenMaya as om2
import maya.cmds as cmds
import maya.mel as mel
from pprint import pprint
from collections import defaultdict
import itertools
description = "Check Mesh has vertex not weld.Error if two vertices the same position "
toolTips = ""

def getDagPath(obj):
    """get mDagPath from objects name"""
    sel = om2.MSelectionList()
    sel.add(obj)
    mDag = sel.getDagPath(0)
    return mDag
    

#_______Function Required_______#
def getDAGNode():
    """get element check"""
    #get transform of shape
    # allSceneMeshes = cmds.filterExpand(cmds.ls(l=False, typ='transform'), sm=12)
    allSceneMeshes = [cmds.listRelatives(m, parent=True, f=True)[0] for m in cmds.ls(type='mesh', long=False)]
    return allSceneMeshes
    
def getValueDictSimilar(d):
    """get value dict with value the same"""
    dd = defaultdict(list)
    #invert value to key and opposite
    for key, value in d.items():
        dd[tuple(value)].append(key)
    return dd
    
    
def getVertNotWeld(obj):
    """get vertices not weld on only mesh """
    posVert = {}
    mDag = getDagPath(obj)
    itVert = om2.MItMeshVertex(mDag)
    # itMesh = om2.MItMeshPolygon(mDag)
    while not itVert.isDone():
        vertID = itVert.index()
        position = itVert.position(space=4)
        keyPos = [round(position[0], 4), round(position[1], 4), round(position[2], 4)]
        posVert["{}.vtx[{}]".format(obj, vertID)] = keyPos
        itVert.next()
    
    newposVert = getValueDictSimilar(posVert)
    posVertIssuse = [v for v in newposVert.values() if len(v) > 1]

    return posVertIssuse


def result():
    bad = []
    good = ["Vertices Welded:"]

    allSceneMeshes = getDAGNode()
    for mesh in allSceneMeshes:
        # print mesh
        merged = list(itertools.chain.from_iterable(getVertNotWeld(mesh)))
        bad.extend(merged)
        
    if bad:
        # bad.insert(0, "Vertices not Weld:")
        return "bad", bad
    else:
        return "good", good


def doubleclick():
    pass