import sys

V = 9 #Number of nodes in the graph

def printSolution(dist):
	print("Vertex\t\tDistance From Source")
	for i in range(len(dist)):
		print("{0}\t\t{1}".format(i, dist[i]))

def binaryHeap(dist, sdpSet):
	minVal = sys.maxsize
	minIndex = 0

	for i in range(V):
		if(sdpSet[i] == False and dist[i] < minVal):
			minVal = dist[i]
			minIndex = i

	return minIndex
	

def djikstra(graph, src):
	sdpSet = [False for i in range(V)] #Shortest Distance Point
	dist = [sys.maxsize for i in range(V)] #distance of vertex from src.
	
	dist[src] = 0	

	for i in range(V-1):
		u = binaryHeap(dist, sdpSet)
		sdpSet[u] = True

		for v in range(V):
			if(sdpSet[v] == False and graph[u][v] and (dist[u] + graph[u][v] < dist[v])):				
				dist[v] = graph[u][v] + dist[u]

	printSolution(dist)


if __name__ == '__main__':

	# Creates a list containing 9 lists, each of 9 items, all set to 0
	w, h = 9, 9;
	graph = [[0 for x in range(w)] for y in range(h)] 		

	#creating a sample graph in its adjacent matrix representation
	graph[0] = [0, 4, 0, 0, 0, 0, 0, 8, 0]
	graph[1] = [4, 0, 8, 0, 0, 0, 0, 11, 0]
	graph[2] = [0, 8, 0, 7, 0, 4, 0, 0, 2]
	graph[3] = [0, 0, 7, 0, 9, 14, 0, 0, 0]
	graph[4] = [0, 0, 0, 9, 0, 10, 0, 0, 0]
	graph[5] = [0, 0, 4, 14, 10, 0, 2, 0, 0]
	graph[6] = [0, 0, 0, 0, 0, 2, 0, 1, 6]
	graph[7] = [8, 11, 0, 0, 0, 0, 1, 0, 7]
	graph[8] = [0, 0, 2, 0, 0, 0, 6, 7, 0]
	
	djikstra(graph, 0)