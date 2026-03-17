class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# 1 -> 2 -> 3
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
b = reverse_list(a)
print(b.val)
print(b.next.val)
print(b.next.next.val)