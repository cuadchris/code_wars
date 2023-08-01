# https://www.codewars.com/kata/55d9f257d60c5fd98d00001b/python

# DESCRIPTION:

# Linked Lists - Remove Duplicates

# Write a RemoveDuplicates() function which takes a list sorted in increasing order and 
# deletes any duplicate nodes from the list. Ideally, the list should only be traversed 
# once. The head of the resulting list should be returned.

# var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
# removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null
# If the passed in list is null/None/nil, simply return null.

# Note: Your solution is expected to work on long lists. Recursive solutions may fail due 
# to stack size limitations.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return None
    if not head.next:
        return head
    
    current = head
    
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
        
    return head 