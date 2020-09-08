description = "Remove Layer not Default"
toolTips = ""

import maya.cmds as cmds

def run():
    layerDefault = ["defaultLayer", "renderLayerManager", "defaultRenderLayer", "displayLayerManager", "layerManager"]
    
    
    layerdisplay = [l for l in cmds.ls(type = "displayLayer") if l not in layerDefault]
    layerdisplayManager = [l for l in cmds.ls(type = "displayLayerManager") if l not in layerDefault]
    
    layerRender = [l for l in cmds.ls(type = "renderLayer") if l not in layerDefault]
    layerRenderManager = [lm for lm in cmds.ls(type = "renderLayerManager") if lm not in layerDefault]
    
    layeranim = [l for l in cmds.ls(type = "animLayer") if l not in layerDefault]
    
    if layerdisplay + layerdisplayManager + layerRender + layerRenderManager + layeranim:
        cmds.delete(layerdisplay + layerdisplayManager + layerRender + layerRenderManager + layeranim)
