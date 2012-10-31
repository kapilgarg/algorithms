def selection_sort(list):
	for j in range(len(list)-1):		
		i=j+1
		while i<=len(list)-1:
			if(list[j]>list[i]):				
				list[j],list[i]=list[i],list[j]
			i=i+1
				
def linear_search(list,num):
	for i in range(len(list)):
		if(list[i]==num):
			return i
		i=i+1	
	return None	