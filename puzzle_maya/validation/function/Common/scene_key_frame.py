
functionDescription = " Scene Set Keyframe"
toolTips = ""

import maya.api.OpenMaya as om2
import maya.mel as mel
import maya.cmds as cmds
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    )


def get_dag_objects():
    """get all dg node in scene"""
    meshes = cmds.ls(type='mesh', long=True)
    transfroms = cmds.ls(type='transform', long=True)
    materials =  cmds.ls(mat = True)
    files = cmds.ls(type='file')
    dag_objects = meshes + materials + transfroms + files 
    return dag_objects


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


#_______Function Required_______#  
def get_objects_set_keyframe():
    bad_list = []
    selected_objects = get_dag_objects_to_check()
    for obj in selected_objects:
        # print element
        if cmds.keyframe(obj) > 0:
            bad_list.append(obj)
    return bad_list


def do_check():
    """returns the names objects error"""
    error_list = get_objects_set_keyframe()
    # clean select
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return error_list


def result():
    """function required"""
    result_error_list = do_check()
    result_non_error_list = []
    error_dict = {}
    non_error_dict = {}
    
    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "---has set keyframe. :("
    else: 
        non_error_dict["Scene:"] = "---Clean. :)"
    return error_dict, non_error_dict


def fix(lst):
    error_list = get_objects_set_keyframe()
    keyframes = []
    try:
        keyframes += cmds.listConnections(error_list, s=True, type="animCurveTU")
    except:
        pass
    try:
        keyframes += cmds.listConnections(error_list, s=True, type="animCurveTL")
    except:
        pass
    try:
        keyframes += cmds.listConnections(error_list, s=True, type="animCurveTA")
    except:
        pass

    cmds.delete(keyframes)
    # print keyframes
    









            
            

