from linkedlist import LinkedList, Node

def split_with(lst, x):
    before, cand = lst.head, lst.head.next
    while cand:
        if cand.val < x:
            before.next = cand.next
            cand.next = lst.head
            lst.head = cand
            cand = before.next
        else:
            before, cand = before.next, before.next.next
    return lst.head

lst = LinkedList(Node(3))
lst.make_list([3, 5, 8, 5, 10, 2, 1])
split_with(lst, 5)
lst.print()
lst.make_list([10, 3, 5, 8, 5, 10, 2, 1])
split_with(lst, 5)
lst.print()