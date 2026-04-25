class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        explored = set()
        path = set()

        for i in range(numCourses):
            if i not in explored:
                if self.dfs(i, adj, explored, path):
                    return False
        return True

    def dfs(self, src, adj, explored, path):
        if src in path:
            return True
        if src in explored:
            return False
  
        path.add(src)

        for neighbor in adj[src]:
            if self.dfs(neighbor, adj, explored, path):
                return True
        
        path.remove(src)
        explored.add(src)
        return False