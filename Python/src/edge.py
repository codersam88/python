class edge:
	def __init__(self,frm,to,dist):
		self.frm = frm
		self.to = to
		self.dist = dist
	
	def __repr__(self):
		return str(self.frm)+' '+str(self.to)+' '+str(self.dist)