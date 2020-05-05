# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:07:03 2019

@author: Vipin Amar
"""

## Articulation points are those points in graph that connect two disjoint graphs 
## and must be avoided as they cause a single point of failure. This code finds out 
## all the articulation points in a given graph so that we can create a workaround for this.

## Here I have the Facebook graph for which I am going to find the articulation points

count1=1
count2=1
DF1={}
DF2={}
def LoadDi(nodeF,edgeF):
    n = open(nodeF,"r")
    nodes = n.readlines()
    n.close()
    node = [int(i) for i in nodes]
    e = open(edgeF,"r")
    edges = e.readlines()
    e.close()
    I = []
    F = []
    for e in edges:
        n1,n2 = e.split()
        I.append(int(n1))
        F.append(int(n2))
    graph = {}
    for i in range(0,len(node)):
        graph.setdefault(node[i],[])
    for i in range(0,len(I)):
        graph[I[i]].append(F[i])
        graph[F[i]].append(I[i])
    return graph 

V=LoadDi("nodes.txt","edges.txt")

dfst={}
for i in range(0,len(V.keys())):
    dfst.setdefault(i,[])
visited = [False] * (len(V.keys()))  
low = [float("Inf")] * (len(V.keys()))
parent = [-1] * (len(V.keys()))


    
def Low(V):      
    global DF1    
    for i in range(0,len(V.keys())):
        DF1.update({i:0})
    for i in range(0,len(V.keys())):
        if DF1[i] == 0 :
            visit1(i,V)
            
def visit1(v,V):
    global count1
    visited[v]= True
    DF1[v]=count1
    low[v]=count1
    count1=count1+1
    for w in V[v]:
        if visited[w] == False : 
                parent[w] = v 
                visit1(w,V)
                low[v] = min(low[v], low[w])                
        elif w!= parent[v]:  
                low[v] = min(low[v], DF1[w])
                
def DFST(V):      
    global DF2    
    for i in range(0,len(V.keys())):
        DF2.update({i:0})
    for i in range(0,len(V.keys())):
        if DF2[i] == 0 :
            visit2(i,V)

def visit2(v,V):
    global count2
    DF2[v]=count2
    count2=count2+1
    for w in V[v]:
        if DF2[w] == 0:
          dfst[v].append(w)
          visit2(w,V)
        else:
            if DF2[w]>DF2[v]:
                dfst[w].append(v)

DFST(V)
Low(V)
#print DF1

def AP():
    ap=[]
    if len(dfst[0])>1:
        ap.append(1)
    for i in range(1,len(V.keys())):
        for j in dfst[i]:
            if low[j]>=DF1[i]:
                ap.append(i)
                break
    return ap

ans=AP()
print(ans)

import sys
sys.setrecursionlimit(2500)
sys.getrecursionlimit()