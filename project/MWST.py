#!/usr/local/bin/python3
# your python code starts here

import heapq
import sys

infile=open(sys.argv[1], "r")
outfile=open(sys.argv[2], "w")


num_vertices=int(infile.readline())
num_edges=int(infile.readline())

adj={ i:[] for i in range(1, num_vertices+1) }

for lineNumber in range(1, num_edges+1):
    inputLine=infile.readline().split()
    i, j, weight=int(inputLine[0]), int(inputLine[1]), int(inputLine[2])
    adj[i].append([weight,j,lineNumber])
    adj[j].append([weight,i,lineNumber])

total_weight=0
visit=set()
minH=[[0, 1, None, None]]

res=[]

while len(visit)<num_vertices:
    cost, i, j, label=heapq.heappop(minH)

    if i in visit:
        continue

    total_weight+=cost
    
    if label:
        res.append([cost, 
            "{:>4}".format(str(label))+": ("+str(min(i, j))+", "+
            str(max(i, j))+") "+"{:0.1f}".format(round(cost,1))])

    visit.add(i)

    for neiCost, nei, line in adj[i]:
        if nei not in visit:
            heapq.heappush(minH,[neiCost, nei, i, line])

res.sort()

for i, [cost, edge] in enumerate(res):
    outfile.write(edge+"\n")
    
outfile.write("Total Weight = {:0.2f}".format(round(total_weight, 2))+"\n")

infile.close()
outfile.close()