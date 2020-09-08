functionDescription = " Scene File Extension Maya "
toolTips = ""
import os
import maya.mel as mel
import maya.cmds as cmds
import maya.api.OpenMaya as om2


def get_type_file_extension(type_file = ".ma"):
    bad_list = []
    # return the name of the current scene.
    current_file_open = cmds.file(query=True, list=True)[0]  
    name_file = os.path.basename(current_file_open) 
    if not name_file.endswith(type_file):
        bad_list.append(name_file)
    return bad_list


def result():
    """function required"""
    result_error_list = get_type_file_extension()
    error_dict = {}
    non_error_dict = {}
    if result_error_list:
        error_dict[result_error_list[0]] = "---is type file extension incorret. :("
    else:
        non_error_dict = {"Scene":"---is type file extension correct. :)"}   
    return error_dict, non_error_dict



        
   
