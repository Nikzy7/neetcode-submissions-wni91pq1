# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = []
        queue.append(root)

        answer = []

        while queue:
            nodes_to_pop = len(queue)
            curr_level = []

            for _ in range(nodes_to_pop):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                curr_level.append(node.val)

            answer.append(curr_level[-1])

        return answer