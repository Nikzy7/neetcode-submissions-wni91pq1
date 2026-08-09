"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        root.next = None

        queue = []
        queue.append(root)

        while queue:
            nodes_to_pop = len(queue)

            current_level_to_print = []
            current_level = []

            for _ in range(nodes_to_pop):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                current_level.append(node)
                current_level_to_print.append(node.val)

            # print(current_level_to_print)

            for node_ptr in range(len(current_level)):
                if node_ptr == len(current_level) - 1:
                    current_level[node_ptr].next = None
                else:
                    current_level[node_ptr].next = current_level[node_ptr + 1]

        return root
