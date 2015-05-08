import adjacencyListW
import quickSort
import disjoint
import edge

def makeMST():
	
	wgraph = adjacencyListW.makeAdjListW()
	
	disj=[] #represents list of disjoint sets
	edgesList =[]
	
	print('printing the vertices')
	
	for ver in wgraph: #making disjoint sets and sorting adj vertices of each vertex
		
		discurr = []	#creating each disjoint set
		discurr.append(disjoint.disjVer(ver.name,discurr))
		print(str(discurr[0].name)+' ',end ='')
		disj.append(discurr)
		
		quickSort.sortQuicklyAtt(ver.adj,0,len(ver.adj)-1)
		
	for ver in wgraph:
		
		for i in ver.adj: #just for printing edges of vertices
			print(str(i.name)+' '+str(i.dist)+' ',end ='')	
			edgesList.append(edge.edge(disj[int(ver.name)-1],disj[int(i.name)-1],i.dist))
		print()
		
	print('printing disjoint set')
	
	for i in disj:
		print(str(i[0].name)+' ',end='')
		
	print('done printing disjoint sets')
	
	print(edgesList)
	print('done printing vertices and their edges')
	quickSort.sortQuicklyAttr(wgraph,0,len(wgraph)-1)#sorts all the vertices in adjacency list
	
	print('after quick sort')
	
	for ver in wgraph:
		print(str(ver.name)+' ',end ='')
		for i in ver.adj: #just for printing edges of vertices
			print(str(i.name)+' '+str(i.dist)+' ',end ='')	
		print()
	
	print('done printing after quick sort')
	
	for i in wgraph: #just for printing
		print(str(i.name)+' ',end = '')
		for j in i.adj: #just for printing
			print(str(j.dist)+' ',end ='')	
		print()	
		
	quickSort.sortQuicklyAtt(edgesList,0,len(edgesList)-1)
	
	print('printing sorted edges')
	
	for i in edgesList: #just for printing edges of vertices
		print(str(i.frm)+' '+str(i.to)+' '+' '+str(i.dist),end ='')	
		print()
		
	print('done printing sorted edges')
	
	print('here comes the mst')
	
	for i in edgesList:
		if(disj[i.frm-1].list != disj[i.to-1].list):
			print(str(i.frm)+' '+str(i.to)+' '+' '+str(i.dist))
			disj[i.frm-1].list = disj[i.to-1].list
	
			
makeMST()