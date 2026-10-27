class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = {i: i for i in range(1, n+1)}
        rank = [0] * (n+1)

        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union_find(f, s):
            p1 = find(f)
            p2 = find(s)

            if p1 == p2:
                return [f, s] 
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            
            else:
                par[p1] = p2
                rank[p2] += 1
            return True

        count = n
        for r, v in edges:
            return_val = union_find(r, v)
            if return_val != True:
                return return_val
        