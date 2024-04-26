def find_loop(lst):
    node_set = set()
    node = lst.node
    while node:
        if node in node_set:
            return node
        node_set.add(node)
        node = node.next
    return None

def find_loop_without_space(lst):
    slow, fast = lst.head, lst.head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return None
    slow = lst.head
    while slow != fast:
        slow, fast = slow.next, fast.next
    return fast