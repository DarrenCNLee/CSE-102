#!/usr/local/bin/python3
# your python code starts here

import heapq

num_vertices=int(input())
num_edges=int(input())

adj={ i:[] for i in range(num_vertices) }

for _ in range(num_edges):
    weight, i, j=input()
    adj[i].append(weight,j)
    adj[j].append(weight,i)

total_weight=0
visit=set()
minH=[[0,0]]

while len(visit)<num_vertices:
    cost,i=heapq.heappop(minH)
    if i in visit:
        continue

    total_weight+=cost
    visit.add(i)
    for neiCost,nei in adj[i]:
        if nei not in visit:
            heapq.heappush(minH,[neiCost,nei])

print("Total Weight =", total_weight)