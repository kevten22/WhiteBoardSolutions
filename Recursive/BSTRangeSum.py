# Problem: https://leetcode.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def recursiveSum(root):
            if root is None:
                return
            
            if L <= root.val <= R:
                self.sum += root.val
            if root.val > L:
                recursiveSum(root.left)
            if root.val < R:   
                recursiveSum(root.right)
        
        self.sum = 0
        recursiveSum(root)
        return self.sum