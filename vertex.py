class Vertex:

	#color = 'w'
		
	def __init__(self,name,color = 'w',dist = 0,mom = None):
		self.name = name
		self.color = color
		self.dist = dist
		self.mom = mom
		self.adj = []
		
	def  __str__(self):
		return "vertex"
		
	def  __repr__(self):
		return "vertex"
		
