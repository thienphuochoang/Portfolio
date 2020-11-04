import os
import json
import sys
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
global puzzleRootPath
puzzleRootPath = "/".join(currentFilePath.split("/")[:-1])
sys.path.append(puzzleRootPath)
maxMenuItems = puzzleRootPath + "/launch/" + "MaxSystemItems.json"
mainMenuName = "PUZZLE_Tools"


import pymxs
rt = pymxs.runtime
rt.puzzleRootPath = puzzleRootPath
#defaultUserMacroFolder = r"C:\Users\PhuocHoang\AppData\Local\Autodesk\3dsMax\2021 - 64bit\ENU\usermacros"
def setToOldUserMacroFolder():
	maxEnuFolder = rt.getDir(rt.Name("maxData"))
	maxEnuFolder = maxEnuFolder.replace("\\","/")

	defaultUserIconFolder = maxEnuFolder + "usericons"
	rt.setDir(rt.Name("usericons"), defaultUserIconFolder)
	
	defaultUserMacroFolder = maxEnuFolder + "usermacros"
	rt.setDir(rt.Name("usermacros"), defaultUserMacroFolder)

class mainMenuUI():
	def __init__(self):
		"""
		Create drop down menu in Max
		"""
		
		#Change user macroscript folder path
		self.changeUserMacroScript()

		#Change user icon folder path
		self.changeUserIconDirectory()

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
				numberOfActionItems = value["subItem"]
				if len(numberOfActionItems) > 0:
					menuItem = subMenuItem(self.htpMenu, macro_text)
					appendSubMenu = menuItem.appendSubMenuToHTPMenu()
					for action in numberOfActionItems:
						actionCommand = action["command"]
						actionMacro_name = action["macro_name"]
						actionMacro_tooltip = action["macro_tooltip"]
						actionMacro_text = action["macro_text"]
						actionItem = subMenuAction(appendSubMenu, actionMacro_name, actionMacro_tooltip, actionMacro_text, actionCommand)
				else:
					actionItem = subMenuAction(self.htpMenu, macro_name, macro_tooltip, macro_text, command)


		rt.menuMan.updateMenuBar()
		rt.callbacks.addScript(rt.Name("postSystemShutdown"), "python.execute(\"setToOldUserMacroFolder()\")")

	def changeUserMacroScript(self):
		'''
		Change macro script directory
		'''
		self.oldCurrentUserMacroFolder = rt.getDir(rt.Name("usermacros"))
		self.newUserMacroScriptFolder = self.oldCurrentUserMacroFolder.replace("\\","/")
		self.newUserMacroScriptFolder = "/".join(self.newUserMacroScriptFolder.split("/")[:-1])
		self.newUserMacroScriptFolder = self.newUserMacroScriptFolder + "/" + "PUZZLE_Tools_usermacros"
		if not os.path.isdir(self.newUserMacroScriptFolder):
			os.mkdir(self.newUserMacroScriptFolder)
		rt.setDir(rt.Name("usermacros"), self.newUserMacroScriptFolder)

	def changeUserIconDirectory(self):
		'''
		Change user icon directory
		'''
		self.oldCurrentUserIconFolder = rt.getDir(rt.Name("usericons"))
		self.newUserIconFolder = self.oldCurrentUserIconFolder.replace("\\","/")
		self.newUserIconFolder = puzzleRootPath + "/" + "lib/icon"
		if not os.path.isdir(self.newUserIconFolder):
			os.mkdir(self.newUserIconFolder)
		rt.setDir(rt.Name("usericons"), self.newUserIconFolder)
		
class subMenuItem():
	def __init__(self, htpMenu, macroText):
		self.htpMenu = htpMenu
		self.macroscript_text = macroText

	def appendSubMenuToHTPMenu(self):
		self.menu = rt.menuMan.createMenu(self.macroscript_text)
		self.subMenu = rt.menuMan.createSubMenuItem(self.macroscript_text, self.menu)
		self.htpMenu.addItem(self.subMenu, -1)
		return self.menu

class subMenuAction():
	def __init__(self, parentMenu, macroName, macroTooltip, macroText, commandExecution):
		self.commandExecution = commandExecution

		self.checkFileMaxScriptOrPython()

		self.macroscript_name = macroName
		self.macroscript_category = mainMenuName
		self.macroscript_tooltip = macroTooltip
		self.macroscript_text = macroText
		self.macroscript_content = self.commandExecution
		self.parentMenu = parentMenu

		self.macro_id = rt.macros.new(self.macroscript_category, self.macroscript_name, self.macroscript_tooltip, self.macroscript_text, self.macroscript_content)
		self.menu_item = rt.menuMan.createActionItem(self.macroscript_name, self.macroscript_category)
		parentMenu.addItem(self.menu_item, -1)

	def checkFileMaxScriptOrPython(self):
		if self.commandExecution:
			checkMaxscriptFlag = self.commandExecution.endswith(".ms")
			if checkMaxscriptFlag == True:
				self.commandExecution = 'filein' + '("'+puzzleRootPath+ "/" + self.commandExecution + '")'
			else:
				self.commandExecution = repr(self.commandExecution)
				self.commandExecution = self.commandExecution.replace("'","\"")
				self.commandExecution = 'python.execute ' + self.commandExecution
		
def main():
	menuCreation = mainMenuUI()
	print ("Load Max Tools SUCCESSFULLY: " + puzzleRootPath)
	print ("Global root path variable: puzzleRootPath")
main()