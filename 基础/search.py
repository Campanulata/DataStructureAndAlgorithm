def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
        	return ind
    return None

def binary_search(li,tar):
	left=0
	right=len(li)-1
	
	while(left<=right):
		mid=(left+right)//2
		if li[mid]==tar:
			return mid
		elif li[mid]<tar:
			left=mid+1
		else:
			right=mid-1
	return None




seq = [1, 2, 3, 4,5]
print(linear_search(seq,2))
print(binary_search(seq,2))
