import random
import math

def read_file():
    graph = {}

    f = open('kargerMinCut.txt', 'r')
    for i in range(0, 201):
        read_data = f.readline()
        linelist = read_data.split('\t')
        graph[linelist[0]] = [int(i) for i in linelist[1:-1]]

    f.close()
    graph.pop('')
    return graph

def pick_pair(graph):
    pivot = random.choice(list(graph.keys()))
    off = str(random.choice(graph[pivot]))
    return pivot, off

def one_trail():
    graph = read_file()
    while len(graph) >2:
        pivot, off  = pick_pair(graph)
        v1 = graph.pop(pivot)
        v2 = graph.pop(off)

        graph[pivot] = v1+v2

        for i in graph.keys():
            if int(off) in graph[i]:
                count = graph[i].count(int(off))
                graph[i] = list(filter(lambda x: x != int(off), graph[i]))
                graph[i] += [int(pivot)]*count

        graph[pivot] = list(filter(lambda x: x != int(pivot), graph[pivot]))
    return len(list(graph.values())[0])



if __name__ == "__main__":
    result = list()
    for i in range(round(100)): #should be 20**2*math.log(200) times to reduce the probability down to 1/n
        result.append(one_trail())

    print(min(result))          #the result should be 17
    print(result)