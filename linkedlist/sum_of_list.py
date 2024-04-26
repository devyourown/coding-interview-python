from linkedlist import LinkedList, Node

def sum_of_list(lst1, lst2):
    return make_list(get_num(lst1) + get_num(lst2))

def get_num(lst):
    result = 0
    digit = 1
    head = lst.head
    while head:
        result += head.val * digit
        digit *= 10
        head = head.next
    return result

def make_list(num):
    head = result = Node(num%10)
    num //= 10
    while num > 0:
        head.next = Node(num%10)
        num //= 10
        head = head.next
    return LinkedList(result)

def sum_of_straight_list(lst1, lst2):
    return make_list_straight((get_num_straight(lst1) + get_num_straight(lst2)))

def get_num_straight(lst):
    head = lst.head
    nums = []
    while head:
        nums.append(str(head.val))
        head = head.next
    return int(''.join(nums))

def make_list_straight(num):
    num = str(num)
    result = head = Node(int(num[0]))
    for s in num[1:]:
        head.next = Node(int(s))
        head = head.next
    return LinkedList(result)

lst1 = LinkedList(Node(0))
lst1.make_list([7, 1, 6])
lst2 = LinkedList(Node(0))
lst2.make_list([5, 9, 2])
sum_of_straight_list(lst1, lst2).print()