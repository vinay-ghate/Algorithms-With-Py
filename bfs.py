#breath first search algorithm
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
queue = []   #Initialize a queue

def bfs(visited,graph,node):
    visited.append(node) #append node to visited list
    queue.append(node)   #append node to queue
    
    while queue:
        s = queue.pop(0) #pop first element from queue
        print(s,end = " ")         #print popped element
        
        for neighbour in graph[s]:         #for every neighbour of popped element
            if neighbour not in visited:   #if neighbour is not visited
                visited.append(neighbour)  #append neighbour to visited list
                queue.append(neighbour)    #append neighbour to queue

# Driver Code
bfs(visited, graph, 'A')
