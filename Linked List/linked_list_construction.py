# Attempt II: After referencing Algoexpert solution
# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Draw and code every case. Be careful about 3 cases: at head, at tail, in middle. Be careful when assigning pointers
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
    	self.head = node
		node.prev = None

    def setTail(self, node):
        self.tail = node
        node.next = None
	
	# Note: that a lot of complication in the code os because of avoiding duplicate entry
    def insertBefore(self, node, nodeToInsert):
		# if the node to be inserted is already available in the list at the head or tail
		if self.head == nodeToInsert or self.tail == nodeToInsert:
			# nothing to do as duplicate entry not required
			return
		# to be careful about duplicate entries: remove the nodeToInsert (if it exists in the linked list - taken care of in remove code) and re-insert
		self.remove(nodeToInsert)
		
		# insert in front
		if self.head == node:
			self.setHead(nodeToInsert)
			nodeToInsert.next = node
		# insert in middle
		else:
			node.prev.next = nodeToInsert
			nodeToInsert.next = node
			nodeToInsert.prev = node.prev
			node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
		# if the node to be inserted is already available in the list at the head or tail
		if self.head == nodeToInsert or self.tail == nodeToInsert:
			# nothing to do as duplicate entry not required
			return
		# to be careful about duplicate entries: remove the nodeToInsert (if it exists in the linked list - taken care of in remove code) and re-insert
		self.remove(nodeToInsert)
		
		# insert in end
		if node.next == None:
			node.next = nodeToInsert
			nodeToInsert.prev = node
			self.setTail(nodeToInsert)
		else:
			self.insertBefore(node.next, nodeToInsert)

	# question: Can you insert in end? i.e at position n+1 where n is the length of linked list
    def insertAtPosition(self, position, nodeToInsert):
        current = self.head
		current_position = 1
    	while current != None:
			if current_position == position:
				self.insertBefore(current, nodeToInsert)
				break
			current = current.next
			current_position += 1
		# handle appending at end case
	
	def removalHelper(self, method_type, target):
		node = self.head
    	while node != None:
			source = node
			if method_type == "byValue":
				source = node.value
			if source == target:
				# removing head
				if node.prev == None:
					if node.next != None:
						self.setHead(node.next)
					else:
						self.head = None
						self.tail = None
				else:
					node.prev.next = node.next
					if node.next != None:
						node.next.prev = node.prev
					else:
						# removing tail
						self.setTail(node.prev)
			node = node.next	
	
    def removeNodesWithValue(self, value):
        self.removalHelper("byValue", value)

    def remove(self, node):
		# Note: this does not need object comparison. The node to be removed itself is given
		# if removing head
		if node == self.head:
			self.setHead(self.head.next)
		# if removing tail
		if node == self.tail:
			self.setTail(self.tail.prev)
		
		# update pointers
		if node.prev != None:
			node.prev.next = node.next
		if node.next != None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None

    def containsNodeWithValue(self, value):
		node = self.head
    	while node != None:
			if node.value == value:
				return True
			node = node.next
		return False


##########################################################

# Attempt I: Initial (misunderstood removal, inxertBefore, insertAfter. No loop needed)

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# TODO: Remove node doesn't need loop
# TODO: Insert Before & Insert After also do not need loop
# Draw and code every case. Be careful about 3 cases: at head, at tail, in middle. Be careful when assigning pointers
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
    	self.head = node
		node.prev = None

    def setTail(self, node):
        self.tail = node
        node.next = None

    def insertBefore(self, node, nodeToInsert):
		current = self.head
		while current != None:
			if current == node:
				# insert in front
				if self.head == node:
					self.setHead(nodeToInsert)
					nodeToInsert.next = node
				# insert in middle
				else:
					node.prev.next = nodeToInsert
					nodeToInsert.next = node
					nodeToInsert.prev = node.prev
					node.prev = nodeToInsert
				# break after insert done
				break
			current = current.next

    def insertAfter(self, node, nodeToInsert):
        current = self.head
    	while current != None:
			if current == node:
				# insert in end
				if current.next == None:
					current.next = nodeToInsert
					nodeToInsert.prev = current
					self.setTail(nodeToInsert)
				else:
					self.insertBefore(current.next, nodeToInsert)
				# break after insert done
				break
			current = current.next
        pass

	# Can you insert in end? YES i.e at position n+1 where n is the length of linked list
    def insertAtPosition(self, position, nodeToInsert):
        current = self.head
		current_position = 1
    	while current != None:
			if current_position == position:
				self.insertBefore(current, nodeToInsert)
				break
			current = current.next
			current_position += 1
		# TODO: handle appending at end case
	
	def removalHelper(self, method_type, target):
		node = self.head
    	while node != None:
			source = node
			if method_type == "byValue":
				source = node.value
			if source == target:
				# removing head
				if node.prev == None:
					if node.next != None:
						self.setHead(node.next)
					else:
						self.head = None
						self.tail = None
				else:
					node.prev.next = node.next
					if node.next != None:
						node.next.prev = node.prev
					else:
						# removing tail
						self.setTail(node.prev)
			node = node.next	
	
    def removeNodesWithValue(self, value):
        self.removalHelper("byValue", value)

    def remove(self, node):
		# TODO: this does not need object comparison. The node to be removed itself is given
        self.removalHelper("byObject", node)

    def containsNodeWithValue(self, value):
		node = self.head
    	while node != None:
			if node.value == value:
				return True
			node = node.next
		return False
