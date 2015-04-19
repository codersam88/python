import re
import vertex

def makeGraph():

	gfile = open('graph.txt')
	graph = []

	nov = int(gfile.readline())

	for i in range(nov-1):#doing separately for last because last doesn't end with \n
		line = gfile.readline()
		
		adjv = re.split(r' ',line[:-1]) #except last
		adjv = [int(i) for i in adjv] #converting to int
		currVer = vertex.Vertex(adjv[0])
		currVer.adj = adjv[1:]
		graph.append(currVer)
	
	line = gfile.readline()		
	adjv = re.split(r' ',line) #because last line doesn't have new line char
	adjv = [int(i) for i in adjv]
	currVer = vertex.Vertex(adjv[0])
	currVer.adj = adjv[1:]
	graph.append(currVer)
	
	#print(graph)
	
	return graph


