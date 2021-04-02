import importlib
import sys
import os

# Have to append root path because of running outside Python
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
puzzleRootPath = "/".join(currentFilePath.split("/")[:-3])
sys.path.append(puzzleRootPath)

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

importerFunction.importModule('puzzle_substance_designer.thumbnail_rendering.controller.controller')
