-- start building UI
if geNormalTool2019 != undefined do
(
	closeRolloutFloater  geNormalTool2019
)

-- create floater
geNormalTool2019 = newRolloutFloater "GE_Normal_Tool_Test" 200 740

rollout displayToolRollout "Normal Display"
(
	spinner normalLength "Normal Length" range:[0.0,100.0,10.0]
	button displayAll "Toggle All (SLOW)" width:160
	button displaySelected "Toggle Selected" width:160
	 ---------------------
	----------------------
	fn display_vertex_normal len all:True = 
	(
		allObj = #()
		if all then
		(
			for OBJ in Geometry do
			(
	-- 			print OBJ as string
				join allObj  #(OBJ)
			)
		)
		else
		(
			sel = selection[1]
			join allObj #(sel)
		)
	-- 	print allObj as string
	-- 	
	-- 	addModifier allObj (Edit_Normals())
	-- 	current_modifier =  allObj.modifiers[#Edit_Normals]
	-- 	x.showHandles = true
	-- 	x.displayLength = len
		
		local turn_on = true
		for o in allObj do
		(
	-- 		print o.modifiers[1]
			if classOf o.modifiers[1] != edit_normals then
			(
	-- 			addModifier o (Edit_Normals())
	-- 			current_modifier =  o.modifiers[#Edit_Normals]
	-- 			current_modifier.displayLength = len
			)
			else
			(
				if o.modifiers[1].name == "GE Display Normal" then
				(
					turn_on = false
					break
		-- 			deletemodifier o 1
				)
			)
			
		)
		
		if turn_on then
		(
-- 			print "haha"
			local temp = Edit_Normals()
			temp.name = "GE Display Normal"
			addModifier allObj (temp)
			
			for o in allObj do
			(
	-- 			if o.modifiers[1] != "GE Display Normal" then
	-- 			(
	-- 				addModifier o (Edit_Normals())	
	-- 			) 
				current_modifier =  o.modifiers[1]
				current_modifier.name = "GE Display Normal"
				current_modifier.displayLength = len
			)
		)
		else
		(
			for o in allObj do
			(
				if classOf o.modifiers[1] == edit_normals then
				(
					if o.modifiers[1].name == "GE Display Normal" then
					(
						deletemodifier o 1
					)
				)

			)
		)
	)
	-----------------------------
	fn change_normal_length len =
	(
		for obj in Geometry do
		(
	-- 		if obj.modifiers[1] == edit_normals then
	-- 		(
			try
			(
				current_modifier = obj.modifiers[#GE_Display_Normal]
				current_modifier.displayLength = len
			)
			catch()
	-- 		)
		)
	)
	-----------------------------
	on displayAll pressed do 
	(
		display_vertex_normal normalLength.value  all:true
	)
	
	on displaySelected pressed do 
	(
		display_vertex_normal normalLength.value  all:false
	)
	
	on normalLength changed temp_val do 
	(
		change_normal_length temp_val
	)
)

rollout workingWithNormalTools "Normal Modeling Tools "
(
	fn detach_keeping_normal dup = 
	(
		local thisNode = selection[1]
		local thisObj = modPanel.getCurrentObject()
		
-- 		print thisNode
-- 		print thisObj
		
		if classOf thisNode != editable_poly then			
		(
			messageBox "Please convert to editable poly before processing"
		)
		else
		(
			local faces_selection = polyOp.getFaceSelection thisObj
			local all_faces = #{1..polyop.getNumFaces thisObj}
			local invert_selection = all_faces - faces_selection
			maxOps.cloneNodes thisNode cloneType:#copy newNodes:&new_node #nodialog
			new_node.name = uniqueName thisNode.name numDigits:3
			
-- 			print new_node
-- 			local new_obj = getNodeByName 
			select new_node
			local new_obj = modPanel.getCurrentObject()
			
			polyop.deleteFaces new_obj invert_selection
			if dup == false then
			(
				polyop.deleteFaces thisObj faces_selection
			)
			
			
			
		)
    )
    
    
	
	button detachKeepingNormals "Detach (Keep Normal)" toolTip:"Detach faces to new object, keep vertex normals intact" width:160
	button duplicateKeepingNormals "Duplicate (Keep Normal)" toolTip:"Duplicate faces to new object, keep vertex normals intact" width:160
	
	
	
	on detachKeepingNormals pressed do
	(
		detach_keeping_normal false
	)
	on duplicateKeepingNormals pressed do
	(
		detach_keeping_normal true
    )
    
)

rollout normalEditTools "Normal Edit Tools" 
(
	group  "1. Tweak Normals:"
	(
		button convertSelectionToNormal "Convert Selection To Normals" width:160
		
		button unlockSelectedVert "Unlock 'Selected'" width:160 tooltip:"Reset vertex normals of selected verticles" offset:[0,10]
		button lockUnlocked "Lock 'Unlocked'" width:160 tooltip:"Lock vertex normal that currently unlocked"

		button copyVertexNormal "Copy Average Normals" width:160 toolTip:"Pick vertices or normals" offset:[0,10]
		button pasteVertexNormal "Paste Normals" width:160 toolTip:"Paste the copied normal to selected normals"
		
		
	)
	
	group "2. Lock Bevel Edges:"
	(
		checkBox collapseAfterComputing "Collapse After Locking" 
		button lockByLargerFaces "Lock Edges --> 'Larger Area Side'" width:176 toolTip:"Pick edges first"
		button lockBySmallerFaces "Lock Edges --> 'Smaller Area Side" width:176 toolTip:"Pick edges first"
	)
	
	group "3. Transfer Surfaces:"
	(
		checkBox collapseAfterTransfer "Collapse After Transfering" 
		pickButton pickSourceTarget "Pick Source (Good Reflection)" width:160 autoDisplay:True
		button transferNormalFromSourceToTarger "Transfer Source->Target"  width:160 toolTip:"pick target"
	)
	
	group "4. Fix Panel Seams:"
	(
		button copyEdgeNormal "Copy Edge Normals" width:160 toolTip:"Copy normal from selected Edges, use for matching seams." 
		button pasteEdgeNormal "Paste Edge Normals" width:160
	)
	
	group "5. Set Weighted Normals:"
	(
		checkBox useAngle "Use Angle (SLOW)"
		button setWeightedNormal "Set Weighted For Selection" width:160
	)
	
	fn AngleBetweenVectors v1 v2 =
	(
		return (acos (dot (normalize v1) (normalize v2) ) )
	)
	
	--------------------------
	fn SetAreaWeightedNormal use_angle = 
	(
		local sel_list = selection
		for sel_item in sel_list do
		(
	-- 		local currentModifier = sel_item.modifiers[1]
-- 			print sel_item
			
			if classof sel_item != editable_poly then
			(
				messageBox "Please convert to editable poly"
			)
			else
			(
				addModifier sel_item (Edit_Normals())
				local theEditNormal = sel_item.modifiers[#Edit_Normals]
	-- 			print theEditNormal
				local surround_faces = #{}
				
				local normal_per_vertex = #{}
					
				local edge_vert = #{}
					
	-- 			print (polyOp.getNumVerts sel_item)
				for v = 1 to polyOp.getNumVerts sel_item do
				(
-- 					print ("vert:" + v as string)
					edge_vert = polyOp.getEdgesUsingVert sel_item v
					surround_faces = polyOp.getFacesUsingVert sel_item v
					local edge_face = #{}
	-- 				print surround_faces
					local temp_normal = [0,0,0]				
					for f in surround_faces do
					(
-- 						print f
						
						local temp_angle = 1.0
						if use_angle then
						(
							edge_face = polyOp.getEdgesUsingFace sel_item f
							local angle_edge = edge_face * edge_vert
							
                            local face_verts = polyOp.getVertsUsingEdge sel_item angle_edge as Array
                            local vec1 = [0,0,0]
                            local vec2 = [0,0,0]
                            if v == face_verts[1] then 
                            (
                                vec1 = polyOp.getVert sel_item face_verts[2] - polyOp.getVert sel_item v
                                vec2 =  polyOp.getVert sel_item face_verts[3] - polyOp.getVert sel_item v
                            )
                            else if v == face_verts[2] then 
                            (
                                vec1 = polyOp.getVert sel_item face_verts[1] - polyOp.getVert sel_item v
                                vec2 =  polyOp.getVert sel_item face_verts[3] - polyOp.getVert sel_item v
                            )
                            else if v == face_verts[3] then 
                            (
                                vec1 = polyOp.getVert sel_item face_verts[2] - polyOp.getVert sel_item v
                                vec2 =  polyOp.getVert sel_item face_verts[1] - polyOp.getVert sel_item v
                            )
                            
                            temp_angle = AngleBetweenVectors vec1 vec2

                        )
--                         print temp_angle
						temp_normal += (polyOp.getFaceNormal sel_item f) * (polyOp.getFaceArea sel_item f) * temp_angle
					)
					temp_normal = normalize(temp_normal)
	-- 				print temp_normal
					-- print v
					theEditNormal.ConvertVertexSelection #{v} normal_per_vertex node:sel_item
					-- print normal_per_vertex
					for n in normal_per_vertex do
					(
						theEditNormal.makeExplicit selection:#{n} node:sel_item
						theEditNormal.setNormal  n temp_normal node:sel_item
					)
					 
					
				)				
			)
		)
	)
	-------------------------
	on setWeightedNormal pressed do
	(
		SetAreaWeightedNormal useAngle.checked
	)
	
	
	
    -------------------------------

    local source_object = undefined
    fn TransferNormals sObj tObj = 
	(
		if sObj == undefined then 
		(
			messageBox "Please pick source before transfering"
		)
		else
		(
            start = timestamp()
            
            local thisNode = selection[1]
            local selected_element = #{}
            if subObjectLevel == 0 then 
            (
                selected_element = #{1..(polyOp.getNumVerts tObj)}
            )
            else if subObjectLevel == 1 then 
            (
                selected_element = polyOp.getVertSelection tObj     
            )
            else if subObjectLevel == 2 or subObjectLevel == 3 then 
            (
--                 print "2"
                selected_element = polyOp.getEdgeSelection tObj 
--                 print selected_element
                selected_element = polyOp.getVertsUsingEdge tObj selected_element
--                 print selected_element
            )
            else if subObjectLevel == 4 or subObjectLevel == 5 then 
            (
                selected_element = polyOp.getFaceSelection tObj
                selected_element = polyOp.getVertsUsingFace tObj selected_element 
            )

			--get selected faces using copy instead of snapshot to keep poly :[
			selFaces = #{}
			disableRefMsgs()
			tObjCopy = copy tObj
			if (classof tObjCopy != editable_poly) and (classof tObjCopy != editable_mesh) do converttopoly tObjCopy
			selFaces = getFaceSelection tObjCopy
            --if no faces selected, select all
            if (subObjectLevel > 0) then (selFaces = polyOp.getFacesUsingVert tObjCopy selected_element)
            else if (selFaces.numberset == 0 or subObjectLevel == 0) then (selFaces = #{1..tObjCopy.numfaces})
            
			delete tObjCopy
			enableRefMsgs()
			
			--snapshot/xform the source object so we don't mess with it
			sMesh = snapshotasmesh sObj
			sObjSnap = editable_mesh()
			sObjSnap.mesh = sMesh

			mod_tObj = Edit_Normals ()
			mod_tObj.displayLength = 1

			mod_sObjSnap = Edit_Normals ()
			mod_sObjSnap.displayLength = 0

			addmodifier tObj mod_tObj
            addmodifier sObjSnap mod_sObjSnap
            
            local edit_normal_modifier = tObj.modifiers[#Edit_Normals]

            local selected_to_normal = #{}
--             print selected_element
            edit_normal_modifier.convertVertexSelection selected_element selected_to_normal node:thisNode
--             print selected_to_normal


			--cache
			_getNormalID = mod_sObjSnap.GetNormalID
			_getNormal = mod_sObjSnap.GetNormal

			_getFaceDegree = mod_tObj.GetFaceDegree
			_getVertexID = mod_tObj.GetVertexID
			_getVertex = mod_tObj.GetVertex
			_getNormalIDt = mod_tObj.getNormalID
			_ConvertVertexSelection = mod_tObj.ConvertVertexSelection
			_setSelection = mod_tObj.SetSelection
			_makeExplicit = mod_tObj.MakeExplicit
			_setNormal = mod_tObj.Setnormal

			nID_Arr = #()
			nVal_Arr = #()
			hitFaceBary_Arr = #()
			faceID_Arr = #()
			done = #()
			
			mpi = MeshProjIntersect()
			mpi.setNode sObjSnap
			mpi.build()
			
			--! editNormals has to be the current selection, with modify panel on !
			select tObj --should be already selected but just in case
			tObjTransform = tObj.transform
			
			max modify mode

			--for each selected face...
			for f in selFaces do
			(
				corners = _getFaceDegree f 
				--for each face corner...
				for c=1 to corners do
				(
					--get vertex ID
					v = _getVertexID f c
					if finditem done v == 0 do
					(
						try
						(
							--get vert closest face barycenter in source mesh
							--get vert normal ID
							pos = (_getVertex v)*tObjTransform --world pos
							mpi.closestFace pos doubleSided:True
							hitFace = mpi.GetHitFace()+1 --zero based
							bary = mpi.GetHitBary()
							nID = _getNormalIDt f c
							--? should we break the id if only 1 smoothing group ?
							append hitFaceBary_Arr #(hitFace,bary)
							append nID_Arr  nID
						)
						catch (format "Error on vert:%\n" v)
						sharedNorm = #{}
						_ConvertVertexSelection #{v} sharedNorm
						--if the vertex has only 1 normal, we're done with it
						--? could be more optimized ?
						if sharedNorm.numberset == 1 do append done v
					)
				)
			)

			--get normal from source faces barycenters
			select sObjSnap
			--for each hitFace...
			for faceBary in hitFaceBary_Arr do
			(
				f = faceBary[1]
				bary = faceBary[2]
				--get its vertex normals
				n1 = _getNormal (_getNormalID f 1)
				n2 = _getNormal (_getNormalID f 2)
				n3 = _getNormal (_getNormalID f 3)
				--get barycenter normal
				n= (bary.x*n1)+(bary.y*n2)+(bary.z*n3)
				append nVal_Arr n
			)

			--set normals on target object
			select tObj
			subobjectLevel = 1
			disableRefMsgs()
			for i=1 to nID_Arr.count do
			(
				nID = nID_Arr[i]
                n = nVal_Arr[i]
                if findItem selected_to_normal nID > 0 then 
                (
                    _setSelection #{nID}
                    _MakeExplicit()
                    _setNormal nID n
                )
				
			)
			enableRefMsgs()

			--clean
			mpi.Free()
			delete sObjSnap
			gc light:true

			select tObj
            format "Normals transfer took % seconds\n" ((timestamp()-start)/1000.0)
            
            if collapseAfterTransfer.checked then 
            (
                maxOps.CollapseNodeTo $ 1 true
                subObjectLevel = 2
            )
		)
	)
	 ------------------------------
    on transferNormalFromSourceToTarger pressed do
    (
-- 		local thisNode = selection[1]
-- 		local thisObj = modPanel.getCurrentObject()
-- 		print subObjectLevel
        TransferNormals source_object selection[1]
    )
    on pickSourceTarget picked obj do 
    (
        if obj != undefined then 
        (
            source_object = obj
        )
    )
	
	 ---------------------------
	
	fn get_faces_to_compute edgeSelectionList large =
	(
		local theNode = selection[1]
		local theEditObj = modPanel.getCurrentObject()
		local temp_face = #{}
		local left_area = 0
		local right_area = 0
		local left_face_list = #()
		local right_face_list = #()
		local already_calculate_edge_list = #{}
		
		local left_edge_list = #{}
		local right_edge_list = #{}
		
		local current_calcualting_edge = (edgeSelectionList as array)[1]
		local temp_face = #{}
		
-- 			local debug = 0
		local remaining_edge = #{}
		
-- 		start compute which is left and which is right
		while current_calcualting_edge != undefined do
		(
-- 			print ("edge: " + current_calcualting_edge as string)
			temp_face = polyOp.getFacesUsingEdge theEditObj current_calcualting_edge
			
			local temp_left_face = undefined
			local temp_right_face = undefined
			
			if left_face_list.count == 0 and right_face_list.count == 0 then
			(
				temp_left_face = (temp_face as array)[1]
				temp_right_face = (temp_face as array)[2]
			)
			else
			(
				local edge_list_1 =  polyOp.getEdgesUsingFace theEditObj  (temp_face as array)[1]
-- 				local edge_list_2 =  polyOp.getEdgesUsingFace theEditObj  temp_face[2]
-- 				print left_edge_list2
-- 				print edge_list_1
-- 				local check1 = #{}
				
				local check1 = edge_list_1 * left_edge_list
				local check2 = edge_list_1 * right_edge_list
-- 				print check1
-- 				print((check1 as array).count == 0)
				
				if (check1 as array).count != 0 then
				(
					temp_left_face = (temp_face as array)[1]
					temp_right_face = (temp_face as array)[2]
				)
				else
				(
					if (check2 as array).count != 0 then
					(
						temp_left_face = (temp_face as array)[2]
						temp_right_face = (temp_face as array)[1]
					)
					else
					(
						local edge_list_2 =  polyOp.getEdgesUsingFace theEditObj  (temp_face as array)[2]
						local check3 = (edge_list_2 * left_edge_list) as array
						local check4 = (edge_list_2 * left_edge_list) as array
						
						if check3.count != 0 then
						(
							temp_left_face = (temp_face as array)[2]
							temp_right_face = (temp_face as array)[1]	
						)
						else
						(
							if check4.count != 0 then
							(
								temp_left_face = (temp_face as array)[1]
								temp_right_face = (temp_face as array)[2]
							)
							else
							(
								local special_case_edge = polyOp.getEdgesUsingFace theEditObj (temp_face as array)[1]
								deleteItem special_case_edge current_calcualting_edge
								local special_case_face = polyOp.getFacesUsingEdge theEditObj special_case_edge
-- 								print "haha"
								local special_case_edge2 = polyOp.getEdgesUsingFace theEditObj special_case_face
								
								local check5 = (special_case_edge2 * left_edge_list) as array
								local check6 = (special_case_edge2 * right_edge_list) as array
								
								if check5.count != 0 then
								(
									temp_left_face = (temp_face as array)[1]
									temp_right_face = (temp_face as array)[2]
								)
								else
								(
									if check6.count != 0 then
									(
										temp_left_face = (temp_face as array)[2]
										temp_right_face = (temp_face as array)[1]
									)
									else
									(
										messageBox "Some errors occure. Please clean up topology!"
									)
								)
							)
						)
					)
				)
			)
-- 			print ("left " + temp_left_face as string)
-- 			print ("right " + temp_right_face as string)
			appendIfUnique  left_face_list temp_left_face
			appendIfUnique  right_face_list temp_right_face
			
			local temp_left_edge = polyOp.getEdgesUsingFace theEditObj temp_left_face
			local temp_right_edge = polyOp.getEdgesUsingFace theEditObj temp_right_face
			
			left_edge_list += temp_left_edge
			right_edge_list += temp_right_edge
			
			append already_calculate_edge_list current_calcualting_edge
			
			local next_edge_list = polyOp.getEdgesUsingVert theEditObj (polyOp.getVertsUsingEdge theEditObj current_calcualting_edge)
			
			local end = true
			
			local edge_to_proceed = (next_edge_list * edgeSelectionList) - already_calculate_edge_list
-- 			print edge_to_proceed
			
			if (edge_to_proceed as array).count > 0 then 
			(
				end = false
				current_calcualting_edge = (edge_to_proceed as array)[1]
				
				if (edge_to_proceed as array).count == 2 then
				(
					append remaining_edge (edge_to_proceed as array)[2]
				)
				
			)
			
			
-- 			else
-- 			(
-- 				if (edge_to_proceed as array).count == 1
-- 			)
			
			
			
			if end then
			(
				if (remaining_edge as array).count > 0  then
				(
					current_calcualting_edge = (remaining_edge as array)[1]
					deleteItem remaining_edge (remaining_edge as array)[1]
				)
				else
				(
					current_calcualting_edge = undefined
				)
				
			)
			
-- 			prevent infinite loop, remove after tesing
-- 			debug += 1
-- 			if debug == 10 then
-- 			(
-- 				break
-- 			)
			
			
		)
		
-- 		print left_face_list
-- 		print right_face_list
		
		
		for f1 in left_face_list do
		(
			left_area += polyOp.getFaceArea theEditObj f1
		)
		for f2 in right_face_list do
		(
			right_area += polyOp.getFaceArea theEditObj f2
		)
		
		local face_to_compute = #{}
		
		if large then
		(
			if left_area > right_area then
			(
				face_to_compute = left_face_list
			)
			else
			(
				face_to_compute = right_face_list
			)
		)
		else
		(
			if left_area < right_area then
			(
				face_to_compute = left_face_list
			)
			else
			(
				face_to_compute = right_face_list
			)
		)
		
		return (#(face_to_compute, already_calculate_edge_list))
	)
	 
	fn lock_normal_by_face large col=
	(
		-- tobe continued
		local theNode = selection[1]
		local theEditObj = modPanel.getCurrentObject()
		
		if classOf theEditObj == editable_poly then
		(
			local edgeSelectionList = polyOp.getEdgeSelection theEditObj
            local vert_to_apply = polyOp.getVertsUsingEdge theEditObj edgeSelectionList
            local face_to_compute = #()
            local edgeSelectionList_bk = edgeSelectionList
			while (edgeSelectionList as array).count > 0 do
			(
				local temp_result = get_faces_to_compute edgeSelectionList large
				face_to_compute += temp_result[1] 
				edgeSelectionList = edgeSelectionList - temp_result[2]
			)
			
			
	-- 		print face_to_compute
			
			addModifier theNode (Edit_Normals())
			local edit_normal_modifier = theNode.modifiers[#Edit_Normals]
            
            local normal_to_apply = #{}
            edit_normal_modifier.ConvertEdgeSelection edgeSelectionList_bk normal_to_apply node:theNode
			print normal_to_apply

			for v in vert_to_apply do
			(
				local temp_surround_faces = polyOp.getFacesUsingVert theEditObj v
				local this_normal = [0,0,0]
				for temp_f in temp_surround_faces do
				(
					if findItem face_to_compute temp_f > 0 then
					(
						this_normal += (polyOp.getFaceNormal theEditObj temp_f) * (polyOp.getFaceArea theEditObj temp_f)
					)
				)
				this_normal = normalize(this_normal)
				local temp_normal_from_vertex = #{}
				edit_normal_modifier.ConvertVertexSelection #{v} temp_normal_from_vertex node:theNode
				
				for normal_vector in temp_normal_from_vertex do
				(
                    if findItem normal_to_apply normal_vector > 0 then
                    (
                        edit_normal_modifier.SetNormalExplicit normal_vector explicit:True
                        edit_normal_modifier.SetNormal normal_vector this_normal
                    )
				)
			)
			
	-- 		for edge_item in edgeSelectionList do
	-- 		(
	-- 			temp_face = polyOp.getFacesUsingEdge theEditObj edge_item
	-- 		)
			
			if col then
			(
				maxOps.CollapseNodeTo $ 1 true
				subObjectLevel = 2
			)
		)
	)
	 -------------------------------
	on lockByLargerFaces pressed do
	(
		lock_normal_by_face true collapseAfterComputing.checked
	)
	on lockBySmallerFaces pressed do
	(
		lock_normal_by_face false collapseAfterComputing.checked
	)
	
	fn convert_selection_to_normal arg = 
    (
        local thisNode = selection[1]
        local thisObj = modPanel.getCurrentObject()
        local temp = subObjectLevel
        local sel = #{}
        addModifier thisNode (Edit_Normals())
        local edit_normal_modifier = thisNode.modifiers[#Edit_Normals]
        local normal_to_select = #{}

        if temp == 1 then 
        (
            sel = polyOp.getVertSelection thisObj
            edit_normal_modifier.convertVertexSelection sel normal_to_select node:thisNode
        )
        else if temp == 2 or temp == 3 then 
        (
            sel = polyOp.getEdgeSelection thisObj
            edit_normal_modifier.convertEdgeSelection sel normal_to_select node:thisNode
        )
        else if temp == 4 or temp == 5 then 
        (
            sel = polyOp.getFaceSelection thisObj
            edit_normal_modifier.convertFaceSelection sel normal_to_select node:thisNode
        )
        edit_normal_modifier.setSelection normal_to_select node:thisNode

    )
	
	on convertSelectionToNormal pressed do
    (
        convert_selection_to_normal true
    )

    local selected_edge_to_copy = #{}
	fn get_edge_normal arr = 
	(
        -- local edge_normal_array = #{}
        local vert_transform_array = #()
        local vert_normal_array = #()

		local thisNode = selection[1]
		local thisObj = modPanel.getCurrentObject()
		
        local selected_edge = polyOp.getEdgeSelection thisObj

        local vert_from_selected_edge = polyOp.getVertsUsingEdge thisObj selected_edge 
        local vert_from_selected_edge_array = vert_from_selected_edge as array

        addModifier thisNode (Edit_Normals())
        local normal_modifier = thisNode.modifiers[#Edit_Normals]
        -- local i = 1
        for i = 1 to  vert_from_selected_edge_array.count do 
        (
            vert_transform_array[i] = polyOp.getVert thisNode vert_from_selected_edge_array[i]

            local this_normal_array = #{}
            local this_normal_average_value = [0,0,0]
            normal_modifier.convertVertexSelection #{vert_from_selected_edge_array[i]} this_normal_array node:thisNode

            for n in this_normal_array do 
            (
                this_normal_average_value += normal_modifier.getNormal n node:thisNode
            )
            this_normal_average_value = normalize(this_normal_average_value)
            vert_normal_array[i] = this_normal_average_value

            i += 1
        )

        

        -- normal_modifier.convertVertexSelection vert_from_selected_edge edge_normal_array node:thisNode

        -- j = 1
        -- for en in edge_normal_array do
        -- (
        --     vert_normal_array[j] = normal_modifier.GetNormal en

        --     j += 1
        -- )

        maxOps.CollapseNodeTo $ 1 true
        subObjectLevel = 2

        -- print vert_transform_array
        -- print vert_normal_array
 
        return #(#(vert_transform_array, vert_normal_array), thisObj, thisNode)
    )
    
    fn paste_edge_normal source_vert_info source_obj source_node = 
    (
-- 		print source_vert_info
        local thisNode = selection[1]
        local thisObj = modPanel.getCurrentObject()
        local selected_edge_to_paste = polyOp.getEdgeSelection thisObj

        local vert_from_selected_edge_to_paste = polyOp.getVertsUsingEdge thisObj selected_edge_to_paste
        local vert_from_selected_edge_to_paste_array = vert_from_selected_edge_to_paste as array

        if vert_from_selected_edge_to_paste_array.count != source_vert_info[1].count then 
        (
            messageBox "Target edge loop need to have the same number of verts as source"
        )
        else 
        (
            local selected_vert_transform_array = #()
            local normal_to_paste_array = #()

            addModifier thisNode (Edit_Normals())
            local this_edit_normal_modifier = thisNode.modifiers[#Edit_Normals]
            
            for i = 1 to vert_from_selected_edge_to_paste_array.count do 
            (
                local min_distance = undefined 
                local normal_to_paste = [0,0,0] 
                selected_vert_transform_array[i] = polyOp.getVert thisNode vert_from_selected_edge_to_paste_array[i]
                for j = 1 to source_vert_info[1].count do 
                (
                    if min_distance == undefined then 
                    (
                        min_distance = distance selected_vert_transform_array[i] source_vert_info[1][j]
                        normal_to_paste = source_vert_info[2][j]
                    )
                    else 
                    (
                        local this_distance = distance selected_vert_transform_array[i] source_vert_info[1][j]
                        if this_distance < min_distance then 
                        (
                            min_distance = this_distance
                            normal_to_paste = source_vert_info[2][j]
                        )
                    )
                )
                normal_to_paste_array[i] = normal_to_paste
                local selected_normal_array = #{}
                this_edit_normal_modifier.convertVertexSelection #{vert_from_selected_edge_to_paste_array[i]} selected_normal_array node:thisNode
                
                if classOf normal_to_paste == point3 then 
                (
                    for n in selected_normal_array do 
                    (
                        this_edit_normal_modifier.makeExplicit selection:#{n} node:thisNode
                        this_edit_normal_modifier.setNormal n normal_to_paste node:thisNode
                    )
                )
                -- if classOf normal_to_paste == array then 
                -- (
                --     k = 1
                --     for n in selected_normal_array do 
                --         (
                --             this_edit_normal_modifier.makeExplicit selection:#{n} node:thisNode
                --             this_edit_normal_modifier.setNormal n normal_to_paste[k] node:thisNode

                --             k += 1
                --         )
                -- )
                
            )
			
			maxOps.CollapseNodeTo $ 1 true
			subObjectLevel = 2
        )


    )
    
    local edge_value_to_paste = #()
    on copyEdgeNormal pressed do 
    (
        edge_value_to_paste = get_edge_normal true
    )
    on pasteEdgeNormal pressed do 
    (
        paste_edge_normal edge_value_to_paste[1] edge_value_to_paste[2] edge_value_to_paste[3]  
    )
	 
    
    
	 
	local averageNormal = [0,0,0]
	 -----------------------------
	fn get_average_vector theEditNormal vertorArray = 
	(
	-- 	local i = 1
		local averageNormal = [0,0,0]
		for vtxNrm in vertorArray do
		(
	-- 		print vtxNrm
			averageNormal +=  theEditNormal.GetNormal vtxNrm
	-- 		i += 1
	-- 		print (theEditNormal.GetNormal vtxNrm)
		)
		averageNormal = normalize(averageNormal)
		return averageNormal
	)

	fn set_vertex_normal val = 
	(
		local theNode = selection[1]
		local theEditObj = modPanel.getCurrentObject()
		local currentModifier = theNode.modifiers[1]
		local selNorm = #{}
		
		if classOf currentModifier == Edit_Normals then
		(
			selNorm = currentModifier.GetSelection node:theNode
		)
		
		for nor in selNorm do
		(
			currentModifier.setNormalExplicit nor explicit:True
			currentModifier.setNormal nor val
		)
		
	)
	 --------------
	 fn get_average_normal sel:true = 
	(
		local theNode = selection[1]
		local theEditObj = modPanel.getCurrentObject()
		
		if ((classOf theEditObj) == Editable_Poly) then
		(
			
			local theEditObj = modPanel.getCurrentObject()
			local vertSel = polyOp.getVertSelection theEditObj
			
			if theNode.modifiers.count > 1 then
			(
				print "Please collapse to editable poly before proceeding"
			)
			else
			(
	-- 			theEditNorm = theNode.modifiers[1]
				addModifier theNode (Edit_Normals())
				local theEditNormal = theNode.modifiers[#Edit_Normals]
				local vertNormalArray = #{}
				theEditNormal.convertVertexSelection vertSel vertNormalArray node:theNode
				theEditNormal.selectBy = 1
	-- 			print vertNormalArray
				local averageNormal = get_average_vector theEditNormal vertNormalArray
				
				maxOps.CollapseNodeTo $ 1 true
				subObjectLevel = 1
	-- 			print averageNormal
				return averageNormal
			)
			
		)
	-- 	print theNode.modifiers[1]
	-- 	print ( classOf theNode.modifiers[1] == Edit_Normals)
		
		if (classOf theNode.modifiers[1] == Edit_Normals) then
		(
			
			local theEditNormal = theNode.modifiers[1]
			local selNormal = theEditNormal.GetSelection node:theNode
	-- 		print selNormal
			local averageNormal = get_average_vector theEditNormal selNormal
			return averageNormal
		)
		
		
		
	)
	 ------------------------------
	on copyVertexNormal pressed do
	(
		averageNormal = get_average_normal sel:true
-- 		print averageNormal
	)
	on pasteVertexNormal pressed do
	(
		if averageNormal != [0,0,0] then
		(
			set_vertex_normal averageNormal
		)	
    )
	
	fn unlock_normal_selection col = 
	(
		if subObjectLevel != 1 then 
		(
			messageBox "Choose verticles to unlock"
		)
		else 
		(
			local thisNode = selection[1]
			local thisObj = modPanel.getCurrentObject()

			addModifier thisNode (Edit_Normals())
			local edit_normal_modifier = thisNode.modifiers[#Edit_Normals]

			local selected_vert = polyOp.getVertSelection thisObj

			local normal_from_selected = #{}
			edit_normal_modifier.convertVertexSelection selected_vert normal_from_selected node:thisNode

			edit_normal_modifier.Reset selection:normal_from_selected node:thisNode
			
		)

		if col then
		(
			maxOps.CollapseNodeTo $ 1 true
			subObjectLevel = 1 
		)

	)
	
	fn lock_unlocked_normal col = 
	(
		local thisNode = selection[1]
		local thisObj = modPanel.getCurrentObject()

		addModifier thisNode (Edit_Normals())
		local edit_normal_modifier = thisNode.modifiers[#Edit_Normals]	
		local num_normal = edit_normal_modifier.GetNumNormals node:thisNode
			
		local temp = #{1..num_normal}
-- 		for i = 1 to num_normal
			
		edit_normal_modifier.makeExplicit selection:temp node:thisNode 
			
		if col then
		(
			maxOps.CollapseNodeTo $ 1 true
		)
		
	)

	on unlockSelectedVert pressed do 
	(
		unlock_normal_selection true
	)
	on lockUnlocked pressed do 
	(
		lock_unlocked_normal true
	)
	
)


addRollout displayToolRollout geNormalTool2019
addRollout workingWithNormalTools geNormalTool2019
addRollout normalEditTools geNormalTool2019
