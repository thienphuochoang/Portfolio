functionDescription = " Mesh Freeze Transformations "
toolTips = ""


import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    "|front","|persp", '|side', '|top'
    )

def get_dag_objects():
    """get all dg node in scene"""
    transforms= cmds.ls(type='transform', long=True)
    return transforms


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


def get_transform():
    bad_list = []
    transform_user = get_dag_objects_to_check()

    for transform in transform_user:
        translate = cmds.getAttr('{0}.translate'.format(transform))
        rotate = cmds.getAttr('{0}.rotate'.format(transform))
        scale = cmds.getAttr('{0}.scale'.format(transform))
        if translate != [(0.0, 0.0, 0.0)] or rotate != [(0.0, 0.0, 0.0)] or scale != [(1, 1, 1)]:
            bad_list.append(transform)
    return bad_list
            

def do_check():
    """returns the names objects error"""
    error_list = get_transform()
    # clean select
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return error_list


def result():
    """function required"""
    result_error_list = do_check()
    error_dict = {}
    non_error_dict = {}
    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "---has freeze transformations. :("
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}   
    return error_dict, non_error_dict


        
