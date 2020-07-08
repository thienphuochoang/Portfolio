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
class mainMenuUI():
	def __init__(self):
		"""
		Create drop down menu in Max
		"""
		#theMainMenu = menuMan.getMainMenuBar() --get the main menu bar
		#theMenu = menuMan.createMenu "Forum Help" --create a menu called Forum Help
		#theSubMenu = menuMan.createSubMenuItem "Forum Help" theMenu --create a SubMenuItem
		#theMainMenu.addItem theSubMenu (theMainMenu.numItems()+1) --add the SubMenu to the Main Menu
		#theAction = menuMan.createActionItem "PutMeOnAMenu" "Forum Help" --create an ActionItem from the MacroScript
		#theMenu.addItem theAction (theMenu.numItems()+1) --add the ActionItem to the menu
		#menuMan.updateMenuBar() --update the menu bar
		
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
			for key, value in self.data.items():
				command = value["command"]
				macro_name = value["macro_name"]
				macro_tooltip = value["macro_tooltip"]
				macro_text = value["macro_text"]
				print (command)
				actionItem = subMenuItem(self.htpMenu, macro_name, macro_tooltip, macro_text, command)
				#actionItem = rt.menuMan.createActionItem("Bend", "Modifiers")
				#self.mainMenuBar.addItem(actionItem, index)

		rt.menuMan.updateMenuBar()
				#rt.menuMan.createActionItem("Bend", "Modifiers")

		# sub = rt.menuMan.createMenu("Apply Modifier")
		# a = rt.menuMan.createActionItem("Bend", "Modifiers")
		# sub.addItem(a, -1)
		# b = rt.menuMan.createActionItem("Taper", "Modifiers")
		# sub.addItem(b, -1)
		# item = rt.menuMan.createSubMenuItem("Apply Modifier", sub)
		# menu.addItem(item, -1)
		# mitem = rt.menuMan.createSubMenuItem(mainMenuName, menu)
		# index = mainMenuBar.numItems()
		# mainMenuBar.addItem(mitem, index)
		# rt.menuMan.updateMenuBar()
		'''

		(
		menu = menuMan.createMenu "Custom Tools"
		sub = menuMan.createMenu "Apply Modifier"
		test = menuMan.createMenu "test"
		a = menuMan.createActionItem "Bend" "Modifiers"
		sub.addItem a -1
		b = menuMan.createActionItem "Taper" "Modifiers"
		sub.addItem b -1
		item = menuMan.createSubMenuItem "Apply Modifier" sub
		item2 = menuMan.createSubMenuItem "test" test
		menu.addItem item -1
		menu.addItem item2 -1
		mitem = menuMan.createSubMenuItem "Custom Tools" menu
		index = mainMenuBar.numItems() -- add before last (usualy it's "Help")
		mainMenuBar.addItem mitem index
		menuMan.updateMenuBar()
		)


		mainWindow = mel.eval('global string $gMainWindow; $temp = $gMainWindow')
		if cmds.menu(mainMenuName, q = True, exists = True):
			cmds.deleteUI(mainMenuName, menu = True)
		self.mainMenu = cmds.menu(mainMenuName, l = mainMenuName, parent = mainWindow, tearOff= True)
		with open(mayaMenuItems) as menuItemDatabase:
			self.data = json.load(menuItemDatabase)
			for key, value in self.data.iteritems():
				imagePath = iconPath + value["icon"]
				command = value["command"]
				if value["subItem"]:
					item = mainMenuItem(self.mainMenu, key, imagePath, command, True)
				else:
					item = mainMenuItem(self.mainMenu, key, imagePath, command, False)
		'''
		
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