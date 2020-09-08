import maya.cmds as cmds
import maya.mel as mel
description = "Check Lamina Faces"
toolTips = ""


#_______Function Required_______#  
def result():
    bad = []
    good = ["Scene not Edge Nonmanifold"]
 
    meshs = cmds.ls(type =  "mesh", long = True)
    meshCheck = [ m for m in meshs if m.startswith("|LODS") or m.startswith("|BLOCKOUT")]
    cmds.select(meshCheck)
    
    # meshs = cmds.ls(type = "mesh")
    # bad =  cmds.polyInfo(meshs, nonManifoldUVs = True)
    bad = mel.eval('polyCleanupArgList 4 { "0","2","1","0","0","1","0","0","0","1e-005","0","1e-005","0","1e-005","0","-1","0","0" };')
    # cmds.hilite(replace=True)
    # cmds.select(clear=True)

    if bad:
        return "bad", bad
    else:
        return "good", good

def doubleclick():
    pass
