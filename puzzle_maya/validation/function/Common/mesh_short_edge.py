functionDescription = " Mesh Short Edge"
toolTips = ""


import maya.api.OpenMaya as om2
import maya.mel as mel
import maya.cmds as cmds
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    "|front","|persp", '|side', '|top',
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

#_______________________________________________________________________________________
def get_m_dag_path(name_obj): 
    m_sel = om2.MSelectionList()
    m_sel.add(name_obj)
    m_dag_path = m_sel.getDagPath(0)
    return m_dag_path

    
def get_short_edge(m_dag_path, distance=0.005):
    bad_edges = []
    full_name = m_dag_path.fullPathName()   
    # create list iterator of Edges
    iterator_Edges = om2.MItMeshEdge(m_dag_path)  
    while not iterator_Edges.isDone():
        len_edge = iterator_Edges.length(space=4)
        index_edge = iterator_Edges.index()
       
        if len_edge < distance:
            # print len_edge
            bad_edges.append("{}.e[{}]".format(full_name, index_edge))
        iterator_Edges.next()
    return bad_edges

def get_error_short_edges():
    error_list = []
    objects_to_check = get_dag_objects_to_check()
    for obj in objects_to_check: 
        m_dag_path = get_m_dag_path(obj)
        error_edge = get_short_edge(m_dag_path, distance=0.2)
        if error_edge:
            error_list.extend(error_edge)
    return error_list
#_______________________________________________________________________________________    


def result():
    """function required"""
    result_error_list = get_error_short_edges()
    error_dict = {}
    non_error_dict = {}
    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "---has short edge < 0.2cm"
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}    
    return error_dict, non_error_dict




