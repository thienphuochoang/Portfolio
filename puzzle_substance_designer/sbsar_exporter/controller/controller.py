import importlib
import sys


moduleImporterPath = 'general.modules_importer.modules_importer_function'
importerFunction = None

if moduleImporterPath in sys.modules:
	importerFunction = sys.modules[moduleImporterPath]
	try:
		importlib.reload(importerFunction)
	except:
		reload(importerFunction)
else:
	importerFunction = importlib.import_module(moduleImporterPath)
	
#import Function____________________
thumbnail_rendering_function = importerFunction.importModule("puzzle_substance_designer.sbsar_exporter.function.export_sbsar_function")






