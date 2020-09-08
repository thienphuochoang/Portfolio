description = "Remove Namespace"
toolTips = ""

import maya.cmds as cmds

def run():
    defaults = [':UI', ':shared']
    namespaces = [ns for ns in cmds.namespaceInfo( lon=True, an=True, ) if ns not in defaults]

    while len(namespaces) > 0:
        for namespace in namespaces:
            print namespace
            cmds.namespace(force=True, removeNamespace = namespace, mergeNamespaceWithRoot = True )
        namespaces = [ns for ns in cmds.namespaceInfo( lon=True, an=True, ) if ns not in defaults]
        
