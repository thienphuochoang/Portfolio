functionDescription = " UV Out Range"
toolTip = ""

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


def get_uv_out_range(min_range=0.002, max_range=0.998, uv_set="map1"):
    vertices_out_range = []
    
    # get all node Mesh
    all_node_meshes = om2.MItDependencyNodes(om2.MFn.kMesh) 
    while not all_node_meshes.isDone():
        m_object = all_node_meshes.thisNode() # points MObject
        mfn_dag_node = om2.MFnDagNode(m_object)
        # nameMesh =  mfn_dag_node.fullPathName() #get Shape of MObject
        nameMesh =  mfn_dag_node.partialPathName()

        itVertex = om2.MItMeshFaceVertex(m_object)

        while not itVertex.isDone():
            try:
                indexUV = itVertex.getUVIndex(uvSet=uv_set)  #-> (float, float)
                coordinateUV = itVertex.getUV(uvSet=uv_set)  #-> int
                # print indexUV
                # print coordinateUV
                if not (min_range < coordinateUV[0] < max_range) or not (min_range < coordinateUV[1] < max_range):
                    nameSelect = "{}.map[{}]".format(nameMesh, indexUV)
                    vertices_out_range.append(nameSelect)
            except:
                pass
 
            itVertex.next()
            
        all_node_meshes.next()
    return vertices_out_range


def result():
    """function required"""
    error_list_map1 = get_uv_out_range()
   
    error_dict = {}
    non_error_dict = {}
    
    if error_list_map1:
        for er in error_list_map1:
            error_dict[er] = "---map1 has the uv map out range [0:1]"
    else: 
        non_error_dict["Scene"] = "---Clean :)"
    return error_dict, non_error_dict








