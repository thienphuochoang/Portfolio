functionDescription = " Scene Layer Name"
toolTips = ""

import maya.api.OpenMaya as om2
import maya.mel as mel
import maya.cmds as cmds

#If suffix name had in list exclude_objs, It's not check
NAME_DEFAULT_LAYERS = (
        "defaultLayer", 
        "defaultRenderLayer", 
        "layerManager", 
        "renderLayerManager", 
        )

EXCLUDE_DISPLAY_LAYERS = (
    "defaultLayer",
    "Render_L0_Props",
    "REF",
    "Render_L0",
    "PieceRoot",
    "Background"
    )


#proceed
def get_scene_layers():
    type_layers = (
        "renderLayer",
        "displayLayerManager",
        "renderLayerManager",
        "animLayer"
        )
    scene_layers = cmds.ls(type=type_layers, long=True)
    return scene_layers


def get_scene_layers_default():
    scene_layers = get_scene_layers()
    scene_layers_default = [ul for ul in scene_layers if ul not in NAME_DEFAULT_LAYERS]
    return scene_layers_default


def get_user_display_layers():
    display_layers = cmds.ls(type="displayLayer", long=True)
    user_layers_default = [ul for ul in display_layers if ul not in EXCLUDE_DISPLAY_LAYERS]
    return user_layers_default


def get_layers_wrong():
    scene_layers_error = get_scene_layers_default()
    user_layers_error = get_user_display_layers()
    layers_error = scene_layers_error + user_layers_error
    return layers_error


def do_check():
    """returns the names objects error"""
    error_list = get_layers_wrong()
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
            error_dict[er] = "---is incorrect name.:("
    else: 
        non_error_dict["Scene:"] = "---Layers are correct :)"
    return error_dict, non_error_dict


        
def fix(lst):
    camera_error = get_layers_wrong()
    cmds.delete(camera_error)







            
            

