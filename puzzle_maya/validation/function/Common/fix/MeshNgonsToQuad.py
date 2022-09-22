description = "Delete Camera User Define"
toolTips = ""
import maya.mel as mel
import maya.cmds as cmds

def run():
    selection = cmds.ls(selection=True)
    for sel in selection:
        cmds.select(sel)
        mel.eval('ConvertSelectionToFaces; polySelectConstraint -m 2 -t 8 -sz 3; polyTriangulate -ch 1 ;  polyQuad  -a 30 -kgb 1 -ktb 1 -khe 1 -ws 1 -ch 0; polySelectConstraint -m 0; resetPolySelectConstraint;')
    cmds.select(selection)