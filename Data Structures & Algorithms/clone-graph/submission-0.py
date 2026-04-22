"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        ret = {}

        def dfs(original):
            if original in ret:
                return ret[original]
            
            copy = Node(original.val)

            ret[original] = copy

            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        return dfs(node)
