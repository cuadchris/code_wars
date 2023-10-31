"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]


Example 2:

Input: root = []
Output: []


Example 3:

Input: root = [1]
Output: [1]
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive approach.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inOrder(node, res = []):
            if node:
                inOrder(node.left)
                res.append(node.val)
                inOrder(node.right)

            return res

        return inOrder(root)
    
# Iterative approach using a stack.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res