# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:05:32 2019

@author: Vipin Amar Vivekanandan
"""

'''
Wikipedia is one of the largest and best indexed collections of knowledge currently available. 
If analyzed properly, it can shed light on the semantic similarity and relationship among apparently unrelated topics.

Here we are going to find short link chains from a source link to a destination link given their URLs.
We will be using priority queues to keep track of the most promising link to follow to reach the destination. 
''' 

class PriorityQ:
    def __init__(self, type, arr):
        self.A = []
        self.typ = type
        for i in arr:
            self.insert(i)
    
    def insert(self, val):
        #for i in val:
        assert type(val) == self.typ
        self.A.append(val)
        self.BuildHeap()
    
    def BuildHeap(self):
        for i in range(len(self.A)//2 -1,-1,-1):
            self.maxheapify(i)
    
    def maxheapify(self, i):
        n = len(self.A)
        l=2*i+1
        r=2*i+2
        largest = i
        if l <n and self.A[l] > self.A[i]:
            largest = l
        if r <n and self.A[r] > self.A[largest]:
            largest= r
        if largest!= i: 
            self.A[i],self.A[largest] = self.A[largest],self.A[i] 
            self.maxheapify(largest)  
        return A
    
    def extractmax(self):
        Max=self.A[0]
        if len(self.A)<1:
            return "Heap Underflow"
        self.A[0],self.A[len(A)-1]=self.A[len(A)-1],self.A[0]
        self.A.pop()
        self.maxheapify(0)
        print(self.A)
        return Max
    
    def getmax(self):
        return self.A[0]
    
    def empty(self):
        return len(self.A)==0
    
    def Print(self):
        print(self.A
    
import bs4
import requests

def WikiLinks(name):    
    myurl = "https://en.wikipedia.org/wiki/"
    myurl = myurl + name
    res = requests.get(myurl)
    link = bs4.BeautifulSoup(res.text,'lxml')
    links=[]    
    for i in link.find_all('a', href=True):
        links.append(i['href'])
    link=[]
    for i in range(0,len(links)):
    tmp=links[i].split("/")
    if("wiki" in tmp and "#" not in tmp[-1] and ":" not in tmp[-1]):
       link.append(tmp[-1])


class chain:
    def __init__(self):
        self.A=[]
        self.p=0
    def affix(self,v,p):
        del self.A[:]
        self.A.append(v)
        self.p=p
        h.insert([v, p])
    def detach(self):
        temp = h.extractmax()
        return temp[0]
    
        
class WikiChain:
    def __init__(self):
        self.C = []
        self.Tlink = []
        self.t = None
        self.s = None
    
    def start(self, source, target):
        self.s = source.lower()
        self.t = target.lower()
        del link[:]
        WikiLinks(source)
        Slink = []
        for i in link:
            Slink.append(i)
        del link[:]
        WikiLinks(target)
        for i in link:
            self.Tlink.append(i)
        self.C = list(set(Slink).intersection(self.Tlink))
        P = len(self.C)
        c.affix([source], P)
        
    def source_to_target(self):
        del link[:]
        source1 = c.detach()
        source = source1[-1]
        WikiLinks(source)
        Slink  = []
        for i in link:
            Slink.append(str(i))
        for i in Slink:
            if(i == self.t):
                output = []
                for _ in source1:
                    output.append(_)
                output.append(i)
                return output
            del link[:]
            try:
                WikiLinks(i)
            except:
                continue
            self.C = list(set(self.Tlink).intersection(link))
            P = len(self.C)
            source1.append(i)
            c.affix(list(source1), P)
            source1.pop()
        return(self.source_to_target())

p = PriorityQ(str) 
c = chain()
w = WikiChain()
WikiLinks("Multipartite_graph")
del link[:]
w.start("Fur", "Pacific_Ocean")
w.source_to_target()
 