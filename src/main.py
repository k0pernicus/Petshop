from Animals import Animal
from Petshop import Petshop
from Player import Player

import sys

#Paramètres généraux
nomJoueur = ""
sexeJoueur = ""
difficulte = ""
choix_animalerie = -1
liste_animaleries = []

#Instanciation
liste_animaleries.append(Petshop.Petshop("A Rebrousse Poil", "20", "15", 4500))
liste_animaleries.append(Petshop.Petshop("Pattoune", "15", "15", 3700))
liste_animaleries.append(Petshop.Petshop("Animalia", "15", "18", 3200))
liste_animaleries.append(Petshop.Petshop("Hamstagram", "12", "20", 2200))

#Fonctions

def printBienvenue():
	"""Affichage d'un message de bienvenue"""
	print("\nJOUEUR, BIENVENUE DANS \"PETSHOP\"!!\n")

def sexeJoueurOk(sexe):
	"""Vérification de la bonne entrée du sexe du joueur"""
	return (sexe == "Homme" or sexe == "Femme")

def infoJoueur():
	"""Demande les informations principales du joueur"""
	global nomJoueur
	global sexeJoueur
	nomJoueur = input("Tout d'abord, veuillez choisir un nom: ")
	while (not sexeJoueurOk(sexeJoueur)):
		print("Entrez votre sexe [Homme, Femme]: ",)
		sexeJoueur = sys.stdin.readline().capitalize().strip()

def getArgent():
	"""Choix de la somme d'argent de départ, en fonction de la difficulté"""
	global difficulte
	if (difficulte == "easy"):
		return 10000
	if (difficulte == "medium"):
		return 5000
	if (difficulte == "hard"):
		return 2500

def printAnimaleries():
	"""Affichage des animaleries créés"""
	global liste_animaleries
	print("\n")
	i = 1
	for animalerie in liste_animaleries:
		print(i,":", )
		animalerie.printInfo()
		print("\n")
		i = i + 1

def delAll():
	"""Supprime les objets créés"""
	player.__del__
	for animalerie in liste_animaleries:
		animalerie.__del__

def printCredits():
	"""Affiche les crédits de fin"""
	print("\n")
	print("**FIN DU JEU!!")
	print("Merci d'y avoir jouer!")
	print("Des remarques -> antonin[dot]carette[at]gmail[dot]com")

#MAIN

if __name__ == "__main__":

	##DÉBUT

	#Chargement des variables globales
	global nomJoueur
	global sexeJoueur
	global difficulte
	global choix_animalerie

	#Affichage du message de bienvenue
	printBienvenue()

	#Demande des informations du joueur
	infoJoueur()

	#Choix de la difficulté
	while ((difficulte != "easy") and (difficulte != "medium") and (difficulte != "hard")):
		print("Veuillez entrer le niveau de difficulté du jeu [easy, medium, hard]:")
		difficulte = sys.stdin.readline()
		difficulte = difficulte.strip()

	#Sauvegarde de la somme d'argent initiale
	argentDepart = getArgent()

	#Création du joueur
	player = Player.Player(nomJoueur, sexeJoueur, argentDepart, False)

	#Affichage des animaleries
	printAnimaleries()

	#Choix de la première animalerie
	while (choix_animalerie > len(liste_animaleries) or choix_animalerie < 0):
		choix_animalerie = int(input("Veuillez choisir une animalerie:"))

	#Le joueur devient propriétaire de l'animalerie qu'il a choisi
	liste_animaleries[choix_animalerie - 1].setProprietaire(True)

	animalerie_choisie = liste_animaleries[choix_animalerie - 1]

	print("\nVous avez choisi l'animalerie", animalerie_choisie.getNom())

	##LE JEU COMMENCE

	#Condition de sortie -> Le joueur est endetté, et détient une dette de -(argentDepart)
	while (not player.isTerm(-argentDepart)):

		#Tour de jeu // TODO

		print("Je joues!")

		player.setMontant(-10000)


	##FIN DU JEU##

	print("Le joueur a perdu...")

	#Déconstruction des objets créés auparavant
	delAll()

	#Crédits de fin
	printCredits()