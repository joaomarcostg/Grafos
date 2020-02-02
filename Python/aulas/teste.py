#import info
import busca
#leitura do arquivo fonte do grafo
import caminhominimo
#fileName = input("Insira o nome do arquivo: ")
file = open("grafo.txt")
import arvoresgeradoras

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

print(listaAdj)
print(matrizAdj)
arestas = [(0,2,7), (0,1,2), (2,3,1), (1,2,2), (1,3,8), (2,1,3), (3,4,4), (1,4,5), (4,3,5)]
print(arestas)

def densidade(vertices, arestas):
    d = len(arestas)/(len(vertices) * (len(vertices) -1))
    return d


def complemento(matAdj):
    matCopy = matAdj.copy()
    for i in range(len(matAdj)):
        for j in range(len(matAdj[i])):
            if(i != j):
                if(matAdj[i][j] == 0):
                   matCopy[i][j] = 1
                else:
                    matCopy[i][j] = 0
    return matCopy

def completo(matAdj):
    for i in range(len(matAdj)):
        for j in range(len(matAdj[i])):
            if(i != j):
                if(matAdj[i][j] == 0):
                    return False

    return True

def regular(matAdj):
    grauAnterior = -1
    for i in range(len(matAdj)):
        grau = 0
        for j in range(len(matAdj[i])):
            if(matAdj[i][j] != 0):
                grau+=1
        if(grauAnterior != -1 and grauAnterior != grau):
            return False
        grauAnterior = grau
    return True
            


op = 1
print("Lista ADJ")
print(listaAdj)
while (op != 0):
    op = int(input("Operacao: \n" +
            "1. Densidade\n" +
            "2. Complemento\n" +
            "3. Completo\n" +
            "4. Regular\n" + 
            "5. Busca Largura\n" + 
            "6. Busca Profundidade\n" + 
            "7. Busca Profundidade - Recursiva\n" + 
            "8. Componentes Conexas\n" + 
            "9. Ordem Topológica\n" + 
            "10. Dijkstra\n" +
            "11. Bellman-Ford\n" +
            "12. Floyd-Warshall\n" +
            "13. Prim\n" +
            "14. GreedyCol\n" +
            "0. Sair\n"))
    if(op == 1):
        den = densidade(vertices, arestas)
        print(den)
    elif(op == 2):
        cmp = complemento(matrizAdj)
        print(cmp)
    elif(op == 3):
        completo = completo(matrizAdj)
        if(completo):
            print('Grafo Completo')
        else:
            print('Grafo incompleto')
    elif(op == 4):
        reg = regular(matrizAdj)
        if(reg):
            print('Grafo Regular')
        else:
            print('Grafo Irregular')
    elif(op == 5):
        busca.buscalargura(listaAdj, 0)
    elif(op == 6):
        busca.buscaprofundidade(listaAdj, 0)
    elif(op == 7):
        busca.profundidade(listaAdj, 0)
    elif(op == 8):
        busca.componentesconexas(listaAdj)
    elif(op == 9):
        busca.ordemtopologica(listaAdj)
    elif(op == 10):
        caminhominimo.dijkstra(listaAdj, 0, 4)
    elif(op == 11):
        caminhominimo.bellmanford(listaAdj, arestas, 0, 4)
    elif(op == 12):
        caminhominimo.floydwarshal(listaAdj, arestas, 0, 4)
    elif(op == 13):
        arestas = arvoresgeradoras.prim(listaAdj, 0)
    elif(op == 14):
        S = arvoresgeradoras.greedycol(listaAdj)
        print(S)
    
        

    


