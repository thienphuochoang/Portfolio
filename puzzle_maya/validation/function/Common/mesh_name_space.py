functionDescription = " Mesh Namespace"
toolTips = ""


import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    "|front","|persp", '|side', '|top',
    )

def get_dag_objects():
    """get all dg node in scene"""
    camera_scene = cmds.ls(type='camera', long=True)
    return camera_scene


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


def get_mesh_namespace():
    bad_mesh = []

    ref_list = [n.replace('RN','') for n in cmds.ls(rf=True)] 
    cmds.namespace(set=':')
    all_namespace = [
        n.split(':')[len(n.split(':'))-1] 
        for n in cmds.namespaceInfo(lon=True, fn=True, r=True) 
        if n not in ['UI', 'shared']
        ]

    if all_namespace:
        for n in all_namespace:
            if n not in ref_list:
                bad_mesh.append(n)

    return bad_mesh
        
            
def do_check():
    """returns the names objects error"""
    error_list = get_mesh_namespace()
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
            error_dict[er] = "---has Namespace"
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}    
    return error_dict, non_error_dict


def selectSimilarity(lst):
    cmds.NamespaceEditor()

def fix(lst):
    pass
    defaults = [':UI', ':shared']
    namespaces = [ns for ns in cmds.namespaceInfo(
        lon=True, an=True, ) if ns not in defaults]

    while len(namespaces) > 0:
        for namespace in namespaces:
            cmds.namespace(force=True, removeNamespace=namespace,
               mergeNamespaceWithRoot=True)
        namespaces = [ns for ns in cmds.namespaceInfo(
            lon=True, an=True, ) if ns not in defaults]