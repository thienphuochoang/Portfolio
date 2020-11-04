try destroydialog rl_faogen catch()
rollout rl_faogen "Faogen 3 AO bake" width:162 height:224
(
	groupBox 'grp1' "Settings" pos:[4,4] width:154 height:184 align:#left
	checkbox 'ui_hemi' "Hemisphere mode" pos:[13,74] width:109 height:15 checked:false align:#left
	checkbox 'ui_env' "Use all scene objects" pos:[13,96] width:124 height:15 checked:true align:#left
	spinner 'ui_quality' "Quality" pos:[44,121] width:70 height:16 range:[1,100,15] type:#integer align:#left
	dropdownList 'bake_type' "Bake Type" pos:[13,143] width:136 height:40 items:#("Vertex", "Texture") align:#left
	
	button 'ui_bake' "Bake Selected" pos:[41,194] width:83 height:21 align:#left
	dropDownList 'ddlWidth' "    Width" pos:[12,24] width:52 height:40 align:#left items:#("128","256","512","1024","2048","4096") selection:3
	dropDownList 'ddlHeight' "    Height" pos:[85,24] width:52 height:40 align:#left items:#("128","256","512","1024","2048","4096") selection:3
	
	-- get path to faogenbatch.exe
	fn get_batch =
	(
		registry.openKey HKEY_LOCAL_MACHINE "Software\Microsoft\Windows\CurrentVersion\Uninstall\faogen3" accessRights:#readOnly key:&key
		if key != undefined then
		(
			registry.queryValue key "UninstallString" type:&type value:&uninst_cmd
			if uninst_cmd != undefined then
				substituteString uninst_cmd "uninstall.exe" "faogenbatch.exe"
		)
	)
	
	local batch_exe = get_batch()
	
	-- create temporary copy for exporting
	fn copy_object obj prefix =
	(
		if obj.category != #Editable_Objects then converttopoly obj -- fix a weird bug with unecessary faces generated on some primitives (teapot) directly converted in "editable_mesh"
		convertToMesh obj
		obj_copy = copy obj
		id = formattedPrint obj.inode.handle format:"x"
		obj_copy.name = prefix+id
		obj_copy
	)

	-- assing vertex colors from src object to dst
	fn assign_vcolors src dst =
	(
		if src.faces.count == dst.faces.count then
		(
			meshop.setMapSupport dst 0 true
			numverts = meshop.getNumMapVerts src 0
			meshop.setNumMapVerts dst 0 numverts
			for i = 1 to numverts do
			(
				v = meshop.getMapVert src 0 i
				meshop.setMapVert dst 0 i v
			)
			
			for i = 1 to meshop.getNumMapFaces src 0 do
			(
				f = meshop.getMapFace src 0 i
				meshop.setMapFace dst 0 i f
			)
			
			dst.showVertexColors = true
			dst.vertexColorsShaded = false
			dst.vertexColorMapChannel = 0
			dst.vertexColorType = #color 
		)
	)

	function fnbakeVertexColor batch_exe hemis quality= 
	(
		disableSceneRedraw()
		infile = sysinfo.tempdir+"faogen_in.fbx"
		outfile = sysinfo.tempdir+"faogen_out.fbx"
		
		cmdline = "call " + batch_exe+" -i \""+infile+"\" -o \""+outfile+"\" -vert -only faogenbake# -q "+quality as string;
		if hemis then
			cmdline += " -hemiZ"
		
		cloned_selection = for obj in selection where not obj.ishidden collect copy_object obj "faogenbake#"
		cloned_env = #()
		
		if ui_env.checked then
		(
			max select invert
			deselect cloned_selection
			cloned_env = for obj in selection where not obj.ishidden collect copy_object obj "faogenoccl#"
			select cloned_env
		)
		else clearSelection()
		
		selectmore cloned_selection
		exportfile infile #noprompt selectedOnly:true
		delete cloned_selection
		delete cloned_env
		
		DOSCommand cmdline
		
		importfile outfile #noprompt
		
		for obj in geometry where substring obj.name 1 11 == "faogenbake#" do
		(
			id = bit.hexasint (substring obj.name 12 100)
			dst = maxOps.getNodeByHandle id
			assign_vcolors obj dst
		)
		
		loaded_objects = for obj in geometry where substring obj.name 1 11 == "faogenbake#" or substring obj.name 1 11 == "faogenoccl#" collect obj
		delete loaded_objects
		
		enableSceneRedraw()
	)

	function fnbakeTexture batch_exe width height hemis quality=
	(
		if maxfilename != "" then
		(
			--disableSceneRedraw()
			infile = sysinfo.tempdir+"faogen_in.fbx"
			--outfile = sysinfo.tempdir+"faogen_out.fbx"
			arrName = filterstring maxfilename "."
			
			outfile = maxFilePath +  arrName[1] + "_ao" + ".tga"
			print (outfile)
			-- get selection and swap UV2 to UV 1
			maxOps.cloneNodes $ cloneType:#copy newNodes:&nnl
			select nnl
			
			--swap UV2 to UV1 
			channelInfo.CopyChannel $ 3 2
			channelInfo.PasteChannel $ 3 1
			channelInfo.NameChannel $ 3 1 "-none-"
			maxOps.CollapseNode $ off
			
			-- export file 
			exportfile infile #noprompt selectedOnly:true
			
			-- delete tmp file
			delete $
			
			cmdline = "call " + batch_exe+" -i \""+infile+"\" -o \""+outfile+"\" -width "+ (width as string) + " -height "+ (height as string) + " -q "+ (quality as string) + " -msaa 8";
			if hemis then
				cmdline += " -hemiZ"
			
			print (cmdline)
			DOSCommand cmdline
			
			--argv = outfile
			--bi = Python.Import "__builtin__"
			--python.reload bi
			--tp = bi.List(#(argv))
			--print tp
			--python.init()
			--python.Execute "import sys"
			--python.execute "sys.path.append('//glassegg.com/TOOLS/TECHNICAL_SCRIPT/Projects/Environment_Default/Lib/pymodule')"
			--python.Execute "import QzImageMagick"
			--python.Execute "reload(QzImageMagick)"
			--pythonCommand = "QzImageMagick.convert_model(in_textures = [r'"+argv+"'] , out_textures = [r'"+argv+"'])"
			--python.Execute pythonCommand throwOnError:True clearUndoBuffer:false
			--enableSceneRedraw()
		)
		else
		(
			messageBox "Please save your work before AO baking"
		)
	)
	
	on ui_bake pressed do
	(
		if batch_exe == undefined then
		(
			messagebox "Faogen 3 not found.\nGet it from www.faogen.com"
			destroydialog rl_faogen	
		)
		else
		(
			
			if bake_type.selection == 1 then
				fnbakeVertexColor batch_exe ui_hemi.checked ui_quality.value
			else
				fnbakeTexture batch_exe ddlWidth.selected ddlHeight.selected ui_hemi.checked ui_quality.value
		)
	)
)

createdialog rl_faogen