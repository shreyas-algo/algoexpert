# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# algo - Have 2 pointers - one fast and one slow. If the fast moves 2 steps for each step of the slow ptr, by the time the fast will reach the end, the slow would reach only half
def middleNode(linkedList):
    single_hop = linkedList
    double_hop = linkedList
    while double_hop and double_hop.next != None and double_hop.next.next != None:
        single_hop = single_hop.next
        double_hop = double_hop.next.next
    # check if even number of nodes (try with an example. this will only be possible with even nodes. With odd nodes, you are at the complete end)
    if double_hop.next:
        return single_hop.next
    return single_hop
