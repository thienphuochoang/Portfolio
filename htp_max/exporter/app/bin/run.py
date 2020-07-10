import sys
import importlib
try:
	import current_working_directory
	reload(current_working_directory)
	path_project, name_project = current_working_directory.get_cwd()
except:
	path_project = r"\\glassegg.com\TOOLS\TECHNICAL_SCRIPT\Projects"
	name_project = "Environment_Default"

sys.path.append(path_project)

def importStringModule(item):
	nameModule = importlib.import_module(item)
	reload(nameModule)
	return nameModule
	


evn_exporterPath = r"{}.Max.exporter.app.bin.main".format(name_project)
evn_exporter = importStringModule(evn_exporterPath)