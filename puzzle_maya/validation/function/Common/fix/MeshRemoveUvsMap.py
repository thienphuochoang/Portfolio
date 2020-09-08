description = "Remove any Uvs map"
toolTips = ""

import maya.cmds as cmds

def run():
    '''Get all mesh in Scene and Remove any uvSet not name map1 in nodesType "mesh" '''
    list_mesh_sel = cmds.ls(type='mesh')
    for mesh in list_mesh_sel:
        cmds.select(mesh)
        list_uvset = cmds.polyUVSet(query=True, allUVSets=True)
        for uv in list_uvset[1:]:
            cmds.polyUVSet(delete=True, uvSet=uv)
        if list_uvset[0] != 'map1':
            cmds.polyUVSet(rename=True, newUVSet='map1', uvSet=list_uvset[0])          
    cmds.select(clear=True)

            
    