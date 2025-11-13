#Problema triangulo sem oop
#Entrada de dados
#TRIANGULO X
print("Inserir as medidas do triangulo x")
ax = int(input("Digite a medida a: "))
bx = int(input("Digite a medida b: "))
cx = int(input("Digite a medida c: "))

#TRIANGULO Y
print("Inserir as medidas do triangulo y")
ay = int(input("Digite a medida a: "))
by = int(input("Digite a medida b: "))
cy = int(input("Digite a medida c: "))

#Processamento de dados
p = (ax + bx + cx) / 2
areax = (p * (p - ax) * (p - bx) * (p - cx)) ** 0.5

p = (ay + by + cy) / 2
areay = (p * (p - ay) * (p - by) * (p - cy)) ** 0.5

#Saída de dados
if areax > areay:
    saida = "A area do triangulo x é maior que a área do triangulo y"
elif areay > areax:
    saida = "A area do triangulo y é maior que a área do triangulo x"
else:
    saida = "As áreas dos triangulos são iguais"

print(f"A área do triangulo x = {areax:.1f}")
print(f"A área do triangulo y = {areay:.1f}")
print(saida)