import sys

# Feel free to add new properties and methods to the class.
class MinMaxStack:
	# init values
	length = 0
	stack = []
	minDict = {}
	maxDict = {}
    def peek(self):
		if self.length > 0:
        	return self.stack[-1]
		return None

    def pop(self):
		top = self.peek()
		print(self.stack, top)
		if top != None:
			# update min & max
			# ?
			self.length = self.length - 1
        	return self.stack.pop()
		return None

    def push(self, number):
		top = self.peek()
		# init
		self.minDict[number] = number
		self.maxDict[number] = number
		if top != None:
			# update min & max if applicable
			existingMin = self.minDict[top]
			existingMax = self.maxDict[top]
			if number > existingMin:
				self.minDict[number] = existingMin
			if number < existingMax:
				self.maxDict[number] = existingMax
        self.stack.append(number)
		self.length += 1
        return

    def getMin(self):
		top = self.peek()
		if top != None:
			return self.minDict[top]
        return None

    def getMax(self):
		top = self.peek()
		if top != None:
			return self.maxDict[top]
        return None
