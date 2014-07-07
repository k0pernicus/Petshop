#Classe Visitor
#Author: Carette Antonin
#Classe permettant d'instancier un objet Visiteur, personnage permettant de visiter l'animalerie, donner son avis sur celle-ci et acheter des animaux

class Visitor(object):
	"Classe permettant d'instancier un objet, étant un personnage permettant de visiter l'animalerie, donner son avis sur celle-ci et acheter des animaux"

	def __init__(self):
		"Constructeur de Visitor"

	def __del__(self):
		"Déconstructeur de Visitor"
		print("Le visiteur est parti...")
