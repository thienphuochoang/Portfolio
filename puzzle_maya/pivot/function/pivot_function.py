import PySide2
from PySide2 import QtWidgets
import maya.mel as mel
import maya.cmds as cmds

class PivotFunction():
	def __init__(self):
		pass

	def getComboBoxState(self, gbX, gbY, gbZ):
		stateList = []
		for button in gbX.findChildren(QtWidgets.QRadioButton):
			if button.isChecked() == True:
				stateList.append(button.text())
		for button in gbY.findChildren(QtWidgets.QRadioButton):
			if button.isChecked() == True:
				stateList.append(button.text())
		for button in gbZ.findChildren(QtWidgets.QRadioButton):
			if button.isChecked() == True:
				stateList.append(button.text())
		return stateList

	def getSelectionObj(self):
		objList = []
		if cmds.ls(sl = True):
			for obj in cmds.ls(sl = True, long = True):
				objList.append(obj)
			return objList
		else:
			cmds.confirmDialog(title='Warning', message='Please select at least 1 object', icon="critical")
			return None

	def setupPivot(self, selectedRBX, selectedRBY, selectedRBZ):
		objList = self.getSelectionObj()
		if objList != None:
			for obj in objList:
				xPos = None
				yPos = None
				zPos = None
				bbox = cmds.exactWorldBoundingBox(obj)

				if selectedRBX == "min":
					xPos = bbox[0]
				elif selectedRBX == "center":
					xPos = (bbox[0] + bbox[3])/2
				elif selectedRBX == "max":
					xPos = bbox[3]

				if selectedRBY == "min":
					yPos = bbox[1]
				elif selectedRBY == "center":
					yPos = (bbox[1] + bbox[4])/2
				elif selectedRBY == "max":
					yPos = bbox[4]

				if selectedRBZ == "min":
					zPos = bbox[2]
				elif selectedRBZ == "center":
					zPos = (bbox[2] + bbox[5])/2
				elif selectedRBZ == "max":
					zPos = bbox[5]


				pos = [xPos, yPos, zPos]
				cmds.xform(obj, piv = pos, ws = True)

	def setupPivot000(self):
		objList = self.getSelectionObj()
		if objList != None:
			for obj in objList:
				pos = [0, 0, 0]
				cmds.xform(obj, piv = pos, ws = True)

	def setupPivotUp0(self):
		objList = self.getSelectionObj()
		if objList != None:
			for obj in objList:
				currentPos = cmds.xform(obj, query = True, piv = True, ws = True)
				currentPos[1] = 0
				newPos = [currentPos[0], currentPos[1], currentPos[2]]
				cmds.xform(obj, piv = newPos, ws = True)

	def setupPos000(self):
		objList = self.getSelectionObj()
		if objList != None:
			for obj in objList:
				cmds.move(0, 0, 0, obj, rpr = True)