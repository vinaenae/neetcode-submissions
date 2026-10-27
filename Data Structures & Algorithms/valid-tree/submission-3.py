class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        valid = set()
        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            for nei in adj_list[node]:
                if prev == nei:
                    continue
                if not dfs(nei, node):
                    return False
            
            valid.add(node)
            return True

        adj_list = {i: [] for i in range(n)}
        for f, s in edges:
            adj_list[f].append(s)
            adj_list[s].append(f)
        
        if not dfs(0, -1):
            return False
        
        if len(valid) < n:
            return False

        return True
        