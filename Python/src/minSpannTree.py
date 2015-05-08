import adjacencyListW
import disjoint
import edge
import quickSort

def makeMST():
	
    wgraph = adjacencyListW.makeAdjListW()
	
    disj = [] #represents list of disjoint sets
    edgesList = []#stores list of edges
    mst=[] #stores mst
	
    #print('printing the disjoint set')
	
    for ver in wgraph: #making disjoint sets and sorting edges of each vertex
		
        discurr = []	#creating each disjoint set
        discurr.append(disjoint.disjVer(ver.name, discurr))
        #print(str(discurr[0].name) + ' ', end='')
        disj.append(discurr)
		
        quickSort.sortQuicklyAtt(ver.adj, 0, len(ver.adj)-1)#sorting edges adj to each vertex
    #print()
    #print('done printing disjoint sets')	
        
    for ver in wgraph: #making list of edges
		
        for i in ver.adj: #just for printing edges of vertices
            	
            edgesList.append(edge.edge(disj[int(ver.name)-1][0], disj[int(i.name)-1][0], i.dist))
    
    #print('printing in disj')#check again
    #for i in disj:
    #    print(str(i[0].name) + ' ', end='')
		
    #print('done printing disjoint sets')
    '''
    for i in edgesList:
        print(str(i.frm.name)+' '+str(i.to.name)+' '+str(i.dist)+' ,',end='')
    print()
    '''    
        
    quickSort.sortQuicklyAttr(wgraph, 0, len(wgraph)-1)#sorts all the vertices in adjacency list
    '''
    print('after quick sort')
	
    for ver in wgraph:
        print(str(ver.name) + ' ', end='')
        for i in ver.adj: #just for printing edges of vertices
            print(str(i.name) + ' ' + str(i.dist) + ' ', end='')	
        print()
	
    print('done printing after quick sort')
    
    
    for i in wgraph: #just for printing
        print(str(i.name) + ' ', end='')
        for j in i.adj: #just for printing
            print(str(j.dist) + ' ', end='')	
        print()	
    '''
    quickSort.sortQuicklyAtt(edgesList, 0, len(edgesList)-1)
	
    
    print('printing sorted edges')
	
    for i in edgesList:
        print(str(i.frm.name)+' '+str(i.to.name)+' '+str(i.dist)+' ,',end='')
    print()
		
    print('done printing sorted edges')
    
    print('here comes the mst')
	
    for i in edgesList:
        if(i.frm.list != i.to.list):
            mst.append(i)
            toList = i.to.list
            #print('tolist '+str(toList))
            for j in toList:
                j.list = i.frm.list
                i.frm.list.append(j)
                
           
                        
    for i in mst:
        print(str(i.frm.name)+' '+str(i.to.name)+' '+str(i.dist)+' ,',end='')
    print()
			
makeMST()