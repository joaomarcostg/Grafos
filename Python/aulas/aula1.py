#IMC

# peso = float(input("Digite o peso: "))
# altura = float(input("Digite a altura: "))

# imc = peso/pow(altura, 2)

# print('IMC:')
# print(imc)

# if(imc < 18.5):    
#     print('Abaixo do peso')

# elif(imc <= 25 and imc >= 18.5 ):
#     print('Peso Ideal')

# elif(imc > 25):
#     print('Acima do peso')


#BHASKARA

# a = float(input('Insira a: '))
# b = float(input('Insira b: '))
# c = float(input('Insira c: '))

# delta = pow(b, 2) - (4*a*c)
# print('Delta = ' + str(delta))

# if(delta < 0):
#     print('ImpossÍvel realizar a operação')

# elif(delta == 0):
#     raiz1 = (-1*b)/(2*a)
#     print('Raiz 1 = ' + str(raiz1))

# elif(delta > 0):
    
#     raiz1 = (-1*b + pow(delta, 1/2))/(2*a)
#     raiz2 = (-1*b - pow(delta, 1/2))/(2*a)
#     print('Raiz 1 = ' + str(raiz1))
#     print('Raiz 2 = ' + str(raiz2))

# ENCONTRAR INDICE DE ELEMENTO

# lista = ['a', 'b', 'c', 'd', 'e']

# searched = str(input('Insira o elemento: '))

# def find(lista, searched):
#     try:
#         resp = lista.index(searched)    
#         return resp
#     except ValueError:
#         return -1        

# resp = find(lista, searched)

# if(resp != -1):
#     print("Indice: " + str(resp))
# else:
#     print('Nao encontrado')

#CALCULA MÉDIA DA LISTA

# lista = [2,4,6,7,3,0,5,3,8,11]
# soma = 0

# for i in lista:
#     soma = float(i + soma) 

# media = float(soma / len(lista))

# print('Media: ' + str(media))

#MEDIA 2

# n = int(input("Tamanho da lista: "))
# i=0
# lista = []
# soma = 0

# while(i < n):
#     e = input("Insira o elemento %d: " % (i+1))
#     lista.append(e)
#     i+=1

# for j in lista:
#     soma = float(j) + soma

# media = float(soma / len(lista))

# print('Media: ' + str(media))