# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def longestZigZag(root, come_by_left):
            if not root:
                return 0
            if not come_by_left and root.left:
                return 1 + longestZigZag(root.left, True)
            elif come_by_left and root.right:
                return 1 + longestZigZag(root.right, False)
            else:
                return 0
        return max(longestZigZag(root.left, True), longestZigZag(root.right, False))
