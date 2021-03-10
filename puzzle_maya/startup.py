import os
import json
import sys


currentFilePath = os.path.dirname(os.path.abspath(__file__))
# except:
# 	currentFilePath = os.path.dirname(os.path.abspath(sys.argv[0]).replace('app', ''))
global puzzleRootPath
currentFilePath = currentFilePath.replace("\\","/")
puzzleRootPath = "/".join(currentFilePath.split("/")[:-1])
sys.path.append(puzzleRootPath)
mayaMenuItems = puzzleRootPath + "/launch/" + "MayaSystemItems.json"
mainMenuName = "PUZZLE_Tools"
iconPath = puzzleRootPath + "/"



import maya.cmds as cmds
import maya.mel as mel

class shelf_button():
	def __init__(self, shelfName, label, icon, command, description):
		self.shelfName = shelfName
		self.label = label
		self.icon = icon
		self.command = command
		self.labelBackground = (0, 0, 0, 0)
		self.labelColour = (.9, .9, .9)
		self.description = description

		cmds.setParent(self.shelfName)
		if (self.icon != "") and os.path.isfile(self.icon) == True:
			cmds.shelfButton(width=34, height=34, image=self.icon, l=label, command=command, imageOverlayLabel=label, olb=self.labelBackground, olc=self.labelColour, annotation=self.description, style = "iconOnly")
		else:
			self.icon = iconPath + "lib" + "/" + "icon" + "/" + "default_script.png"
			cmds.shelfButton(width=34, height=34, image=self.icon, l=label, command=command, imageOverlayLabel=label, olb=self.labelBackground, olc=self.labelColour, annotation=self.description, style = "iconOnly")
		#elif self.icon == "":
			#self.icon = "commandButton.png"
			#cmds.shelfButton(width=37, height=37, image=self.icon, l=label, command=command, imageOverlayLabel=label, olb=self.labelBackground, olc=self.labelColour, annotation=self.description)

class shelf():
	'''A simple class to build shelves in maya. Since the build method is empty,
	it should be extended by the derived class to build the necessary shelf elements.
	By default it creates an empty shelf called "customShelf".'''

	def __init__(self, name=mainMenuName):
		self.name = name

		self.cleanOldShelf()
		cmds.setParent(self.name)
		self.build()

	def build(self):
		'''This method should be overwritten in derived classes to actually build the shelf
		elements. Otherwise, nothing is added to the shelf.'''
		pass

	def addButon(self, label, icon, command, description):
		'''Adds a shelf button with the specified label, command and image.'''
		shelfButton = shelf_button(self.name, label, icon, command, description)

	def cleanOldShelf(self):
		'''Checks if the shelf exists and empties it if it does or creates it if it does not.'''
		if cmds.shelfLayout(self.name, ex=1):
			if cmds.shelfLayout(self.name, q=1, ca=1):
				for each in cmds.shelfLayout(self.name, q=1, ca=1):
					cmds.deleteUI(each)
		else:
			cmds.shelfLayout(self.name, p="ShelfLayout")

class puzzleShelf(shelf):
	def build(self):
		with open(mayaMenuItems) as menuItemDatabase:
			self.data = json.load(menuItemDatabase)
			for data in self.data:
				name = data["name"]
				description = data["description"]
				command = data["command"]
				icon = iconPath + data["icon"]
				if os.path.isfile(icon) == True:
					self.addButon(label = name, icon = icon, command = command, description = description)
				else:
					self.addButon(label = name, icon = "", command = command, description = description)


def main():
	shelfCreation = puzzleShelf()
	print ("Load Maya Tools SUCCESSFULLY: " + currentFilePath)