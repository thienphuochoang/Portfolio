functionDescription = " Face Nonmanifold "
toolTip = ""

import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = ("|high_poly")



def get_objects():
    """get a list names to check"""
    list_selected = cmds.ls(geometry=True, long=True)
    for obj in list_selected:
        if obj.startswith(exclude_objs):
            list_selected.remove(obj)
    return list_selected


def do(objs):
    """returns the list names objects whose faces had nonmanifold"""
    result_list = []
    cmds.select(objs, replace=True)
    cmds.polySelectConstraint(mode=3, type=0x0001, nonmanifold=1)
    result_list = cmds.ls(selection=True, long=True)
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return result_list


def result():
    objs = get_objects()
    list_error = do(objs)
    error_dict = {}
    non_error_dict = {}

    if list_error:
        for er in list_error:
            error_dict[er] = "---has nonmanifold face. :("
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}
        
    return error_dict, non_error_dict


def selectCustom(lst):
    cmds.select(clear=True)
    for item in lst:
        obj = item.split("---")[0]
        cmds.select(obj, add=True)
    try:
        cmds.select(obj.split(".vtx")[0], add=True)
        mel.eval('doMenuComponentSelection("{}", "vertex")'.format(obj))
        cmds.hilite()
    except:
        cmds.warning("Mesh can't not convert selection")
        
