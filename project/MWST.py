#!/usr/local/bin/python3
# your python code starts here

import heapq

num_vertices=int(input())
num_edges=int(input())

adj={ i:[] for i in range(1, num_vertices+1) }

for _ in range(num_edges):
    inputLine=input()
    i, j, weight=int(inputLine[0]),int(inputLine[2]),int(inputLine[4])
    adj[i].append([weight,j])
    adj[j].append([weight,i])

total_weight=0
visit=set()
minH=[[0,1]]

while len(visit)<num_vertices:
    cost,i=heapq.heappop(minH)
    if i in visit:
        continue

    total_weight+=cost
    visit.add(i)
    for neiCost, nei in adj[i]:
        if nei not in visit:
            heapq.heappush(minH,[neiCost,nei])

print("Total Weight ={:0.2f}".format(round(total_weight, 2)))