# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.

# Approach: Look at conceptual overview
# TODO: Write approach down
import math
import sys
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
	
	# O(N) time when implemented with siftDown (not nlogn cz majority siftDown calls take less time. It's only upper levels that take logn time). Look at conceptual overview
    def buildHeap(self, array):
		self.size = len(array)
		# initialize heap with given array
		self.heap = array
		last_idx = self.size - 1
		# get last element's parent
		parent = math.floor((last_idx-1)/2)
		while parent >= 0:
			array = self.siftDown(parent)
			parent = parent - 1
        return array

	# O(logN) time
    def siftDown(self, index=None):
		if self.size > 0:
			if index is None:
				current = 0
			else:
				current = index
			# default to current if left nor right child exist. In that case it will break out as valueAt[current] will not be greater than valueAt[child] hence breaking the while loop
			# done because eventually child should be a valid index. 3cases:
			# a. left exists right doesn't exist = child is left (assign infinity to right)
			# b. right exists, left doesn't existt = not possible. complete binary tree by definition
			# c. both right & left don't exist = default to current index. When you will check in while -- you'll break out due to equality. No need to shift down which is exactly what we want once you reach the end
			# can also write proper if-else for this. This is just neater
			# do you even need this? - Think? child < self.size should take care. Remove ternary from left? How do you access value then?
			# TODO: Wrap left or right assignment in a function
			print(current)
			left = 2*current+1 if 2*current+1 < self.size else None
			right = 2*current+2 if 2*current+2 < self.size else None
			print(left, right)
			child = None
			if left is not None and right is not None:
				child = left if self.heap[left] < self.heap[right] else right
			elif left is not None:
				child = left
			elif right is not None:
				child = right
			# child = left if self.heap[left] < self.heap[right] else right
			while child is not None and child < self.size:
				if self.heap[current] > self.heap[child]:
					self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
					current = child
					left = 2*current+1 if 2*current+1 < self.size else None
					right = 2*current+2 if 2*current+2 < self.size else None
					if left is not None and right is not None:
						child = left if self.heap[left] < self.heap[right] else right
					elif left is not None:
						child = left
					elif right is not None:
						child = right
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
			self.siftDown()
			self.size -= 1
        return removed
	
	# O(logN) time including balancing
    def insert(self, value):
        self.heap.append(value)
		self.size += 1
		self.siftUp()
        return
