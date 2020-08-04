class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
        return self

    def contains(self, value):
		if value == self.value:
			return True
        elif value < self.value and self.left is not None:
			self.left.contains(value)
		elif value >= self.value and self.right is not None:
			self.right.contains(value)
        return False
	
	# Approach:  notice that to find the right element that replaces a given node that is being replaced (if it has children), you need to find either leftmost element in its right subtree or find rightmost element in its left subtree (to retain the BST strucuture) Draw example and see
    def remove(self, value, parent=None, direction=None):
        if value == self.value:
			# single node tree: no op
			if parent is None and self.left is None and self.right is None:
				return self
			# simple case: when removing leaf
			elif self.left is None and self.right is None:
				if direction == "left":
					parent.left = None
				else:
					parent.right = None
			# TODO: handle case when removing non-leaf node
			# TODO: handle root removal case
		elif value < self.value and self.left is not None:
			self.left.remove(value, self, "left")
		elif value >= self.value and self.right is not None:
			self.right.remove(value, self, "right")
        return self