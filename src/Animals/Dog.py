#Classe Dog
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet représentant l'animal "Chien"

from Animals import *

class Dog(Animal):
	"""Classe permettant d'instancier un objet Dog, représentation l'animal \"Chien\""""

	def __init__(self, pts_de_vie, sexe):
		"""Constructeur d'un objet Dog"""
		Animal.__init__(self, "Dog", pts_de_vie, sexe)

	def __del__(self):
		"""Destructeur d'un objet Dog"""
		Animal.__del__(self)
