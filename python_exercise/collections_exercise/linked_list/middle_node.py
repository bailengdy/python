class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
print(middle_node(a).val)
print(middle_node(b).val)