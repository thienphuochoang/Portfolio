-- try (destroyDialog CreateFX ); catch()

rollout CreateFX "Debug Shader FX" width:352 height:288
(
	radioButtons 'rdo_debug' "Debug Mode:" pos:[8,64] width:332 height:46 labels:#("Default", "Albedo", "Roughness", "Metalness", "Normal", "AO") columns:4 align:#left
	button 'btn_create' "Create ShaderFX" pos:[8,8] width:160 height:39 align:#left
	button 'btn_restore' "Restore Old Material" pos:[184,8] width:160 height:39 align:#left
	slider 'sld_env' "Env Rotation" pos:[8,120] width:328 height:44 range:[0,360,0] type:#float orient:#horizontal align:#left
	slider 'sld_spec' "Spec Scale" pos:[8,168] width:328 height:44 range:[0,5,1] align:#left
	slider 'sld_diff' "Diff Scale" pos:[8,216] width:328 height:44 range:[0,5,1] align:#left
	
-- 	funciton
	fn UpdateSceneMaterials =
	(
		usedMaterials = for node in objects collect node.material
		for j = sceneMaterials.count to 1 by -1 where (finditem usedMaterials sceneMaterials[j] == 0) do (
			deleteitem sceneMaterials j
		)
		for m = 1 to sceneMaterials.count do(
			meditMaterials[m] = sceneMaterials[m]
		)
	)

	fn createFXmat name albedo surface ao decal normal= (
	-- 	sceneMat = for mat in scenematerials collect mat
		dxFile = "S:\\iRacing_Env_20\\Scenes\\Technical\\Tool\GE_Shaders\\ge_iRacing_Decal.fx"
		IBLSpec = "S:\\iRacing_Env_20\\Scenes\\Technical\\Tool\GE_Shaders\\IBL_Cubemaps\\studio05SpecularHDR.dds"
		IBLDiff = "S:\\iRacing_Env_20\\Scenes\\Technical\\Tool\GE_Shaders\\IBL_Cubemaps\\studio05DiffuseHDR.dds"
		IBLbdrf = "S:\\iRacing_Env_20\\Scenes\\Technical\\Tool\GE_Shaders\\IBL_Cubemaps\\SchlickBrdf.dds"
		
		dxIndex = DirectX_9_Shader ()
		dxIndex.name = name
		dxIndex.effectfile = dxFile
		dxIndex.g_IblSpecTexture = openbitmap IBLSpec
		dxIndex.g_IblDiffTexture = openbitmap IBLDiff
		dxIndex.g_IblBrdfTexture = openbitmap IBLbdrf
		
		dxIndex.g_AlbedoTexture = openbitmap albedo
		dxIndex.g_NormalTexture = openbitmap normal
		dxIndex.g_SurfaceTexture = openbitmap surface
		dxIndex.g_OcclusionTexture = openbitmap ao
		dxIndex.g_DecalTexture = openbitmap decal
		dxIndex
	)

	fn createFxFromSelectMultiMat = (
		if selection.count != 0 do( 
			for sel in selection  do(
				objMat = sel.mat
				dataMat = #()
				if objMat != undefined and classof objMat == multimaterial then(
					for submat in objMat do (
						subdata = #(submat.name)
						diff = submat.diffuseMap
						if diff != undefined then (
							append subdata diff.fileName
						)
						else(
							append subdata ""
						)
						
						spec = submat.specularMap
						if spec != undefined then (
							append subdata spec.fileName
						)
						else(
							append subdata ""
						)
						
						ao = submat.filterMap
						if ao != undefined then (
							append subdata ao.fileName
						)
						else(
							append subdata ""
						)
						
						decal = submat.refractionMap
						if decal != undefined then (
							append subdata decal.fileName
						)
						else(
							append subdata ""
						)
						
						normal = submat.bumpMap
						if normal != undefined then (
							append subdata normal.normal_map.fileName
						)
						else(
							append subdata ""
						)
						append dataMat subdata
					)
				)
				dupMultiMat = multimaterial numsubs:dataMat.count
			-- 	UpdateSceneMaterials()
				dxIndex = sceneMaterials.count+1
				dupMat = multimaterial numsubs:dataMat.count
				dupMat.name = objMat.name + "_FX"
				for d = 1 to dataMat.count do(
					fxMat = createFXmat dataMat[d][1] dataMat[d][2] dataMat[d][3] dataMat[d][4] dataMat[d][5] dataMat[d][6]
					dupMat[d] = fxMat
				)
				meditMaterials[dxIndex] = dupMat
				sel.mat = dupMat
			)
		)
	)

	function debugSceneFxMaterial state env spec diff = (
		mats = #()
		for mat in scenematerials do (
			if classof mat == Multimaterial and matchPattern mat.name pattern: "*_FX" then (
				append mats mat		
			)			
		)
		for fx in mats do(
			for m in fx do(
				m.g_CheckerUVChannel = 0
				case  state of (
					1: m.g_SceneDebugMode = 0
					2: m.g_SceneDebugMode = 15 --albedo
					3: m.g_SceneDebugMode = 20 --roughness
					4: m.g_SceneDebugMode = 21 --metal
					5: m.g_SceneDebugMode = 17 --normal
					6: m.g_SceneDebugMode = 19 --ao
				)
				m.g_IblEnvRotation = env
				m.g_IblSpecScale = spec
				m.g_IblDiffScale = diff
			)
		)
	)
	
	fn restoreOldMat =(
		if selection.count != 0 do(
			for sel in selection do(
				curMat = sel.mat
				oldName = substituteString curMat.name "_FX" ""
				for mat in scenematerials do(
					if classof mat == Multimaterial and matchPattern mat.name pattern: oldName do(
						sel.mat = mat
					)
				)
			)
			UpdateSceneMaterials()
		)
	)
	
	on btn_create pressed do(
		createFxFromSelectMultiMat()
	)
	
	on btn_restore pressed do(
		restoreOldMat()
	)
	
	on rdo_debug changed e do(
		debugSceneFxMaterial e sld_env.value sld_spec.value sld_diff.value
	)
	
	on sld_env changed e do(
		debugSceneFxMaterial rdo_debug.state sld_env.value sld_spec.value sld_diff.value
	)
	
	on sld_spec changed e do(
		debugSceneFxMaterial rdo_debug.state sld_env.value sld_spec.value sld_diff.value
	)
	
	on sld_diff changed e do(
		debugSceneFxMaterial rdo_debug.state sld_env.value sld_spec.value sld_diff.value
	)
)

-- createDialog CreateFX