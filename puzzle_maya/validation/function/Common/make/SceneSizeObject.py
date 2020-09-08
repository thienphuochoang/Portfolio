description = "Check Size Mesh in Scene"
toolTips = ""

import maya.cmds as cmds
import maya.mel as mel



#_______Function Required_______#  
def result():
    bad = []

    cmds.SelectAll()
    allObj = cmds.ls(sl=True)
    if allObj:
        bboxAll = cmds.exactWorldBoundingBox(allObj)
        
        bboxX = bboxAll[3] - bboxAll[0]
        bboxY = bboxAll[4] - bboxAll[1]
        bboxZ = bboxAll[5] - bboxAll[2]
        
        if bboxX > 10 or bboxY > 10 or bboxZ > 10:
            bad.append("Size Mesh Wrong: ")
            bad.append("X: " + str(bboxX))
            bad.append("Y: " + str(bboxY))
            bad.append("Z: " + str(bboxZ))

        cmds.select(clear = True)

    if bad:
        return "bad", " \n ".join(bad)
    else:
        return "good", ["Size Mesh Correct"]


def doubleclick():
    pass
        
    
        
        




