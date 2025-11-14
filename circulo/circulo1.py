from calculadora import calculadora1
#Entrada de dados
raio = float(input("Digite o valor do raio: "))
#Processamento de dados
circunferencia = calculadora1.circunferencia(raio)
area = calculadora1.area(raio)
#Saida de dados
print(f''' Circunferencia: {circunferencia:.2f}
      Area: {area:.2f}
      PI: {calculadora1.PI})
      ''')