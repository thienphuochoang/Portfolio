import os
import json
import sys
try:
	currentFilePath = os.path.dirname(os.path.abspath(__file__))
except:
	currentFilePath = os.path.dirname(os.path.abspath(sys.argv[0]).replace('app', ''))

currentFilePath = currentFilePath.replace("\\","/")
sys.path.append(currentFilePath)
mayaMenuItems = "/".join(currentFilePath.split("/")[:-1]) + "/launch/" + "MayaSystemItems.json"
#mayaMenuItems = currentFilePath + "/" + "MayaSystemItems.json"
mainMenuName = "HTP_Tools"
iconPath = "/".join((currentFilePath.split("/"))[:-1]) + "/"

import maya.cmds as cmds
import maya.mel as mel
class mainMenuUI():
	def __init__(self):
		"""
		Create drop down menu in Maya
		"""
		mainWindow = mel.eval('global string $gMainWindow; $temp = $gMainWindow')
		if cmds.menu(mainMenuName, q = True, exists = True):
			cmds.deleteUI(mainMenuName, menu = True)
		self.mainMenu = cmds.menu(mainMenuName, l = mainMenuName, parent = mainWindow, tearOff= True)
		with open(mayaMenuItems) as menuItemDatabase:
			self.data = json.load(menuItemDatabase)
			for data in self.data:
				#print (data)
				imagePath = iconPath + data["icon"]
				command = data["command"]
				if data["subItem"]:
					subMenuItem = mainMenuItem(self.mainMenu, data["name"], imagePath, command, True)
					for eachSubItem in data["subItem"]:
						#cmds.menuItem(label = "ahihi")
						#print data["Name"]
						#print (eachSubItem)
						#cmds.menuItem(l = eachSubItem["name"], parent = subMenuItem, subMenu = False)
						#print (eachSubItem["name"])
						subitemImagePath = iconPath + eachSubItem["icon"]
						subitem = mainMenuItem(subMenuItem, eachSubItem["name"], subitemImagePath, eachSubItem["command"], False)
					cmds.setParent( '..', menu=True )
				else:
					item = mainMenuItem(self.mainMenu, data["name"], imagePath, command, False)
		
class mainMenuItem():
	def __init__(self, mainMenu, menuItemName, imagePath, commandExecution, subMenuFlag):
		#self.menuItem = cmds.menuItem
		self.mainMenu = mainMenu
		#print (self.mainMenu)
		self.itemName = menuItemName
		self.imagePath = imagePath
		self.command = commandExecution
		self.subMenuFlag = subMenuFlag
		#print (self.command)
		if subMenuFlag == False:
			try:
				self.item = cmds.menuItem(l = self.itemName, parent = self.mainMenu, image = self.imagePath, command = self.command, subMenu = self.subMenuFlag)
			except:
				self.item = cmds.menuItem(l = self.itemName, image = self.imagePath, command = self.command, subMenu = self.subMenuFlag)
		else:
			self.item = cmds.menuItem(l = self.itemName, image = self.imagePath, command = self.command, subMenu = self.subMenuFlag)
		
		
def main():
	menuCreation = mainMenuUI()
	print ("Load Maya Tools SUCCESSFULLY: " + currentFilePath)