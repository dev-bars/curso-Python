class Pessoa:
    #Atributos
    nome: str
    idade: int

    #Construtor
    def __init__(self, nome:str = "", idade:int = 0):
        self.nome = nome
        self.idade = idade

    #Metodos
    def eh_mais_velha(self, outra_pessoa):
        return self.idade > outra_pessoa


        
    
    