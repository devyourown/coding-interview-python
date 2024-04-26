from linkedlist import LinkedList, Node

def get_kth_from_back(lst, k):
    ahead_kth = lst.head
    for _ in range(k):
        ahead_kth = ahead_kth.next
        if ahead_kth is None:
            return lst.head
    head = lst.head
    while ahead_kth is not None:
        head, ahead_kth = head.next, ahead_kth.next
    return head

head = origin = Node(0)
for i in range(1, 10):
    temp = Node(i)
    head.next = temp
    head = temp
lst = LinkedList(origin)
print(get_kth_from_back(lst, 3).val)