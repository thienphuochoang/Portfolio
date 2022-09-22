functionDescription = " Material Type "
toolTips = ""

import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model"
    )
default_shaders = ['lambert1', 'particleCloud1', "default_shaders"]
type_shaders_correct = ["lambert"]

def get_dag_objects():
    """get all shalders in scene, excluded default shaders"""
    shaders_user = [m for m in cmds.ls(materials=True, long=True) 
        if m not in default_shaders]
    return shaders_user


def dag_objects_do_not_check(objects, ignor):
    """remove the objects do not check"""
    result = []
    for obj in objects:
        if not obj.startswith(ignor):
            result.append(obj)
    return result


def get_dag_objects_to_check():
    """get a list dag nodes to check"""
    dag_objects = get_dag_objects()
    dag_objects_to_check = dag_objects_do_not_check(dag_objects, exclude_objs)
    return dag_objects_to_check

#______________________________________________________________________________________________

    
def check_type_shaders():
    type_shaders_error = []
    shaders_to_check = get_dag_objects_to_check()
    for shader in shaders_to_check:
        type_shader = cmds.nodeType(shader)
        if type_shader != "lambert":
            type_shaders_error.append(shader)
    return type_shaders_error
    
#______________________________________________________________#___________________________________
def result():
    """function requird"""
    result_error_list = check_type_shaders()
    error_dict = {}
    non_error_dict = {}
    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "---incorrect Material :("
    else:
        non_error_dict = {"Scene ":"---correct Materials. :)"}   
    return error_dict, non_error_dict

