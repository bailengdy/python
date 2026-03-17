class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True

    # find the middle_node
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half of list
    prev = None
    curr = slow
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # compare 2 half lists
    first = head
    second = prev
    while first:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
print(is_palindrome(a))