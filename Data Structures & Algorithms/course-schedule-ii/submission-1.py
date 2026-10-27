class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen, visit = set(), set()
        output = []
        def dfs(node):
            if node in seen:
                return False
            if node in visit:
                return True
            
            seen.add(node)
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False   
            seen.remove(node) 
            visit.add(node)

            adj_list[node] = []

            output.append(node)

            return True



        adj_list = {i: [] for i in range(numCourses)}
        for course, res in prerequisites:
            adj_list[course].append(res)
                
        for key in adj_list:
            if not dfs(key):
                return []
        return output