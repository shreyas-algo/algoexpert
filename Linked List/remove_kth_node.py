# Approach: Get length of linked list. Get node to remove and its previous (so that next can be updated). Remove the node by updating bindings
# Analysis: O(N) time, O(1) space

# Status: Just one case not working when head needs to be updated

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    length = lengthOf(head)
	prev, nodeToRemove = findKthNode(head, length, k)
	# removing head
	if head == nodeToRemove:
		# Issue: Updating local parameter here doesn't change the actual LinkedList's head (variable scoping. local var changes are not reflected outside functions). For that you need reference to the LinkedList. Though this technique to update head is great and logically makes sense. There doesn't seem to be a way to update the linked list head unless a reference is passed.
		head = nodeToRemove.next
	else:
		prev.next = nodeToRemove.next
	nodeToRemove.next = None
    return

def lengthOf(node):
	len = 0
	while node is not None:
		len += 1
		node = node.next
	return len

def findKthNode(node, length, k):
	index = 0
	prev = node
	while node is not None and index + k < length:
		prev = node
		node = node.next
		index += 1
	return (prev, node)
