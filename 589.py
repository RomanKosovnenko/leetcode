from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans
        else:
            ans.append(root.val)
        
        for child in root.children:
            ans.extend(self.preorder(child))
        
        return ans