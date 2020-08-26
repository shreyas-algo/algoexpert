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
        # Write your code here.
        pass

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
