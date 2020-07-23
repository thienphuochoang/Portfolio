import importlib
from puzzle_max.exporter.controller import controller
try:
	importlib.reload(controller)
except:
	reload(controller)