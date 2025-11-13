import trianguloOOP as tl 

#Instanciar a classe
trianguloX = tl.triangulo()
trianguloY = tl.triangulo()

#Entrada de dados
print("Inserir as medidas do triangulo X")
trianguloX.a = (int(input("Medida a: ")))
trianguloX.b = (int(input("Medida b: ")))
trianguloX.c = (int(input("Medida c: ")))
print("Inserir as medidas do triangulo Y")
trianguloY.a = (int(input("Medida a: ")))
trianguloY.b = (int(input("Medida b: ")))
trianguloY.c = (int(input("Medida c: ")))

#Processamento de dados
areax = trianguloX.area()
areay = trianguloY.area()

#Condicional
if areax > areay:
    saida = "A area do triangulo x é maior que a área do triangulo y"
elif areay > areax:
    saida = "A area do triangulo y é maior que a área do triangulo x"
else:
    saida = "As áreas dos triangulos são iguais"

#Saida de dados         
print(f"A área do triangulo x = {areax:.1f}")
print(f"A área do triangulo y = {areay:.1f}")
print(saida)