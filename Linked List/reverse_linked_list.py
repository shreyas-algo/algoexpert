# Approach: Simple approach to keep the next pointer safe (from overriding) in a temp variable (link) so that you can access it to keep traversing and chenge current node's "next" at the same time so that the linked list can be reversed
# Analysis: O(N)
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

