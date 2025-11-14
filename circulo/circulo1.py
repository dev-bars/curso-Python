import calculadora as c
#Instanciação do objeto
circulo = c.calculadora1()
#Entrada de dados
raio = float(input("Digite o valor do raio: "))
#Processamento de dados
#chamar os métodos
circunferencia = circulo.circunferencia(raio)
area = circulo.area(raio)
#Saida de dados
print(f''' Circunferencia: {circunferencia:.2f}
      Area: {area:.2f}
      PI: {circulo.PI})
      ''')