functionDescription = " Material Assign Lambert1 "
toolTips = ""

import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model"
    )


def objects_do_not_check(objects, objects_ignor):
    """return a list had objects to check"""
    result = []
    for obj in objects:
        if not obj.startswith(objects_ignor):
            result.append(obj)
    return result


def get_objects():
    """get a list names to check"""
    list_selected = cmds.ls(geometry=True, long=True)
    objects_slected_to_check = objects_do_not_check(list_selected, exclude_objs)
    return objects_slected_to_check



def do_check(objs):
    """returns the list names objects error"""
    error_list = []
    #seleted objects to check
    cmds.select(objs, replace=True)
    # select meshes had assign material Lamber1
    mel.eval('hyperShade -objects initialShadingGroup') 
    all_error_list = cmds.ls(selection=True, long=True)
    error_list = objects_do_not_check(all_error_list, exclude_objs)
    # clean select
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return error_list


def result():
    """function requird"""
    objs = get_objects()
    result_error_list = do_check(objs)
    error_dict = {}
    non_error_dict = {}
    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "---has assigned material Lambert1. :("
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}   
    return error_dict, non_error_dict

