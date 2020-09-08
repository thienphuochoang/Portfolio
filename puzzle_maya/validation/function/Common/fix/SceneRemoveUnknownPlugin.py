import maya.cmds as cmds

description = "Remove unknown Plugin"
toolTips = ""

def run():

    unknownPlugins = cmds.unknownPlugin(query=True, list=True)
    for plugin in unknownPlugins:
        print plugin
        try:
            cmds.unknownPlugin(plugin, remove=True)
        except:
            cmds.warning(plugin + " Not delete")