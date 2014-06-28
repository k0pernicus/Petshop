#Classe Workman
#Auteur: Carette Antonin
#Classe permettant d'instancier un objet Workman, correspondant à un employé

from Player import Player

class Workman(Player.Player):
	"""Constructeur d'un objet Workman"""
	def __init__(self, nom, sexe, qualifications):
		Player.Player.__init__(self, nom, sexe, qualifications)
		self._embauche = False;
		self._content = 10;
		self._qualifications = qualifications
		self._paye = self.calculPaye()
		self._date_embauche = 0

	def __del__(self):
		"""Destructeur d'un objet Workman"""
		Player.Player.__del__(self)

	def getEmbauche(self):
		"""Fonction permettant de savoir si l'employé sur lequel on invoque la méthode est embauché ou non"""
		return self._embauche

	def getContent(self):
		"""Fonction permettant de savoir si l'employé est content de ses conditions de travail ou non"""
		return self._content

	def getQualifications(self):
		"""Fonction permettant de retourner les qualifications de l'employé"""
		return self._qualifications

	def setQualifications(self, qualifications):
		"""Fonction permettant de modifier les qualifications de l'employé"""
		self._qualifications = qualifications

	def setEmbauche(self):
		"""Fonction permettant de modifier le booléen attaché à la propriété 'embauche'"""
		if (self.getEmbauche()):
			self._embauche = False
		else:
			self._embauche = True

	def decrContent(self):
		"""Fonction permettant de décrémenter le degré de satisfaction de l'employé"""
		self._content = self._content - 1

	def incrContent(self):
		"""Fonction permettant d'incrémenter le degré de satisfaction de l'employé"""
		self._content = self._content + 1

	def calculPaye(self):
		"""Fonction permettant de (re)calculer la paye de l'embauché"""
		if (self.getQualifications() == "Novice"):
			return 1200
		if (self.getQualifications() == "Medium"):
			return 1500
		if (self.getQualifications() == "Maitre"):
			return 1800
		if (self.getQualifications() == "Expert"):
			return 2100

	def getPaye(self):
		"""Fonction permettant de retourner la paye de l'embauché"""
		return self._paye

	def setPaye(self):
		"""Fonction permettant de modifier dynamiquement la paye de l'embauché, en fonction de son expérience professionnelle"""
		self._paye = self.calculPaye()

	def getDateEmbauche(self):
		"""Fonction permettant de retourner la date d'embauche de l'employé (le nombre de tour)"""
		return self._date_embauche

	def setDateEmbauche(self, date_embauche):
		"""Fonction permettant de modifier la date d'embauche de l'employé"""
		self._date_embauche = date_embauche

	def printInfo(self):
		"""Surcharge de la fonction printInfo()"""
		print("Nom:", self.getNom())
		print("Sexe:", self.getSexe())
		print("Embauché:", self.getEmbauche())
		print("Degré de satisfaction:", self.getContent())
		print("Qualifications:", self.getQualifications())
		print("Paye:", self.getPaye())