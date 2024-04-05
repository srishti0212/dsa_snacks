# Breadth-first Search Algorithm has a wide range of applications in the real-world. Some of them are as discussed below:

#  In GPS navigation, it helps in finding the shortest path available from one point to another.
#  In pathfinding algorithms
#  Cycle detection in an undirected graph
#  In minimum spanning tree
#  To build index by search index
#  In Ford-Fulkerson algorithm to find maximum flow in a network.

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

visited = []
queue = []

def bfs(graph, node, visited): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.extend(neighbour)
        queue.extend(neighbour)



#dfs(graph, '15', visited)
# there is no node with value 15
bfs(graph, '5', visited)
# output 5 3 7 2 4 8 