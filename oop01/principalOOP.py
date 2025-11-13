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
p = (trianguloX.a + trianguloX.b + trianguloX.c) / 2
areax = (p * (p - trianguloX.a) * (p - trianguloX.b) * (p - trianguloX.c)) ** 0.5

p = (trianguloY.a + trianguloY.b + trianguloY.c) / 2
areay = (p * (p - trianguloY.a) * (p - trianguloY.b) * (p - trianguloY.c)) ** 0.5

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