string1 = input("enter the first string ")
string2 = input("enter the second string ")

length = []
subs = []

print(length)

for i in range(0,len(string1)+1):

	length.append([])
	subs.append([])
	
	for j in range(0,len(string2)+1):
		
		length[i].append(0)
		subs[i].append(0)
		#pass
i1=0
for i in string1:
	
	j1=0
	
	for j in string2:
	
		if(i==j):
			
			length[i1+1][j1+1] = length[i1][j1]+1
			subs[i1+1][j1+1] = 'c'
			
		elif(length[i1][j1+1] >= length[i1+1][j1]):
		
			length[i1+1][j1+1] = length[i1][j1+1]
			subs[i1+1][j1+1] = 'u'
			
		else:
			
			length[i1+1][j1+1] = length[i1+1][j1]
			subs[i1+1][j1+1] = 'l'
			
		j1+=1
		
	i1+=1
		
i = len(string1)
j = len(string2)

def lcs(i,j):

	if(subs[i][j]==0):
		return
	
	if(subs[i][j]=='c')	:
		lcs(i-1,j-1)
		print(string2[j-1],end='')
	elif(subs[i][j]=='l'):
		lcs(i,j-1)
	else:
		lcs(i-1,j)
	
	
lcs(i,j)

print(length)
print(subs)