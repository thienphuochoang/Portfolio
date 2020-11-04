tool AlignToSurface
(
	local SnapObj=undefined
	local OrgPos=undefined
	local OrgRot=undefined
	local target_mesh=undefined
	local StartMouseMove=0
	local posy=undefined
	local roty=undefined
	local OrgViewY=undefined
	local Rotated = 0
	local vectorAngle  = 0
	
	fn clamp minVal maxVal val =
	(
		if val < minVal then val = minVal
		else if val > maxVal then val = maxVal
		return val
	)
		
	fn GetVectorsAngle v1 v2 =
	(
		dotProduct = dot (normalize v1) (normalize v2)
		dotProduct = clamp -1.0 1.0 dotProduct
		theAngle = acos(dotProduct)
		return theAngle
	)

	fn getRotateAngle snapObj=
	(
		local v1 = polyop.getfacenormal snapObj 1
		if(v1 != [0,0,1]) then
		(
			vectorAngle = GetVectorsAngle v1 [0,0,1]
		)
		return vectorAngle
	)
	
	fn createSplines PointA res=
	(
		sp = splineShape()
		addnewSpline sp
		addKnot sp 1 #corner #line pointA
		addKnot sp 1 #corner #line res
		return sp
	)

	fn g_filter Obj =
	(
		if Obj != SnapObj then
		(
			superclassof Obj == Geometryclass
		 )else false
	)

	fn ResetOrg =
	(
		SnapObj.pos = OrgPos
		SnapObj.dir = OrgRot
	 )

	fn snapToIntersect str =
	(
		--find the intersect pixel between select object and screen pos
		--viewPoint: mouse position in 2D
		if vectorAngle != 0 then 
		(
			local v1 = polyop.getfacenormal SnapObj 1
			crossProduct = cross (normalize v1) [0,0,1]
			rotate SnapObj vectorAngle crossProduct
			 resetxform $
			collapsestack $
			vectorAngle = 0
			print "collaspe"
		)
		local mouseRay = mapScreenToWorldRay viewPoint   -- make a ray from active viewport
		local intersect_Ray= intersectRay target_mesh mouseRay --see if the ray hits the picked object
		if intersect_Ray != undefined then --if we actually hit the picked object set to surface
		(
			SnapObj.pos = intersect_Ray.pos + intersect_Ray.dir * 0.15
			SnapObj.dir = intersect_Ray.dir

		 )
		else -- reset to original pos and rotation if not intersect
		(
			ResetOrg()
		)
		return str --functions need to return somethin right
	)

	on start do
	(
		--if something is selectede
		if $ != undefined then
		 (
			--maxops.cloneNodes $ cloneType:#copy newNodes: &nnl
			SnapObj = $
			getRotateAngle snapObj
			OrgPos = SnapObj.pos--save original position
			OrgRot = SnapObj.dir --save original rotation
			target_mesh = pickObject message:"Pick Target Surface" forceListenerFocus:false filter:g_filter
			select $
		)
		else -- if nothing is selected
		(
			messageBox "Start this tool with an object selected"
			#stop -- aborttool
		)
	)

	on mouseAbort clicker do 
	(                       --reset position and rotation
		ResetOrg()
	)

	 on mousePoint clickno do
	(
		if (clickno == 1 and target_mesh != undefined)then
		(
			snapToIntersect ahihi -- function calls dont seem to work without a parameter
		)
		else
		(
			#stop -- abort tool
		)
	)

	on freeMove do
	(
		if target_mesh != undefined then
		(
			snapToIntersect ahihi --this way it actually shows it is workin
					
			if Rotated != undefined then 
			(
				local tempRot = eulerangles 0 0 Rotated  
				in coordsys local rotate SnapObj tempRot 
			)
		)
		else
		(
			#stop 
		)
	 )

	on mouseMove clickno do
	(
		local pos = [0,0,0]
		 if StartMouseMove == 0 then
		(
			posy = SnapObj.pos 
			roty = SnapObj.rotation 
			OrgViewY = viewPoint.y 
			StartMouseMove = 1
		)
		SnapObj.rotation = roty 
		SnapObj.pos = posy 
		local tempRot = eulerangles 0 0 0   
		tempRot.z=((viewPoint.y-OrgViewY)/2) 
		local tempPos = [0,0,0]
		tempPos.z = ((viewPoint.y-OrgViewY)/20) 
		
		in coordsys local rotate SnapObj tempRot -- rotate locally
	)
)
startTool AlignToSurface
