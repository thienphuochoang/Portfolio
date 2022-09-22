import socket
import inspect
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds

class EventManager():
	__instance = None
	def __init__(self):
		self.is_drag_release = False
		self.drag_release_callable_dict = {}
		self.callable_message_sender_class_list = []
		self.sender_callable_list = []
		self.dragReleaseCallbackIndex = OpenMaya.MEventMessage.addEventCallback("DragRelease", self.__drag_release_message_callable)
		self.register_objs = []

	def __drag_release_message_callable(self, *args):
		for f in self.drag_release_callable_dict.values():
			f()

	@staticmethod 
	def get_instance():
		if EventManager.__instance == None:
			 EventManager.__instance = EventManager()
		return EventManager.__instance

	@staticmethod 
	def startup():
		EventManager.__instance = EventManager()

	@staticmethod 
	def shutdown():
		OpenMaya.MMessage.removeCallback(EventManager.__instance.dragReleaseCallbackIndex)
		for obj in EventManager.__instance.register_objs:
			if not obj.unregister == None:
				obj.unregister()

	def register_sender(self, sender_instance):
		self.register_objs.append(sender_instance)
		sender_instance.register()

	def register_drag_release_callable(self, sender):
		self.drag_release_callable_dict['{0}_{1}'.format(sender.object_name, sender.__class__)] = sender.drag_release_command

class ProcessHook():
	def __init__(self, pid):
		self.hookSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.hookSocket.connect(('localhost', pid))

	def send_command(self, command):
		self.hookSocket.send(str.encode(command))

	def close(self):
		self.hookSocket.close()

class ProcessMessageSender():
	def __init__(self, process_hook, object_name):
		self.process_hook = process_hook
		self.object_name = object_name
		self.callback_index = -1
		self.is_drag_release_callable = False
	
	def register(self):
		pass

	def get_str_command(self, arg):
		return ""

	def message_callable(self, *args):
		pass

	def drag_release_command(self):
		pass

	def unregister(self):
		if not self.callback_index == -1:
			OpenMaya.MMessage.removeCallback(self.callback_index)
			self.callback_index = -1
			if not self.process_hook == None:
				self.process_hook.close()

class TransformMessageSender(ProcessMessageSender):
	def __init__(self, process_hook, object_name):
		ProcessMessageSender.__init__(self, process_hook, object_name)
		self.event_manager = EventManager.get_instance()
		self.is_drag_release_callable = False

	def register(self):
		selectionList = OpenMaya.MSelectionList()
		selectionList.clear()
		try:
			selectionList.add(self.object_name)
		except:
			print (self.object_name + 'not exists')
		node = selectionList.getDependNode(0)
		self.callback_index = OpenMaya.MNodeMessage.addNodeDirtyPlugCallback(node, self.message_callable)

	def get_str_command(self, arg):
		self.transformation = cmds.xform(self.object_name, query=True, worldSpace=True, matrix=True )
		code = 'import maya.cmds as cmds\ntry:\n    cmds.xform("{0}", worldSpace=True, matrix={1})\nexcept:\n    if cmds.ls(sl = True):\n        cmds.xform(cmds.ls(sl = True)[0], worldSpace=True, matrix={2})\n    else:\n        pass'.format(self.object_name, self.transformation, self.transformation)
		#code = 'import maya.cmds as cmds\ncmds.xform(cmds.ls(sl = True)[0], worldSpace=True, matrix={0})'.format(self.transformation)
		return code

	def drag_release_command(self):
		if self.is_drag_release_callable:
			self.process_hook.send_command(self.get_str_command(None))
			self.is_drag_release_callable = False

	def message_callable(self, *args):
		test_case = ('translateX', 'translateY', 'translateZ', 'translate', 'rotateX', 'rotateY', 'rotateZ', 'rotate', 'scaleX', 'scaleY', 'scaleZ', 'scale')
		name = args[1].name()
		for t in test_case:
			if name.find(t) >= 0:
				self.is_drag_release_callable = True
				return
				
class PortFunction():
	def __init__(self):
		pass
		
	def openPort(self):
		cmds.commandPort(n = ":5050", sourceType = "python")
		
	def closePort(self):
		cmds.commandPort(n = ":5050", close = True)

	def checkPortStatus(self):
		if cmds.commandPort(":5050", query = True):
			return True
		else:
			return False

