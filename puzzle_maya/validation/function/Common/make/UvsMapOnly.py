import os
import maya.cmds as cmds
import maya.mel as mel
description = "Check Uvs map1"
toolTips = ""



#_______Function Required_______#  
def result():
    bad = []
    good = ["Uvs map1 Correct"]


    # meshs = [cmds.listRelatives(m, p = True, f = True)[0] for m in cmds.ls(type = 'mesh', l = True)]
    # cmds.select("|LODS", "|BLOCKOUT")
    meshs = [cmds.listRelatives(m, p = True, f = True)[0] for m in cmds.ls(type = 'mesh', l = True)]
    # lodsSel = [lod for lod in meshs if "|LODS" or "|BLOCKOUT" in lod]
    for obj in meshs:
        # print obj
        maps = cmds.polyUVSet(obj, q = True, auv = True)
        if maps:
            if maps[0] != 'map1' or len(maps) > 1:
                bad.append(obj)
        else:
            bad.append(obj)

    if bad:
        return "bad", bad
    else:
        return "good", good

def doubleclick():
    pass
