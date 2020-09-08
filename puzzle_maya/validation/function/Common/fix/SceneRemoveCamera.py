description = "Delete Camera User Define"
toolTips = ""

import maya.cmds as cmds


def run():
    camDefault = ["perspShape", "topShape", "frontShape", "sideShape"]
    camScene = cmds.ls(type="camera")
    for cam in camScene:
        if cam not in camDefault:
            print cam
            cmds.camera(cam, edit=True, startupCamera=False)
            camTranform = cmds.listRelatives(cam, allParents=True)
            try:
                cmds.delete(camTranform)
            except:
                cmds.warning("Camera not delete")