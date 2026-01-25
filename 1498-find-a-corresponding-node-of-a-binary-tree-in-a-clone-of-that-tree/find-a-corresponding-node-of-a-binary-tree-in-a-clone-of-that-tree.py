# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # do dfs search to find the target node
        # return said target node in the cloned tree
        if original is None: # null check
            return
        elif original == target: # if match, then return
            return cloned
        else: # if no match, go left or go right to find the target
            return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)