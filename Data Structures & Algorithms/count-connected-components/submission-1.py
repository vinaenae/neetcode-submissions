class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        for f, s in edges:
            adj_list[f].append(s)
            adj_list[s].append(f)
        seen = set()
        last_elem = 0
        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            last_elem = node
            for nei in adj_list[node]:
                if not dfs(nei):
                    continue
        prev, count = 0, 0
        for i in range(len(adj_list)):
            if i not in seen:
                dfs(i)
                count += 1
        return count
            



        