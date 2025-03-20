'''
Jennifer Marlene Gutiérrez Beteta
20 de Marzo de 2025.
Descripción del programa:
'''

class CuentaBancaria:

    # __________________Constructor___________________________
    def __init__(self, titular: str, saldo_inicial: float = 0) -> None:
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self,cantidad:float)-> None:
        #self._saldo = cantidad
        pass

    def retirar(self,cantidad:float)-> None:
        pass

    @property
    def saldo(self)-> float:
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo: float) -> None:
        self._saldo = nuevo_saldo

    def __str__(self) -> str:
        return (f"Titular id: {self.titular},Saldo:{self.saldo}")

#- privados
##protegido
#+ metodos publicos
if __name__ == '__main__':
    cuenta_guadalupe = CuentaBancaria("Guadalupe",10)
    print(cuenta_guadalupe)