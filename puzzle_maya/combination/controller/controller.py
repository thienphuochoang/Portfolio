import importlib
def import_file(str_module):
	"""import a module from string"""
	nameModule = importlib.import_module(str_module)
	try:
		reload(nameModule)
	except:
		importlib.reload(nameModule)
	return nameModule
	
#import Function____________________
flatten_combine_function = import_file("puzzle_maya.combination.function.flatten_combine_function")

#execute function
def main():
	flattenCombineFunctionInstance = flatten_combine_function.FlattenCombineFunction()
	flattenCombineFunctionInstance.flattenCombine()

main()