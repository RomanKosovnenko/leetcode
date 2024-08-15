# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        counter = 0
        def dfs(node, counter):
            if not node:
                return [0, 0], counter
            left, counter = dfs(node.left, counter)
            print(left)
            print(counter)
            right, counter = dfs(node.right, counter)
            print(counter)
            print(right)
            node_sum = left[0] + right[0] + node.val
            node_count = left[1] + right[1] + 1

            if node.val == int((node_sum/node_count)):
                counter += 1
            
            return [node_sum, node_count], counter
        _, counter = dfs(root, counter)
        return counter
        