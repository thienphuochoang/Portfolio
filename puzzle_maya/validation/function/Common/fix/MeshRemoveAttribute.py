description = "Check Attribute Mesh, Transform, Materials, Files"
toolTips = ""

import os
import maya.cmds as cmds
import maya.mel as mel


def run():

    meshs = cmds.ls(type = 'mesh', l = True)
    transfroms =  cmds.ls(type = 'transform', l = True)
    # materials =  cmds.ls(mat = True)
    files = cmds.ls(type = 'file')
    
    
   
    for obj in meshs:
        print obj
        attrUser = cmds.listAttr(obj, userDefined=True)  # Get attribulate User Defined
        if attrUser:
            for att in attrUser:
                try:
                    cmds.deleteAttr( obj, attribute = att )
                except:
                    cmds.warning("Attribulte Not delete: " + att)
                
    for obj in transfroms:
        print obj
        attrUser = cmds.listAttr(obj, userDefined=True)  # Get attribulate User Defined
        if attrUser:
            for att in attrUser:
                try:
                    cmds.deleteAttr( obj, attribute = att )
                except:
                    cmds.warning("Attribulte Not delete: " + att)
    
    # for obj in materials:
    #     print obj
    #     attrUser = cmds.listAttr(obj, userDefined=True)  # Get attribulate User Defined
    #     if attrUser:
    #         for att in attrUser:
    #             try:
    #                 cmds.deleteAttr( obj, attribute = att )
    #             except:
    #                 cmds.warning("Attribulte Not delete: " + att)
                
    for obj in files:
        print obj
        attrUser = cmds.listAttr(obj, userDefined=True)  # Get attribulate User Defined
        if attrUser:
            for att in attrUser:
                try:
                    cmds.deleteAttr( obj, attribute = att )
                except:
                    cmds.warning("Attribulte Not delete: " + att)
    