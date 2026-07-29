# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans

        if root.left:
            ans += self.inorderTraversal(root.left)

        ans.append(root.val)

        if root.right:
            ans += self.inorderTraversal(root.right)

        return ans