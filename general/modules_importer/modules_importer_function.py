import importlib
import sys
def importModule(modulePath):
	if modulePath in sys.modules:
		try:
			importlib.reload(sys.modules[modulePath])
		except:
			reload(sys.modules[modulePath])
		return sys.modules[modulePath]
	else:
		importedModule = importlib.import_module(modulePath)
		return importedModule