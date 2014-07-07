#Classe Person
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet Person - représentant un personnage quelconque

class Person(object):
	"""Classe permettant d'instancier un objet Person - représentant un personnage"""

	def __init__(self, nom, sexe, argent = 0):
		"""Constructeur d'un objet Person, représentant un personnage quelconque"""
		self._nom = nom
		self._sexe = sexe
		self._argent = argent

	def __del__(self):
		"""Destructeur d'un objet Person"""
		print(self.getNom()," a quitté l'animalerie...")

	def getNom(self):
		"""Méthode permettant de retourner le nom de l'objet auquel la méthode est instanciée"""
		return self._nom

	def getSexe(self):
		"""Méthode permettant de retourner le sexe de l'objet auquel la méthode est instanciée"""
		return self._sexe

	def getMontant(self):
		"""Méthode permettant de retourner l'argent à dépenser pour l'animalerie, pour le personnage sur lequel on instancie la méthode"""
		return self._argent

	def setMontant(self, argent):
		"""Méthode permettant de définir un montant d'argent pour le personnage sur lequel on instancie la méthode"""
		self._argent = argent

	def rmMontant(self, argent):
		"""Méthode permettant d'enlever un montant de la somme totale de l'objet Person"""
		self._argent = self._argent - argent

	def incrMontant(self, argent):
		"""Méthode permettant d'ajouter un montant à la somme de l'objet Person"""
		self._argent = self._argent + argent

