functionDescription = " Face N-Gons "
toolTip = ""

import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = ("|high_poly")



def get_objects():
    """get a list names to check"""
    list_selected = cmds.ls(geometry=True, long=True)
    for obj in list_selected:
        if obj.startswith(exclude_objs):
            list_selected.remove(obj)
    return list_selected

def poly_nsided_to_quad():
    cmds.ConvertSelectionToFaces() 
    mel.eval('polySelectConstraint -m 2 -t 8 -sz 3;')
    mel.eval('polyTriangulate -ch 1 ;')
    mel.eval('polyQuad  -a 30 -kgb 1 -ktb 1 -khe 1 -ws 1 -ch 0;')
    mel.eval('polySelectConstraint -m 0;')
    mel.eval('resetPolySelectConstraint;')


def do_check(objs):
    """returns the list names objects whose faces had Concave"""
    result_list = []
    cmds.select(objs, replace=True)
    result_list = mel.eval('polyCleanupArgList 4 { "0","2","1","0","1","0","0","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')

    cmds.polySelectConstraint(disable=True)
    cmds.hilite(replace=True)
    cmds.select(clear=True)
    return result_list



def result():
    print ("ahihi")
    objs = get_objects()
    list_error = do_check(objs)
    error_dict = {}
    non_error_dict = {}

    if list_error:
        for er in list_error:
            error_dict[er] = "---has N-gons face."
    else:
        non_error_dict = {"Scene ":"---Clean. :)"}

    return error_dict, non_error_dict

def fix(lst):
    poly_nsided_to_quad()
    
def selectSimilarity():
    print ("test Select Similarity")

# def selectCustom(lst):
#     cmds.select(clear=True)
#     for item in lst:
#         obj = item.split("---")[0]
#         cmds.select(obj, add=True)
#     try:
#         cmds.select(obj.split(".f")[0], add=True)
#         mel.eval('doMenuComponentSelection("{}", "facet")'.format(obj))
#         cmds.hilite()
#     except:
#         cmds.warning("Mesh can't not convert selection")
        
