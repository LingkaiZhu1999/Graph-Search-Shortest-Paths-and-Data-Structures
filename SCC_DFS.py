# Kosaraju
import sys, threading

# Compute the number of SCCs using DFS
from collections import defaultdict

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

    explored_G_rev = []  # mark all vertices of the reversive G as unexplored
    explored_G = []
    # for vertex in graph:
    #   explored_G_rev[vertex]=False
    #  explored_G[vertex]=False
    f_s = {}
    numSCC = 0
    G_rev = defaultdict(list)
    for head in G:
        for tail in G[head]:
            G_rev[tail].append(head)


    def Kosaraju(directed_graph):
        global numSCC
        # Compute the reverse graph, with all edges reversed
        # first pass of depth-first search, computes f(v)'s, the magical ordering
        TopoSort(G_rev)
        print(f_s)
        # second pass of depth-first search, finds SCCs in reverse topological order
        order = {v: k for k, v in f_s.items()}

        for i in range(len(order)):
            element = order[i + 1]
            if element not in explored_G:
                # print(element)
                numSCC += 1
                # assign scc-values
                DFS_SCC(directed_graph, element)

    def DFS_SCC(graph, vertex):
        explored_G.append(vertex)
        scc[vertex] = numSCC
        for tail in graph[vertex]:
            if tail not in explored_G:
                DFS_SCC(graph, tail)

    # TopoSort Algorithm
    # Input directed acyclic graph

    # mark all vertices as unexplored
    def TopoSort(graph):
        # f_s = {}
        # keep track of ordering
        for vertex in list(graph):
            if vertex not in explored_G_rev:
                DFSTopo(graph, vertex)

    # DFS-Topo
    # Input graph and vertex
    stack = []
    global curLabel
    curLabel = 875714

    def DFSTopo(graph, start_vertex):
        global curLabel

        explored_G_rev.append(start_vertex)
        for neighbour in graph[start_vertex]:
            if neighbour not in explored_G_rev:
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
    print(scc)


thread = threading.Thread(target=main)
thread.start()
