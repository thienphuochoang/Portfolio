description = "Delete all Color Set for Mesh"
toolTips = ""

import maya.cmds as cmds
import maya.mel as mel


def run():
    meshs = cmds.ls(type = 'mesh', l = True)
    for obj in meshs:
        colorSets = cmds.polyColorSet(obj, query = True, acs = True) #  Get colorSet from Mesh
        if colorSets:
            for colSet in colorSets:
                print colSet
                try:
                    cmds.polyColorSet( obj, delete = True, colorSet = colSet )
                except:
                    pass


