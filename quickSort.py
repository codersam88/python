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
			
def sortQuickly(list,start,end):
	if(start<end):
		pivInd = partition(list,start,end)
		sortQuickly(list,start,pivInd-1)
		sortQuickly(list,pivInd+1,end)
		
list = [1,3,5,6,4,2]
		
sortQuickly(list,0,5)
print(list)
		
	