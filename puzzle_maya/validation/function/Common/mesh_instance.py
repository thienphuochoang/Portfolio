functionDescription = " Mesh Instance "
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

def get_meshes_instance():
    bad_list = []
    objects = [a for a in cmds.ls(type='mesh') 
        if len(cmds.listRelatives(a, ap=True)) > 1]

    if objects:
        for obj in objects:
            bad_list.append(obj)
    return bad_list

def do_check(objs):
    """returns the list names objects error"""
    error_list = []
    #seleted objects to check
   
    all_error_list = get_meshes_instance()
    error_list = objects_do_not_check(all_error_list, exclude_objs)
    # clean select
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return error_list


def result():
    """function requird"""
    result_error_list = do_check(None)
    error_dict = {}
    non_error_dict = {}
    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "---is mesh instance. :("
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}   
    return error_dict, non_error_dict

