class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def print_list(head):
    while head:
        print(head.val)
        head = head.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
print_list(a)