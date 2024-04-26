from linkedlist import Node, LinkedList

def get_size(lst):
    result = 0
    head = lst.head
    while head is not None:
        result += 1
        head = head.next
    return result

def remove_mid_node(lst):
    size = get_size(lst) // 2 - 1
    node = lst.head
    for _ in range(size):
        node = node.next
    node.next = node.next.next

head = origin = Node(0)
for i in range(1, 10):
    temp = Node(i)
    head.next = temp
    head = temp
lst = LinkedList(origin)
remove_mid_node(lst)
lst.print()