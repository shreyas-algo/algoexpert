# Implement min, max, peek, push & pop as O(1) time & O(1) space functions

import sys

# Feel free to add new properties and methods to the class.
class MinMaxStack:
	min = -sys.maxsize - 1
	max = sys.maxsize
	length = 0
	stack = []
    def peek(self):
        return self.stack[-1]

    def pop(self):
		# update length
		self.length = self.length - 1 if self.length > 0 else 0
		# update min & max
		# ?
        return self.stack.pop()

    def push(self, number):
		self.length += 1
		# update min & max if applicable
		self.min = min(self.min, number)
		self.max = min(self.max, number)
        self.stack.push(number)
        pass

    def getMin(self):
		min = self.min if self.length > 0 else None
        return min

    def getMax(self):
		max = self.max if self.length > 0 else None
        return max
