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
flatten_combine_function = importerFunction.importModule('puzzle_maya.combination.function.flatten_combine_function')

#execute function
def main():
	flattenCombineFunctionInstance = flatten_combine_function.FlattenCombineFunction()
	flattenCombineFunctionInstance.flattenCombine()

main()