"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	#checking base case
	if right >= left:

		mid = (right + left) // 2

		#if element is at the middle
		if mylist[mid] == key:
			return mid
		#if element is smaller than mid, if so it is present in left
		elif mylist[mid] > key:
			return binary_search(mylist, left, mid - 1, key)
		#else thhe element is in the right
		else:
			return binary_search(mylist, mid + 1, right, key)

	else:
		#else the element is not in the list
		return -1


def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1,2,3,4,5], 4) == 3
	assert binary_search([1,2,3,4,5], 7) == -1


def time_search(search_fn, mylist, key):
	#start time
	start = time.time()
	search_fn(mylist, key)
	#end time
	end = time.time()
	#calculate runtime
	runtime = start - end

	return runtime*1000


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):

	tuplelist = []
	alist = []
	key = -1

	for n in sizes:
		for j in range(0, n-1):
			alist.append(j)

		binary_search_time = time_search(binary_search, alist, -1)
		linear_search_time = time_search(linear_search, alist, -1)
		tuple = (n, linear_search_time, binary_search_time)
		tuplelist.append(tuple)

		return tuplelist


def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

print_results(compare_search())
