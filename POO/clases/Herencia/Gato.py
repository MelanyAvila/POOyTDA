from clases.Herencia.Animal import Animal

class Gato(Animal):
    def hacer_sonido(self)-> str:
        sonido = 'miauu'
        return sonido
