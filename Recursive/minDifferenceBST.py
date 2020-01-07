# Problem: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min = 99999999999999
        self.pre = -99999999999999
        def recursiveBST(node):
            if node is None:
                return
            recursiveBST(node.left)
            self.min = min(self.min, node.val - self.pre)
            self.pre = node.val
            recursiveBST(node.right)
        recursiveBST(root)
        return self.min
            