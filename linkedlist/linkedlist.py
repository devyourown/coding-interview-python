class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def make_list(self, lst):
        head = temp = Node(lst[0])
        for n in lst[1:]:
            node = Node(n)
            temp.next = node
            temp = temp.next
        self.head = head

    def print(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(node.val)
            node = node.next
        print(*nodes)