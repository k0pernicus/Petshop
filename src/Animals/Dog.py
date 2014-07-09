#Classe Dog
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet représentant l'animal "Chien"

from Animals import Animal

class Dog(Animal.Animal):
	"""Classe permettant d'instancier un objet Dog, représentation l'animal \"Chien\""""

	def __init__(self, sexe):
		"""Constructeur d'un objet Dog"""
		Animal.Animal.__init__(self, "Chien", 50, sexe, 25, 100, 500)

	def __del__(self):
		"""Destructeur d'un objet Dog"""
		Animal.Animal.__del__(self)
