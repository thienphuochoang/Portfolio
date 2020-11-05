import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya
from puzzle_maya.transfer_transformation.function import MayaProcessHook as mph
class HookMainFunction():
	def __init__(self):
		pass
		#self.globalEventManager = mph.EventManager()
		#self.globalServerHook = mph.ProcessHook(5050)
		
	def startHook(self):
		try:
			self.globalEventManager = mph.EventManager()
			self.globalServerHook = mph.ProcessHook(5050)
			self.selection_changed_callback = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", self.createSelectionChangedCallbackFunction)
			self.globalEventManager.startup()
			cmds.confirmDialog(title = "Main Working Maya", message = "This Maya is chosen to be main working")
			for obj in cmds.ls(type = "transform", long = True):
				sender = mph.TransformMessageSender(self.globalServerHook, obj)
				self.globalEventManager.get_instance().register_sender(sender)
				self.globalEventManager.get_instance().register_drag_release_callable(sender)
			return True
		except:
			cmds.confirmDialog(title = "Error", message = "Please open client port on other Maya first")
	
	def createSelectionChangedCallbackFunction(self, *args, **kwargs):
		for obj in cmds.ls(sl = True, type = "transform", long = True):
			try:
				sender = mph.TransformMessageSender(self.globalServerHook, obj)
				self.globalEventManager.get_instance().register_sender(sender)
				self.globalEventManager.get_instance().register_drag_release_callable(sender)
			except:
				pass
				
	def updateTransformationThroughButtonFunction(self):
		if cmds.ls(sl = True):
			sender = mph.TransformMessageSender(self.globalServerHook, cmds.ls(sl = True, type = "transform", long = True)[0])
			self.globalEventManager.get_instance().register_sender(sender)
			self.globalEventManager.get_instance().register_drag_release_callable(sender)
			transformation = cmds.xform(cmds.ls(sl = True, type = "transform", long = True)[0], query=True, worldSpace=True, matrix=True )
			oldX = transformation[12]
			transformation[12] = oldX + 0.001
			cmds.xform(cmds.ls(sl = True, type = "transform", long = True)[0], worldSpace=True, matrix=transformation)
			transformation[12] = oldX
			cmds.xform(cmds.ls(sl = True, type = "transform", long = True)[0], worldSpace=True, matrix=transformation)
			
			
	def shutdownSocket(self):
		try:
			self.globalEventManager.shutdown()
			OpenMaya.MMessage.removeCallback(self.selection_changed_callback)
		except:
			pass

#startHook()
#if __name__ == '__main__':
	#globalEventManager = mph.EventManager()
	#globalServerHook = mph.ProcessHook(5050)	
	#try:
		#cmds.commandPort(n = ":5050", sourceType = "python")
	#except:
		#print "Command Port is already active"
	#startHook()
	#