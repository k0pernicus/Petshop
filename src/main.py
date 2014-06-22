#Classe Main
#Auteur: Carette Antonin

from Animals import Animal
from Animals import Hamster
from Animals import Perruche
from Animals import Dog
from Petshop import Petshop
from Player import Player

import sys
import random

#Paramètres généraux
nomJoueur = ""
sexeJoueur = ""
nbrTours = 0
difficulte = ""
choix_animalerie = -1
liste_animaleries = []
liste_cmd = ["aide", "acheter_animal", "acheter_nourriture", "info_animaux", "consulter_compte_banquaire", "contact"]
liste_animaux = ["Hamster", "Perruche", "Chien"]

#Instanciation
liste_animaleries.append(Petshop.Petshop("A Rebrousse Poil", "20", "15", 4500))
liste_animaleries.append(Petshop.Petshop("Pattoune", "15", "15", 3700))
liste_animaleries.append(Petshop.Petshop("Animalia", "15", "18", 3200))
liste_animaleries.append(Petshop.Petshop("Hamsteragram", "12", "20", 2200))

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

def delAll():
	"""Supprime les objets créés"""
	player.__del__
	for animalerie in liste_animaleries:
		animalerie.__del__

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

def printInfoJoueur(player):
	"""Affichage des données du joueur - en début de tour"""
	player.printInfo()

def printInfoAnimalerie():
	global animalerie_choisie
	animalerie_choisie.printInfo()

def printInstructions():
	"""Méthode permettant d'afficher les instructions à l'écran"""
	print("Voici les instructions")
	print("Vous êtes propriétaire d'une animalerie, et désirez que tout aille pour le mieux (logique!). Or, tout n'est pas aussi rose que celà...")
	print("Votre but est donc de survivre un maximum de tours.")
	print("Voici comment va se passer chaque tour de jeu:")
	print("\t --Vous dénombrez les animaux morts du jour (malheureusement... :'(),")
	print("\t --Vous recevez votre inventaire, et devez payer la livraison,")
	print("\t --Vous recevez un nombre indéfini de clients,")
	print("\t --Vous pouvez commander de nouvelles choses pour le lendemain, effectuer des travaux dans votre animalerie, embaucher du personnel, etc...")
	print("\n ATTENTION!")
	print("Vous avez une liste de choses qui pourront vous mettre dans l'embarras (ce ne serai pas marrant sinon!):")
	print("\t --Votre magasin détient des dégâts - cela influe sur la santé des animaux! Plus les dégâts seront forts et moins vos animaux vivront longtemps... De plus, plus ils seront vite malades, ce qui ne pourrai pas plaire au client...")
	print("\t --Votre animal a besoin de nourriture pour vivre! Il faudra donc en acheter régulièrement! Un animal sans nourriture s'affaibliera, et pourra être malade très vite...")
	print("\t --Faites attention à votre argent! Vous en avez besoin pour vivre. Aussi, vous avez droit à un découvert équivalent à votre somme de départ - si vous le dépassez, c'est foutu...")
	print("\t --Des clients pourraient venir vous apporter de petits animaux abandonnés (so cuuute!) - attention à celà! Les prendre pourraient diminuer drastiquement votre stock de nourriture, mais ne pas les prendre pourraient faire que vos clients vous prennent pour un monstre, vous fasse une mauvaise pub et fasse fuir vos employés...")
	print("\t --C'est bien d'avoir un beau magasin, et d'embaucher du personnel! Attention toutefois: plus vous avez d'animaux et plus de dégâts il y aura! Aussi, il se pourrai qu'un événement inattendu vienne vous causer du tord dans un tour (une tempête, une tornade, etc...). De plus, embauche beaucoup de personnel coûte, et ils ne seront pas content si jamais vous les payez tard...")
	print("\n Alors, prêt à jouer? :-) C'est parti!")
	print("\nPour avoir une liste des commandes pouvant être exécutées durant le jeu, tapez aide dans la console!\n")

def printCredits():
	"""Affiche les crédits de fin"""
	print("**FIN DU JEU!!")
	print("Merci d'y avoir jouer!")
	print("Des remarques -> antonin[dot]carette[at]gmail[dot]com")

	#CMD

def print_aide():
	"""Fonction permettant d'afficher une liste exhaustive des commandes accessibles dans le terminal"""
	print("\n")
	print('Liste des commandes:')
	print('\taide:', 'affiche la liste des commandes du programme')
	print('\tcontact:', 'affiche les informations concernant l\'auteur du jeu, et comment le contacter')
	print('\tinfo_animaux:', 'affiche les informations concernant la liste des animaux achetés')
	print('\tinfo_banquaire:', 'affiche les informtions banquaires du joueur')
	print('\tacheter_animal:', 'permet d\'acheter un animal')
	print('\tacheter_nourriture:', 'permet d\'acheter de la nourriture')
	print("\n")

def print_info_animaux():
	"""Fonction permettant d'afficher une liste exhaustive des animaux et de leurs propriétés"""
	global animalerie_choisie
	print("\n")
	animalerie_choisie.getListeAnimaux()
	print("\n")

def print_info_banquaire(player):
	"""Fonction permettant d'afficher une sortie du compte en banque du joueur"""
	print("\n")
	print("Compte en banque du joueur: ", player.getMontant())
	print("\n")

def print_contact():
	"""Fonction permettant d'afficher les informations du développeur"""
	print("\n")
	print("Développeur principal: Carette Antonin")
	print("Contact: antonin[dot]carette[at]gmail[dot]com")
	print("\n")

def fun_acheter_animal(player):
	"""Fonction permettant d'acheter un animal, pour son animalerie"""
	global liste_animaux
	global animalerie_choisie
	choixAnimal = ""
	print("Veuillez entrer l'espèce animale que vous voulez choisir [Hamster, Perruche, Chien]: ")
	while (choixAnimal not in liste_animaux):
		choixAnimal = sys.stdin.readline().capitalize().strip()
	alea = random.randrange(0,2,1)
	if (alea == 0):
		sexe = "Male"
	else:
		sexe = "Femelle"
	if (choixAnimal ==  "Hamster"):
		animal = Hamster.Hamster(sexe)
	if (choixAnimal == "Perruche"):
		animal = Perruche.Perruche(sexe)
	if (choixAnimal == "Dog"):
		animal = Dog.Dog(sexe)
	player.rmMontant(animal.getPrixAchat())
	animalerie_choisie.addAnimal(animal)
	print("\n")
	print("Vous venez d'acheter", animal.printInfo())
	print("\n")


def fun_acheter_nourriture():
	"""Fonction permettant d'acheter de la nourriture pour un type d'animal, ou plusieurs"""

#MAIN

if __name__ == "__main__":

	##DÉBUT

	#Chargement des variables globales
	global nomJoueur
	global sexeJoueur
	global nbrTours
	global difficulte
	global choix_animalerie
	global liste_cmd

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

	animalerie_choisie.setProprietaire(True, player)

	print("\nLe jeux va pouvoir commencer!")

	##LE JEU COMMENCE

	#Instructions
	printInstructions()

	#Variable contenant la commande principale du jeu à rentrer
	commande = ""

	#Condition de sortie -> Le joueur est endetté, et détient une dette de -(argentDepart)
	while (not player.isTerm(-argentDepart)):

		#Affichage des infos du joueur
		printInfoJoueur(player)

		print("\n")

		#Affichage des infos de l'animalerie
		printInfoAnimalerie()

		#Attente de la commande utilisateur
		print("Commande:",)

		commande = sys.stdin.readline().lower().strip()

		while (commande not in liste_cmd):
			print("Mauvaise commande - veuillez réessayer")
			commande = sys.stdin.readline().lower().strip()

		if (commande == "aide"):
			print_aide()

		if (commande == "info_animaux"):
			print_info_animaux()

		if (commande == "consulter_compte_banquaire"):
			print_info_banquaire(player)

		if (commande == "acheter_animal"):
			fun_acheter_animal(player)

		if (commande == "acheter_nourriture"):
			fun_acheter_nourriture()

		if (commande == "contact"):
			print_contact()

		#Tour de jeu // TODO

		player.setMontant(-10000)

		nbrTours = nbrTours+1;


	##FIN DU JEU##

	print("Vous avez perdu...")

	#Déconstruction des objets créés auparavant
	delAll()

	#Crédits de fin
	printCredits()