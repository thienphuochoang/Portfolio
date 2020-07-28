import importlib
import controller
try:
	importlib.reload(controller)
except:
	reload(controller)