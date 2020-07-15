import os
import json
import sys
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
currentFilePath = "/".join(currentFilePath.split("/")[:-1])
sys.path.append(currentFilePath)
maxMenuItems = currentFilePath + "/launch/" + "MaxSystemItems.json"
mainMenuName = "HTP_Tools"


import pymxs
rt = pymxs.runtime
#defaultUserMacroFolder = r"C:\Users\PhuocHoang\AppData\Local\Autodesk\3dsMax\2021 - 64bit\ENU\usermacros"
def setToOldUserMacroFolder():
	maxEnuFolder = rt.getDir(rt.Name("maxData"))
	maxEnuFolder = maxEnuFolder.replace("\\","/")
	defaultUserMacroFolder = maxEnuFolder + "usermacros"
	rt.setDir(rt.Name("usermacros"), defaultUserMacroFolder)

class mainMenuUI():
	def __init__(self):
		"""
		Create drop down menu in Max
		"""
		
		#Change user macroscript folder path
		self.changeUserMacroScript()

		#Remove old menu
		self.htpMenu = rt.menuMan.findMenu(mainMenuName)
		if self.htpMenu != rt.undefined:
			rt.menuMan.unRegisterMenu(self.htpMenu)
			rt.menuMan.updateMenuBar()

		#Create htp_tools menu
		self.htpMenu = rt.menuMan.createMenu(mainMenuName)

		#Get main menu
		self.mainMenuBar = rt.menuMan.getMainMenuBar()
		index = self.mainMenuBar.numItems() + 1
		mitem = rt.menuMan.createSubMenuItem(mainMenuName, self.htpMenu)
		self.mainMenuBar.addItem(mitem, index)

		


		with open(maxMenuItems) as menuItemDatabase:
			self.data = json.load(menuItemDatabase)
			for value in self.data:
				command = value["command"]
				macro_name = value["macro_name"]
				macro_tooltip = value["macro_tooltip"]
				macro_text = value["macro_text"]
				actionItem = subMenuItem(self.htpMenu, macro_name, macro_tooltip, macro_text, command)


		rt.menuMan.updateMenuBar()
		rt.callbacks.addScript(rt.Name("postSystemShutdown"), "python.execute(\"setToOldUserMacroFolder()\")")
		#print (defaultUserMacroFolder)

	def changeUserMacroScript(self):
		self.oldCurrentUserMacroFolder = rt.getDir(rt.Name("usermacros"))
		self.newUserMacroScriptFolder = self.oldCurrentUserMacroFolder.replace("\\","/")
		self.newUserMacroScriptFolder = "/".join(self.newUserMacroScriptFolder.split("/")[:-1])
		self.newUserMacroScriptFolder = self.newUserMacroScriptFolder + "/" + "HTP_Tools_usermacros"
		if not os.path.isdir(self.newUserMacroScriptFolder):
			os.mkdir(self.newUserMacroScriptFolder)
		rt.setDir(rt.Name("usermacros"), self.newUserMacroScriptFolder)
		
class subMenuItem():
	def __init__(self, htpMenu, macroName, macroTooltip, macroText, commandExecution):
		self.commandExecution = commandExecution

		self.checkFileMaxScriptOrPython()

		self.macroscript_name = macroName
		self.macroscript_category = mainMenuName
		self.macroscript_tooltip = macroTooltip
		self.macroscript_text = macroText
		self.macroscript_content = self.commandExecution



		self.macro_id = rt.macros.new(self.macroscript_category, self.macroscript_name, self.macroscript_tooltip, self.macroscript_text, self.macroscript_content)
		self.menu_item = rt.menuMan.createActionItem(self.macroscript_name, self.macroscript_category)
		htpMenu.addItem(self.menu_item, (htpMenu.numItems()+1))

	def checkFileMaxScriptOrPython(self):
		checkFlag = self.commandExecution.endswith(".ms")
		if checkFlag == True:
			self.commandExecution = 'filein' + '("'+currentFilePath+ "/" + self.commandExecution + '")'
		else:
			self.commandExecution = repr(self.commandExecution)
			self.commandExecution = self.commandExecution.replace("'","\"")
			self.commandExecution = 'python.execute ' + self.commandExecution
		
def main():
	menuCreation = mainMenuUI()
	print ("Load Max Tools SUCCESSFULLY: " + currentFilePath)
main()