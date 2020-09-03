# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.

# Approach: Look at conceptual overview. 
# The implementation is based on two basic methods: siftUp & siftDown
# peek: return min. heap[0]
# siftUp: works on last element. compare with parent and keep swapping if parent is larger in value
# siftDown: works on top if no index passed. compare with smaller child and keep swapping if smaller child is smaller than the parent
# insert: insert in end and siftUp
# remove: removes top (heap only works on top - min value). First swap top with last element. Remove last (easier -- simple pop). Then siftDown
# buildHeap: initialize with given array. Call siftDown on all on-leaf nodes starting from the last non-leaf node

# extra:
# 1. maintain heap size all the time (start from buildHeap) and keep updating on every insert / remove call so that it can be used in internal calls in constant time
# 2. Indexing:
# parent = int((index - 1)/2)
# left_child = 2*index + 1
# right_child = 2*index + 2

# TODO: Write approach down
# TODO: watch code walkthrough

# Learning: As long as you understand the conceptual overview, code will be fine. Eg loko at the code. It might look complicated but the underlying logic is pretty straight forward (Look at conceptual overview)
import math
import sys
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
	
	# O(N) time when implemented with siftDown (not nlogn cz majority siftDown calls take less time. It's only upper levels that take logn time). Look at conceptual overview
    def buildHeap(self, array):
        # initialize heap with given array and its size
		self.size = len(array)
		self.heap = array
		last_idx = self.size - 1
		# get last element's parent
		parent = math.floor((last_idx-1)/2)
		while parent >= 0:
			array = self.siftDown(parent)
			parent = parent - 1
        return array

	# O(logN) time
    # index used for buildHeap() when you need to siftDown every parent
    def siftDown(self, index=None):
		if self.size > 0:
			if index is None:
				current = 0
			else:
				current = index
			child = self.getSmallerChild(current)
			while child is not None and child < self.size:
				if self.heap[current] > self.heap[child]:
					self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
					current = child
					child = self.getSmallerChild(current)
				else:
					break
		return self.heap
		
	# O(logN) time
    def siftUp(self):
		current = self.size - 1
		parent = math.floor((current-1)/2)
        while parent >= 0:
			if self.heap[current] < self.heap[parent]:
				self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
				current = parent
				parent = math.floor((current-1)/2)
			else:
				break
		return
			
	# O(1) time
    def peek(self):
		if len(self.heap) > 0:
			return self.heap[0]
		return None
	
	# O(logN) time including balancing
    def remove(self):
        removed = None
		if self.size > 0:
			# swap top with last element so that it can be removed
			self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
			removed = self.heap.pop()
			self.size -= 1
			self.siftDown()
        return removed
	
	# O(logN) time including balancing
    def insert(self, value):
        self.heap.append(value)
		self.size += 1
		self.siftUp()
        return
	
	# helper method. O(1) time
	def getSmallerChild(self, current):
		left = 2*current+1 if 2*current+1 < self.size else None
		right = 2*current+2 if 2*current+2 < self.size else None
		child = None
		if left is not None and right is not None:
			child = left if self.heap[left] < self.heap[right] else right
		elif left is not None:
			child = left
		elif right is not None:
			child = right
		return child
