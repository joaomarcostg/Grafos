def buscalargura(listaAdj, s):
    visitado = []
    for i in range(len(listaAdj)):
        visitado.append(0)
    visitado[s] = 1
    print(s)
    fila = []
    fila.append(s)
    while(len(fila) != 0):
        u = fila.pop(0)
        for i in listaAdj[u]:
            v = i[0]
            if(visitado[v] == 0):
                visitado[v] = 1
                print(v)
                fila.append(v)


# def buscaprofundidade(listaAdj, s):
#     visitado  = []
#     for v in range(len(listaAdj)):
#         visitado.append(0)
#     visitado[s] = 1
#     print(s)
#     pilha = []
#     pilha.append(s)
#     while(len(pilha) != 0):
#         u = pilha[len(pilha) - 1]
#         vadj = listaAdj[u]
#         if(len(vadj)>0):
#             for v in vadj:
#                 if(visitado[v[0]] == 0):
#                     visitado[v[0]] = 1
#                     print(v[0])
#                     pilha.append(v[0])
#                 else:
#                     pilha.pop()

def buscaprofundidade(listaAdj, s):
    visitado  = []
    for v in range(len(listaAdj)):
        visitado.append(0)
    visitado[s] = 1
    print(s)
    pilha = []
    pilha.append(s)
    while(len(pilha) != 0):
        u = pilha[-1]
        existeAdj = False
        for i in listaAdj[u]:
            v = i[0]
            if(visitado[v] == 0):
                visitado[v] = 1
                print(v)
                pilha.append(v)
                existeAdj = True
                break
        if(not existeAdj):
            pilha.pop()


def profundidade(listaAdj, s):
    global visitado
    visitado = [0 for x in range(len(listaAdj))]
    prof(listaAdj, 0)
    

def prof(listaAdj, u):
    global visitado
    visitado[u] = 1
    print(u)
    for i in listaAdj[u]:
        v = i[0]
        if(visitado[v] == 0):
            prof(listaAdj, v)

def componentesconexas(listaAdj):
    global visitado
    visitado = []
    for v in range(len(listaAdj)):
        visitado.append(0)
    marca = 0
    for v in range(len(listaAdj)):
        if(visitado[v] == 0):
            marca += 1
            profcon(listaAdj, v, marca)

def profcon(listaAdj, u, marca):
    global visitado
    visitado[u] = marca
    print(u, marca)
    for i in listaAdj[u]:
        v = i[0]
        if(visitado[v] == 0):
            profcon(listaAdj, v, marca)

def ordemtopologica(listaAdj):
    global visitado
    global ordem
    ordem = []
    visitado = []
    for v in range(len(listaAdj)):
        visitado.append(0)
    for v in range(len(listaAdj)):
        if(visitado[v] == 0):
            proford(listaAdj, v)
    print(ordem)

def proford(listaAdj, u):
    global visitado
    global ordem
    visitado[u] = 1
    for i in listaAdj[u]:
        v = i[0]
        if(visitado[v] == 0):
            proford(listaAdj, v)
    ordem.insert(0, u)
