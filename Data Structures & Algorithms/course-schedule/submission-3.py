class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for s, p in prerequisites:
            adj[s].append(p)
        print(adj)
        visit = set()
        
        def dfs(s):
            if s in visit:
                return False
            if adj[s] == []:
                return True

            visit.add(s)
            for child in adj[s]:
                if not dfs(child):
                    return False

            visit.remove(s)
            adj[s] = []
            return True

        for key in adj:
            if not dfs(key):
                return False
        return True
        

        

        

