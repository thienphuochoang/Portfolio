import json
import os
import importlib
import sys
try:
    import PySide2
    from PySide2 import QtGui, QtCore, QtWidgets, QtUiTools
    from PySide2 import __version__
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtCore import QFile, QObject, QSize
    from PySide2.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QPushButton, QFileDialog, QStyleFactory, QMessageBox, QApplication
    from PySide2.QtGui import QIcon
    from shiboken2 import wrapInstance 
except ImportError:
    import PySide
    from PySide import QtGui, QtCore
    import PySide.QtGui as QtWidgets
    from PySide import __version__
    from PySide.QtUiTools import QUiLoader
    from shiboken import wrapInstance

try:
    import maya.OpenMayaUI as omui
    import maya.mel as mel
    import maya.cmds as cmds
    application = "Maya"
except ImportError:
    import MaxPlus
    import MaxPlusExtend
    import pymxs
    rt = pymxs.runtime
    application = "Max"


try:
    import current_working_directory
    reload(current_working_directory)
    path_project, name_project = current_working_directory.get_cwd()
except:
    path_project = r"\\glassegg.com\TOOLS\TECHNICAL_SCRIPT\Projects"
    name_project = "Environment_Default"


sys.path.append(path_project)


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
        with open (presetPath + "\\" + action, "r") as json_file:
            data = json.load(json_file)
            return data



    def setButtonStatusThroughFileJson(self, action, wrapperDict, presetPath, iconPath):
        self.MainWindowFunction.resetToDefault(wrapperDict, iconPath)
        data = self.readFileJson(action, presetPath)
        for filePython in data:
            for item, wrapper in wrapperDict.iteritems():
                if filePython == item:
                    if data[filePython] == True:
                        try:
                            wrapper.newItemCheckWidget.window.btnStatus.setChecked(True)
                            wrapper.newItemCheckWidget.window.btnStatus.setIcon(QIcon(iconPath + "\\checkIconOn.png"))
                        except:
                            pass
                    if data[filePython] == False:
                        try:
                            wrapper.newItemCheckWidget.window.btnStatus.setChecked(False)
                            wrapper.newItemCheckWidget.window.btnStatus.setIcon(QIcon(iconPath + "\\checkIconOff.png"))
                        except:
                            pass

    def openPresetFolder(self, presetPath):
        os.startfile(presetPath)
                            
    def createAndSavePreset(self, presetPath, wrapperDict):
        data = {}
        fileName, filterName = QFileDialog.getSaveFileName(parent = None, caption = 'Create Or Save File', dir = presetPath)
        if fileName and ".json" in fileName.lower():
            presetFilePath = fileName
            for item, wrapper in wrapperDict.iteritems():
                data[item] = wrapper.newItemCheckWidget.window.btnStatus.isChecked()
            with open (presetFilePath, "w") as write_file:
                json.dump(data, write_file)
            messageBox = QMessageBox()
            messageBox.setText("Preset has been CREATED and SAVED!!!")
            messageBox.exec_()
        elif fileName and ".json" not in fileName.lower():
            presetFilePath = fileName + ".json"
            for item, wrapper in wrapperDict.iteritems():
                data[item] = wrapper.newItemCheckWidget.window.btnStatus.isChecked()
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
        btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
        btnResult.setStyleSheet('QPushButton {background-color: grey; border: 0px;}')

    def setDisplayAddonsWindow(self, btnCollapse, iconPath):
        btnCollapse.setChecked(True)
        btnCollapse.setIcon(QIcon(iconPath + "\\arrow-down.png"))


    def setVisibility(self, v, centralwidget, btnCollapse,  iconPath):
        centralwidget.setVisible(v)
        btnCollapse.setChecked(False)
        btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
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
            if os.path.isdir(collapsiblePath + "\\" + projectName) == False:
                pass
            else:
                for i in os.listdir(collapsiblePath + "\\" + projectName):
                    functionPath = collapsiblePath + "\\" + projectName
                    if os.path.exists(functionPath + "\\" + item + ".py"):
                        try:
                            importedModulePath = r"{}.{}.validation.app.res.{}.{}".format(name_project, application, projectName, item)
                            nameModule = importlib.import_module(importedModulePath)
                            reload(nameModule)
                            moduleCheck = nameModule
                            return moduleCheck
                        except:
                            pass
                    else:
                        pass

    def getSelectedListWidgetItem(self, moduleCheck, listWidget, errorDict, nonErrorDict):
        if "Maya" in application:
            cmds.select(clear=True)
        elif "Max" in application:
            rt.clearSelection()

        self.inputList = []

        try:
            for selectedItem in listWidget.selectedItems():
                for key, value in sorted(errorDict.iteritems()):
                    if key + value == selectedItem.text():
                        try:
                            self.inputList.append(key)
                            moduleCheck.selectCustom(self.inputList)
                        except:
                            if "Maya" in application:
                                cmds.select(key, add = True)
                            elif "Max" in application:
                                rt.selectmore(rt.getnodebyname(key))
        except:
            pass

        try:
            for selectedItem in listWidget.selectedItems():
                for key, value in sorted(nonErrorDict.iteritems()):
                    if key + value == selectedItem.text():
                        try:
                            self.inputList.append(key)
                            moduleCheck.selectCustom(self.inputList)
                        except:
                            if "Maya" in application:
                                cmds.select(key, add=True)
                            elif "Max" in application:
                                rt.selectmore(rt.getnodebyname(key))
        except:
            pass



    def showHideAddonsUI(self, widget, btnCollapse, iconPath):
        if btnCollapse.isChecked():
            btnCollapse.setIcon(QIcon(iconPath + "\\arrow-down.png"))
            btnCollapse.setIconSize(QSize(18,18))
            widget.setVisible(True)
        else:
            btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
            widget.setVisible(False)

    def setOnOffCheckButton(self, btnStatus, iconPath):
        if btnStatus.isChecked():
            btnStatus.setIcon(QIcon(iconPath + "\\checkIconOn.png"))
        else:
            btnStatus.setIcon(QIcon(iconPath + "\\checkIconOff.png"))

    def showErrorToListWidget(self, item, listWidget, errorDict, iconPath):
        listWidget.clear()
        if errorDict:
            try:
                for key, value in errorDict.iteritems():
                    item = QtWidgets.QListWidgetItem(key + value)
                    item.setIcon(QIcon(iconPath + "\\wrongIcon.png"))
                    listWidget.addItem(item)
            except:
                pass
        else:
            pass
        
    def showInfoToListWidget(self, item, listWidget, nonErrorDict, iconPath):
        listWidget.clear()
        if nonErrorDict:
            try:
                for key, value in nonErrorDict.iteritems():
                    item = QtWidgets.QListWidgetItem(key + value)
                    item.setIcon(QIcon(iconPath + "\\correctIcon.png"))
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
                    for key, value in sorted(errorDict.iteritems()):
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
                for key, value in sorted(errorDict.iteritems()):
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
            for key, value in errorDict.iteritems():
                content = QtWidgets.QListWidgetItem(key + value)
                content.setIcon(QIcon(iconPath + "\\wrongIcon.png"))
                listWidget.addItem(content)
                btnResult.setChecked(True)
                btnResult.setStyleSheet('QPushButton {background-color: red; border: 0px;}')
            return errorDict, nonErrorDict
        elif nonErrorDict and not errorDict:
            for key, value in nonErrorDict.iteritems():
                content = QtWidgets.QListWidgetItem(key + value)
                content.setIcon(QIcon(iconPath + "\\correctIcon.png"))
                listWidget.addItem(content)
                btnResult.setChecked(False)
                btnResult.setStyleSheet('QPushButton {background-color: rgb(85,255,0); border: 0px;}')
            return errorDict, nonErrorDict
        elif nonErrorDict and errorDict:
            for key, value in errorDict.iteritems():
                content = QtWidgets.QListWidgetItem(key + value)
                content.setIcon(QIcon(iconPath + "\\wrongIcon.png"))
                listWidget.addItem(content)
                btnResult.setChecked(True)
                btnResult.setStyleSheet('QPushButton {background-color: red; border: 0px;}')
            return errorDict, nonErrorDict

    def maximizeWindow(self, currentNewAddonsWindowWidget, currentNewItemCheckWidget, wrapperDict, iconPath):
        if currentNewItemCheckWidget.window.btnMaximize.isChecked():
            for item, wrapper in sorted(wrapperDict.iteritems()):
                if currentNewAddonsWindowWidget == wrapper.newAddonsWindowWidget:
                    currentNewItemCheckWidget.window.btnCollapse.setChecked(True)
                    currentNewItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-down.png"))
                    currentNewAddonsWindowWidget.window.centralwidget.setVisible(True)
                    currentNewAddonsWindowWidget.window.listWidget.setMinimumSize(350, 3200)
                    currentNewItemCheckWidget.window.btnMaximize.setIcon(QIcon(iconPath + "\\maximizedIcon.png"))
                else:
                    wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(False)
                    wrapper.newItemCheckWidget.window.centralwidget.setVisible(False)
            
        else:
            for item, wrapper in sorted(wrapperDict.iteritems()):
                wrapper.newItemCheckWidget.window.centralwidget.setVisible(True)
                wrapper.newItemCheckWidget.window.btnCollapse.setChecked(False)
                wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
                wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(False)

            currentNewAddonsWindowWidget.window.listWidget.setMinimumSize(0, 200)
            currentNewItemCheckWidget.window.btnMaximize.setIcon(QIcon(iconPath + "\\minimizedIcon.png"))

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
        for item, wrapper in sorted(wrapperDict.iteritems()):
            #wrapper.newItemCheckWidget.window.btnStatus.setChecked(True)
            #wrapper.newItemCheckWidget.window.btnStatus.setIcon(QIcon(iconPath + "\\checkIconOn.png"))
            wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(False)
            wrapper.newItemCheckWidget.window.btnCollapse.setChecked(False)
            wrapper.newItemCheckWidget.window.btnResult.setStyleSheet('QPushButton {background-color: grey; border: 0px;}')
            wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
            wrapper.errorDict = {}
            wrapper.nonErrorDict = {}
            wrapper.newAddonsWindowWidget.window.listWidget.clear()
            #wrapper.newItemCheckWidget.window.centralwidget.repaint()
            wrapper.newAddonsWindowWidget.window.centralwidget.repaint()



    def validateCheckedFunction(self, wrapperDict, iconPath, progressBar, lbValidationResult):
        lbValidationResult.setStyleSheet("background-color: grey;")
        self.checkedList = []
        self.completed = 0
        self.resetToDefault(wrapperDict, iconPath)
        

        itemList = []
        for item, wrapper in sorted(wrapperDict.iteritems()):
            if wrapper.newItemCheckWidget.window.centralwidget.isVisible():
                if wrapper.newItemCheckWidget.window.btnStatus.isChecked():
                    itemList.append(wrapper)
        progressBar.setMaximum(len(itemList))

        for item, wrapper in sorted(wrapperDict.iteritems()):
            if wrapper.newItemCheckWidget.window.centralwidget.isVisible():
                if wrapper.newItemCheckWidget.window.btnStatus.isChecked():
                    if wrapper.newItemCheckWidget.window.btnCollapse.isChecked():
                        self.checkedList.append(wrapper)
                        self.completed += 1
                        wrapper.newItemCheckWidget.window.btnCollapse.setChecked(True)
                        wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-down.png"))
                        wrapper.do(wrapper.moduleCheck, wrapper.errorDict, wrapper.nonErrorDict, wrapper.newAddonsWindowWidget.window.listWidget, wrapper.newItemCheckWidget.window.btnResult, iconPath)
                        progressBar.setValue(self.completed)
                        wrapper.newItemCheckWidget.window.centralwidget.repaint()
                    else:
                        self.checkedList.append(wrapper)
                        self.completed += 1
                        wrapper.newAddonsWindowWidget.window.listWidget.clear()
                        wrapper.newAddonsWindowWidget.window.listWidget.setVisible(True)
                        #wrapper.newItemCheckWidget.setDefault(wrapper.newItemCheckWidget.window.btnCollapse, iconPath)
                        wrapper.newItemCheckWidget.window.btnCollapse.setChecked(False)
                        wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
                        wrapper.newItemCheckWidget.window.btnResult.setStyleSheet('QPushButton {background-color: grey; border: 0px;}')
                        #wrapper.newAddonsWindowWidget.setDefault(wrapper.newAddonsWindowWidget.window.listWidget)
                        #wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-down.png"))
                        wrapper.do(wrapper.moduleCheck, wrapper.errorDict, wrapper.nonErrorDict, wrapper.newAddonsWindowWidget.window.listWidget, wrapper.newItemCheckWidget.window.btnResult, iconPath)
                        progressBar.setValue(self.completed)
                        wrapper.newItemCheckWidget.window.centralwidget.repaint()
                else:
                    wrapper.newItemCheckWidget.window.btnCollapse.setChecked(False)
                    wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
                    wrapper.newItemCheckWidget.window.btnResult.setStyleSheet('QPushButton {background-color: grey; border: 0px;}')
                    wrapper.newAddonsWindowWidget.window.listWidget.clear()
                    wrapper.newAddonsWindowWidget.window.listWidget.setVisible(True)
                    wrapper.newItemCheckWidget.window.btnCollapse.setChecked(False)
                    wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(False)

        errorAvailable = False
        for wrapper in self.checkedList:
            if wrapper.newItemCheckWidget.window.centralwidget.isVisible():
                if wrapper.newItemCheckWidget.window.btnResult.isChecked():
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
        if wrapperDict[next(iter(wrapperDict))].newItemCheckWidget.window.btnStatus.isChecked():
            checkedFlag = True
        else:
            checkedFlag = False

        if checkedFlag == True:
            for item, wrapper in sorted(wrapperDict.iteritems()):
                wrapper.newItemCheckWidget.window.btnStatus.setChecked(False)
                wrapper.newItemCheckWidget.window.btnStatus.setIcon(QIcon(iconPath + "\\checkIconOff.png"))
        else:
            for item, wrapper in sorted(wrapperDict.iteritems()):
                wrapper.newItemCheckWidget.window.btnStatus.setChecked(True)
                wrapper.newItemCheckWidget.window.btnStatus.setIcon(QIcon(iconPath + "\\checkIconOn.png"))

    def showError(self, wrapperDict, iconPath):
        checkFlag = False
        self.tempList = []
        for item, wrapper in sorted(wrapperDict.iteritems()):
            if wrapper.newItemCheckWidget.window.centralwidget.isVisible() == False:
                checkFlag = True
                break
        if checkFlag == True:
            for item, wrapper in sorted(wrapperDict.iteritems()):
                wrapper.newItemCheckWidget.window.centralwidget.setVisible(True)
                wrapper.newItemCheckWidget.window.btnCollapse.setChecked(False)
                wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
                wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(False)
                wrapper.newItemCheckWidget.window.btnMaximize.setChecked(False)
                wrapper.newAddonsWindowWidget.window.listWidget.setMinimumSize(0, 200)
                wrapper.newItemCheckWidget.window.btnMaximize.setIcon(QIcon(iconPath + "\\minimizedIcon.png"))
        else:
            self.remainingErrorList = []
            for item, wrapper in sorted(wrapperDict.iteritems()):
                if wrapper.errorDict:
                    self.remainingErrorList.append(wrapper)
                else:
                    wrapper.newItemCheckWidget.window.centralwidget.setVisible(False)
                    wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(False)

            for wrapper in self.remainingErrorList:
                wrapper.newItemCheckWidget.window.centralwidget.setVisible(True)
                wrapper.newItemCheckWidget.window.btnCollapse.setChecked(True)
                wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-down.png"))
                wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(True)
                wrapper.newItemCheckWidget.window.btnMaximize.setChecked(False)
                wrapper.newAddonsWindowWidget.window.listWidget.setMinimumSize(0, 200)
                wrapper.newItemCheckWidget.window.btnMaximize.setIcon(QIcon(iconPath + "\\minimizedIcon.png"))

    def collapseUncollapseAllWidget(self, wrapperDict, iconPath):
        self.tempDict = {}
        #if wrapperDict[next(iter(wrapperDict))].newItemCheckWidget.window.btnCollapse.isChecked():
        for item, wrapper in sorted(wrapperDict.iteritems()):
            if wrapper.newItemCheckWidget.window.centralwidget.isVisible():
                self.tempDict[item] = wrapper

        checkedFlag = True
        if self.tempDict[next(iter(self.tempDict))].newItemCheckWidget.window.btnCollapse.isChecked():
            checkedFlag = True
        else:
            checkedFlag = False

        if checkedFlag == True:
            for item, wrapper in sorted(self.tempDict.iteritems()):
                wrapper.newItemCheckWidget.window.btnCollapse.setChecked(False)
                wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-left.png"))
                wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(False)
        else:
            for item, wrapper in sorted(self.tempDict.iteritems()):
                wrapper.newItemCheckWidget.window.btnCollapse.setChecked(True)
                wrapper.newItemCheckWidget.window.btnCollapse.setIcon(QIcon(iconPath + "\\arrow-down.png"))
                wrapper.newAddonsWindowWidget.window.centralwidget.setVisible(True)
