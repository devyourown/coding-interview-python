from linkedlist import Node

def remove_dup(lst):
    value_set = set()
    before, cur = lst.head, lst.head.next
    value_set.add(before)
    while cur is not None:
        if cur.val in value_set:
            before.next = cur.next
            cur = before.next
        else:
            value_set.add(cur.val)
            before, cur = cur, cur.next
    return lst.head

def remove_dup_without_buf(lst):
    head, before, cur = lst.head, lst.head, lst.head.next
    while head is not None:
        while cur is not None:
            if head.val == cur.val:
                cur, before.next = cur.next, cur.next
            else:
                before, cur = cur, cur.next
        head = head.next
    return lst.head