# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
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
        elif value < self.value:
			if self.left is not None:
				self.left.contains(value)
		elif self.right is not None:
			self.right.contains(value)
        return False
	
	# Approach:  notice that to find the right element that replaces a given node that is being replaced (if it has children), you need to find either leftmost element in its right subtree or find rightmost element in its left subtree (to retain the BST strucuture) Draw example and see
    def remove(self, value):
        if value == self.value:
			pass
        return self