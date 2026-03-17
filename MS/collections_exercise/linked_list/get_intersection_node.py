from linked_list import ListNode

def get_intersection_node(l1: ListNode, l2: ListNode) -> ListNode:
    h1 = l1
    h2 = l2
    while h1 is not h2:
        h1 = h1.next if h1 else l2
        h2 = h2.next if h2 else l1
    return h1

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
f.next = c
print(get_intersection_node(a, f).val)