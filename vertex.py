class Vertex:

	#color = 'w'
		
	def __init__(self,name,color = 'w',dist = 0,mom = None):
		self.name = name
		self.color = color
		self.dist = dist
		self.mom = mom
		self.adj = []
			
	def  __repr__(self):
	
		namePlusAdj = str(self.name)
		for i in self.adj:
			namePlusAdj+=' '+str(i.name)+' '+str(i.dist)
			
		return str(len(self.adj))
		
