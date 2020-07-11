def reverseLinkedList(head):
    curr = head
    prev = None
    link = curr
    while link is not None:
        print(link.value)
        link = link.next
        curr.next = prev
        prev = curr
        curr = link
    print("as",prev.next.value)
    head = prev
    head.value = prev.value
    head.next = prev.next
