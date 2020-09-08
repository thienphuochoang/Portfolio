functionDescription = " Face Concave "
toolTips = ""

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om2
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    "|front","|persp", '|side', '|top'
    )

def get_dag_objects():
    """get all dag node in scene"""
    geometrys = cmds.ls(geometry=True, long=True)
    return geometrys


def dag_objects_do_not_check(objects, ignor):
    """remove the objects do not check"""
    result = []
    for obj in objects:
        if not obj.startswith(ignor):
            result.append(obj)
    return result


def get_dag_objects_to_check():
    """get a list dag node to check"""
    dag_objects = get_dag_objects()
    dag_objects_to_check = dag_objects_do_not_check(dag_objects, exclude_objs)
    return dag_objects_to_check


def do_check():
    """returns the names objects error"""
    error_list = []
    cmds.polySelectConstraint(mode=3, type=0x0008, convexity=1)
    result_list = cmds.ls(selection=True, long=True)
    error_list = dag_objects_do_not_check(result_list, exclude_objs)
    # clean select
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return error_list


def result():
    error_result = do_check()
    error_dict = {}
    non_error_dict = {}

    if error_result:
        for er in error_result:
            error_dict[er] = "---has concave face."
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}
        
    return error_dict, non_error_dict


def selectCustom(lst):
    cmds.select(clear=True)
    for item in lst:
        obj = item.split("---")[0]
        cmds.select(obj, add=True)
    try:
        cmds.select(obj.split(".f")[0], add=True)
        mel.eval('doMenuComponentSelection("{}", "facet")'.format(obj))
        cmds.hilite()
    except:
        cmds.warning("Mesh can't not convert selection")
        