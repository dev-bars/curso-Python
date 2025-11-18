#-----classe ContaBancaria------
class ContaBancaria:
    #Atributos privados da classe
    __numero:int
    __titular:str
    __saldo:float

    #Propriedades para acessar os membros da classe
    @property
    def numero(self, numero):
        self.__numero = numero

    @property
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self, saldo):
        self.__saldo = saldo

    #Construtor
    def __init__(self, num:int = 0, titular:str = "", saldo:float = 0):
        self.__numero = num
        self.__titular = titular
        self.__saldo = saldo

    #Metodos
    def depositar(self, quantia):
        self.__saldo = self.__saldo + quantia
    
    def sacar(self, quantia):
        self.__saldo = self.__saldo - quantia

    def mostrarDados(self):
        print("Numero da conta: ", self.__numero)
        print("Titular da conta: ", self.__titular)
        print("Saldo da conta: R$ %.2f" % self.__saldo)
#------Fim classe------


#------Programa Principal------
#Entrada de dados
numero = int(input("Digite o numero da conta: "))
titular = str(input("Digite o nome do titular: "))
adriano = str(input("Deseja fazer um depósito inicial (s/n): "))

if adriano == "s":
    saldo = float(input("Digite o saldo inicial: "))
    conta = ContaBancaria(numero, titular, saldo)
else:
    conta = ContaBancaria(numero, titular, 0.0)

#Saida de dados
print("Dados da conta:")
conta.mostrarDados()

#Depósito
quantia = float(input("Digite a quantia a ser depositada: R$ "))
conta.depositar(quantia)
print("Dados da conta atualizados: ")
conta.mostrarDados()

#Saque
quantia = float(input("Digite a quantia do saque: R$ "))
conta.sacar(quantia)
print("Dados da conta atualizados: ")
conta.mostrarDados()