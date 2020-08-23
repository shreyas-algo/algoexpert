# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# Approach: get ancestors of one descendant in a set. Traverse up through the second descendant while checking any of the ancestor exists in 1's ancentor set. Return if it does
# Analysis: O(d) where d is the depth of the first ancestor
# TODO: Watch video
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestors_one = getAncestory(descendantOne) 
	current = descendantTwo
	# initialize common as topAncestor
	common = topAncestor
	while current is not None:
		# check in set in constant time
		if current in ancestors_one:
			common = current
			break
		current = current.ancestor
    return common

def getAncestory(descendantOne):
	curr = descendantOne
	ancestory = set()
	while curr is not None:
		ancestory.add(curr)
		curr = curr.ancestor
	return ancestory
		
