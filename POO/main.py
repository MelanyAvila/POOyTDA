from clases.Libro import *
from clases.Rectangulo import *
from clases.Calculadora import *
from clases.Herencia.Animal import *
from clases.Herencia.Perro import *
from clases.Herencia.Gato import *
from clases.Cuenta_bancaria import *

from funciones.metodos import *

# CLASES
# 1-
libro_ej = Libro('Harry Potter y la piedra filosofal', 'J.K. Rowling', 1997)

informacion_libro1 = libro_ej.obtener_informacion()
print(informacion_libro1)

# 2-
rectangulo_ej = Rectangulo(5.0, 3.0)

area_rectangulo_ej = rectangulo_ej.calcular_area()
print(f'el area del rectángulo es: {area_rectangulo_ej}')

perimetro_rectangulo_ej = rectangulo_ej.calcular_perimetro()
print(f'el perímetro del rectángulo es: {perimetro_rectangulo_ej}')

# 3-
calculadora = Calculadora()

suma = calculadora.sumar(8, 9)
print(f'la suma da: {suma}')

resta = calculadora.restar(4, 2)
print(f'la resta da: {resta}')

multiplicacion = calculadora.multiplicar(4, 2)
print(f'la multiplicación da: {multiplicacion}')

division = calculadora.dividir(8, 2)
print(f'la división da: {division}')

division_error = calculadora.dividir(6, 0)
print(division_error)

# 4-
perro_ej = Perro("Firulais")
gato_ej = Gato("Misu")

print(f'el perro {perro_ej.nombre} hace: {perro_ej.hacer_sonido()}') 
print(f'Ee gato {gato_ej.nombre} hace: {gato_ej.hacer_sonido()}')

# 5-
cuenta = CuentaBancaria("Juan Pérez", 10000)

saldo_ej = cuenta.obtener_saldo()
print(f'saldo actual: {saldo_ej}')

depositar_saldo_ej = cuenta.depositar(500.0)
if depositar_saldo_ej:
    print(f'deposito exitoso, saldo actual: {depositar_saldo_ej}')

retirar_saldo = cuenta.retirar(300.0)
if retirar_saldo:
    print(f'retiro exitoso, saldo actual: {retirar_saldo}')

# CADENA DE CARACTERES-Métodos
# 1-
cadena_ej = 'HOLA MUNDOOooOOOOo'
cadena_invertida = invertir_cadena(cadena_ej)
print(cadena_invertida)  

# 2-
cadena_ej_2 = 'un ejemplo de cadena con palabras'
numero_de_palabras = contar_palabras(cadena_ej_2)
print(f'número de palabras: {numero_de_palabras}') 

# 3-
cadena_ej_3 = 'hola mundo, este es un ejemplo de cadena'
cadena_modificada = reemplazar_palabra(cadena_ej_3, 'mundo', 'amigo(?)')
print(cadena_modificada)  

# 4-
lista_peli = [
    ["Matrix", "El Padrino", "Titanic"],
    ["Forrest Gump", "Pulp Fiction", "Gladiador"],
    ["Blade Runner", "El Rey León", "Volver al Futuro"],
    ["La La Land", "El Gran Lebowski", "Blade Runner"],
    ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
    ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
    ["Titanic", "Star Wars", "El Señor de los Anillos"],
    ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
    ["Forrest Gump", "The Godfather", "Goodfellas"],
    ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]

recomendaciones = recomendar_peliculas(lista_peli)
print(recomendaciones)
