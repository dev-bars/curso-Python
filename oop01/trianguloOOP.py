class triangulo:
    #Atributos
    a:int
    b:int
    c:int

    a = 0
    b = 0
    c = 0
    
    #Métodos
    def area(self): #Self é um paramettro, aponta a informação que foi inseridos pelo usuario
        p = (self.a + self.b +self.c) / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return area