
functionDescription = " Scene Unit Axis Setup"
toolTips = ""

import maya.api.OpenMaya as om2
import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    )

def get_dag_objects():
    """get all dg node in scene"""
    iter_meshes = om2.MItDependencyNodes(om2.MFn.kMesh)
    return iter_meshes


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

def get_unit_scene(unit_user):
    bads = []
    goods = []
    unit_currnent = cmds.currentUnit(query=True, fullName=True)
 
    if unit_currnent != unit_user:
        bads.append('Unit wrong: current is "{}"  :(!'.format(unit_currnent))
    else:
        goods.append('Unit correct: current is "{}"  :)!'.format(unit_currnent))
    return bads, goods

def get_axis_scene(axis_user):
    bads = []
    goods = []
    axis_current = cmds.upAxis(query=True, axis=True)

    if axis_current != axis_user:
        bads.append('Axis wrong---current is "{}". :('.format(axis_current))
    else:
        goods.append('Axis correct---current is "{}". :)'.format(axis_current))
    return bads, goods
   

def do_check():
    """returns the names objects error"""
    #centimeter
    error_list = get_unit_scene("centimeter")[0] + get_axis_scene("y")[0]
    non_error_list = get_unit_scene("centimeter")[1] + get_axis_scene("y")[1]  
    # clean select
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return error_list, non_error_list


def result():
    """function required"""
    result_error_list = do_check()[0]
    result_non_error_list = do_check()[1]
    error_dict = {}
    non_error_dict = {}
    if result_error_list:
        for er in result_error_list:
            error_dict[er] = " "
            
    if result_non_error_list:
        for non_er in result_non_error_list:
            non_error_dict[non_er] = " "
    return error_dict, non_error_dict


def fix():
    cmds.currentUnit(linear="meter")
    cmds.upAxis(axis="y")
    


        




