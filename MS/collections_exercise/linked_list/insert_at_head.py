class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_at_head(head, val):
    node = ListNode(val)
    node.next = head
    return node

a = ListNode(1)
b = ListNode(2)
a.next = b
l = insert_at_head(a, 0)
while l:
    print(l.val)
    l = l.next