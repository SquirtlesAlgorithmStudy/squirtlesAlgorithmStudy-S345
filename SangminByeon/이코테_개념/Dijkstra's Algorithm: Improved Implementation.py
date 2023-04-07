import heapq
from sys import stdin

INF = int(1e9) # Set billion as meaning of INFINITY

n, m = map(int, stdin.readline().split()) # n: number of NODE, m: number of BRANCH
start = int(stdin.readline()) # Recieve input for starting node number
graph = [[] for i in range(n+1)] # Node connetion information 
distance = [INF] * (n+1) # Initialize the shortest distance table to INFINITY

# Recieve input for all branch information
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # c is the distance between a and b

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) # Push in q after setting the starting node's distance to 0
    distance[start] = 0
    while q: # If q is not empty
        dist, now = heapq.heappop(q) # Pop out the shortest node information
        if distance[now] < dist: continue # Ignore the current node if it has already been processed
        for i in graph[now]: # Check the other adjacnet nodes connected to the current node
            cost = dist + i[i]
            if cost < distance[i[0]]: # Update distance if shorter path found through current node
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start) # Perform dijkstra's algorithm

for i in range(1, n+1): # Print the shortest distance for reaching out all nodes
    if distance[i] == INF: print("INFINITY")
    else: print(distance[i])