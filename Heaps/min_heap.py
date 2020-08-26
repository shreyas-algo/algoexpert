# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.

import math
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
		self.size = len(self.heap)

    def buildHeap(self, array):
        # Write your code here.
		
		self.size = len(array)
        pass

    def siftDown(self):
		if self.size > 0:
			current = self.size - 1
			# default to current if left nor right child exist. In that case it will break out as valueAt[current] will not be greater than valueAt[child] hence breaking the while loop
			# done because eventually child should be a valid index. 3cases:
			# a. left exists right doesn't exist = child is left (assign infinity to right)
			# b. right exists, left doesn't existt = not possible. complete binary tree by definition
			# c. both right & left don't exist = default to current index. When you will check in while -- you'll break out due to equality. No need to shift down which is exactly what we want once you reach the end
			# can also write proper if-else for this. This is just neater
			# do you even need this? - Think? child < self.size should take care. Remove ternary from left? How do you access value then?
			# TODO: Wrap left or right assignment in a function
			left = 2*current+1 if 2*current+1 < self.size else current
			right = 2*current+2 if 2*current+2 < self.size else math.inf
			child = left if self.heap[left] < self.heap[right] else right
			while child < self.size:
				if self.heap[current] > self.heap[child]:
					self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
					current = child
					left = 2*current+1 if 2*current+1 < self.size else current
					right = 2*current+2 if 2*current+2 < self.size else math.inf
					child = left if self.heap[left] < self.heap[right] else right
				else:
					break
		return

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
			

    def peek(self):
		if len(self.heap) > 0:
			return self.heap[0]
		return None

    def remove(self):
        # Write your code here.
		if self.size > 0:
			
			self.size -= 1
        pass

    def insert(self, value):
        # Write your code here.
		
		self.size += 1
        pass
