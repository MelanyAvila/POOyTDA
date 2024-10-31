from clases.Herencia.Animal import Animal

class Perro(Animal):
    def hacer_sonido(self)-> str:
        sonido = 'guau guau'
        return sonido
