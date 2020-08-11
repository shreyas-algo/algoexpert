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
				return self
			
			# removing non-leaf node
			# TODO: check root removal case
			if self.left is not None:
				coming_from = "left"
				closest, closest_parent  = self.left.findClosestValueInBst(self.value, self)
			if self.right is not None:
				closest, closest_parent = self.right.findClosestValueInBst(self.value, self)
			
			# DRAW cases and observe:
			# closest will definitely have value because neither left nor right child case (leaf node) covered above
			# Issues to consider:
			# a) the `closest` node value (or the new root) to the target (that is being removed) may have a child linked which will need to be relinked to the new root. 
			# a) Also, Notice that if closest is retrieved from right sub-tree, it can at max have a right subtree cz a left subtree will mean that it is not the smallest element which contradicts it being the closest to the target element. Similarly a closest from left subtree can have at max left subtrees and cannot have further right subtrees (draw and check)
			# a) Also, a closest coming from left can never be to the left of its parent because that will contradict it being the largest in the left subtree unless it's the first child itself (which is a case being hendled: where closest_parent == self). Similarly a closest coming from ritgh can never be to right of its parent unless it is the first right child pf target (again case being hedled by closest_parent == self)
			# b) Also, if the closest is immediate right or immediate left to the target, you don't need to do the relinking cz closest's parent = target (node to be removed), so no relinking required
			
			# Think?: you don't need delinking of closest logic. Simply call remove() to delink it -- problem might be that our remove method works on value. 
			# relink closest's sub-trees to its parent if they exist and when closest's parent is not same as the target to be removed
			if closest_parent != self:
				# coming from left and has a right sub tree which needs relinking
				if coming_from == "left" and closest.left is not None:
					closest_parent.right = closest.left
				# coming from right and has a right sub tree which needs relinking
				elif closest.right is not None:
					closest_parent.left = closest.right
			
			# no need for relinking if you simply change values
			# change target's (self) value with closest
			self.value = closest.value
			
			# relinking logic
# 			# link closest to target's parent
# 			if parent is not None:
# 				if direction == "left":
# 					parent.left = closest
# 				else:
# 					parent.right = closest
			
			
# 			# link target's left and right to closest
# 			if closest_parent != self:
# 				# condition put for cases when immediate left or right is the closest. Draw and check
# 				if closest.right != self.right:
# 					closest.right = self.right
# 				if closest.left != self.left:
# 					closest.left = self.left
# 			# else:
# 			# 	# immediate left child was closest
# 			# 	if coming_from == "left":
# 			# 		closest.right = self.right
# 			# 	# immediate right child was closest
# 			# 	elif closest.right is not None:
# 			# 		closest.left = self.left
			
# 			# delink target (self)
# 			self.left = None
# 			self.right = None
			return self
			
		elif value < self.value and self.left is not None:
			self.left.remove(value, self, "left")
		elif value >= self.value and self.right is not None:
			self.right.remove(value, self, "right")
        return self
	
	# find node which is closest to given targrt. Return alongside its parent
	def findClosestValueInBst(self, target, parent, minDiff=1000000, closest=None, closest_parent=None):
		print(target)
		if self.value == target:
			return (self, parent)
		if abs(self.value - target) < minDiff:
			minDiff = abs(self.value - target)
			closest = self
			closest_parent = parent
		if self.value < target and self.right:
			closest, closest_parent = self.right.findClosestValueInBst(target, self, minDiff, closest, closest_parent)
		elif self.left:
			closest, closest_parent = self.left.findClosestValueInBst(target, self, minDiff, closest, closest_parent)
		# if no branch left to explore
		return (closest, closest_parent)
