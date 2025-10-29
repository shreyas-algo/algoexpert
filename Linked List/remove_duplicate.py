# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    prev = None
    current = linkedList
    while current != None:
        if prev and prev.value == current.value:
            # remove from linkedList
            prev.next = current.next
        else:
            # update prev only when current was not removed
            prev = current
        current = current.next
    
    return linkedList
