def minimo(copiaQ, dist):
    menor = 999999
    pos = None
    for i in range(len(copiaQ)):
        j = int(copiaQ[i])
        if(dist[j] < menor):
            menor = dist[j]
            pos = j
    return pos

def prim(listAdj, s):
    dist = []
    pai = []
    interligado = []
    Q = []
    A = []
    for v in range(len(listAdj)):
        dist.append(99999)
        pai.append(None)
        interligado.append(False)
        Q.append(v)
    dist[s] = 0
    interligado[s] = False
    print(Q)
    Q.remove(s)
    for v in listAdj[s]:
        if(dist[v[0]] > v[1]):
            dist[v[0]] = v[1]
            pai[v[0]] = s
    while(len(Q) != 0):
        u = minimo(Q, dist)
        print(u)
        print(Q)
        Q.remove(u) 
        interligado[u] = True
        for v in listAdj[u]:
            if(dist[v[0]] > v[1]):
                dist[v[0]] = v[1]
                pai[v[0]] = u
        A.append((pai[u], u))
    print(A)
    return A


def kruskal(listAdj, arestas):
    C = []
    for i in range(len(listAdj)):
        C[i] = i

def greedycol(listAdj):
    S = []
    Cores = []
    for i in range(len(listAdj)):
        S.append(i)
        Cores.append(i)
    print('S:')
    print(S)
    print('Cores:')
    print(Cores)
    for u in range(len(listAdj)):
        print('u: ' + str(u))
        print('Adj: ' + str(listAdj[u]))
        CoresPossiveis = Cores.copy()
        for i in Cores:
            print('i: ' + str(i))
            for v in listAdj[u]:
                if(v[0] == i and (CoresPossiveis.count(i) > 0)):
                    CoresPossiveis.remove(i)
            S[u] = CoresPossiveis[0]
        print(CoresPossiveis)
    return S
     