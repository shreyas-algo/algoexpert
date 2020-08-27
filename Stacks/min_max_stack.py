# Approach: Keep updating max & min on every push based on what you've seen. Maintain min & max for every top position so that at any top position you have all the info you need. 
# Analysis: each opreation is O(1) time & O(1) space independently

# Learning: 
# a) `if var` is not the right way to check "not None" cz it won't pass even for `if 0`. Thus use `if var is not None`
# b) Storing tuples as keys in dictionary

# Note: implementation can be done based on max & min lists also where you check the appropriate index (top). You dont need dictionaries. But both are fine
# Note: TODO: Notice that you do not really need the tuple in dictionary. You can simply store across the top index value

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
