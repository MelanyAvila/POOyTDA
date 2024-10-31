# 5- Encapsulamiento Crear una clase Cuenta Bancaria que tenga las características titular y
# saldo encapsulado. 
# De la cuenta bancaria se puede obtener el saldo, depositar o retirar (en
# cada caso imprimir que fue exitoso). Se debe crear la clase e implementarla

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0)-> None:
        self.__titular = titular  
        self.__saldo = saldo  

    def obtener_saldo(self) -> float:
        return self.__saldo

    def depositar(self, cantidad: float):
        if cantidad > 0:
            self.__saldo += cantidad
            return self.__saldo
        else:
            print('la cantidad debe ser positiva.')

    def retirar(self, cantidad: float):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return self.__saldo
        else:
            print('cantidad inválida.')

