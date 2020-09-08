description = "Set Scene Unit"
toolTips = ""

import maya.cmds as cmds
import maya.mel as mel

def run():
    unit = cmds.currentUnit( query=True, linear = True, fullName=True)
    axis = cmds.upAxis( query=True,  axis = True )
    
    if unit != "cm":
        unit = cmds.currentUnit( linear = "cm")
    if axis != "y":
        cmds.upAxis(axis = "y",  rotateView = True)
        mel.eval('{ string $panel = `getPanel -withFocus`;viewSet -animate `optionVar -query animateRoll` -home `hotkeyCurrentCamera $panel`;}')
    
        
