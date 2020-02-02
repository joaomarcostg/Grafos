import numpy as np
import time

def minimo(copiaQ, dist):
    menor = 99999
    pos = None
    for i in range(len(copiaQ)):
        j = int(copiaQ[i])
        if(dist[j] < menor):
            menor = dist[j]
            pos = j
    return pos

def arestaij(listaAdj, i, j):
    for k in listaAdj[i]:
        if(k[0] == j):
            return k[1]
    return False

def dijkstra(listaAdj, s, t):
    dist = []
    pred = []
    time1 = time.time()
    for v in range(len(listaAdj)):
        dist.append(99999)
        pred.append(None)
    dist[s] = 0
    copyAdj = []
    for i in range(len(listaAdj)):
        copyAdj.append(i)
    while(len(copyAdj) != 0):
        u = minimo(copyAdj, dist)
        copyAdj.remove(u)
        for v in listaAdj[u]:
            if(dist[v[0]] > (dist[u] + v[1])):
                dist[v[0]] = (dist[u] + v[1])
                pred[v[0]] = u
    time2 = time.time()
    print('Dijkstra demorou {:.3f} segundos' .format((time2-time1),float))
    menorcaminho = recaminho(s, t, pred)
    print('Menor Caminho: ' + str(menorcaminho))
    custo = dist[t]
    print('Custo: ' + str(custo))


def bellmanford(listaAdj, arestas, s, t):
    dist = []
    pred = []
    time1 = time.time()
    for v in range(len(listaAdj)):
        dist.append(99999)
        pred.append(None)
    dist[s] = 0
    for i in range(len(listaAdj)):
        for a in arestas:
            if(dist[a[1]] > (dist[a[0]] + a[2])):
                dist[a[1]] = (dist[a[0]] + a[2])
                pred[a[1]] = a[0]
    for a in arestas:
        if(dist[a[1]] > (dist[a[0]] + a[2])): 
            menorcaminho = recaminho(0, 4, pred)
            print('Menor Caminho: ' + str(menorcaminho))
            return False
    time2 = time.time()
    print('Bellman-Ford demorou {:.3f} segundos' .format((time2-time1),float))
    menorcaminho = recaminho(s, t, pred)
    print('Menor Caminho: ' + str(menorcaminho))
    custo = dist[t]
    print('Custo: ' + str(custo))
    return True


def floydwarshal(listaAdj, arestas, s, t):
    dist = [[None for x in range(len(listaAdj))] for x in range(len(listaAdj))]
    pred = [[None for x in range(len(listaAdj))] for x in range(len(listaAdj))]

    time1 = time.time()

    for i in range(len(listaAdj)):
        for j in range(len(listaAdj)):
            w = False
            for k in listaAdj[i]:
                if(k[0] == j):
                    w = k[1]
            if(i == j):
                dist[i][j] = 0
            elif(w != False):
                dist[i][j] = w
                pred[i][j] = i
            else:
                dist[i][j] = 99999
                pred[i][j] = None
    for k in range(len(listaAdj)):
        for i in range(len(listaAdj)):
            for j in range(len(listaAdj)):
                if(dist[i][j] > dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    time2 = time.time()
    print('Floyd-Warshal demorou {:.3f} segundos' .format((time2-time1),float))
    menorcaminho = recaminho(s, t, pred[s])
    print('Menor Caminho: ' + str(menorcaminho))
    custo = dist[s][t]
    print('Custo: ' + str(custo))


def recaminho(s, t, pred):
    C = [t]
    aux = t
    while(aux != s):
        aux = pred[aux]
        C.insert(0, aux)
    return C
