## Read input as specified in the question.
## Print output as specified in the question.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:38:47 2020

@author: Cheerag
"""

"""
Code : BFS Traversal

    Given an undirected and disconnected graph G(V, E), print its BFS traversal.
    Here you need to consider that you need to print BFS path starting from vertex 0 only.
    V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
    E is the number of edges present in graph G.
    Note : 1. Take graph input in the adjacency matrix.
    2. Handle for Disconnected Graphs as well
    Input Format :
    Line 1: Two Integers V and E (separated by space)
    Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
    Output Format :
    BFS Traversal (separated by space)
    Constraints :
    2 <= V <= 1000
    1 <= E <= 1000
    Sample Input 1:
    4 4
    0 1
    0 3
    1 2
    2 3
    Sample Output 1:
    0 1 3 2
"""
import queue 

class graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(self.nVertices)] for i in range(self.nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def removeEdge(self,v1,v2):
        if self.isEdgeExists(v1,v2) is True:
            self.adjMatrix[v1][v2] = 0
            self.adjMatrix[v2][v1] = 0
        else:
            return 
        
    def isEdgeExists(self,v1,v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else:
            return False
    
    def bfsHelper(self,visitedArray,sV):
        q = queue.Queue()
        q.put(sV) 
        
        while not q.empty():
            vertex = q.get()
            print(vertex,end=" ")
            visitedArray[vertex] = True
            for col in range(self.nVertices):
                if self.adjMatrix[vertex][col] == 1 and visitedArray[col] is False:
                    q.put(col)
                    visitedArray[col] = True
                    
        
    def bfs(self):
        visitedArray = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visitedArray[i] is False:
                self.bfsHelper(visitedArray, i)
        # self.bfsHelper(visitedArray,0)
        
        
vert,edge = [int(x) for x in input().split()]
g = graph(vert)
edges = []
for i in range(edge):
    edges.append([int(x) for x in input().split()])


for data in edges:
    g.addEdge(data[0],data[1])

    
g.bfs()