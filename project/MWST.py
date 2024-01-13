#!/usr/local/bin/python3
# your python code starts here

import heapq
import sys

def main():
    infile=open(sys.argv[1], "r")
    outfile=open(sys.argv[2], "w")
    
    # read the number of vertices and the number of edges
    num_vertices=int(infile.readline())
    num_edges=int(infile.readline())

    # create an adjacency list
    adj={ i:[] for i in range(1, num_vertices+1) }

    # read the vertex numbers and the weights
    for lineNumber in range(1, num_edges+1):
        inputLine=infile.readline().split()
        i, j, weight=int(inputLine[0]), int(inputLine[1]), float(inputLine[2])
        adj[i].append([weight,j,lineNumber])
        adj[j].append([weight,i,lineNumber])

    # initialize the total weight and visited set
    total_weight=0
    visit=set()
    minH=[[0, 1, None, None]]

    res=[]

    # use Prim's algorithm
    # The algorithm starts with an empty spanning tree. The idea is to maintain two sets of vertices. 
    # The first set contains the vertices already included in the MST, and the other set contains the vertices not yet included. 
    # At every step, it considers all the edges that connect the two sets and picks the minimum weight edge from these edges. 
    # After picking the edge, it moves the other endpoint of the edge to the set containing MST. 
    while len(visit)<num_vertices:
        weight, i, j, label=heapq.heappop(minH)

        if i in visit:
            continue

        total_weight+=weight
        
        if label:
            res.append([weight, 
                "{:>4}".format(str(label))+": ("+str(min(i, j))+", "+
                str(max(i, j))+") "+"{:0.1f}".format(round(weight,1))])

        visit.add(i)

        for neighborweight, neighbor, line in adj[i]:
            if neighbor not in visit:
                heapq.heappush(minH,[neighborweight, neighbor, i, line])

    # sort the result by weight
    res.sort()

    # write the edges to the output file
    for i, [weight, edge] in enumerate(res):
        outfile.write(edge+"\n")

    # write the total weight to the output file
    outfile.write("Total Weight = {:0.2f}".format(round(total_weight, 2))+"\n")


    infile.close()
    outfile.close()

if __name__ == "__main__":
    main()
