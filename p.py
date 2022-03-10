from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print( 'func:%r took: %2.4f sec' % (f.__name__, te-ts))
        return result
    return wrap

@timing
def f(a):
    for _ in range(a):
        i = 0
    return -1


@timing
def f(array):
    def fnq(array):
        if len(array) <= 1: 
            return array
        higher = [i for i in array[1:] if i > array[0]]
        lower = [i for i in array[1:] if i <= array[0]]
        return fnq(lower) + [array[0]] + fnq(higher)
    return fnq(array)

def partition(arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

@timing
def im (arr, low, high):
    def impq(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            impq(arr, low, pi-1)
            impq(arr, pi+1, high)
    return impq(arr,low,high)

import random
randomlist = []
testlength = int(input("gimmi the length: "))
for i in range(0,testlength):
    n = random.randint(1,testlength)
    randomlist.append(n)

print(randomlist)
# f(randomlist)
# im(randomlist,0,len(randomlist)-1)