#depth first search algorithm
#this is a graph traversal algorithm

graph = {
    'A' : ['B','C','D','E'],
    'B' : ['A','F','G'],
    'C' : [],
    'D' : ['A','H'],
    'E' : ['A'],
    'F' : ['B'],
    'G' : ['C'],
    'H' : ['D']
}
visited = [] # List to keep track of visited nodes.

def dfs(visited, graph, node):                  #function for dfs
    if node not in visited:                     #if node is not visited
        print(node,end=" ")                             #print node
        visited.append(node)                    #append node to visited list
        for neighbour in graph[node]:           #for every neighbour of node
            dfs(visited, graph, neighbour)      #call dfs function

# Driver Code
dfs(visited, graph, 'A')


