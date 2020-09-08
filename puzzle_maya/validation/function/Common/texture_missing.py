functionDescription = " Texture File Missing "
toolTips = ""
import os
import maya.api.OpenMaya as om2
import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check



def get_textures_missing():
    bad_list = []
    file_textures = [f for f in cmds.ls(type='file')]

    if file_textures == []:
        return bad_list

    for f in file_textures:
        missing_file = cmds.getAttr(f + '.fileTextureName')
        if not os.path.exists(missing_file):
            bad_list.append(f)
    return bad_list



def result():
    """function required"""
    result_error_list = get_textures_missing()
    result_non_error_list =[]
    error_dict = {}
    non_error_dict = {}

    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "----is missed textures file. :("
            
    else:
        non_error_dict = {"Scene " : "----Correct. :)"}   
    return error_dict, non_error_dict


        









        
