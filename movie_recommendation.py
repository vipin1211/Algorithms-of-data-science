## Problem Statement : 

'''
 We are working on a movie recommendation system that requires us to measure the degree to which the 
 rankings of a common set of movies by two people are similar or different. A ranking is simply a sequence 
 of movie ids, ordered from best to worst. Once the system finds someone with rankings similar to yours,
 it can recommend new movies that this individual has liked and you have not yet seen.
'''
#Distancebetween R and S
def rankingdist(r,s, array_size):
    sr=[None for i in s]
    for i in range(len(s)):
        sr[i] = r.index(s[i])+1
    temp = [None] * array_size
    return _rankingdist(sr, temp, 0, array_size - 1)

def _rankingdist(arr, temp, left, right): 

    mid = inv_count = 0 
    if (right > left):
        mid = (right + left) // 2 
  
        inv_count = _rankingdist(arr, temp, left, mid)
        inv_count += _rankingdist(arr, temp, mid + 1, right) 
  
        inv_count += dist(arr, temp, left, mid + 1, right)
     
    return inv_count

def dist(arr, temp, left, mid, right): 
     
    inv_count = 0
  
    i = left
    j = mid
    l=0
    while (i <= mid - 1) and (j < right):
        if (arr[i] <= arr[j]):
            temp[l] = arr[i]
            l+=1
            i+=1
         
        else: 
            temp[l] = arr[j]
            l+=1
            j+=1
            inv_count = inv_count + (mid - i)
        
    while i <= (mid - 1): 
        temp[l] = arr[i]
        l+=1
        i+=1
  
    while j <= right: 
        temp[l] = arr[j]
        l+=1
        j+=1
  
    for i in range(left,right+1):
        arr[i] = temp[i]
  
    return inv_count

r=[71,23,18,45,57,61]
s=[23,45,71,61,18,57]
print(rankingdist(r,s, len(r)))

#Nearest neibhour
def nearestneighbour(di):
    G=dict()
    for s in di:
        G.setdefault(s,[])
        d=dict()
        for i in di:
            if i!=s:
                res=rankingdist(di[s],di[i],len(di[i]))
                d.update({i:res})
        m=min(d.values())
        for _ in d:
            if d[_]==m:
                G[s].append(_)
    return G
    
r=open("rankings.txt","r")
m=r.readlines()
dic=dict()
for i in m:
    user=i.split(",")
    user=list(map(int,user))
    dic.setdefault(user[0],[])
    for i in user[1:]:
        dic[user[0]].append(i)
        
g=nearestneighbour(dic)        

#Reverse Nearest neibhour
def revnearestneighbour(di):
    G=dict()
    for s in di:
        G.setdefault(s,[])
    for s in di:
        d={}
        for i in di:
            if i!=s:
                res=rankingdist(di[s],di[i],len(di[i]))
                d.update({i:res})
        m=min(d.values())
        for _ in d:
            if d[_]==m:
                G[_].append(s)
    return G  

r=open("rankings.txt","r")
m=r.readlines()
dic=dict()
for i in m:
    user=i.split(",")
    user=list(map(int,user))
    dic.setdefault(user[0],[])
    for i in user[1:]:
        dic[user[0]].append(i)
        
g=revnearestneighbour(dic) 