functionDescription = " Mesh Color Set "
toolTips = ""

import maya.cmds as cmds
import maya.mel as mel
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
    return list(set(meshes))



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


def get_meshes_had_colorset():
    bad_list = {}
    meshes = get_dag_objects_to_check()

    for obj in meshes:
        name_color_sets = cmds.polyColorSet(obj, query=True, allColorSets=True)
        type_color_sets = cmds.polyColorSet(obj, query=True,  representation=True)
        if name_color_sets:
            bad_list[obj] = name_color_sets
    return bad_list


def do_check():
    """returns the list names objects error"""
    error_list = get_meshes_had_colorset()
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
        for k,v in result_error_list.items():
            #print k,v 
            error_dict[k] = "---are had wrong colorsets  {}".format(str(v))
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}   
    return error_dict, non_error_dict

def fix():
    meshes = get_dag_objects_to_check()
    for obj in meshs:
        colorSets = cmds.polyColorSet(obj, query=True, acs=True) #  Get colorSet from Mesh
        if colorSets:
            for colSet in colorSets:
                # print colSet
                try:
                    cmds.polyColorSet( obj, delete=True, colorSet=colSet )
                except:
                    pass

def selectSimilarity(lst):
    pass

