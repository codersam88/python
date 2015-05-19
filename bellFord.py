import adjacencyListW

def bellFord():
	nwgraph = adjacencyListW.makeAdjListW()

	for i in nwgraph:
	  # print('hello')
		print(str(i.name)+' ',end='')
		for j in i.adj:
			print(str(j)+' ',end='')
		print()

bellFord()
