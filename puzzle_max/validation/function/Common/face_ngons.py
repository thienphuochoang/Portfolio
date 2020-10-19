toolTip = ""

import pymxs
rt = pymxs.runtime

exclude_objs = ("|high_poly")



def get_objects():
    """get a list names to check"""
    list_selected = rt.selection
    for obj in list_selected:
        if obj.name.startswith(exclude_objs):
            list_selected.remove(obj)
    return list_selected

# def poly_nsided_to_quad():
#     cmds.ConvertSelectionToFaces() 
#     mel.eval('polySelectConstraint -m 2 -t 8 -sz 3;')
#     mel.eval('polyTriangulate -ch 1 ;')
#     mel.eval('polyQuad  -a 30 -kgb 1 -ktb 1 -khe 1 -ws 1 -ch 0;')
#     mel.eval('polySelectConstraint -m 0;')
#     mel.eval('resetPolySelectConstraint;')


def do_check(objs):
    result_list = []
    for obj in objs:
        rt.subObjectLevel = 0
        numberOfFacesList = (rt.polyop.getNumFaces(obj))
        for face in range(1, numberOfFacesList + 1):
            numberOfVertsList = rt.polyop.getFaceVerts(obj, face)
            if numberOfVertsList != None:
                if len(numberOfVertsList) > 4:
                    result_list.append(face)
    return result_list



def result():
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
    #poly_nsided_to_quad()
	
def selectSimilarity():
	print "test Select Similarity"