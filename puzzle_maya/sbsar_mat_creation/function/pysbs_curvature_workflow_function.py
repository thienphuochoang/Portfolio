import sys
sys.path.append(r"D:\WIP_Portfolio\modules\Lib\site-packages")
import pysbs
from pysbs import context
from pysbs import sbsenum
from pysbs import sbsgenerator

class PYSBSCurvatureWorkflowFunction():
	def __init__(self):
		pass

	def getInputs(self, *args, **kwargs):
		self.destination = kwargs['destination']
		self.colorIDNodePath = kwargs['colorIDNodePath']
		self.AmbientOcclusion_Node_Path = kwargs['AmbientOcclusion_Node_Path']
		self.Curvature_Node_Path = kwargs['Curvature_Node_Path']
		self.Position_Node_Path = kwargs['Position_Node_Path']
		self.WorldSpaceNormal_Node_Path = kwargs['WorldSpaceNormal_Node_Path']
		self.substancePath = kwargs['substancePath']
		self.MaterialNameAndColorDict = kwargs['MaterialNameAndColorDict']
		self.SBSDependencyPath = kwargs['SBSDependencyPath']

	def cookSBS(self):
		aContext = context.Context()

		startPosX = 0
		startPosY = 0
		startPosZ = 0
		#startPos = [48, 48, 0]
		#xOffset  = [192, 0, 0]
		#yOffset  = [0, 192, 0]

		# Create a new SBSDocument from scratch
		sbsDoc = sbsgenerator.createSBSDocument(aContext, aFileAbsPath = destination)

		# Create the graph
		temp = destination.split("/")
		graphName = temp[-1].split(".")[0]
		aGraph = sbsDoc.createGraph(aGraphIdentifier = graphName)

		

		# Create Input Node
	
		AmbientOcclusion_Node   = aGraph.createBitmapNode(aSBSDocument  = sbsDoc,
														  aResourcePath = self.AmbientOcclusion_Node_Path,
														  aParameters   = {sbsenum.CompNodeParamEnum.COLOR_MODE:False},
														  aGUIPos		= [startPosX, startPosY, startPosZ])
		
		Curvature_Node		  = aGraph.createBitmapNode(aSBSDocument	= sbsDoc,
														 aResourcePath  = self.Curvature_Node_Path,
														 aParameters	= {sbsenum.CompNodeParamEnum.COLOR_MODE:False},
														 aGUIPos		= [startPosX, startPosY + 100, startPosZ])
		
		Position_Node		   = aGraph.createBitmapNode(aSBSDocument   = sbsDoc,
														 aResourcePath  = self.Position_Node_Path,
														 aParameters	= {sbsenum.CompNodeParamEnum.COLOR_MODE:True},
														 aGUIPos		= [startPosX, startPosY + 200, startPosZ])
		
		WorldSpaceNormal_Node   = aGraph.createBitmapNode(aSBSDocument  = sbsDoc,
														 aResourcePath  = self.WorldSpaceNormal_Node_Path,
														 aParameters	= {sbsenum.CompNodeParamEnum.COLOR_MODE:True},
														 aGUIPos		= [startPosX, startPosY + 300, startPosZ])

		sbsDoc.writeDoc()