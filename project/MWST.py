#!/usr/local/bin/python3
# your python code starts here

import heapq

num_vertices=int(input())
num_edges=int(input())

adj={ i:[] for i in range(1, num_vertices+1) }

for lineNumber in range(1, num_edges+1):
    inputLine=input()
    i, j, weight=int(inputLine[0]), int(inputLine[2]), int(inputLine[4])
    adj[i].append([weight,j,lineNumber])
    adj[j].append([weight,i,lineNumber])

total_weight=0
visit=set()
minH=[[0, 1, None, None]]

res=[]

while len(visit)<num_vertices:
    cost, i, j, lineNumber=heapq.heappop(minH)
    if i in visit:
        continue

    total_weight+=cost
    print("i:",i)
    print("j:",j)
    
    print("adj[i]:",adj[i])
    print()
    
    if lineNumber:
        res.append([cost, 
            str(lineNumber)+": ("+str(i)+", "+str(j)+") "+"{:0.1f}".format(round(cost,1))])

    visit.add(i)
    for neiCost, nei, line in adj[i]:
        if nei not in visit:
            heapq.heappush(minH,[neiCost, nei, i, line])

print()
print("visit:",visit)
print()
print("minH:",minH)
print()
print("adj:",adj)
print()

res.sort()

for i, edge in enumerate(res):
    print(edge)
    
print("Total Weight = {:0.2f}".format(round(total_weight, 2)))