def partition(list,start,end):
	pivot = list[end]
	
	seperator = start -1 
	
	for i in range(start,end):
		if(list[i] <= pivot):
			seperator+=1
			list[i],list[seperator] = list[seperator],list[i]
			
	seperator+=1			
	list[end],list[seperator] = list[seperator],list[end]
	
	return seperator
	
def partitionAtt(list,start,end):
	pivot = list[end].dist
	
	seperator = start -1 
	
	for i in range(start,end):
		if(list[i].dist <= pivot):
			seperator+=1
			list[i],list[seperator] = list[seperator],list[i]
			
	seperator+=1			
	list[end],list[seperator] = list[seperator],list[end]
	
	return seperator
	
def partitionAttr(list,start,end):
	pivot = list[end].adj[0].dist
	
	seperator = start -1 
	
	for i in range(start,end):
		if(list[i].adj[0].dist <= pivot):
			seperator+=1
			list[i],list[seperator] = list[seperator],list[i]
			
	seperator+=1			
	list[end],list[seperator] = list[seperator],list[end]
	
	return seperator
	
def sortQuickly(list,start,end):
	if(start<end):
		pivInd = partition(list,start,end)
		sortQuickly(list,start,pivInd-1)
		sortQuickly(list,pivInd+1,end)
		
def sortQuicklyAtt(list,start,end):
	if(start<end):
		pivInd = partitionAtt(list,start,end)
		sortQuicklyAtt(list,start,pivInd-1)
		sortQuicklyAtt(list,pivInd+1,end)
		
def sortQuicklyAttr(list,start,end):
	if(start<end):
		pivInd = partitionAttr(list,start,end)
		sortQuicklyAttr(list,start,pivInd-1)
		sortQuicklyAttr(list,pivInd+1,end)
