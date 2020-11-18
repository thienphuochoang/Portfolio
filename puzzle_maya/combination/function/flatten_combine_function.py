import maya.cmds as cmds

class FlattenCombineFunction():
	def __init__(self):
		pass

	def flattenCombine(self):
		objSelection = cmds.ls(sl = True, l = True)

		if len(objSelection) >= 2:

			selected = []
			stupidArrays = []
			DAGMarker = []


			cmds.selectMode(object = True)


			selected = cmds.ls(sl = True, l = True)

			master = selected[0]

			if cmds.ls(master, type = "shape"):
				stupidArrays = cmds.listRelatives(selected[0], p = True, f = True)
				master = stupidArrays[0]

		# 	store all of "masters" initial properties:
			endname = master.split("|")[-1]

			DAGPos = cmds.listRelatives(master, p = True, f = True)

			position = cmds.getAttr(master+".translate")
		# //	float $rotation[3] = `getAttr ($master+".rotate")` ;	// store it's rotation
			# rotation = cmds.getAttr(master+".rotate")
		# //	float $scale[3] = `getAttr ($master+".scale")` ;	// store it's scale
			# scale = cmds.getAttr(master+".scale")

			pivpos = cmds.xform(master, q = True, ws = True, sp = True)

			layer = cmds.listConnections(master, s = 1, type = "displayLayer")

		# 	now we need to clean up the selection list to *only* include single instances of geometry transforms

			selGeomShapes = cmds.ls(sl = True, l = True, dag = True, lf = True, g = True)
		# 	select -cl;
			cmds.select(cl = True)
			for shape in selGeomShapes:
				cmds.select(cmds.listRelatives(shape, p = True, f = True), add = True)

			selected = cmds.ls(sl = True, l = True)

			cmds.showHidden(b = True)
			cmds.lockNode(l = False)

		# 	Do the actual merge
			stupidArrays = cmds.polyUnite()

			combined = stupidArrays[0]
		# 	// polyPerformAction "polyMergeVertex -d 0.001 -tx 1" f 0;

		# 	insert Locator into the original heirarchy position to keep branch alive
			if DAGPos != None:
				DAGMarker = cmds.spaceLocator()
				cmds.parent(DAGMarker, DAGPos[0], r = True)

			cmds.selectMode(o = True)

			cmds.delete(combined, ch = True)

			for sel in selected:
				if cmds.objExists(sel):
					cmds.delete(sel)


			cmds.setAttr(combined+".doubleSided", 0)
			cmds.setAttr(combined+".opposite", 0)

		# 	Reverse it's channels
			cmds.move(0-position[0][0], 0-position[0][1], 0-position[0][2], combined, absolute = True)
		# //	rotate	-a (0-$rotation[0]) (0-$rotation[1]) (0-$rotation[2]) $combined ;
			# cmds.rotate(0-rotation[0], 0-rotation[1], 0-rotation[2], combined, absolute = True)
		# //	scale	-a (0-$scale[0]) (0-$scale[1]) (0-$scale[2]) $combined ;
			# cmds.scale(0-scale[0], 0-scale[1], 0-scale[2], combined, absolute = True)
		# 	Move its pivot to 0 0 0
			cmds.move(0, 0, 0, combined + ".scalePivot")
			cmds.move(0, 0, 0, combined + ".rotatePivot")

			cmds.makeIdentity(combined, a = True)

		# 	Move it to original position
			cmds.move(position[0][0], position[0][1], position[0][2], combined, a = True)

		# //	rotate	-a $rotation[0] $rotation[1] $rotation[2] $combined ;
		# //	scale	-a $scale[0] $scale[1] $scale[2] $combined ;
		# 	Move its pivot to original position

			cmds.move(pivpos[0], pivpos[1], pivpos[2], (combined + ".scalePivot"))

			cmds.move(pivpos[0], pivpos[1], pivpos[2], (combined + ".rotatePivot"))

		# 	Move it to the original Heirarchy position...
			if DAGPos != None:
				cmds.parent(combined, DAGPos[0], a = True)
				cmds.reorder(combined, f = True)

		# 	Re-add to layer
			if layer != None:
				for i in range(0, len(layer)):
					cmds.editDisplayLayerMembers(layer[i], combined, noRecurse = True)
			
			if cmds.objExists(master):
				cmds.warning(endname + " Still exists - Appending index on original Name")
			finalName = cmds.rename(combined, endname)

			if len(DAGMarker) > 0:
				if cmds.objExists(DAGMarker[0]):
					cmds.delete(DAGMarker[0])

			return finalName

		else:
			cmds.error("Please select at least 2 objects")