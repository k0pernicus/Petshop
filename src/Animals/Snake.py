#Classe Snake
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet représentant l'animal "Serpent"

from Animals import Animal

class Snake(Animal.Animal):
	"""Classe permettant d'instancier un objet Snake, représentation l'animal \"Serpent\""""

	def __init__(self, sexe):
		"""Constructeur d'un objet Snake"""
		Animal.Animal.__init__(self, "Serpent", 70, sexe, 17, 150, 300)

	def __del__(self):
		"""Destructeur d'un objet Snake"""
		Animal.Animal.__del__(self)
