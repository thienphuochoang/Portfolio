import json
import os
import importlib
import sys
import PySide2
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QPushButton, QFileDialog, QMessageBox
from PySide2.QtGui import QIcon
from shiboken2 import wrapInstance 


import maya.OpenMayaUI as omui
import maya.mel as mel
import maya.cmds as cmds



class MenuPresetFunction():
	def __init__(self):
		pass

	def checkFileJsonExistance(self, presetPath):
		presenFileList = []
		for presetFile in os.listdir(presetPath):
			if ".json" in presetFile.lower():
				presenFileList.append(presetFile)
		return presenFileList

class MenuActionFunction():
	def __init__(self):
		self.MainWindowFunction = MainWindowFunction()

	def readFileJson(self, action, presetPath):
		with open (presetPath + "/" + action, "r") as json_file:
			data = json.load(json_file)
			return data



	def setButtonStatusThroughFileJson(self, action, wrapperDict, presetPath, iconPath):
		self.MainWindowFunction.resetToDefault(wrapperDict, iconPath)
		data = self.readFileJson(action, presetPath)
		for filePython in data:
			for item, wrapper in wrapperDict.items():
				if filePython == item:
					if data[filePython] == True:
						try:
							wrapper.newItemCheckWidget.btnStatus.setChecked(True)
							wrapper.newItemCheckWidget.btnStatus.setIcon(QIcon(iconPath + "/checkIconOn.png"))
						except:
							pass
					if data[filePython] == False:
						try:
							wrapper.newItemCheckWidget.btnStatus.setChecked(False)
							wrapper.newItemCheckWidget.btnStatus.setIcon(QIcon(iconPath + "/checkIconOff.png"))
						except:
							pass

	def openPresetFolder(self, presetPath):
		os.startfile(presetPath)
							
	def createAndSavePreset(self, presetPath, wrapperDict):
		data = {}
		fileName, filterName = QFileDialog.getSaveFileName(parent = None, caption = 'Create Or Save File', dir = presetPath)
		if fileName and ".json" in fileName.lower():
			presetFilePath = fileName
			for item, wrapper in wrapperDict.items():
				data[item] = wrapper.newItemCheckWidget.btnStatus.isChecked()
			with open (presetFilePath, "w") as write_file:
				json.dump(data, write_file)
			messageBox = QMessageBox()
			messageBox.setText("Preset has been CREATED and SAVED!!!")
			messageBox.exec_()
		elif fileName and ".json" not in fileName.lower():
			presetFilePath = fileName + ".json"
			for item, wrapper in wrapperDict.items():
				data[item] = wrapper.newItemCheckWidget.btnStatus.isChecked()
			with open (presetFilePath, "w") as write_file:
				json.dump(data, write_file)
			messageBox = QMessageBox()
			messageBox.setText("Preset has been CREATED and SAVED!!!")
			messageBox.exec_()

class CollapsibleButtonFunction():
	def __init__(self):
		pass

	def collapseWidget(self, collapsibleButton, childList):
		for wrapper in childList:
			if collapsibleButton.isChecked():
				wrapper.setWrapperVisibility(True)
			else:
				wrapper.setWrapperVisibility(False)


class ItemCheckWindowFunction():
	def __init__(self):
		pass

	def setDefault(self, btnCollapse, iconPath):
		btnCollapse.setChecked(False)
		btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
		btnResult.setStyleSheet('QPushButton {background-color: grey; border: 0px;}')

	def setDisplayAddonsWindow(self, btnCollapse, iconPath):
		btnCollapse.setChecked(True)
		btnCollapse.setIcon(QIcon(iconPath + "/arrow-down.png"))


	def setVisibility(self, v, centralwidget, btnCollapse,  iconPath):
		centralwidget.setVisible(v)
		btnCollapse.setChecked(False)
		btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
		btnCollapse.setIconSize(QSize(18,18))


class AddonsWindowFunction():
	def __init__(self):
		pass

	def setVisibility(self, v, centralwidget):
		centralwidget.setVisible(v)
	
	def setDefault(self, listWidget):
		listWidget.clear()
		listWidget.setVisible(False)


class ItemCheckAndAddonsWrapperFunction():
	def __init__(self):
		pass

	def importFileFunction(self, item, collapsiblePath):
		for projectName in os.listdir(collapsiblePath):
			if os.path.isdir(collapsiblePath + "/" + projectName) == False:
				pass
			else:
				for i in os.listdir(collapsiblePath + "/" + projectName):
					functionPath = collapsiblePath + "/" + projectName
					if os.path.exists(functionPath + "/" + item + ".py"):
						importedModulePath = r"puzzle_maya.validation.function.{}.{}".format(projectName, item)
						print (importedModulePath)
						nameModule = importlib.import_module(importedModulePath)
						importlib.reload(nameModule)
						moduleCheck = nameModule
						return moduleCheck
					else:
						pass

	def getSelectedListWidgetItem(self, moduleCheck, listWidget, errorDict, nonErrorDict):
		#if "Maya" in application:
		cmds.select(clear=True)
		#elif "Max" in application:
			#rt.clearSelection()

		self.inputList = []

		try:
			for selectedItem in listWidget.selectedItems():
				for key, value in sorted(errorDict.items()):
					if key + value == selectedItem.text():
						try:
							self.inputList.append(key)
							moduleCheck.selectCustom(self.inputList)
						except:
							#if "Maya" in application:
							cmds.select(key, add = True)
							#elif "Max" in application:
								#rt.selectmore(rt.getnodebyname(key))
		except:
			pass

		try:
			for selectedItem in listWidget.selectedItems():
				for key, value in sorted(nonErrorDict.items()):
					if key + value == selectedItem.text():
						try:
							self.inputList.append(key)
							moduleCheck.selectCustom(self.inputList)
						except:
							#if "Maya" in application:
							cmds.select(key, add=True)
							#elif "Max" in application:
								#rt.selectmore(rt.getnodebyname(key))
		except:
			pass



	def showHideAddonsUI(self, widget, btnCollapse, iconPath):
		if btnCollapse.isChecked():
			btnCollapse.setIcon(QIcon(iconPath + "/arrow-down.png"))
			btnCollapse.setIconSize(QSize(18,18))
			widget.setVisible(True)
		else:
			btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
			widget.setVisible(False)

	def setOnOffCheckButton(self, btnStatus, iconPath):
		if btnStatus.isChecked():
			btnStatus.setIcon(QIcon(iconPath + "/checkIconOn.png"))
		else:
			btnStatus.setIcon(QIcon(iconPath + "/checkIconOff.png"))

	def showErrorToListWidget(self, item, listWidget, errorDict, iconPath):
		listWidget.clear()
		if errorDict:
			try:
				for key, value in errorDict.items():
					item = QtWidgets.QListWidgetItem(key + value)
					item.setIcon(QIcon(iconPath + "/wrongIcon.png"))
					listWidget.addItem(item)
			except:
				pass
		else:
			pass
		
	def showInfoToListWidget(self, item, listWidget, nonErrorDict, iconPath):
		listWidget.clear()
		if nonErrorDict:
			try:
				for key, value in nonErrorDict.items():
					item = QtWidgets.QListWidgetItem(key + value)
					item.setIcon(QIcon(iconPath + "/correctIcon.png"))
					listWidget.addItem(item)
			except:
				pass
		else:
			pass

	def autoFix(self, moduleCheck, listWidget, btnResult, errorDict):
		self.fixList = []
		try:
			if listWidget.selectedItems():
				for selectedItem in listWidget.selectedItems():
					for key, value in sorted(errorDict.items()):
						if key + value == selectedItem.text():
							try:
								self.fixList.append(key)
								btnResult.setStyleSheet('QPushButton {background-color: yellow; border: 0px;}')
								#listWidget.clear()
							except:
								pass
				try:
					moduleCheck.fix(self.fixList)
				except:
					pass

				try:
					for selectedItem in listWidget.selectedItems():
						listWidget.takeItem(listWidget.row(selectedItem))
				except:
					pass

			else:
				for key, value in sorted(errorDict.items()):
					try:
						self.fixList.append(key)
						#listWidget.takeItem(listWidget.row(selectedItem))
						btnResult.setStyleSheet('QPushButton {background-color: yellow; border: 0px;}')
						listWidget.clear()
					except:
						pass
				try:
					moduleCheck.fix(self.fixList)
				except:
					pass
		except:
			pass

	def openDoc(self, moduleCheck):
		try:
			moduleCheck.doc()
		except:
			pass

	def do(self, moduleCheck, errorDict, nonErrorDict, listWidget, btnResult, iconPath):
		errorDict, nonErrorDict = moduleCheck.result()
		listWidget.clear()
		if errorDict and not nonErrorDict:
			for key, value in errorDict.items():
				content = QtWidgets.QListWidgetItem(key + value)
				content.setIcon(QIcon(iconPath + "/wrongIcon.png"))
				listWidget.addItem(content)
				btnResult.setChecked(True)
				btnResult.setStyleSheet('QPushButton {background-color: red; border: 0px;}')
			return errorDict, nonErrorDict
		elif nonErrorDict and not errorDict:
			for key, value in nonErrorDict.items():
				content = QtWidgets.QListWidgetItem(key + value)
				content.setIcon(QIcon(iconPath + "/correctIcon.png"))
				listWidget.addItem(content)
				btnResult.setChecked(False)
				btnResult.setStyleSheet('QPushButton {background-color: rgb(85,255,0); border: 0px;}')
			return errorDict, nonErrorDict
		elif nonErrorDict and errorDict:
			for key, value in errorDict.items():
				content = QtWidgets.QListWidgetItem(key + value)
				content.setIcon(QIcon(iconPath + "/wrongIcon.png"))
				listWidget.addItem(content)
				btnResult.setChecked(True)
				btnResult.setStyleSheet('QPushButton {background-color: red; border: 0px;}')
			return errorDict, nonErrorDict

	def maximizeWindow(self, currentNewAddonsWindowWidget, currentNewItemCheckWidget, wrapperDict, iconPath):
		if currentNewItemCheckWidget.btnMaximize.isChecked():
			for item, wrapper in sorted(wrapperDict.items()):
				if currentNewAddonsWindowWidget == wrapper.newAddonsWindowWidget:
					currentNewItemCheckWidget.btnCollapse.setChecked(True)
					currentNewItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-down.png"))
					currentNewAddonsWindowWidget.centralwidget.setVisible(True)
					currentNewAddonsWindowWidget.listWidget.setMinimumSize(350, 3200)
					currentNewItemCheckWidget.btnMaximize.setIcon(QIcon(iconPath + "/maximizedIcon.png"))
				else:
					wrapper.newAddonsWindowWidget.centralwidget.setVisible(False)
					wrapper.newItemCheckWidget.centralwidget.setVisible(False)
			
		else:
			for item, wrapper in sorted(wrapperDict.items()):
				wrapper.newItemCheckWidget.centralwidget.setVisible(True)
				wrapper.newItemCheckWidget.btnCollapse.setChecked(False)
				wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
				wrapper.newAddonsWindowWidget.centralwidget.setVisible(False)

			currentNewAddonsWindowWidget.listWidget.setMinimumSize(0, 200)
			currentNewItemCheckWidget.btnMaximize.setIcon(QIcon(iconPath + "/minimizedIcon.png"))

	def selectSimilarity(self, moduleCheck):
		try:
			moduleCheck.selectSimilarity()
		except:
			pass


class MainWindowFunction():
	def __init__(self):
		pass

	def resetAllToDefault(self, wrapperDict, iconPath, progressBar, lbValidationResult):
		lbValidationResult.setStyleSheet("background-color: grey;")
		progressBar.reset()
		self.resetToDefault(wrapperDict, iconPath)

	def resetToDefault(self, wrapperDict, iconPath):
		for item, wrapper in sorted(wrapperDict.items()):
			#wrapper.newItemCheckWidget.btnStatus.setChecked(True)
			#wrapper.newItemCheckWidget.btnStatus.setIcon(QIcon(iconPath + "/checkIconOn.png"))
			wrapper.newAddonsWindowWidget.centralwidget.setVisible(False)
			wrapper.newItemCheckWidget.btnCollapse.setChecked(False)
			wrapper.newItemCheckWidget.btnResult.setStyleSheet('QPushButton {background-color: grey; border: 0px;}')
			wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
			wrapper.errorDict = {}
			wrapper.nonErrorDict = {}
			wrapper.newAddonsWindowWidget.listWidget.clear()
			#wrapper.newItemCheckWidget.centralwidget.repaint()
			wrapper.newAddonsWindowWidget.centralwidget.repaint()



	def validateCheckedFunction(self, wrapperDict, iconPath, progressBar, lbValidationResult):
		lbValidationResult.setStyleSheet("background-color: grey;")
		self.checkedList = []
		self.completed = 0
		self.resetToDefault(wrapperDict, iconPath)
		

		itemList = []
		for item, wrapper in sorted(wrapperDict.items()):
			if wrapper.newItemCheckWidget.centralwidget.isVisible():
				if wrapper.newItemCheckWidget.btnStatus.isChecked():
					itemList.append(wrapper)
		progressBar.setMaximum(len(itemList))

		for item, wrapper in sorted(wrapperDict.items()):
			if wrapper.newItemCheckWidget.centralwidget.isVisible():
				if wrapper.newItemCheckWidget.btnStatus.isChecked():
					if wrapper.newItemCheckWidget.btnCollapse.isChecked():
						self.checkedList.append(wrapper)
						self.completed += 1
						wrapper.newItemCheckWidget.btnCollapse.setChecked(True)
						wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-down.png"))
						wrapper.do(wrapper.moduleCheck, wrapper.errorDict, wrapper.nonErrorDict, wrapper.newAddonsWindowWidget.listWidget, wrapper.newItemCheckWidget.btnResult, iconPath)
						progressBar.setValue(self.completed)
						wrapper.newItemCheckWidget.centralwidget.repaint()
					else:
						self.checkedList.append(wrapper)
						self.completed += 1
						wrapper.newAddonsWindowWidget.listWidget.clear()
						wrapper.newAddonsWindowWidget.listWidget.setVisible(True)
						#wrapper.newItemCheckWidget.setDefault(wrapper.newItemCheckWidget.btnCollapse, iconPath)
						wrapper.newItemCheckWidget.btnCollapse.setChecked(False)
						wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
						wrapper.newItemCheckWidget.btnResult.setStyleSheet('QPushButton {background-color: grey; border: 0px;}')
						#wrapper.newAddonsWindowWidget.setDefault(wrapper.newAddonsWindowWidget.listWidget)
						#wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-down.png"))
						wrapper.do(wrapper.moduleCheck, wrapper.errorDict, wrapper.nonErrorDict, wrapper.newAddonsWindowWidget.listWidget, wrapper.newItemCheckWidget.btnResult, iconPath)
						progressBar.setValue(self.completed)
						wrapper.newItemCheckWidget.centralwidget.repaint()
				else:
					wrapper.newItemCheckWidget.btnCollapse.setChecked(False)
					wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
					wrapper.newItemCheckWidget.btnResult.setStyleSheet('QPushButton {background-color: grey; border: 0px;}')
					wrapper.newAddonsWindowWidget.listWidget.clear()
					wrapper.newAddonsWindowWidget.listWidget.setVisible(True)
					wrapper.newItemCheckWidget.btnCollapse.setChecked(False)
					wrapper.newAddonsWindowWidget.centralwidget.setVisible(False)

		errorAvailable = False
		for wrapper in self.checkedList:
			if wrapper.newItemCheckWidget.centralwidget.isVisible():
				if wrapper.newItemCheckWidget.btnResult.isChecked():
					errorAvailable = True
					break
				else:
					continue

		if errorAvailable:
			lbValidationResult.setStyleSheet("background-color: rgb(255, 0, 0);")
		else:
			lbValidationResult.setStyleSheet("background-color: rgb(0, 255, 0);")

	def checkUncheckAll(self, wrapperDict, iconPath):
		checkedFlag = True
		if wrapperDict[next(iter(wrapperDict))].newItemCheckWidget.btnStatus.isChecked():
			checkedFlag = True
		else:
			checkedFlag = False

		if checkedFlag == True:
			for item, wrapper in sorted(wrapperDict.items()):
				wrapper.newItemCheckWidget.btnStatus.setChecked(False)
				wrapper.newItemCheckWidget.btnStatus.setIcon(QIcon(iconPath + "/checkIconOff.png"))
		else:
			for item, wrapper in sorted(wrapperDict.items()):
				wrapper.newItemCheckWidget.btnStatus.setChecked(True)
				wrapper.newItemCheckWidget.btnStatus.setIcon(QIcon(iconPath + "/checkIconOn.png"))

	def showError(self, wrapperDict, iconPath):
		checkFlag = False
		self.tempList = []
		for item, wrapper in sorted(wrapperDict.items()):
			if wrapper.newItemCheckWidget.centralwidget.isVisible() == False:
				checkFlag = True
				break
		if checkFlag == True:
			for item, wrapper in sorted(wrapperDict.items()):
				wrapper.newItemCheckWidget.centralwidget.setVisible(True)
				wrapper.newItemCheckWidget.btnCollapse.setChecked(False)
				wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
				wrapper.newAddonsWindowWidget.centralwidget.setVisible(False)
				wrapper.newItemCheckWidget.btnMaximize.setChecked(False)
				wrapper.newAddonsWindowWidget.listWidget.setMinimumSize(0, 200)
				wrapper.newItemCheckWidget.btnMaximize.setIcon(QIcon(iconPath + "/minimizedIcon.png"))
		else:
			self.remainingErrorList = []
			for item, wrapper in sorted(wrapperDict.items()):
				if wrapper.errorDict:
					self.remainingErrorList.append(wrapper)
				else:
					wrapper.newItemCheckWidget.centralwidget.setVisible(False)
					wrapper.newAddonsWindowWidget.centralwidget.setVisible(False)

			for wrapper in self.remainingErrorList:
				wrapper.newItemCheckWidget.centralwidget.setVisible(True)
				wrapper.newItemCheckWidget.btnCollapse.setChecked(True)
				wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-down.png"))
				wrapper.newAddonsWindowWidget.centralwidget.setVisible(True)
				wrapper.newItemCheckWidget.btnMaximize.setChecked(False)
				wrapper.newAddonsWindowWidget.listWidget.setMinimumSize(0, 200)
				wrapper.newItemCheckWidget.btnMaximize.setIcon(QIcon(iconPath + "/minimizedIcon.png"))

	def collapseUncollapseAllWidget(self, wrapperDict, iconPath):
		self.tempDict = {}
		#if wrapperDict[next(iter(wrapperDict))].newItemCheckWidget.btnCollapse.isChecked():
		for item, wrapper in sorted(wrapperDict.items()):
			if wrapper.newItemCheckWidget.centralwidget.isVisible():
				self.tempDict[item] = wrapper

		checkedFlag = True
		if self.tempDict[next(iter(self.tempDict))].newItemCheckWidget.btnCollapse.isChecked():
			checkedFlag = True
		else:
			checkedFlag = False

		if checkedFlag == True:
			for item, wrapper in sorted(self.tempDict.items()):
				wrapper.newItemCheckWidget.btnCollapse.setChecked(False)
				wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-left.png"))
				wrapper.newAddonsWindowWidget.centralwidget.setVisible(False)
		else:
			for item, wrapper in sorted(self.tempDict.items()):
				wrapper.newItemCheckWidget.btnCollapse.setChecked(True)
				wrapper.newItemCheckWidget.btnCollapse.setIcon(QIcon(iconPath + "/arrow-down.png"))
				wrapper.newAddonsWindowWidget.centralwidget.setVisible(True)
