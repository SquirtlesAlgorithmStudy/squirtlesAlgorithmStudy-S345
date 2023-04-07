from sys import stdin
INF = int(1e9) # Set billion as meaning of INFINITY

n, m = map(int, stdin.readline().split()) #n: number of NODE, m = number of BRANCH
start = int(stdin.readline()) # Receive input for start node number
graph = [[] for i in range(n+1)] # Node connection information
visited = [False] + (n+1) # Check visited or not
distance = [INF] * (n+1) # Initialize the shortest distance table to INFINITY

# Receive input for all branch information
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c)) # c is the distance between a and b

# Return the shortest node number among not visited nodes
def get_smallest_node():
    min_value = INF
    index = 0 # The shortest node number
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # Initialize for starting node
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # Repeat for all nodes except the starting node, for a total of n-1 nodes
    for i in range(n-1):
        # Pop out the node with the currently shortest distance and mark it as visited:True
        now = get_smallest_node()
        visited[now] = True

        # Check the other nodes that are connected to current node.
        for j in graph[now]:
            cost = distance[now] + j[i]

            # Update distance if shorter path found through current node
            if cost < distance[j[0]]:
                distance[j[0]] = cost
        
# Perform Dijkstra's algorithm
dijkstra(start)

# Print the shortest distance for reaching to all nodes
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
