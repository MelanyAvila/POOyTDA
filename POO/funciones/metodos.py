# CADENA DE CARACTERES-Métodos
# Ejercicio 1:
def invertir_cadena(cadena: str) -> str:
    cadena_invertida = cadena[::-1]
    return cadena_invertida

# Ejercicio 2:
def contar_palabras(cadena: str) -> int:
    palabras = cadena.split()
    numero_de_palabras = len(palabras)
    return numero_de_palabras

# Ejercicio 3
def reemplazar_palabra(cadena: str, antigua_palabra: str, nueva_palabra: str) -> str:
    resultado = ''
    longitud_antigua = len(antigua_palabra)
    i = 0
    
    while i < len(cadena):
        if (cadena[i:i+longitud_antigua] == antigua_palabra and 
            (i + longitud_antigua == len(cadena) or cadena[i+longitud_antigua] in (' ', ','))):
            resultado += nueva_palabra
            i += longitud_antigua
        else:
            resultado += cadena[i]
            i += 1
    return resultado

# Ejercicio 4
def recomendar_peliculas(lista_peli: list) -> str:
    recomendacion = ''
    for peliculas in lista_peli:
        if len(peliculas) == 1:
            recomendacion += f'se recomienda ver "{peliculas[0]}"\n'
        else:
            recomendacion += 'se recomienda ver '
            for i in range(len(peliculas)):
                if i == len(peliculas) - 1:
                    recomendacion += f'y "{peliculas[i]}"'
                else:
                    recomendacion += f'"{peliculas[i]}", '
            recomendacion += '\n'
    
    resultado_final = ''
    for i in range(len(recomendacion)):
        if i == len(recomendacion) - 1 and recomendacion[i] == '\n':
            break
        resultado_final += recomendacion[i]
    
    return resultado_final

# Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.
# Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo:
# Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta
# la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo,
# anilina.
# Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o
# -1). Se debe retornar el string ordenado de manera ascendente (si recibió 1 por
# parámetros) o descendente (si recibió -1)
# Nota: Determinar parámetros y retornos de manera que las funciones sean
# genéricas y reutilizables.