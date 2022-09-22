functionDescription = " Mesh Delete History "
toolTips = ""

import maya.mel as mel
import maya.cmds as cmds
import maya.api.OpenMaya as om2
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    "|Background_Geo"
    )


def get_dag_objects():
    """get all dg node in scene"""
    meshes = [cmds.listRelatives(m, p=True, f=True)[0]
              for m in cmds.ls(type='mesh', l=True)]
    return meshes


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


def get_mesh_had_history():
    bad_list = []
    default_history = ['mesh', 'groupId', 'shadingEngine']
    meshes = get_dag_objects_to_check()
    for obj in meshes:
        list_history = cmds.listHistory(obj)
        for h in list_history:
            type_history = cmds.nodeType(h)
            if type_history not in default_history:
                bad_list.append(obj)
                bad_list.append(h)
        deform_history = cmds.ls(type_history, type="geometryFilter", long=True)
        if deform_history:
            bad_list.append(obj)       
    return bad_list
   

def do_check():
    """returns the list names objects error"""
    error_list = get_mesh_had_history()
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
            error_dict[er] = "---is not delete the history"
    else:
        non_error_dict = {"Scene---" : "Clean :)!"}   
    return error_dict, non_error_dict


def fix(lst):
    delete_history_lst = ("objectSet")
    for err in lst:
        type_error = cmds.nodeType(err)
        if  type_error.endswith(delete_history_lst):
            try:
                cmds.delete(err)
            except:
                pass
        else:
            cmds.DeleteHistory()


# def selectCustom(lst):
#     cmds.select(lst, replace=True, noExpand=True)


