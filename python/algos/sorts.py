#!/usr/bin/env python3
 
from collections import deque
import random
import time
 
### INSERTION SORT ###
def InsertionSort ( unsorted ):
    sorted = [ unsorted[0] ]
    for i in range(1, len(unsorted)):
        j = 0
        while j < len(sorted) and sorted[j] < unsorted[i]:
            j += 1
        sorted.insert(j, unsorted[i])
        #print ( sorted )
    return sorted
 
### SELECTION SORT ###
# based on creating a new sorted list by extracting elements from the unsorted list
def SelectionSort1 ( unsorted ):
    sorted = []
    for j in range( len(unsorted) ):
        smallest = max(unsorted)
        for i in range( len(unsorted) ):
            if unsorted[i] <= smallest:
                smallest = unsorted[i]
                position = i
        sorted.append(smallest)
        del unsorted[position]
    return sorted
 
# based on swapping elements
def SelectionSort2 ( array ):
    for i in range( len(array) ):
        smallest = i
        for j in range( i+1, len(array) ):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array
 
### MERGESORT ###
def Merge ( array, lo, md, hi ):
    queue1 = deque(array[lo:md+1])
    queue2 = deque(array[md+1:hi+1])
 
    pos = lo
    while len(queue1) and len(queue2):
        if queue1[0] < queue2[0]:
            array[pos] = queue1.popleft()
        else:
            array[pos] = queue2.popleft()
        pos += 1
 
    while len(queue1):
        array[pos] = queue1.popleft()
        pos += 1
    while len(queue2):
        array[pos] = queue2.popleft()
        pos += 1
 
def MergeSort ( array, lo, hi ):
    if hi > lo:
        md = int ((hi+lo)/2)
        MergeSort ( array,lo,md )
        MergeSort ( array,md+1,hi )
        Merge ( array, lo, md, hi )
 
### QUICKSORT ###
def Partition ( array, lo, hi ):
    # print ( ''.join(array[lo:hi+1]) )
    pivot = array[hi]
 
    pivotPosition = lo
    for i in range ( lo, hi ):
        if array[i] < pivot:
            array[pivotPosition], array[i] = array[i], array[pivotPosition]
            pivotPosition += 1
 
    array[pivotPosition], array[hi] = array[hi], array[pivotPosition]
    # print ( ''.join(array[lo:hi+1]) )
    return pivotPosition
 
def QuickSort ( array, lo, hi ):
    # avoid problems for almost sorted data
    if lo == 0 and hi == len(array) - 1:
        random.shuffle ( array )
    if hi > lo:
        pivotPosition = Partition ( array, lo, hi )
        QuickSort ( array, lo, pivotPosition-1 )
        QuickSort ( array, pivotPosition+1, hi )
 
### MAIN ###
if __name__ == "__main__":
    # unsorted = [ 'T', 'H', 'I', 'S', 'L', 'I', 'S', 'T', 'I', 'S', 'U', 'N', 'S', 'O', 'R', 'T', 'E', 'D' ]
    # print ( ''.join(unsorted) )
    #N = 20000
    N = 10
 
    unsorted = [int(random.random() * N) for i in range(N)]
    start = time.time()
    sorted = InsertionSort( unsorted )
    print ( "InsertionSort:  " + str( time.time() - start ) )
    # print ( ''.join(sorted) )
"""
    unsorted = [int(random.random() * N) for i in range(N)]
    start = time.time()
    sorted = SelectionSort1( unsorted )
    print ( "SelectionSort1: " + str( time.time() - start ) )
    # print ( ''.join(sorted) )
 
    unsorted = [int(random.random() * N) for i in range(N)]
    start = time.time()
    sorted = SelectionSort2( unsorted )
    print ( "SelectionSort2: " + str( time.time() - start ) )
    # print ( ''.join(sorted) )
 
    array = [int(random.random() * N) for i in range(N)]
    start = time.time()
    MergeSort( array, 0, len(array)-1 )
    print ( "MergeSort:      " + str( time.time() - start ) )
    # print ( ''.join(array) )
 
    array = [int(random.random() * N) for i in range(N)]
    start = time.time()
    QuickSort( array, 0, len(array)-1 )
    print ( "QuickSort:      " + str( time.time() - start ) )
    # print ( ''.join(array) )
"""
