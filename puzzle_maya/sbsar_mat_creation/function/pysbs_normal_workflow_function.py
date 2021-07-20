import pysbs
from pysbs import context
from pysbs import sbsenum
from pysbs import sbsgenerator

class PYSBSNormalWorkflowFunction():
	def __init__(self):
		pass

	def cookSBS(self):
		aContext = context.Context()

		startPos = [48, 48, 0]
		xOffset  = [192, 0, 0]
		yOffset  = [0, 192, 0]

		# Create a new SBSDocument from scratch
		sbsDoc = sbsgenerator.createSBSDocument(aContext, aFileAbsPath = destination)

		# Create the graph
		temp = destination.split("/")
		graphName = temp[-1].split(".")[0]
		aGraph = sbsDoc.createGraph(aGraphIdentifier = graphName)