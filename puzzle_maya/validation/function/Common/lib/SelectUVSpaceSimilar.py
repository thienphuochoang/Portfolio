import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om2


def collectUVShellDots(lst):
    """only take own dot of each UV shell"""
    cmds.select(lst)
    mel.eval('PolySelectConvert 4;')#convert selection to uv's
    mel.eval('polySelectBorderShell 1;')#convert selected to border uv
    uvs = cmds.ls(selection=True, flatten=True, long=True)#base uv's
    uvShellDots = []
    while len(uvs) > 0:
        cmds.select(uvs[0])
        dot = cmds.ls(selection=True, long=True)
        uvShellDots.insert(0, dot[0])
        mel.eval("polySelectBorderShell 1;")
        shell = cmds.ls(selection=True, flatten=True, long=True)
        uvs = list(set(uvs) - set(shell))
    cmds.select(clear=True)
    return uvShellDots
    
    
# def selToUVSpace(u, v):
#     listSelSpace = []
#     selected = cmds.ls(sl=True)
#     mel.eval('PolySelectConvert 4;')#convert selection to uv's
#     selected = cmds.ls(sl=True)
#     shellDots = collectUVShellDots(selected)
#     for dot in shellDots:
#         # print dot
#         spaceDot = cmds.polyEditUVShell(dot, q=True, vValue=True, relative=False)
#         spaceU = str(spaceDot[0]).split(".")[0]
#         spaceV = str(spaceDot[1]).split(".")[0]
#         # print spaceU, spaceV
#         if u == spaceU and v == spaceV:
#             listSelSpace.append(dot)
#     cmds.select(listSelSpace)
#     mel.eval("ConvertSelectionToUVShell;")
    
    
def do():
    listSelSpace = []
    mel.eval('PolySelectConvert 4;')#convert selection to uv's
    space = cmds.ls(sl=True, flatten=True)[0]
    spacePattern = cmds.polyEditUVShell(space, q=True, vValue=True, relative=False)
    spacePatternU = str(spacePattern[0]).split(".")[0]
    spacePatternV = str(spacePattern[1]).split(".")[0]
    
    mel.eval('SelectAll')#selected all uvs map
    selected = cmds.ls(sl=True)
    shellDots = collectUVShellDots(selected)
    for dot in shellDots:
        # print dot
        spaceDot = cmds.polyEditUVShell(dot, q=True, vValue=True, relative=False)
        spaceU = str(spaceDot[0]).split(".")[0]
        spaceV = str(spaceDot[1]).split(".")[0]
        # print spaceU, spaceV
        if spacePatternU == spaceU and spacePatternV == spaceV:
            listSelSpace.append(dot)
    cmds.select(listSelSpace)
    mel.eval("ConvertSelectionToUVShell;")

