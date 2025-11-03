#Problema terreno
largura:float
comprimento:float

#Entrada de dados
largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))
valor_metro_quadrado = float(input("Digite o valor do metro quadrado em reais: "))

# Processamento de dados
area = largura * comprimento
preco = area * valor_metro_quadrado

# Saida de dados
print(f"A area do terreno é: {area:.2f}, o preço do terreno é de: R$ {preco:.2f}")