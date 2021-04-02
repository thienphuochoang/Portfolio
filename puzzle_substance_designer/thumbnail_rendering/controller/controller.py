import importlib
import sys


moduleImporterPath = 'general.modules_importer.modules_importer_function'
importerFunction = None
print (sys.modules)
if moduleImporterPath in sys.modules:
	importerFunction = sys.modules[moduleImporterPath]
	try:
		importlib.reload(importerFunction)
	except:
		reload(importerFunction)
else:
	importerFunction = importlib.import_module(moduleImporterPath)
	
#import Function____________________
thumbnail_rendering_function = importerFunction.importModule("puzzle_substance_designer.thumbnail_rendering.function.thumbnail_rendering_function")






