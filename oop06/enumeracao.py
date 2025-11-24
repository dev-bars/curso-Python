from enum import Enum 
class Estados_Pedidos(Enum):
    Pagamento_Pendente = 0
    Processamento = 1
    Enviado = 2
    Entregue = 3
    Cancelado = 4

#Exemplos de uso
print(Estados_Pedidos(2))
print(Estados_Pedidos.Enviado.name)#Imprime nome do estado
print(Estados_Pedidos.Enviado.value)#Imprime valor do estado
print(Estados_Pedidos.Cancelado)
print(Estados_Pedidos(1).name)#Imprime o nome do estado a partir do valor