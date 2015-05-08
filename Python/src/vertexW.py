class VertexW:
	def __init__(self,name,dist=0):
		self.name = name
		self.dist = dist
		
	def __repr__(self):
		return str(self.name)+' '+str(self.dist)