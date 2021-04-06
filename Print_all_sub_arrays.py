#number of elements in list is n
n=3
#lsi is the list or array
lst = [2,7,5]

#subarray gen is the recursive function that will print all the subarrays
def subarray_gen(lst,start,end):
	#this is the end of recursion
	if end == n:
		return
	#passing to next recursion
	elif start>end:
		return subarray_gen(lst,0,end+1)
	#printing the present subarray
	else:
		print(lst[start:end + 1])
		return subarray_gen(lst, start + 1, end)

#calling the subarray gen function or driver code
subarray_gen(lst,0,0)




