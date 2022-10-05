import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om2


class UVClass:
    def __init__(self, uvs = "selection"):
        #Set self.uvs from a list of uvs or automatically
        if uvs == "selection": #No list was sent
            self.uvs = cmds.ls(cmds.polyListComponentConversion(tuv=True),fl=True)
        else: self.uvs = uvs

        self.type = "standard"
        self.shells = []
        self.borderEdges = []

    def setMinMax(self):
        xPositions = sorted([cmds.polyEditUV(i, query=True)[0] for i in self.uvs])
        yPositions = sorted([cmds.polyEditUV(i, query=True)[1] for i in self.uvs])

        self.minMax = (xPositions[0],xPositions[-1]),(yPositions[0],yPositions[-1])
        self.xMin = self.minMax[0][0]
        self.xMax = self.minMax[0][1]
        self.yMin = self.minMax[1][0]
        self.yMax = self.minMax[1][1]

    def getPivot(self):
        pivot = cmds.polyEvaluate(self.uvs,bc2=True)
        pivU = ((pivot[0][0] + pivot[0][1]) * 0.5)
        pivV = ((pivot[1][0] + pivot[1][1]) * 0.5)
        return pivU,pivV

    def getShells(self):
        """ This creates a list object (shells) within the class containing a UVClass per shell found"""
        if len(self.shells): #No need to do this twice
            if self.type == "shell":
                print "Class is already of shell type. This function call is redundant"
            return

        currentSelection = cmds.ls(sl = True)
        self.shells = []
        for uv in self.uvs:
            found = False
            for shell in self.shells:
                if uv in shell.uvs:
                    found = True
            if not found:
                cmds.select(uv)
                mel.eval('polySelectBorderShell 0;')
                thisShell = UVClass()
                thisShell.type = "shell"
                thisShell.setMinMax()

                self.shells.append(thisShell)
        cmds.select(currentSelection)

def gatherShells(*args):
    selected = UVClass()
    selected.getShells()

    for shell in selected.shells:
        x_center = (shell.xMin + shell.xMax)/2.0
        y_center = (shell.yMin + shell.yMax)/2.0
        if x_center > 1:
            cmds.polyEditUV(shell.uvs, u= -int(x_center),v=0)
        if x_center < 0:
            cmds.polyEditUV(shell.uvs, u= -int(x_center) + 1,v=0)
        if y_center > 1:
            cmds.polyEditUV(shell.uvs, u= 0, v= -int(y_center))
        if y_center < 0:
            cmds.polyEditUV(shell.uvs, u= 0, v= -int(y_center) + 1)
    return
    
def do():
    cmds.undoInfo(openChunk=True)
    gatherShells()
    cmds.undoInfo(closeChunk=True)
