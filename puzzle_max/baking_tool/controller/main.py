import importlib
from puzzle_max.decal_tool.controller import controller
try:
	importlib.reload(controller)
except:
	reload(controller)