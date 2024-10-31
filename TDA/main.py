from funciones.generales import *

ejecutar = True

lista_alumnos = []
lista_cursos = []

while ejecutar == True:

    print('''\nseleccione una opción:
        1- cargar lista de alumnos.
        2- cargar lista de cursos.
        3- generar set de preceptores por año.
        4- obtener promedio de edad de un curso.
        5- buscar preceptores repetidos en dos años distintos.
        6- buscar preceptores en un solo año.
        7- mostrar alumno más joven y más grande.
        8- salir.\n''')
    
    opcion = input("ingrese la opcion que desea realizar: ")
    
    match opcion:
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            pass
        case '8':
            print('tarea terminada')
            ejecutar = False


