from collections import deque
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        access = deque([self])
        while len(access) > 0:
            node = access.popleft()
            array.append(node.name)
            for child in node.children:
                access.append(child)
        return array