class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 构建一个链表 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# print list
def print_list(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

print_list(head)
# 时间复杂度：O(n)，因为你从头走到尾。

# insert at head
def insert_at_head(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

head = insert_at_head(head, 0)  # 0 -> 1 -> 2 -> 3
print_list(head)
# This illustrates the trade-off:
# linked lists are good at O(1) inserts at head,
# but random access is O(n).