functionDescription = " Scene Camera Name Wrong"
toolTips = ""


import maya.cmds as cmds
import maya.mel as mel
#If suffix name had in list exclude_objs, It's not check
exclude_objs = (
    "|high_poly",
    "|Ref_Materials",
    "|Props_Do_Not_Model",
    )
camera_default = ["|persp|perspShape", "|top|topShape", "|front|frontShape", "|side|sideShape"]
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


def get_camera_user():
    
    bad_camera = []
    all_caneras = get_dag_objects()
    for cam in all_caneras:
        if cam not in camera_default:
            bad_camera.append(cam)
    return bad_camera
        
            
def do_check():
    """returns the names objects error"""
    error_list = get_camera_user()
    # clean select
    cmds.polySelectConstraint(disable=True)
    cmds.select(clear=True)
    return error_list


def result():
    """function required"""
    result_error_list = do_check()
    result_non_error_list = []
    error_dict = {}
    non_error_dict = {}

    if result_error_list:
        for er in result_error_list:
            error_dict[er] = "---is incorrect :("
    else:
        non_error_dict = {"Scene ":"---Camera is correct. :)"}
        
    return error_dict, non_error_dict


def fix(lst):
    scene_camera = get_camera_user()
    for cam in scene_camera:
        if cam not in camera_default:
            cmds.camera(cam, edit=True, startupCamera=False)
            cam_tranform = cmds.listRelatives(cam, allParents=True)
            try:
                cmds.delete(cam_tranform)
            except:
                cmds.warning("Camera can't delete")    




