import pymxs
rt = pymxs.runtime
import os
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
currentFilePath = "/".join(currentFilePath.split("/")[:-1])
msScriptFile = currentFilePath + "/function/vertex_normal_tools.ms"
def openNormalTool():
    rt.Filein(msScriptFile)

openNormalTool()