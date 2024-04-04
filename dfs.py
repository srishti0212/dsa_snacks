# Depth-First Search Algorithm has a wide range of applications for practical purposes. Some of them are:

# For finding the strongly connected components of the graph
# For finding the path
# To test if the graph is bipartite
# For detecting cycles in a graph
# Topological Sorting
# Solving the puzzle with only one solution.
# Network Analysis
# Mapping Routes
# Scheduling a problem

#    5
#  /  \
#  3   7
# / \   \
# 2  4 - 8

graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '2' : [],
    '7' : ['8'],
    '4' : ['8'],
    '8' : []
}

visited = set()

def dfs(graph, node, visited):
    if node not in graph:
        print('there is no node with value', node)
        exit()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


#dfs(graph, '15', visited)
# there is no node with value 15
dfs(graph, '5', visited)
# output 5 3 2 4 8 7 