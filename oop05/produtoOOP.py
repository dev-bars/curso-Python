class Produto(): #Super classe ou classe pai
    #1° Membro - ATRIBUTOS
    __nome:str 
    __preco:float 
    __quantidade:int 

    #2° Membro - PROPRIEDADES PROTEGIDAS
    #Propriedades do atributo Nome
    @property
    def _nome(self)->str:
        return self.__nome 
    @_nome.setter 
    def _nome(self, nome:str)->str:
        self.__nome = nome
    #Propriedades do atributo Preco
    @property
    def preco(self)->float:
        return self.__preco 
    @_nome.setter 
    def _nome(self, nome:str)->str:
        self.__nome = nome
    #Propriedades do atributo quantidade
    @property
    def quantidade(self)->int:
        return self.__quantidade 
    @_quantidade.setter 
    def _quantidade(self, quantidade:int)->int:
        self.__quantidade = quantidade

    #3° Membro - CONSTRUTOR
    def __init__(self, nome:str, preco:float, quantidade:int):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    #4° Membro - METODOS
    def operacao():
        pass

    class Software(Produto):  #Subclasse de produto
        #1° Membro - Atributo
        licenca:str 
        #2° Menbro - Propriedade
        @property
        def licenca(self)->str:
            return self.__licenca 
        @licenca.setter
        def _licenca(self, licenca:str):
            self.__licenca = licenca
        #3° Membro - Construtor
    def __init__(self, nome:str, preco:float, quantidade:int, licenca:str, garantia:int):
        super().__init__(nome, preco, quantidade)
        self.__garantia = garantia

#------ FIM CLASSES ------

#------ MAIN CODE ------
software = Software("Adobe", 1000, 10, "2010")
hardware = Hardware("Dell", 2000, 10, 6)

software.operacao()
hardware.operacao()

