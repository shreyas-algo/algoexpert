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
			# removing non-leaf node
			# TODO: check root removal case
			if self.left is not None:
				closest = self.left.findClosestValueInBst(self.value)
			if self.right is not None:
				closest = self.right.findClosestValueInBst(self.value)
			
			# closest will definitely have value because neither left nor right child case (leaf node) covered above
			# Issues to consider:
			# a) the `closest` node value (or the new root) to the target (that is being removed) may have a child linked which will need to be relinked to the new root. 
			# a) Also, Notice that if closest is retrieved from right sub-tree, it can at max have a right subtree cz a left subtree will mean that it is not the smallest element which contradicts it being the closest to the target element. Similarly a closest from left subtree can have at max left subtrees and cannot have further right subtrees (draw and check)
			# b) Also, if the closest is immediate right or immediate left to the target, you don't need to do the relinking cz closest's parent = target (node to be removed), so no relinking required
			
			
			
		elif value < self.value and self.left is not None:
			self.left.remove(value, self, "left")
		elif value >= self.value and self.right is not None:
			self.right.remove(value, self, "right")
        return self
	
	def findClosestValueInBst(self, target, parent, minDiff=1000000, closest=None):
		if self.value == target:
			return tree
		if abs(self.value - target) < minDiff:
			minDiff = abs(self.value - target)
			closest = self
		if self.value < target and self.right:
			closest = findClosestValueInBst(self.right, target, minDiff, closest)
		elif tree.left:
			closest = findClosestValueInBst(self.left, target, minDiff, closest)
		# if no branch left to explore
		return closest
