import re
import vertex
import vertexW

def makeAdjListW():
	gfile = open(input("enter the name of graph file"))
	wgraph = [] #contains list of vertex objects 
	nov = int(gfile.readline())#number of vertices
	
	for i in range(nov-1): #for each line
		adjvw = gfile.readline()
		j=0 #for comprehension
		adjvw = re.split(r' ',adjvw[:-1])#leaving last char which is \n
		adjvw = [int(j) for j in adjvw]
		
		currVertex = vertex.Vertex(adjvw[0]) #first location contains name of the vertex
		#print(str(currVertex.name)+' ',end='')
		sizeOfLine=0 #storing name done
		
		while sizeOfLine+1 < len(adjvw):
			c = sizeOfLine +1
			n = sizeOfLine +2
			currAdjVer = vertexW.VertexW(adjvw[c],adjvw[n])
			currVertex.adj.append(currAdjVer)
			#print(str(currVertex.adj[int(sizeOfLine/2)].name)+' '+str(currVertex.adj[int(sizeOfLine/2)].dist)+' ',end='')
			sizeOfLine +=2	
		
		#print()
		wgraph.append(currVertex)
		
	adjvw = gfile.readline() #last line
	j=0
	adjvw = re.split(r' ',adjvw)#leaving last char which is \n
	adjvw = [int(j) for j in adjvw]
		
	currVertex = vertex.Vertex(adjvw[0]) #first location contains name of the vertex
		
	sizeOfLine=0 #storing name done
		
	while sizeOfLine+1 < len(adjvw):
		c = sizeOfLine +1
		n = sizeOfLine +2
		currAdjVer = vertexW.VertexW(adjvw[c],adjvw[n])
		currVertex.adj.append(currAdjVer)
		sizeOfLine +=2	
		
	wgraph.append(currVertex)
		
	return wgraph
	
#adjlW = makeAdjListW()
#print(adjlW)