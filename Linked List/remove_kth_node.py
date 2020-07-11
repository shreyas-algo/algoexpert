# Approach: Get length of linked list. Get node to remove and its previous (so that next can be updated). Remove the node by updating bindings
# Analysis: O(N) time, O(1) space

# Status: All working. Pointers of head updated. But strange to see how left side of assignment also affected. as I changed the head on line 24: `head.next = nodeToRemove.next.next`, nodeToRemove is also changed. Hence when later we change `nodeToRemove.next = None` to change old head's next pointer, the upfated head loses next (changes to None). Basically head pointer and nodeToRemove pointers are tightly (two-way) coupled. Solution is to return in case of head removal

# Note: 
# 1. All comments and detailing is with respect to a single case: head removal
# 2. Ignore all comments and print statements if you just want to focus on the problem. Read comments after. The solution itself is pretty simple

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
		# head = nodeToRemove.next		
		print(nodeToRemove.next.value)  # 1 when linked list : 0 -> 1 -> 2 -> 3 ... -> 9 and k = 10 ie trying to remove head(0)
		head.value = nodeToRemove.next.value
		head.next = nodeToRemove.next.next
		print(nodeToRemove.next.value)  # 2 What? nodeToRemove.next changed as we changed head.next! Interesting
		return                          # Due to the issue seen in print statements, this return is important. It shouldn't be. Some pointer / Algoexpert issue
	else:
		prev.next = nodeToRemove.next
	# print(nodeToRemove.next.value)     # Prints 2 instead of 1 if return not used for the head removal case. Strange!
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
