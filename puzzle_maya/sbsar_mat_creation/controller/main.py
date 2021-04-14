import importlib
import sys
moduleImporterPath = 'general.modules_importer.modules_importer_function' # Don't change this
importerFunction = None

if moduleImporterPath in sys.modules:
	importerFunction = sys.modules[moduleImporterPath]
	try:
		importlib.reload(importerFunction)
	except:
		reload(importerFunction)
else:
	importerFunction = importlib.import_module(moduleImporterPath)

importerFunction.importModule('puzzle_maya.sbsar_mat_creation.controller.controller')
