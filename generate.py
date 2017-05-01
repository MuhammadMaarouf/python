
def gng(start, end): 
	number = []
	if start == end :
		for x in range (end):
			number=[start]
	elif(start<end):
		for x in range (end-start+1):
			number.append(x+start)
	return number 
