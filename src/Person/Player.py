#Classe Player
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet Player, joueur principal du jeu "PetShop"

from Person import Person

class Player(Person.Person):
	"Classe permettant d'instancier un objet Player, joueur principal du jeu \"PetShop\""

	def __init__(self, nom, sexe, argent = 0, proprietaire = False):
		"""Constructeur d'un objet Player, caractérisé par:
			- son nom
			- son sexe
			- s'il est propriétaire ou non (de la boutique avec laquelle le personnage est associé)
			- l'argent qu'il a à dépenser pour l'animalerie, s'il est propriétaire"""
		Person.Person.__init__(self, nom, sexe, argent)
		self._proprietaire = proprietaire
		self._endette = False

	def __del__(self):
		"""Destructeur d'un objet Player"""
		Person.Person.__del__(self)

	def isProprietaire(self):
		"""Méthode permettant de savoir si le personnage, auquel la méthode est instanciée, est bien propriétaire ou non de l'animalerie à laquelle il est associé"""
		return self._proprietaire

	def setProprietaire(self, status):
		"""Méthode permettant de définir si le personnage sur lequel on instancie la méthode est propriétaire ou non de l'animalerie"""
		self._proprietaire = status

	def isEndette(self):
		"""Méthode permettant de savoir si le personnage est endetté ou non"""
		return self._endette

	def setEndette(self, booleen):
		"""Méthode permettant de modifier le status 'endette' du joueur"""
		self._endette = booleen

	def isTerm(self, argent):
		"""Méthode permettant de clore le jeu"""
		if (self.isEndette):
			if (self.getMontant() <= argent):
				return True
		return False

	def printInfo(self):
		"""Méthode permettant d'afficher toutes les informations nécessaires sur le joueur"""
		print("Joueur: ", self.getNom())
		print("Propriétaire:", self.isProprietaire())
		print("Argent restant:", self.getMontant())
		print("Endetté:", self.isEndette())