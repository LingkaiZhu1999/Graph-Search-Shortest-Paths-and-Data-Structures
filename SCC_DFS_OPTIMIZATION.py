# Kosaraju
import sys, threading

# Compute the number of SCCs using DFS
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(800000)
threading.stack_size(67108864)


def main():
    h = open('SCC.txt', 'r')

    # Reading from the file
    content = h.readlines()

    G = defaultdict(list)

    for line in content:
        data = line.split()
        G[data[0]].append(data[1])
    global numSCC
    scc = {}
      # mark all vertices of the reversive G as unexplored

    # for vertex in graph:
    #   explored_G_rev[vertex]=False
    #  explored_G[vertex]=False
    f_s = {}
    numSCC = 0
    global curLabel
    curLabel = 875714
    print(curLabel)
    G_rev = defaultdict(list)
    for head in G:
        for tail in G[head]:
            G_rev[tail].append(head)
    explored_G = defaultdict(list)
    explored_G_rev = defaultdict(list)
    for i in range(1, curLabel + 1):
        explored_G[str(i)] = False
        explored_G_rev[str(i)] = False

    print(explored_G_rev['1'])

    def Kosaraju(directed_graph):
        global numSCC
        # Compute the reverse graph, with all edges reversed
        # first pass of depth-first search, computes f(v)'s, the magical ordering
        TopoSort(G_rev)
        # second pass of depth-first search, finds SCCs in reverse topological order
        order = {v: k for k, v in f_s.items()}

        for i in range(len(order)):
            element = order[i + 1]
            if explored_G[element] == False:
                # print(element)
                numSCC += 1
                # assign scc-values
                DFS_SCC(directed_graph, element)

    def DFS_SCC(graph, vertex):
        explored_G[vertex] = True
        scc[vertex] = numSCC
        for tail in graph[vertex]:
            if explored_G[tail] == False:
                DFS_SCC(graph, tail)

    # TopoSort Algorithm
    # Input directed acyclic graph

    # mark all vertices as unexplored
    def TopoSort(graph):
        # f_s = {}
        # keep track of ordering
        for vertex in list(graph):
            if explored_G_rev[vertex] == False:
                DFSTopo(graph, vertex)

    # DFS-Topo
    # Input graph and vertex
    stack = []


    def DFSTopo(graph, start_vertex):
        global curLabel

        explored_G_rev[start_vertex] = True
        for neighbour in graph[start_vertex]:

            if explored_G_rev[neighbour] == False:
                # print(neighbour)
                DFSTopo(graph, neighbour)
        f_s[start_vertex] = curLabel  # vertex's position in ordering
        curLabel -= 1

    '''
    stack.append(start_vertex)
    while stack:
        v = stack.pop(-1)
        if v not in explored_G_rev:
            explored_G_rev.append(v)
            for neighbour in graph[v]:
                stack.append(neighbour)
        else:
            try:
                f_s[stack.pop(-1)] = curLabel
                curLabel -= 1
            except:
                print("end")
        '''
    Kosaraju(G)
    for i in range(5):
        print(Counter(scc.values()).most_common(5)[i])


thread = threading.Thread(target=main)
thread.start()
