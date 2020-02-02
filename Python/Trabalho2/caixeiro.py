import random
import time

def menorDist(u, matrizAdj, naoVisitados):
    menorDist = 9999
    menorIndex = None
    for (i,v) in enumerate(matrizAdj[u]):
        try :
            if(naoVisitados.index(i) != ValueError):
                if(matrizAdj[u][i] < menorDist):
                    menorDist = matrizAdj[u][i]
                    menorIndex = i
        except ValueError:
            continue
    return menorIndex

def calcularDist(matrizAdj, S):
    dist = 0
    for (i,v) in enumerate(S):
        if(i < len(S)-1):
            j = i+1
            u = S[i]
            n = S[j]
            dist = dist + matrizAdj[u][n]
    return dist


def nearestneighbour(matrizAdj):
    naoVisitados = []
    for (i,v) in enumerate(matrizAdj[0]):
        naoVisitados.append(i)
    u = 0
    S = []
    S.append(u)
    naoVisitados.remove(u)
    while(len(naoVisitados) > 0):
        v = menorDist(u, matrizAdj, naoVisitados)
        S.append(v)
        naoVisitados.remove(v)
        u = v
    S.append(S[0])
    dist = calcularDist(matrizAdj, S)
    print('Distancia NN: '+ str(dist))
    return S


def twoopt(S, matrizAdj):
    tempoinicio = time.time()
    diff = 0
    while(diff < 60):
        i1 = random.randint(1, len(S)-2)
        i2 = random.randint(1, len(S)-2)
        if(i1 != i2):
            S_ = S.copy()
            aux = S_[i1]
            S_[i1] = S_[i2]
            S_[i2] = aux
            if(avalia(S_, matrizAdj) < avalia(S, matrizAdj)):
                S = S_.copy()
        tempoexec = time.time()
        diff = tempoexec-tempoinicio
    dist = calcularDist(matrizAdj, S)
    print('Distancia 2opt: '+ str(dist))
    print('Rota:')
    print(S)
    return S


def avalia(S, matrizAdj):
    custo = 0
    for i in range(len(S)-1):
        u = S[i]
        v = S[i + 1]
        custo = custo + matrizAdj[u][v]
    return custo