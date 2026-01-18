class Solution(object):
    def main(self):
        graph = [[1], []]
        i = 0
        valid_graph = True
        total_nodes = len(graph)
        for neighbors in graph:
            valid_graph = all(num < total_nodes for num in neighbors)

            if i in neighbors:
                valid_graph = False
            
            if len(set(neighbors)) < len(neighbors):
                valid_graph = False


            if valid_graph == False:
                return valid_graph

            i = i + 1
        return valid_graph


# Main part of the script
sol = Solution()
print(sol.main())

# # Adjacency List Validation

# Given an adjacency list, `graph`, write a function that returns whether `graph` is a _valid_ undirected graph, meaning that:

# 1. Every node is between `0` and `V-1`.
# 2. There are no _self-loops_: edges connecting a node to itself.
# 3. There are no _parallel edges_: two edges connecting the same two nodes.
# 4. If `node1` appears in `graph[node2]`, then `node2` also appears in `graph[node1]`.

# Example 1: graph = [[1], [0]]
# Output: True. This is a simple valid graph with two nodes connected by an edge.

# Example 2: graph = [[2], [0]]
# Output: False. Node index 2 is invalid since there are only 2 nodes.

# Example 3: graph = [[0], []]
# Output: False. Self-loop in node 0.

# Example 4: graph = [[1, 1], [0, 0]]
# Output: False. Parallel edges between nodes 0 and 1.

# Example 5: graph = [[1], []]
# Output: False. Node 0 has node 1 as a neighbor but not vice versa.

# Constraints:

# - `graph.length ≤ 1000`
# - `graph[i].length ≤ 1000`