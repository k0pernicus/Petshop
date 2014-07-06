#Classe Perruche
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet représentant l'animal "Perruche"

from Animals import Animal

class Perruche(Animal.Animal):
    """Classe permettant d'instancier un objet représentation l'animal 'Perruche'"""

    def __init__(self, sexe):
    	"""Constructeur d'un objet Perruche"""
    	Animal.Animal.__init__(self, "Perruche", 20, sexe, 2, 10)

    def __del__(self):
    	"""Destructeur d'un objet Perruche"""
    	Animal.Animal.__del__(self)
