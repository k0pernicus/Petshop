#Classe Visitor
#Author: Carette Antonin
#Classe permettant d'instancier un objet Visiteur, personnage permettant de visiter l'animalerie, donner son avis sur celle-ci et acheter des animaux

from Person import Person

import random

class Visitor(Person.Person):
	"Classe permettant d'instancier un objet, étant un personnage permettant de visiter l'animalerie, donner son avis sur celle-ci et acheter des animaux"

	def __init__(self):
		"Constructeur de Visitor"
		alea_monnaie = random.randrange(0,100,1)
		Person.Person.__init__(self, "Visiteur", "None", alea_monnaie)

	def __del__(self):
		"Déconstructeur de Visitor"
		Person.Person.__del__(self)
		print("Le visiteur est parti...")
