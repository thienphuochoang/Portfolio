functionDescription = " Scene Empty Group "
toolTips = ""

import maya.mel as mel
import maya.cmds as cmds
import maya.api.OpenMaya as om2
#If suffix name had in list exclude_objs, It's not check


def get_empty_group():
    bad_list = []
    
    allNodeTransform = om2.MItDependencyNodes(om2.MFn.kTransform  ) # query all node Mesh
    while not allNodeTransform.isDone():
        mObject = allNodeTransform.thisNode() # points MObject
        mfnDagNode = om2.MFnDagNode(mObject) # assigned MObject into MFnMesh
        fullPath = mfnDagNode.fullPathName()
        childCount = mfnDagNode.childCount()
        if childCount == 0:
            bad_list.append(fullPath)
        allNodeTransform.next()


def do_check():
    """returns the list names objects error"""
    error_list = get_empty_group()
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
            error_dict[er] = "---has empty group. :("
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}   
    return error_dict, non_error_dict

