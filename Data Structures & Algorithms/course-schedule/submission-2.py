class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # def dfs(rc, adj_list, seen):
        #         if not adj_list[rc]:
        #             return
        #         if rc in seen:
        #             return False
        #         seen.add(rc)       
        #         for nei in adj_list[rc]:
        #             visited = dfs(nei, adj_list, seen)
        #             adj_list[rc].remove(nei)

        #         if not visited:
        #             return False
        #         return True
        # adj_list = {}
        # for rc, dc in prerequisites:
        #         if rc not in adj_list:
        #             adj_list[rc] = []
        #         if dc not in adj_list:
        #             adj_list[dc] = []
        #         adj_list[rc].append(dc)
        # seen = set()
        # return dfs(list(adj_list.keys())[0], adj_list, seen) if prerequisites else True

        seen = set()
        def dfs(node):
            if node in seen:
                return False
            if adj_list[node] == []:
                return True
            
            seen.add(node)
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False

            adj_list[node] = []
            seen.remove(node)

            return True



        adj_list = {}
        for rc, dc in prerequisites:
                if rc not in adj_list:
                    adj_list[rc] = []
                if dc not in adj_list:
                    adj_list[dc] = []
                adj_list[rc].append(dc)
        
        for key in adj_list:
            if not dfs(key):
                return False
        return True
