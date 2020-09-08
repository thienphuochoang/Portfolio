functionDescription = " Mesh Tangent Space  "
toolTips = ""


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
    meshes = [
    	cmds.listRelatives(m, parent=True, fullPath=False)[0]
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


def get_tangent_meshes():
    bad_meshes = []
    good_meshes = []

    meshes = get_dag_objects_to_check()
    for mesh in meshes:
        # print mesh
        # Get Attribute of tangent Space. if == 0 >>>Right Handed, elif == 2 >>> Left Handed
        tangent = cmds.getAttr(mesh + ".tangentSpace")
        if tangent != 0:
            bad_meshes.append(mesh)
        elif tangent == 0:
        	good_meshes.append(mesh)

    return bad_meshes, good_meshes
    

def do_check():
    """returns the names objects error"""
    error_list = get_tangent_meshes()[0]
    non_error_list = get_tangent_meshes()[1]
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
            error_dict[er] = "---is not right handed tangent space. :( "
    if result_non_error_list:
        for non_er in result_non_error_list:
            non_error_dict[non_er] = "---is right handed tangent space. :)"
    return error_dict, non_error_dict


        
