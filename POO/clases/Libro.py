# 1 -Clase para representar un Libro
# Crear una clase Libro que tenga las características título, autor y año de publicación. Del
# libro se debe poder obtener información, mostrando por mensaje todos sus datos. Se debe
# crear la clase e implementarla.

class Libro:   
    def __init__(self, titulo: str, autor: str, anio_publicacion: int) -> None:

        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    
    def obtener_informacion(self):
        mensaje = f'Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.anio_publicacion}'

        return mensaje
