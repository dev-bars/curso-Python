#LISTA EM PYTHON
#Lista aceita todos os tipos (string, booleano, inteiro, float) e pode mudar
lista = ["senai", True, 22, 3.5] 
print(lista) #Demonstra todos itens(indicies) da lista}
print(type(lista)) #Demonstra o tipo de classe
print(lista[2])#Demonstra o indicie mencionado
print(len(lista)) #Demonstra a quantidade da lista
lista.insert(1, "Campeao") #Insere no indicie a informação
lista.append("ultimo") #Insere informação no ultimo indicie
del lista[3] #Exclui a informação do indicie
print(lista)

#TUPLA EM PYTHON
#Tupla é uma coleção de dados constantes: que não muda, não altera
tupla = ("senai", True, 22, 3.5)
print(tupla)
print(type(tupla))
print(tupla[3])
print(tupla)

#DICIONÁRIOS EM PYTHON
#Dicionario tem um valor chave e seu valor
dicionario = {"nome": "Senai", "logica:": False, "num": 20}
print(dicionario)
print(dicionario["logica:"])
dicionario.update({"novo": "Senai"})
del dicionario["logica:"]
for chave in dicionario.keys(chave, "=>", dicionario{chave})

#CONJUNTO EM PYTHON
#Conjunto é uma coleção desordenada, (na vdd demonstra por ocupação de memória do CPU)
conjunto = {"Senai", False, 10, 3.69}
print(conjunto)
conjunto.add(23)
conjunto.discard("Senai") #Exclui a informação
conjunto.clear() #Apaga tudo dentro do conjunto