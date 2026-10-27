class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {i: i for i in range(n)}
        size = [1] * n

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
                return False
            
            if size[p1] > size[p2]:
                par[p2] = p1
                size[p1] += size[p2]
            
            else:
                par[p1] = p2
                size[p2] += size[p1]
            return True

        count = n
        for r, v in edges:
            count -= union_find(r, v)
        return count      
        
            



        