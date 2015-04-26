import adjacencyListW

def makeMST():
	
	wgraph = adjacencyListW.makeAdjListW()
	
	disj=[]
	
	for ver in wgraph:
		
		discurr = [ver.name]	
		disj.append(discurr)
		
	for ver in wgraph:
	
makeMST()