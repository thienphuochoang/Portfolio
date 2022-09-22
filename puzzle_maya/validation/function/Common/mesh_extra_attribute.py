functionDescription = " Mesh Extra Attribute "
toolTips = ""

import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model"
    )

def get_dag_objects():
    """get all dg node in scene"""
    meshes = cmds.ls(type='mesh', long=True)
    transfroms = cmds.ls(type='transform', long=True)
    # materials =  cmds.ls(mat = True)
    files = cmds.ls(type='file')
    dag_objects = meshes + transfroms + files
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


def get_mesh_extra_attribute():
    error_extra_attribute = []
    objects_selected_to_check = get_dag_objects_to_check()

    for obj in objects_selected_to_check:
        attr_user = cmds.listAttr(obj, userDefined=True)  # Get attribulate User Defined
        if attr_user:
            error_extra_attribute.append(obj)
    return error_extra_attribute


def remove_extra_attribute(lst):
    for obj in lst:
        # Get attribulate User Defined
        attr_user = cmds.listAttr(obj, userDefined=True)  
        if attr_user:
            for attr in attr_user:
                try:
                    cmds.deleteAttr( obj, attribute = attr )
                except:
                    cmds.warning("Attribulte can't delete: " + attr)


def do_check(objs):
    """returns the list names objects error"""
    error_list = get_mesh_extra_attribute()
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
            error_dict[er] = "---has an extra attribute"
    else:
        non_error_dict = {"Scene":"---Clean :)"}   
    return error_dict, non_error_dict

def fix(lst, *args):
    objects_selected_to_check = get_dag_objects_to_check()
    remove_extra_attribute(objects_selected_to_check)

