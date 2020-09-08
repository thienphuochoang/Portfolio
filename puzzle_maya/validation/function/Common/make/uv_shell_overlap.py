functionDescription = " UV Shell Overlaping "
toolTip = ""

import maya.api.OpenMaya as om2
import maya.mel as mel
import maya.cmds as cmds
import itertools

exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    "|ScaleRef",
    )

def dag_objects_do_not_check(objects, ignor):
    """remove the objects do not check"""
    result = []
    for obj in objects:
        if not obj.startswith(ignor):
            result.append(obj)
    return result
    
    
description = ""
toolTips = ""

import maya.api.OpenMaya as om2
import maya.mel as mel
import maya.cmds as cmds
import itertools

def flattenDict(dict):
    """
        Flatten Dict
    """
    newDict = {}
    for element in dict :
        newDict.update(element)
    return newDict

def findKeyWithDuplicateValues(dict):
    """
        [Dis] If Key with duplicate Values, return a list duplicatre else return list None
    """
    rev_multidict = {}
    for key, value in dict.items():
        rev_multidict.setdefault(value, set()).add(key)  # revert Dictionary
    duplicateValues = [list(values) for key, values in 
                       rev_multidict.items() if len(values) > 1]
    return duplicateValues

def GetUVsShell(mObject):
    """
     [in] mObject
    [out] Return a Dictionary containing UVShellIds and the u and v values of the specified UV.
    """
    mFnMesh =  om2.MFnMesh(mObject) 
    # mFnDepenNode = om2.MFnDependencyNode(mObject)
    # mFnDepenNode.name()   #get name Shape
    uvShellIds = mFnMesh.getUvShellsIds()
    mFnDagNode = om2.MFnDagNode(mObject)
    fullPathObj = mFnDagNode.fullPathName()
    shells = {}
    for i, n in enumerate(uvShellIds[1]):
        # print i , n
        if n in shells:
            shells[n].append({"{}.map[{}]".format(fullPathObj, i) : mFnMesh.getUV(i, "map1")})
        else:
            shells[n] = [{"{}.map[{}]".format(fullPathObj, i) : mFnMesh.getUV(i, "map1")}]
    return shells


#_______Function Required_______# 
def get_uv_shell_overlap():
    bad_list = []
    allNodes = om2.MItDependencyNodes(om2.MFn.kMesh) # get all mObject in Scene 
    while not allNodes.isDone(): 
        mObject = allNodes.thisNode() # points MObject
        mFnDagNode = om2.MFnDagNode(mObject)
        fullPathObj = mFnDagNode.fullPathName() # full path mesh
        objects_to_check = dag_objects_do_not_check([fullPathObj], exclude_objs)
        if objects_to_check:
            cmds.polyUVSet(objects_to_check, currentUVSet=True,  uvSet='map1')
            shellUVs = GetUVsShell(mObject)
            for k, v in shellUVs.items():
                # print v
                flatten = flattenDict(v)
                if findKeyWithDuplicateValues(flatten):
                    shell = findKeyWithDuplicateValues(flatten)
                    merged  = list(itertools.chain.from_iterable(shell))
                    bad_list.extend(merged)
        allNodes.next()  
    return bad_list

   
def result():
    """function required"""
    
    result_error_list_map1 = get_uv_shell_overlap()
    #result_error_list_lightmap = get_uv_shell_overlap(uv_set)
    result_non_error_list = []
    error_dict = {}
    non_error_dict = {}
    
    if result_error_list_map1:
        for er in result_error_list_map1:
            error_dict[er] = "---Map1 had vertex map overlaping. :("
    else: 
        non_error_dict["Scene---Map1"] = " Clean. :)"
        
    #if result_error_list_lightmap:
        #for er in result_error_list_lightmap:
            #error_dict[er] = "---is vertex map overlaping. :("
    #else: 
        #non_error_dict["Scene---Light Map"] = " Clean. :)"
    return error_dict, non_error_dict
    
    
def selectCustom(lst):
    cmds.polyUVSet( currentUVSet=True,  uvSet='map1')
    cmds.select(lst, replace=True)
        
    
    

