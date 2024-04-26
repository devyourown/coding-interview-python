def find_intersection(lst1, lst2):
    node_set = set()
    node = lst1.head
    while node:
        node_set.add(node)
        node = node.next
    node = lst2.head
    while node:
        if node in node_set:
            return node
        node = node.next
    return None