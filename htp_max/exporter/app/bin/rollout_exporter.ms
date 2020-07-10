rollout exporter_Floater "Exporter" width:350 height:600
(
	button btnOpenExporterUI "Exporter Tool" width:140 height:21 align:#center tooltip:"Open Exporter Tool"
	on btnOpenExporterUI pressed do
	(
		--python.executeFile @"\\glassegg.com\TOOLS\TECHNICAL_SCRIPT\Projects\Environment_Default\Max\exporter\app\bin\run.py"
		python.executeFile (path_project + "/" + name_project + "/Max/exporter/app/bin/run.py")
	)
)