# Approach: 
# a) Run single pointer & double pointer (one that goes through every alternate node) through the linked list until they meet. (Realize that they will definitely meet as one is faster than the other)
# b) If they meet at node n, run single pointer intersection check for node n & head - i.e check in how many steps do head & n meet (see through example. this distance will merge into starting point of loop). Return meeting point

# Analysis: O(N) time & O(1) space

# Note: This question is hard because of the constant space constraint. 

# Learning: #Important: Ask for hints if you're stuck. There's no point wasting time if you're getting nowhere. Be smart. Notice that the single hint of single & double pointer made you solve this question (both paper solving & code) in under 30mins! You still have a lot of places where you can showcase your skills. You dont "need to" know "how" behind the idea that the single pointer & double pointer pace will merge (from a coding interview perspective) into this sort of a solution. The "what" is good enough

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    meeting = findDoubleIntersection(head)
    node = findIntersection(head, meeting)
    return node

def findDoubleIntersection(head):
    # no point in starting from start. only complicates solution
    single = head.next
    # put in None check for head.next (edge case) -- talk to interviewer
    double = head.next.next
    while single != double:
        single = single.next
        # put in None check for head.next (edge case) -- talk to interviewer if that's to be considered - basically input which does not have a loop. As here it is mentioned that it will contain a loop, you can skip that None check
        double = double.next.next
    return double

def findIntersection(head, meeting):
    while head != meeting:
        head = head.next
        meeting = meeting.next
    return meeting