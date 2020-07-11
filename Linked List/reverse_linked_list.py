# Approach: Simple approach to keep the next pointer safe (from overriding) in a temp variable (link) so that you can access it to keep traversing and chenge current node's "next" at the same time so that the linked list can be reversed
# Analysis: O(N)

# Learning: Read the question properly. Wasted some time cz I was not returning the new head (was only changing the head inside the function) whereas the question clearly mentions it.
def reverseLinkedList(head):
    curr = head
    prev = None
    while curr is not None:
        link = curr.next
        curr.next = prev
        prev = curr
        curr = link
    head = prev
    return head

