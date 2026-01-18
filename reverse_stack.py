class Solution(object):
    def main(self, stack):
        reverse = []
        for i in range(len(stack)):
            reverse.append(stack.pop())
        
        return reverse


# Main part of the script
sol = Solution()
stack = [10,2,3,4,5,6,7]
print(sol.main(stack))

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