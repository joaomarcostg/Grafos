import caminhominimo
import time
import numpy as np
#fileName = input("Insira o nome do arquivo: ")
file = open('Datasets/rg300_4730.txt')


str = file.readline()
str = str.split(" ")
numVertices = int(str[0])
numArestas = int(str[1])

#preenchimento das estruturas de dados

listaAdj = [[] for x in range(numVertices)]
matrizAdj = [[0 for x in range(numVertices)] for x in range(numVertices)]
vertices = [x for x in range(numVertices)]
arestas = []


for i in range(numArestas):
    str = file.readline()
    str = str.split(" ")
    origem = int(str[0])
    destino = int(str[1])
    peso = int(str[2])
    listaAdj[origem].append((destino, peso))
    matrizAdj[origem][destino] = peso
    arestas.append((origem, destino, peso))


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


opc = 1

while (opc != 0):
    opc = int(input("Selecione o algoritmo de caminho mínimo: \n" +
            "1. Dijkstra\n" +
            "2. Bellman-Ford\n" +
            "3. Floyd-Warshall\n" +
            "0. Sair\n"))
    if(opc == 1):
        # timing(caminhominimo.dijkstra)(listaAdj, 0)
        caminhominimo.dijkstra(listaAdj, 0, 18)
    elif(opc == 2):
        caminhominimo.bellmanford(listaAdj, arestas, 0, 18)
    elif(opc == 3):
        caminhominimo.floydwarshal(listaAdj, arestas, 0, 18)