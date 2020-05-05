# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 03:14:10 2019

@author: Vipin Amar
"""
import time
class Queue:
    def __init__(self,p,o):
        self.u=[None]*o
        self.first=0
        self.last=0
        self.size=0
        self.max=o
        self.make=p

    def enqueue(self,e):
        if self.make==type(e):
            if self.size==self.max:
                print("queue is full")
            else:
                self.u[self.last]=e
                self.last=(self.last+1)%self.max
                self.size=self.size+1
        else:
            print("Queue data type not supported for input:",e)    

    def dequeue(self):
        if self.size==0:
           print("Queue is empty")
        else:
           self.size=self.size-1
           a=self.u[self.first]
           self.u[self.first]=None
           self.first=(self.first+1)%self.max
           return a 
        
    def empty(self):
           return self.size==0

    def full(self):
        return self.size==self.max
    
    def view(self):
        return self.u

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

def BreadthFirst(J,k):
    q=Queue(int,len(J.keys()))
    bf={}
    for i in range(0,len(J.keys())):
        bf.update({i:-1})
    bf[k]=0
    q.enqueue(k)
    while(not q.empty()):
        n=q.dequeue()
        for i in J[n]:
            if bf[i]==-1:
                q.enqueue(i)
                bf[i]=bf[n]+1
    return bf

def Dia(DSTrb):
    return max(DSTrb.keys())

def Dist(J):
    ft={}
    for i in J.values():
        if (i not in ft.keys()) and (i != -1):
            ft.update({i:1})
        else:
            ft[i]=ft[i]+1
    return ft

def mode(DSTrb):
    v=max(DSTrb.values())
    li=[]
    for i in DSTrb:
        if DSTrb[i]==v:
            li.append(i)
    return li

def median(DSTrb):
    return sum(DSTrb.keys())/len(DSTrb.keys())


def DistDstrb(G):
    ft={}
    for j in G.keys():
        d=BreadthFirst(G,j)
        dist=Dist(d)
        for i in dist.keys():
            if (i not in ft.keys()):
                ft.update({i:dist[i]})
            else:
                ft[i]=ft[i]+dist[i]
    for i in ft.keys():
        ft[i]=ft[i]/2
    return ft


tic=time.time()
B=LoadDi("nodes.txt","edges.txt")
ek=BreadthFirst(B,0)
dd=DistDstrb(B)
print("diameter = ",Dia(dd))
toc=time.time()

print("median distance = ",median(dd))
print("mode distance= ",mode(dd))

print("Time taken(to compute Facebook diameter):",toc-tic)
# Data exhibit small world phenomenon with diameter=8

q = Queue(int,5)
q.enqueue(1)
print q.view()

