from multiprocessing import Process
import time
import caixeiro

fileName = input("Insira o nome do arquivo: ")
file = open('Datasets2/' + fileName + '.txt')


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
    peso = float(str[2])
    listaAdj[origem].append((destino, peso))
    matrizAdj[origem][destino] = peso
    arestas.append((origem, destino, peso))


# print(matrizAdj)
tempoinicio = time.time()
S = caixeiro.nearestneighbour(matrizAdj)
print('Processando...')
R = caixeiro.twoopt(S, matrizAdj)
tempofim = time.time()
diff =  tempofim - tempoinicio
print('Tempo: %.8f secs' %diff)