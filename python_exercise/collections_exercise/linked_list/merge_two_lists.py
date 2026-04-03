class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1:
        current.next = l1
    elif l2:
        current.next = l2
    return dummy.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = c
c.next = f
b.next = d
d.next = e
l = merge_two_lists(a, b)
while l:
    print(l.val)
    l = l.next
