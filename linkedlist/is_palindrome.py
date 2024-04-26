from linkedlist import LinkedList

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def add(self, node):
        self.next = node
        node.prev = self


def is_palindrome(lst):
    head = last = lst.head
    while last.next:
        last = last.next
    while head and last:
        if head.val != last.val: return False
        head, last = head.next, last.prev
    return True

head = origin = Node(1)
word = ['a', 'a', 'a']
for w in word:
    temp = Node(w)
    head.add(temp)
    head = temp
lst = LinkedList(origin.next)
print(is_palindrome(lst))