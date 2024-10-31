# 3- Clase para representar una Calculadora Crear una clase Calculadora que pueda calcular
# suma, resta, multiplicación y división. Se debe crear la clase e implementarla.

class Calculadora:
    def __init__(self)-> None:
        pass  # aca no sé que iria
    
    def sumar(self, a: float, b: float) -> float:
        suma = a + b
        return suma
    
    def restar(self, a: float, b: float) -> float:
        resta = a - b
        return resta
    
    def multiplicar(self, a: float, b: float) -> float:
        multiplicacion = a * b
        return multiplicacion
    
    def dividir(self, a: float, b: float):
        if b == 0:
            print('error, no se puede dividir por 0')
        else:
            division = a / b
            return division
        
    def dividir(self, a: float, b: float)-> str: 
        if b == 0: 
            resultado = 'error, no se puede dividir por 0' 
        else: 
            division = a / b 
            resultado = f'La división da: {division}' 
        return resultado