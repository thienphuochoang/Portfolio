description = "Remove Keyframe in Sence"
toolTips = ""


import maya.cmds as cmds

def run():

    scenes = cmds.ls()

    keyframes = []
    try:
        keyframes += cmds.listConnections(scenes,s=True, type="animCurveTU")
    except:
        pass
    try:
        keyframes += cmds.listConnections(scenes,s=True, type="animCurveTL")
    except:
        pass
    try:
        keyframes += cmds.listConnections(scenes,s=True, type="animCurveTA")
    except:
        pass

    cmds.delete(keyframes)
    # print keyframes
