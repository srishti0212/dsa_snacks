from typing import List

class Solution:

    def graph_valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {}

        for i in range(n):
            adj_list[i] = []
        for pair in edges:
            adj_list[pair[0]].append(pair[1])
            adj_list[pair[1]].append(pair[0])
            
        def hascycle(adj_list, node , visited, parent):
            visited[node] = True
            for neighbor in adj_list[node]:
                if visited[neighbor] and neighbor != parent:
                    return True
                elif not visited[neighbor] and hascycle(adj_list , neighbor, visited, node):
                    return True
            return False

            
        visited = [False] * n
        if hascycle(adj_list, 0 , visited, -1):
            return False

        return all(visited)

sol = Solution()
print(sol.graph_valid_tree(4,  [[0,1],[2,3]]))