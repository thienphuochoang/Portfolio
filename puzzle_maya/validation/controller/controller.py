import sys
import os
import importlib
import json
import inspect
import PySide2
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import QFile, QObject, QSize
from PySide2.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QPushButton, QStyleFactory, QMessageBox
from PySide2.QtGui import QIcon
from shiboken2 import wrapInstance 

import maya.OpenMayaUI as omui
import maya.mel as mel
import maya.cmds as cmds

mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)  # create a maya Main window
	
def import_file(str_module):
	"""import a module from string"""
	nameModule = importlib.import_module(str_module)
	try:
		reload(nameModule)
	except:
		importlib.reload(nameModule)
	return nameModule
	
currentFilePath = os.path.dirname(os.path.abspath(__file__))
currentFilePath = currentFilePath.replace("\\","/")
rootDirectory = "/".join((currentFilePath.split("/")[:-3]))

#import Function____________________
ui_file = import_file(r"lib.ui.Validation_MainUI")
itemCheck_uiFile = import_file(r"lib.ui.Validation_ItemCheck")
addons_uiFile = import_file(r"lib.ui.Validation_Addons")
fm = import_file(r"puzzle_maya.validation.function.validate_function")
iconPath = rootDirectory + "/" + "lib" + "/" + "icon"
presetPath = rootDirectory + "/" + "puzzle_maya" + "/" + "validation" + "/" + "preset"
collapsiblePath = rootDirectory + "/" + "puzzle_maya" + "/" + "validation" + "/" + "function"

wrapperDict = {}

class AddonsWindow(QtWidgets.QMainWindow, addons_uiFile.Ui_MainWindow):
	def __init__(self):
		super(AddonsWindow, self).__init__(parent = None)
		self.setupUi(self)

		self.AddonsWindowFunction = fm.AddonsWindowFunction()
		
	def setVisibility(self, v):
		self.AddonsWindowFunction.setVisibility(v, self.centralwidget)
	
	def setDefault(self):
		self.AddonsWindowFunction.setDefault(self.listWidget)

class ItemCheckWindow(QtWidgets.QMainWindow, itemCheck_uiFile.Ui_MainWindow):
	def __init__(self, file):
		super(ItemCheckWindow, self).__init__(parent = None)
		self.setupUi(self)

		#Set Default Icon and Text for Item Check Window
		self.setIconForButtons()
		self.setLabelText(file)
	
		self.ItemCheckWindowFunction = fm.ItemCheckWindowFunction()


		

	def setIconForButtons(self):
		self.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
		self.btnCollapse.setIconSize(QSize(20,20))
		self.btnCollapse.setCheckable(True)
		self.btnStatus.setIcon(QIcon(iconPath + "\\checkIconOn.png"))
		self.btnStatus.setIconSize(QSize(18, 18))
		self.btnStatus.setCheckable(True)
		self.btnDoc.setIcon(QIcon(iconPath + "\\openDoc.png"))
		self.btnDoc.setIconSize(QSize(20,20))
		self.btnFix.setIcon(QIcon(iconPath + "\\fix_icon.png"))
		self.btnFix.setIconSize(QSize(35,35))
		self.btnMaximize.setIcon(QIcon(iconPath + "\\minimizedIcon.png"))
		self.btnMaximize.setIconSize(QSize(18,18))

	def setLabelText(self, file):
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "/" + projectName) == False:
				pass
			else:
				for n in os.listdir(collapsiblePath + "/" + projectName):
					functionPath = collapsiblePath + "/" + projectName
					try:                        
						f = open(functionPath + "/" + file,"r")
						lines = f.read().splitlines()
						for line in lines:
							if "functiondescription" in line.lower():
								str_list = line.split("\"")
								str_list = filter(None, str_list)
								for i in str_list:
									if "functiondescription" not in i.lower():
										self.label.setText(" " + i)
								break
					except:
						pass

	def setAutoFixStatusIcon(self, file):
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "/" + projectName) == False:
				pass
			else:
				for i in os.listdir(collapsiblePath + "/" + projectName):
					functionPath = collapsiblePath + "/" + projectName
					try:
						f = import_file("puzzle_maya.validation.function" + "." + projectName + "." + file.split(".")[0])
						if (hasattr(f, 'fix') and inspect.isfunction(f.fix)):
							self.btnFix.setEnabled(True)
						else:
							self.btnFix.setEnabled(False)
						# f = open(functionPath + "/" + file,"r")
						# lines = f.read().splitlines()
						# flag = False
						# for line in lines:
						# 	if "def fix" in line.lower():
						# 		self.btnFix.setEnabled(True)
						# 		flag = True
						# 	else:
						# 		continue
						# if flag == False:
						# 	self.btnFix.setEnabled(False)
					
					except:
						pass
						
	def setAutoOpenDocStatusIcon(self, file):
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "/" + projectName) == False:
				pass
			else:
				for i in os.listdir(collapsiblePath + "/" + projectName):
					functionPath = collapsiblePath + "/" + projectName
					try:
						f = import_file("puzzle_maya.validation.function" + "." + projectName + "." + file.split(".")[0])
						if (hasattr(f, 'doc') and inspect.isfunction(f.doc)):
							self.btnDoc.setEnabled(True)
						else:
							self.btnDoc.setEnabled(False)
						# f = open(functionPath + "\\" + file,"r")
						# lines = f.read().splitlines()
						# flag = False
						# for line in lines:
						# 	if "def doc" in line.lower():
						# 		self.btnDoc.setEnabled(True)
						# 		flag = True
						# 	else:
						# 		continue
						# if flag == False:
						# 	self.btnDoc.setEnabled(False)
					except:
						pass
			
	def setVisibility(self, v):
		self.ItemCheckWindowFunction.setVisibility(v, self.centralwidget, self.btnCollapse, iconPath)

	def setDefault(self):
		self.ItemCheckWindowFunction.setDefault(self.btnCollapse, iconPath)
		
	def setDisplayAddonsWindow(self):
		self.ItemCheckWindowFunction.setDisplayAddonsWindow(self.btnCollapse, iconPath)

	def setCheckUncheckButton(self, v):
		self.ItemCheckWindowFunction.setCheckUncheckButton(self.btnStatus, v)

class ItemCheckAndAddonsWrapper():
	def __init__(self, i, scrollLayout):
		self.errorDict = {}
		self.nonErrorDict = {}

		#Load ItemCheckAndAddonsWrapper function
		self.ItemCheckAndAddonsWrapperFunction = fm.ItemCheckAndAddonsWrapperFunction()

		#Create new Item Check and new Addons windows
		self.newItemCheckWidget = ItemCheckWindow(i)
		self.newAddonsWindowWidget = AddonsWindow()
		self.createLayoutSettings(scrollLayout)

		#Import module check function
		self.item = i.split(".py")[0]
		self.importFileFunction()

		self.connectUI()
		self.newItemCheckWidget.setAutoFixStatusIcon(i)
		self.newItemCheckWidget.setAutoOpenDocStatusIcon(i)

	def createLayoutSettings(self, scrollLayout):
		scrollLayout.addWidget(self.newItemCheckWidget.centralwidget)
		scrollLayout.addWidget(self.newAddonsWindowWidget.centralwidget)
		self.newAddonsWindowWidget.centralwidget.setVisible(False)

	def importFileFunction(self):
		self.moduleCheck = self.ItemCheckAndAddonsWrapperFunction.importFileFunction(self.item, collapsiblePath)

	
	def getSelectedListWidgetItem(self, moduleCheck, listWidget, errorDict, nonErrorDict):
		self.ItemCheckAndAddonsWrapperFunction.getSelectedListWidgetItem(moduleCheck, listWidget, errorDict, nonErrorDict)
	
	def openDoc(self):
		self.ItemCheckAndAddonsWrapperFunction.openDoc(self.moduleCheck)

	
	def showHideAddonsUI(self, widget, btnCollapse, iconPath):
		self.ItemCheckAndAddonsWrapperFunction.showHideAddonsUI(widget, btnCollapse, iconPath)

	def setOnOffCheckButton(self, btnStatus, iconPath):
		self.ItemCheckAndAddonsWrapperFunction.setOnOffCheckButton(btnStatus, iconPath)
			
	def showErrorToListWidget(self, item, listWidget, errorDict, iconPath):
		self.ItemCheckAndAddonsWrapperFunction.showErrorToListWidget(item, listWidget, errorDict, iconPath)
		
	def showInfoToListWidget(self, item, listWidget, nonErrorDict, iconPath):
		self.ItemCheckAndAddonsWrapperFunction.showInfoToListWidget(item, listWidget, nonErrorDict, iconPath)
		
	def connectUI(self):
		self.newItemCheckWidget.label.clicked.connect(lambda: self.do(self.moduleCheck, self.errorDict, self.nonErrorDict, self.newAddonsWindowWidget.listWidget, self.newItemCheckWidget.btnResult, iconPath))
		self.newItemCheckWidget.btnCollapse.clicked.connect(lambda: self.showHideAddonsUI(self.newAddonsWindowWidget.centralwidget, self.newItemCheckWidget.btnCollapse, iconPath))
		self.newItemCheckWidget.btnStatus.clicked.connect(lambda: self.setOnOffCheckButton(self.newItemCheckWidget.btnStatus, iconPath))
		self.newAddonsWindowWidget.btnError.clicked.connect(lambda: self.showErrorToListWidget(self.item, self.newAddonsWindowWidget.listWidget, self.errorDict, iconPath))
		self.newAddonsWindowWidget.btnInfo.clicked.connect(lambda: self.showInfoToListWidget(self.item, self.newAddonsWindowWidget.listWidget, self.nonErrorDict, iconPath))
		self.newAddonsWindowWidget.listWidget.itemSelectionChanged.connect(lambda: self.getSelectedListWidgetItem(self.moduleCheck, self.newAddonsWindowWidget.listWidget, self.errorDict, self.nonErrorDict))
		self.newAddonsWindowWidget.listWidget.itemClicked.connect(lambda: self.getSelectedListWidgetItem(self.moduleCheck, self.newAddonsWindowWidget.listWidget, self.errorDict, self.nonErrorDict))
		self.newAddonsWindowWidget.listWidget.itemDoubleClicked.connect(lambda: self.selectSimilarity(self.moduleCheck))
		self.newItemCheckWidget.btnFix.clicked.connect(lambda: self.autoFix())
		self.newItemCheckWidget.btnDoc.clicked.connect(lambda: self.openDoc())
		self.newItemCheckWidget.btnMaximize.clicked.connect(lambda: self.maximizeWindow())



	def autoFix(self):
		self.ItemCheckAndAddonsWrapperFunction.autoFix(self.moduleCheck, self.newAddonsWindowWidget.listWidget, self.newItemCheckWidget.btnResult, self.errorDict)
	
	def do(self, moduleCheck, errorDict, nonErrorDict, listWidget, btnResult, iconPath):
		self.errorDict, self.nonErrorDict = self.ItemCheckAndAddonsWrapperFunction.do(moduleCheck, errorDict, nonErrorDict, listWidget, btnResult, iconPath)

	def selectSimilarity(self, moduleCheck):
		self.ItemCheckAndAddonsWrapperFunction.selectSimilarity(moduleCheck)

	def setWrapperVisibility(self, v):
		self.newAddonsWindowWidget.setVisibility(False)
		self.newItemCheckWidget.setVisibility(v)
		
	def maximizeWindow(self):
		self.ItemCheckAndAddonsWrapperFunction.maximizeWindow(self.newAddonsWindowWidget, self.newItemCheckWidget, wrapperDict, iconPath)


class CollapsibleButton():
	def __init__(self, scrollLayout, projectName):
		self.childList = []

		#Create collapsible function
		self.createCollapsibleButton(scrollLayout, projectName)
		self.CollapsibleButtonFunction = fm.CollapsibleButtonFunction()

		#Add collapsible function
		self.collapsibleButton.clicked.connect(lambda: self.CollapsibleButtonFunction.collapseWidget(self.collapsibleButton, self.childList))

	def createCollapsibleButton(self, scrollLayout, projectName):
		self.collapsibleButton = QPushButton("<<< " + projectName + " >>>")
		self.collapsibleButton.setCheckable(True)
		self.collapsibleButton.setChecked(True)
		self.collapsibleButton.setStyle(QStyleFactory.create("Fusion"))
		scrollLayout.addWidget(self.collapsibleButton)
		
	def addChild(self, child):
		self.childList.append(child)

class MenuPreset():
	def __init__(self):
		self.MenuPresetFunction = fm.MenuPresetFunction()
	

	def showPresetFile(self, mainWindow):
		presetFileList = self.MenuPresetFunction.checkFileJsonExistance(presetPath)
		if presetFileList:
			for presetFile in presetFileList:
				newAction = MenuAction()
				newAction.createNewAction(presetFile, mainWindow.menuPreset)

class MenuAction():
	def __init__(self):
		self.MenuActionFunction = fm.MenuActionFunction()

	def createNewAction(self, presetFile, menuPreset):
		self.action = menuPreset.addAction(presetFile.split(".json")[0])
		self.action.setData(presetFile)
		self.action.triggered.connect(lambda: self.loadPreset())

	def loadPreset(self):
		self.MenuActionFunction.setButtonStatusThroughFileJson(self.action.data(), wrapperDict, presetPath, iconPath)
	
	def connectUI(self, mainWindow):
		mainWindow.actionOpen_Preset_Folder.triggered.connect(lambda: self.MenuActionFunction.openPresetFolder(presetPath))
		mainWindow.actionAdd_And_Save_Preset.triggered.connect(lambda: self.MenuActionFunction.createAndSavePreset(presetPath, wrapperDict))


class MainValidationWindow(QtWidgets.QMainWindow, ui_file.Ui_MainWindowValidation):
	def __init__(self):
		super(MainValidationWindow, self).__init__(parent=mayaMainWindow)
		#Load UI
		self.setupUi(self)

		self.MainWindowFunction = fm.MainWindowFunction()
		#Create, edit other sub widgets
		self.changeLabelTitle()
		self.createWidgetAndAddCollapsibleButtonAndAddAddons()
		self.setButtonStyle()



		#Menu Preset show Preset in Preset Folder
		self.menuBar = MenuPreset()
		self.menuBar.showPresetFile(self)
		
		#Menu Action execute action script
		self.menuAction = MenuAction()
		self.menuAction.connectUI(self)

		
		
		self.connectUI()
		#self.window.btnSwapCheckUncheckAll.clicked.connect(lambda: self.CheckUncheckAll())
		#self.window.btnUncollapseAll.clicked.connect(lambda: self.collapseUncollapseAllWidget())
		#self.window.btnUncollapseAll.setChecked(False)

	def createWidgetAndAddCollapsibleButtonAndAddAddons(self):
		scrollAreaWidgetContents = QWidget(self.scrollArea) #Tao 1 QWidget va xet scrollArea lam parent cua no
		scrollLayout = QVBoxLayout(scrollAreaWidgetContents) #Tao 1 QVBoxLayout va xet QWidget o tren lam parent cua no
		self.scrollArea.setWidget(scrollAreaWidgetContents) #Xet scrollAreaWidgetContents lam widget cua scrollArea
		
		verticalSpacer = QtWidgets.QSpacerItem(17, 700, QSizePolicy.Preferred, QSizePolicy.Preferred)
		horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
		
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "/" + projectName) == False:
				pass
			else:
				newCollapsibleButton = CollapsibleButton(scrollLayout, projectName)
				#newCollapsibleButton.createCollapsibleButton(scrollLayout, projectName)
				for i in os.listdir(collapsiblePath + "/" + projectName):
					if "__init__" not in i and ".pyc" not in i and (os.path.isdir(collapsiblePath + "/" + projectName + "/" + i) == False):
						newItemCheckAndAddonsWrapper = ItemCheckAndAddonsWrapper(i, scrollLayout)
						newCollapsibleButton.addChild(newItemCheckAndAddonsWrapper)
						wrapperDict[i.split(".py")[0]] = newItemCheckAndAddonsWrapper
					else:
						pass
								
		scrollLayout.addItem(verticalSpacer) 
		scrollLayout.addItem(horizontalSpacer)

	def setButtonStyle(self):
		self.btnSwapCheckUncheckAll.setStyle(QStyleFactory.create("Fusion"))
		self.btnValidate.setStyle(QStyleFactory.create("Fusion"))
		self.btnUncollapseAll.setStyle(QStyleFactory.create("Fusion"))


	# def attachWindowToSoftware(self):
	# 	try:
	# 		MaxPlus.AttachQWidgetToMax(self.window)
	# 	except:
	# 		self.window.setParent(mayaMainWindow)
	# 		self.window.setWindowFlags(QtCore.Qt.Window)

	def connectUI(self):
		self.btnValidate.clicked.connect(lambda: self.validateCheckedFunction())
		self.btnSwapCheckUncheckAll.clicked.connect(lambda: self.checkUncheckAll())
		self.btnShowError.clicked.connect(lambda: self.showError())
		#self.window.btnShowInfo.clicked.connect(lambda: self.showInfo())
		self.btnResetAll.clicked.connect(lambda: self.resetAllToDefault())
		self.btnUncollapseAll.clicked.connect(lambda: self.collapseUncollapseAllWidget())

	def showError(self):
		self.MainWindowFunction.showError(wrapperDict, iconPath)
	   
	#def showInfo(self):
		#self.remainingInfoList = self.MainWindowFunction.showInfo(wrapperDict, iconPath)

	def validateCheckedFunction(self):
		self.MainWindowFunction.validateCheckedFunction(wrapperDict, iconPath, self.progressBar, self.lbValidationResult)
	
	def checkUncheckAll(self):
		self.MainWindowFunction.checkUncheckAll(wrapperDict, iconPath)
					  
		
	def changeLabelTitle(self):
		self.lbTitle.setText("Validation")

	def collapseUncollapseAllWidget(self):
		self.MainWindowFunction.collapseUncollapseAllWidget(wrapperDict, iconPath)
		
	def resetAllToDefault(self):
		self.MainWindowFunction.resetAllToDefault(wrapperDict, iconPath, self.progressBar, self.lbValidationResult)
'''


	
#import module function
fmPath = r"{}.{}.validation.app.res.controller".format(name_project, application)
fm = importStringModule(fmPath)


wrapperDict = {}

class AddonsWindow(QObject):
	def __init__(self, addons_uiFile):
		
		#Create Addons window
		AddonsFile = QFile(addons_uiFile)
		AddonsFile.open(QFile.ReadOnly)
		loader = QUiLoader()
		self.window = loader.load(AddonsFile)

		self.AddonsWindowFunction = fm.AddonsWindowFunction()
		
	def setVisibility(self, v):
		self.AddonsWindowFunction.setVisibility(v, self.window.centralwidget)
	
	def setDefault(self):
		self.AddonsWindowFunction.setDefault(self.window.listWidget)


class ItemCheckWindow(QObject):
	def __init__(self, itemCheck_uiFile, file):
		
		#Create Item Check Window
		ItemCheckFile = QFile(itemCheck_uiFile)
		ItemCheckFile.open(QFile.ReadOnly)
		loader = QUiLoader()
		self.window = loader.load(ItemCheckFile)

		#Set Default Icon and Text for Item Check Window
		#self.window.centralwidget.setUpdatesEnabled(True)
		self.setIconForButtons()
		self.setLabelText(file)
	
		self.ItemCheckWindowFunction = fm.ItemCheckWindowFunction()


		

	def setIconForButtons(self):
		self.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
		self.window.btnCollapse.setIconSize(QSize(20,20))
		self.window.btnCollapse.setCheckable(True)
		self.window.btnStatus.setIcon(QIcon(iconPath + "\\checkIconOn.png"))
		self.window.btnStatus.setIconSize(QSize(18, 18))
		self.window.btnStatus.setCheckable(True)
		self.window.btnDoc.setIcon(QIcon(iconPath + "\\openDoc.png"))
		self.window.btnDoc.setIconSize(QSize(20,20))
		self.window.btnFix.setIcon(QIcon(iconPath + "\\settings.png"))
		self.window.btnFix.setIconSize(QSize(35,35))
		self.window.btnMaximize.setIcon(QIcon(iconPath + "\\minimizedIcon.png"))
		self.window.btnMaximize.setIconSize(QSize(18,18))

	def setLabelText(self, file):
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "\\" + projectName) == False:
				pass
			else:
				for n in os.listdir(collapsiblePath + "\\" + projectName):
					functionPath = collapsiblePath + "\\" + projectName
					try:
						f = open(functionPath + "\\" + file,"r")
						lines = f.read().splitlines()
						for line in lines:
							if "functiondescription" in line.lower():
								str_list = line.split("\"")
								str_list = filter(None, str_list)
								for i in str_list:
									if "functiondescription" not in i.lower():
										self.window.label.setText(" " + i)
					except:
						pass

	def setAutoFixStatusIcon(self, file):
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "\\" + projectName) == False:
				pass
			else:
				for i in os.listdir(collapsiblePath + "\\" + projectName):
					functionPath = collapsiblePath + "\\" + projectName
					try:
						f = open(functionPath + "\\" + file,"r")
						lines = f.read().splitlines()
						flag = False
						for line in lines:
							if "def fix" in line.lower():
								self.window.btnFix.setEnabled(True)
								flag = True
							else:
								continue
						if flag == False:
							self.window.btnFix.setEnabled(False)
					except:
						pass
						
	def setAutoOpenDocStatusIcon(self, file):
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "\\" + projectName) == False:
				pass
			else:
				for i in os.listdir(collapsiblePath + "\\" + projectName):
					functionPath = collapsiblePath + "\\" + projectName
					try:
						f = open(functionPath + "\\" + file,"r")
						lines = f.read().splitlines()
						flag = False
						for line in lines:
							if "def doc" in line.lower():
								self.window.btnDoc.setEnabled(True)
								flag = True
							else:
								continue
						if flag == False:
							self.window.btnDoc.setEnabled(False)
					except:
						pass
			
	def setVisibility(self, v):
		self.ItemCheckWindowFunction.setVisibility(v, self.window.centralwidget, self.window.btnCollapse, iconPath)

	def setDefault(self):
		self.ItemCheckWindowFunction.setDefault(self.window.btnCollapse, iconPath)
		
	def setDisplayAddonsWindow(self):
		self.ItemCheckWindowFunction.setDisplayAddonsWindow(self.window.btnCollapse, iconPath)

	def setCheckUncheckButton(self, v):
		self.ItemCheckWindowFunction.setCheckUncheckButton(self.window.btnStatus, v)


class ItemCheckAndAddonsWrapper():
	def __init__(self, i, scrollLayout):
		self.errorDict = {}
		self.nonErrorDict = {}

		#Load ItemCheckAndAddonsWrapper function
		self.ItemCheckAndAddonsWrapperFunction = fm.ItemCheckAndAddonsWrapperFunction()

		#Create new Item Check and new Addons windows
		self.newItemCheckWidget = ItemCheckWindow(itemCheck_uiFile, i)
		self.newAddonsWindowWidget = AddonsWindow(addons_uiFile)

		#Create Default layout settings
		self.createLayoutSettings(scrollLayout)
		
		#Import module check function
		self.item = i.split(".py")[0]
		self.importFileFunction()

		self.connectUI()


		
		self.newItemCheckWidget.setAutoFixStatusIcon(i)
		self.newItemCheckWidget.setAutoOpenDocStatusIcon(i)
		
		#self.newItemCheckWidget.window.label.clicked.connect(self.do)


	def createLayoutSettings(self, scrollLayout):
		scrollLayout.addWidget(self.newItemCheckWidget.window.centralwidget)
		scrollLayout.addWidget(self.newAddonsWindowWidget.window.centralwidget)
		self.newAddonsWindowWidget.window.centralwidget.setVisible(False)

	def importFileFunction(self):
		self.moduleCheck = self.ItemCheckAndAddonsWrapperFunction.importFileFunction(self.item, collapsiblePath)

	
	def getSelectedListWidgetItem(self, moduleCheck, listWidget, errorDict, nonErrorDict):
		self.ItemCheckAndAddonsWrapperFunction.getSelectedListWidgetItem(moduleCheck, listWidget, errorDict, nonErrorDict)
	
	def openDoc(self):
		self.ItemCheckAndAddonsWrapperFunction.openDoc(self.moduleCheck)

	
	def showHideAddonsUI(self, widget, btnCollapse, iconPath):
		self.ItemCheckAndAddonsWrapperFunction.showHideAddonsUI(widget, btnCollapse, iconPath)

	def setOnOffCheckButton(self, btnStatus, iconPath):
		self.ItemCheckAndAddonsWrapperFunction.setOnOffCheckButton(btnStatus, iconPath)
			
	def showErrorToListWidget(self, item, listWidget, errorDict, iconPath):
		self.ItemCheckAndAddonsWrapperFunction.showErrorToListWidget(item, listWidget, errorDict, iconPath)
		
	def showInfoToListWidget(self, item, listWidget, nonErrorDict, iconPath):
		self.ItemCheckAndAddonsWrapperFunction.showInfoToListWidget(item, listWidget, nonErrorDict, iconPath)
		
	def connectUI(self):
		self.newItemCheckWidget.window.label.clicked.connect(lambda: self.do(self.moduleCheck, self.errorDict, self.nonErrorDict, self.newAddonsWindowWidget.window.listWidget, self.newItemCheckWidget.window.btnResult, iconPath))
		self.newItemCheckWidget.window.btnCollapse.clicked.connect(lambda: self.showHideAddonsUI(self.newAddonsWindowWidget.window.centralwidget, self.newItemCheckWidget.window.btnCollapse, iconPath))
		self.newItemCheckWidget.window.btnStatus.clicked.connect(lambda: self.setOnOffCheckButton(self.newItemCheckWidget.window.btnStatus, iconPath))
		self.newAddonsWindowWidget.window.btnError.clicked.connect(lambda: self.showErrorToListWidget(self.item, self.newAddonsWindowWidget.window.listWidget, self.errorDict, iconPath))
		self.newAddonsWindowWidget.window.btnInfo.clicked.connect(lambda: self.showInfoToListWidget(self.item, self.newAddonsWindowWidget.window.listWidget, self.nonErrorDict, iconPath))
		self.newAddonsWindowWidget.window.listWidget.itemSelectionChanged.connect(lambda: self.getSelectedListWidgetItem(self.moduleCheck, self.newAddonsWindowWidget.window.listWidget, self.errorDict, self.nonErrorDict))
		self.newAddonsWindowWidget.window.listWidget.itemClicked.connect(lambda: self.getSelectedListWidgetItem(self.moduleCheck, self.newAddonsWindowWidget.window.listWidget, self.errorDict, self.nonErrorDict))
		self.newAddonsWindowWidget.window.listWidget.itemDoubleClicked.connect(lambda: self.selectSimilarity(self.moduleCheck))
		self.newItemCheckWidget.window.btnFix.clicked.connect(lambda: self.autoFix())
		self.newItemCheckWidget.window.btnDoc.clicked.connect(lambda: self.openDoc())
		self.newItemCheckWidget.window.btnMaximize.clicked.connect(lambda: self.maximizeWindow())



	def autoFix(self):
		self.ItemCheckAndAddonsWrapperFunction.autoFix(self.moduleCheck, self.newAddonsWindowWidget.window.listWidget, self.newItemCheckWidget.window.btnResult, self.errorDict)
	
	def do(self, moduleCheck, errorDict, nonErrorDict, listWidget, btnResult, iconPath):
		self.errorDict, self.nonErrorDict = self.ItemCheckAndAddonsWrapperFunction.do(moduleCheck, errorDict, nonErrorDict, listWidget, btnResult, iconPath)

	def selectSimilarity(self, moduleCheck):
		self.ItemCheckAndAddonsWrapperFunction.selectSimilarity(moduleCheck)

	def setWrapperVisibility(self, v):
		self.newAddonsWindowWidget.setVisibility(False)
		self.newItemCheckWidget.setVisibility(v)
		
	def maximizeWindow(self):
		self.ItemCheckAndAddonsWrapperFunction.maximizeWindow(self.newAddonsWindowWidget, self.newItemCheckWidget, wrapperDict, iconPath)
				
		
class CollapsibleButton():
	def __init__(self, scrollLayout, projectName):
		self.childList = []

		#Create 
		self.createCollapsibleButton(scrollLayout, projectName)
		self.CollapsibleButtonFunction = fm.CollapsibleButtonFunction()

		#Add collapsible function
		self.collapsibleButton.clicked.connect(lambda: self.CollapsibleButtonFunction.collapseWidget(self.collapsibleButton, self.childList))


		
	
	def createCollapsibleButton(self, scrollLayout, projectName):
		self.collapsibleButton = QPushButton("<<< " + projectName + " >>>")
		self.collapsibleButton.setCheckable(True)
		self.collapsibleButton.setChecked(True)
		self.collapsibleButton.setStyle(QStyleFactory.create("Fusion"))
		scrollLayout.addWidget(self.collapsibleButton)
		
	def addChild(self, child):
		self.childList.append(child)






class MenuPreset():
	def __init__(self):
		self.MenuPresetFunction = fm.MenuPresetFunction()
	

	def showPresetFile(self, mainWindow):
		presetFileList = self.MenuPresetFunction.checkFileJsonExistance(presetPath)
		if presetFileList:
			for presetFile in presetFileList:
				newAction = MenuAction()
				newAction.createNewAction(presetFile, mainWindow.menuPreset)

 



class MenuAction():
	def __init__(self):
		self.MenuActionFunction = fm.MenuActionFunction()

	def createNewAction(self, presetFile, menuPreset):
		self.action = menuPreset.addAction(presetFile.split(".json")[0])
		self.action.setData(presetFile)
		self.action.triggered.connect(lambda: self.loadPreset())

	def loadPreset(self):
		self.MenuActionFunction.setButtonStatusThroughFileJson(self.action.data(), wrapperDict, presetPath, iconPath)
	
	def connectUI(self, mainWindow):
		mainWindow.actionOpen_Preset_Folder.triggered.connect(lambda: self.MenuActionFunction.openPresetFolder(presetPath))
		mainWindow.actionAdd_And_Save_Preset.triggered.connect(lambda: self.MenuActionFunction.createAndSavePreset(presetPath, wrapperDict))
		
class MainWindow(QObject):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		#Load UI
		UIFile = QFile(ui_file)
		UIFile.open(QFile.ReadOnly)
		loader = QUiLoader()
		self.window = loader.load(UIFile)

		self.MainWindowFunction = fm.MainWindowFunction()
		#Create, edit other sub widgets
		self.attachWindowToSoftware()
		self.changeLabelTitle()
		self.createWidgetAndAddCollapsibleButtonAndAddAddons()
		self.setButtonStyle()



		#Menu Preset show Preset in Preset Folder
		self.menuBar = MenuPreset()
		self.menuBar.showPresetFile(self.window)
		
		#Menu Action execute action script
		self.menuAction = MenuAction()
		self.menuAction.connectUI(self.window)

		
		
		self.connectUI()
		#self.window.btnSwapCheckUncheckAll.clicked.connect(lambda: self.CheckUncheckAll())
		#self.window.btnUncollapseAll.clicked.connect(lambda: self.collapseUncollapseAllWidget())
		#self.window.btnUncollapseAll.setChecked(False)
		

		self.window.show()

	def setButtonStyle(self):
		#self.window.btnSwapCheckUncheckAll.setStyle(QStyleFactory.create("Fusion"))
		self.window.btnSwapCheckUncheckAll.setStyle(QStyleFactory.create("Fusion"))
		self.window.btnValidate.setStyle(QStyleFactory.create("Fusion"))
		self.window.btnUncollapseAll.setStyle(QStyleFactory.create("Fusion"))


	def attachWindowToSoftware(self):
		try:
			MaxPlus.AttachQWidgetToMax(self.window)
		except:
			self.window.setParent(mayaMainWindow)
			self.window.setWindowFlags(QtCore.Qt.Window)

	def connectUI(self):
		self.window.btnValidate.clicked.connect(lambda: self.validateCheckedFunction())
		self.window.btnSwapCheckUncheckAll.clicked.connect(lambda: self.checkUncheckAll())
		self.window.btnShowError.clicked.connect(lambda: self.showError())
		#self.window.btnShowInfo.clicked.connect(lambda: self.showInfo())
		self.window.btnResetAll.clicked.connect(lambda: self.resetAllToDefault())
		self.window.btnUncollapseAll.clicked.connect(lambda: self.collapseUncollapseAllWidget())

	def showError(self):
		self.MainWindowFunction.showError(wrapperDict, iconPath)
	   
	#def showInfo(self):
		#self.remainingInfoList = self.MainWindowFunction.showInfo(wrapperDict, iconPath)

	def validateCheckedFunction(self):
		self.MainWindowFunction.validateCheckedFunction(wrapperDict, iconPath, self.window.progressBar, self.window.lbValidationResult)
	
	def checkUncheckAll(self):
		self.MainWindowFunction.checkUncheckAll(wrapperDict, iconPath)
					  
		
	def changeLabelTitle(self):
		self.window.lbTitle.setText(name_project)

	def collapseUncollapseAllWidget(self):
		self.MainWindowFunction.collapseUncollapseAllWidget(wrapperDict, iconPath)
		
	def resetAllToDefault(self):
		self.MainWindowFunction.resetAllToDefault(wrapperDict, iconPath, self.window.progressBar, self.window.lbValidationResult)

	def createWidgetAndAddCollapsibleButtonAndAddAddons(self):
		scrollAreaWidgetContents = QWidget(self.window.scrollArea) #Tao 1 QWidget va xet scrollArea lam parent cua no
		scrollLayout = QVBoxLayout(scrollAreaWidgetContents) #Tao 1 QVBoxLayout va xet QWidget o tren lam parent cua no
		self.window.scrollArea.setWidget(scrollAreaWidgetContents) #Xet scrollAreaWidgetContents lam widget cua scrollArea
		
		verticalSpacer = QtWidgets.QSpacerItem(17, 700, QSizePolicy.Preferred, QSizePolicy.Preferred)
		horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
		
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "\\" + projectName) == False:
				pass
			else:
				newCollapsibleButton = CollapsibleButton(scrollLayout, projectName)
				#newCollapsibleButton.createCollapsibleButton(scrollLayout, projectName)
				for i in os.listdir(collapsiblePath + "\\" + projectName):
					if "__init__" not in i and ".pyc" not in i and (os.path.isdir(collapsiblePath + "\\" + projectName + "\\" + i) == False):
						newItemCheckAndAddonsWrapper = ItemCheckAndAddonsWrapper(i, scrollLayout)
						newCollapsibleButton.addChild(newItemCheckAndAddonsWrapper)
						wrapperDict[i.split(".py")[0]] = newItemCheckAndAddonsWrapper
					else:
						pass
								
		scrollLayout.addItem(verticalSpacer) 
		scrollLayout.addItem(horizontalSpacer)

	#def runProgressBar(self):
		#self.MainWindowFunction.runProgressBar(self.window.progressBar, wrapperDict)
		


def check_exist_window(name_window):
	"""If name window is existed, deletes the window"""
	if application == "Maya":
		if (cmds.window(name_window, exists=True)):
			cmds.deleteUI(name_window, wnd=True)

check_exist_window("MainWindowValidation")
winValidation = MainWindow()
'''
def check_exist_window(name_window):
	"""If name window is existed, deletes the window"""
	if (cmds.window(name_window, exists=True)):
		cmds.deleteUI(name_window, wnd=True)

check_exist_window("MainWindowValidation")
winValidation = MainValidationWindow()
winValidation.show()