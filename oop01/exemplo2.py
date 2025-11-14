import produtoOOP as p #Importar o modulo
p1 = p.Produto() #Instanciar o objeto
#Entrada de dados
print("Digite os dados do produto")
p1.nome = input("\tNome: ")
p1.preco = float(input("\tPreco: R$"))
p1.saldo = int(input("\tQuantidade: "))
#Saída de dados 1
print(p1.dadosDoProduto())
#Adicionar produtos
q = int(input("Digite o número de produtos a ser adicionado ao estoque: "))
p1.adicionarProdutos(q)
#Saida de dados 2
print("--Dados atualizados--")
print(p1.dadosDoProduto())
#Remover produtos
q = int(input("Digite o número de produtos a ser removido ao estoque: "))
p1.removerProdutos(q)
#Saída de dados 3
print("--Dados atualizados--")
print(p1.dadosDoProduto())
