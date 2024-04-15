'''
https://leetcode.com/problems/reverse-linked-list-ii/description/

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy_head = sublist_head = ListNode(0, head)

        # Finds head of sublist.
        for _ in range(1, left):
            sublist_head = sublist_head.next

        # Reverses sublist.
        sublist_iter = sublist_head.next
        for _ in range(right - left):
            temp = sublist_iter.next
            sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                                sublist_head.next,
                                                                temp)

        return dummy_head.next
