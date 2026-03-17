class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
c.next = a
print(has_cycle(a))
c.next = None
print(has_cycle(b))