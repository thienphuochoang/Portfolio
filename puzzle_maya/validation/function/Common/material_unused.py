functionDescription = " Material Unused "
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


def scene_shaders():
    """get all shalders in scene, excluded default shaders"""
    default_shaders = ['lambert1', 'particleCloud1', "default_shaders"]
    all_mat = [m for m in cmds.ls(mat=True, long=True) if m not in default_shaders]
    return all_mat


def do_check(objs):
    """returns the list names objects error"""
    error_list = []
    #seleted objects to check
    cmds.select(objs, replace=True)
    # select meshes had assign material Lamber1
    all_shading = [s for s in cmds.ls(type='shadingEngine', long=True)]
    all_mat = scene_shaders()

    for s in all_shading:
        if not cmds.listConnections(s, t='mesh'):
            for m in cmds.listConnections(s, s=True):
                if m in all_mat:
                    error_list.append (m)
    
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
            error_dict[er] = "---is unused in scene. :("
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}   
    return error_dict, non_error_dict

def fix(lst):
    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')