import classeAtividadeOOP01 as c

# Entrada de dados
nome1 = input("Digite o nome da pessoa 1: ")
idade1 = int(input(f"Digite a idade de {nome1}: "))

nome2 = input("Digite o nome da pessoa 2: ")
idade2 = int(input(f"Digite a idade de {nome2}: "))

# Criação dos objetos
p1 = c.Pessoa(nome1, idade1)
p2 = c.Pessoa(nome2, idade2)

# Comparação usando o método POO
if p1.eh_mais_velha(p2):
    print(f"{p1.nome} é mais velha, com {p1.idade} anos.")
elif p2.eh_mais_velha(p1):
    print(f"{p2.nome} é mais velha, com {p2.idade} anos.")
else:
    print(f"{p1.nome} e {p2.nome} têm a mesma idade.")
