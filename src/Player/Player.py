#Classe Player
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet Player, joueur principal du jeu "PetShop"

class Player(object):
	"Classe permettant d'instancier un objet Player, joueur principal du jeu \"PetShop\""

	def __init__(self, nom, sexe, argent = 0, proprietaire = False):
		"""Constructeur d'un objet Player, caractérisé par:
			- son nom
			- son sexe
			- s'il est propriétaire ou non (de la boutique avec laquelle le personnage est associé)
			- l'argent qu'il a à dépenser pour l'animalerie, s'il est propriétaire"""
		self._nom = nom
		self._sexe = sexe
		self._proprietaire = proprietaire
		self._argent = argent
		self._endette = False

	def __del__(self):
		"""Destructeur d'un objet Player"""
		print(self.getNom()," a quitté l'animalerie...")

	def getNom(self):
		"""Méthode permettant de retourner le nom de l'objet auquel la méthode est instanciée"""
		return self._nom

	def getSexe(self):
		"""Méthode permettant de retourner le sexe de l'objet auquel la méthode est instanciée"""
		return self._sexe

	def isProprietaire(self):
		"""Méthode permettant de savoir si le personnage, auquel la méthode est instanciée, est bien propriétaire ou non de l'animalerie à laquelle il est associé"""
		return self._proprietaire

	def setProprietaire(self, status):
		"""Méthode permettant de définir si le personnage sur lequel on instancie la méthode est propriétaire ou non de l'animalerie"""
		self._proprietaire = status

	def getMontant(self):
		"""Méthode permettant de retourner l'argent à dépenser pour l'animalerie, pour le personnage sur lequel on instancie la méthode"""
		return self._argent

	def setMontant(self, argent):
		"""Méthode permettant de définir un montant d'argent pour le personnage sur lequel on instancie la méthode"""
		self._argent = argent

	def rmMontant(self, argent):
		"""Méthode permettant d'enlever un montant de la somme totale du joueur"""
		self._argent = self._argent - argent

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