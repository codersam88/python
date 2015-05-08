import adjacencylist
import queue
import vertex

def breadthFirstSearch(src):

	src-=1 #because n in graph is represented by n-1 in program
	bfst = queue.Queue() #stores breadth first tree
	graph = adjacencylist.makeGraph()
	
	graph[src].color = 'g'
	graph[src].dist = 0
	graph[src].mom = None
	
	bfst.put(src)
	
	while not bfst.empty():
		ver = bfst.get()
		print("name "+str(graph[ver].name))
		
		for i in graph[ver].adj:
			
			if graph[i-1].color == 'w':
				graph[i-1].color = 'g'
				graph[i-1].dist = graph[ver].dist + 1
				graph[i-1].mom = graph[ver].name
				bfst.put(i-1)
				
	return graph
	
src = input("Enter the source you want ")
	
bfst = breadthFirstSearch(int(src))

print(bfst)

for i in bfst:
	print("name "+str(i.name))
	print("mom "+str(i.mom))
	print("dist "+str(i.dist))
	print()