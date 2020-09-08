functionDescription = "Texture Path"
toolTip = ""

import maya.cmds as cmds
import maya.mel as mel


def getPattern():
    """
         [in] 
        [out] str 
        [des] get name Folder Asset from file opening
    """
    fileOpen = cmds.file(query=True, list=True)[0]
    folderAsset = os.path.dirname(fileOpen)
    pattern = os.path.basename(folderAsset)
    return fileOpen, folderAsset, pattern


#_______Function Required_______#
def get_abc():
    bad = []
    good = ["Path Texutres Correct"]

    nameAsset = getPattern()[2]
    pathPattern = "{}/textures".format(getPattern()[1])

    nodeFiles = [f for f in cmds.ls(type="file") if f.startswith(nameAsset)]
    if nodeFiles:
        for nf in nodeFiles:
            print nf
            pathTex = cmds.getAttr(nf + ".fileTextureName")
            if not pathTex.startswith(pathPattern):
                bad.append(pathTex)
    if bad:
        return "bad", bad
    else:
        return "good", good


def result():
    """function required"""
    result_error_list = []
    result_non_error_list =[]
    error_dict = {}
    non_error_dict = {}

    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "----is missed textures file. :("
            
    else:
        non_error_dict = {"Scene " : "----is not missed textures file. :)"}   
    return error_dict, non_error_dict