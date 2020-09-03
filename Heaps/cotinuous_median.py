# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.

# Approach: 
# maintain 2 heaps: max heap and min heap. initiate with first two numbers. first number (a[0]) being the top of a max heap and the second number (a[1]) being the top of a min heap. 
# As any number smaller than a[0] comes for insertion, it goes to the max heap and then gets balanced (so that max heap property is maintained). Whereas a number bigger than a[0] comes, insert in the min heap and balace
# At any point if |minHeap.size - maxHeap.size| > 1 -> then remove top from min/max heap (depending on which is bigger), insert in the other heap and balance
# In this way, the tops always maintain the middle numbers

# if total size is even:
# median = top(minHeap) + top(maxHeap) / 2
# if odd:
# median = top(larger heap)
import math
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None 
		self.size = 0
		self.maxHeap = MaxHeap()
		self.minHeap = MinHeap()

    def insert(self, number):
        if self.size == 0:
			self.maxHeap.insert(number)
			self.median = number
			self.size += 1
		else:
			peek_max = self.maxHeap.peek()
			if number > peek_max:
				self.minHeap.insert(number)
			else:
				self.maxHeap.insert(number)
			self.size += 1
			
			larger, smaller = (self.maxHeap, self.minHeap) if self.maxHeap.size >= self.minHeap.size else (self.minHeap, self.maxHeap)
			# if size disbalance, rearrange
			if abs(self.maxHeap.size - self.minHeap.size) > 1:
				print(self.size,self.maxHeap.heap,self.minHeap.heap)
				removed = larger.remove()
				smaller.insert(removed)
				
			# assign median based on size
			if self.maxHeap.size == self.minHeap.size:
				peek_max = self.maxHeap.peek()
				peek_min = self.minHeap.peek()
				self.median = (peek_max + peek_min)/2
			else:
				self.median = larger.peek()

    def getMedian(self):
        return self.median

# min heap
class MinHeap:
    def __init__(self):
        self.heap = []
		self.size = 0
		
	# returns minimum from heap
    def peek(self):
		if self.size > 0:
			return self.heap[0]
		return None
	
	# O(logN) time including balancing
    def insert(self, value):
        self.heap.append(value)
		self.size += 1
		self.siftUp()
        return
	
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
	
	# helper method. O(1) time
	def getSmallerChild(self, current):
		print(self.heap,self.size,current)
		left = 2*current+1 if 2*current+1 < self.size else None
		right = 2*current+2 if 2*current+2 < self.size else None
		print(left,right)
		child = None
		if left is not None and right is not None:
			child = left if self.heap[left] < self.heap[right] else right
		elif left is not None:
			child = left
		elif right is not None:
			child = right
		return child
	
# max heap
class MaxHeap:
    def __init__(self):
        self.heap = []
		self.size = 0
		
	# returns minimum from heap
    def peek(self):
		if self.size > 0:
			return self.heap[0]
		return None
	
	# O(logN) time including balancing
    def insert(self, value):
        self.heap.append(value)
		self.size += 1
		self.siftUp()
        return
	
	# O(logN) time
    def siftUp(self):
		current = self.size - 1
		parent = math.floor((current-1)/2)
        while parent >= 0:
			if self.heap[current] > self.heap[parent]:
				self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
				current = parent
				parent = math.floor((current-1)/2)
			else:
				break
		return
	
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
	
	# O(logN) time
    # index used for buildHeap() when you need to siftDown every parent
    def siftDown(self, index=None):
		if self.size > 0:
			if index is None:
				current = 0
			else:
				current = index
			child = self.getLargerChild(current)
			while child is not None and child < self.size:
				if self.heap[current] < self.heap[child]:
					self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
					current = child
					child = self.getSmallerChild(current)
				else:
					break
		return self.heap
	
	# helper method. O(1) time
	def getLargerChild(self, current):
		left = 2*current+1 if 2*current+1 < self.size else None
		right = 2*current+2 if 2*current+2 < self.size else None
		child = None
		if left is not None and right is not None:
			child = left if self.heap[left] > self.heap[right] else right
		elif left is not None:
			child = left
		elif right is not None:
			child = right
		return child
