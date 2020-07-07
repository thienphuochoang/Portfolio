import importlib
from htp_max.normal_tool.controller import controller
try:
	importlib.reload(controller)
except:
	reload(controller)