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
	prev = None
	while node is not None and index + k < length:
		prev = node
		node = node.next
		index += 1
	return (prev, node)
