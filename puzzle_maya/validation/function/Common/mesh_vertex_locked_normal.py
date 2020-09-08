functionDescription = " Mesh Vertex Locked Normal"
toolTips = ""

import maya.api.OpenMaya as om2
import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    "|Background",
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


def get_vertex_locked_normal(allNodesMesh):
    locked_normals = []
    while not allNodesMesh.isDone():
        mObject = allNodesMesh.thisNode() # points MObject
        mFnMesh = om2.MFnMesh(mObject) # assigned MObject into MFnMesh
        itFaceVertex = om2.MItMeshFaceVertex(mObject)
        
        while not itFaceVertex.isDone():
            # vertexID = itFaceVertex.vertexId()  #-> int
            # faceID = itFaceVertex.faceId() #Returns the current face index -> in
            normalId = itFaceVertex.normalId() # -> int
            isNormal = mFnMesh.isNormalLocked(normalId)
            # print isNormal
            if isNormal:
                mFnDagNode = om2.MFnDagNode(mObject)
                # nameMesh =  mFnDagNode.fullPathName().split("|")[-1]
                nameMesh =  mFnDagNode.fullPathName()
                locked_normals.append("{}.vtx[{}]".format(nameMesh ,itFaceVertex.vertexId()))
            itFaceVertex.next()
        allNodesMesh.next()
    return locked_normals

        
def meshes_locked_normal():
    bad_list = []
    # get all node Mesh
    meshes = get_dag_objects()
    bad_list = list(set(get_vertex_locked_normal(meshes))) # get list vertex lock normal
    return bad_list
    
   

def do_check():
    """returns the names objects error"""
    objects = meshes_locked_normal()
    error_list = dag_objects_do_not_check(objects, exclude_objs)
    # clean select
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return error_list


def result():
    """function required"""
    result_error_list = do_check()
    result_non_error_list =[]
    error_dict = {}
    non_error_dict = {}

    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "---has locked normal vertex. :("
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}   
    return error_dict, non_error_dict


        




