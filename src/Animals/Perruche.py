#Classe Perruche
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet représentant l'animal "Perruche"

from Animal import *

class Perruche(Animal):
    """Classe permettant d'instancier un objet représentation l'animal 'Perruche'"""

    def __init__(self, pts_de_vie, sexe):
    	"""Constructeur d'un objet Hamster"""
        Animal.__init__(self, "Perruche", pts_de_vie, sexe)

    def __del__(self):
    	"""Destructeur d'un objet Perruche"""
    	Animal.__del__(self)
