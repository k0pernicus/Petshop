#Classe Hamster
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet représentant l'animal "Hamster"

from Animals import Animal

class Hamster(Animal.Animal):
    """Classe permettant d'instancier un objet représentation l'animal 'Hamster'"""

    def __init__(self, sexe):
    	"""Constructeur d'un objet Hamster"""
    	Animal.Animal.__init__(self, "Hamster", 30, sexe, 15, 5, 10)

    def __del__(self):
    	"""Destructeur d'un objet Hamster"""
    	Animal.Animal.__del__(self)
