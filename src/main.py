#Classe Main
#Auteur: Carette Antonin

from Animals import Animal
from Animals import Hamster
from Animals import Perruche
from Animals import Dog
from Petshop import Petshop
from Player import Player
from Player import Workman

import sys
import random

#Paramètres généraux
nomJoueur = ""
sexeJoueur = ""
nbrTours = 0
difficulte = ""
choix_animalerie = -1
liste_animaleries = []
liste_cmd = ["aide", "acheter_animal", "acheter_nourriture", "info_animaux", "consulter_compte_banquaire", "embaucher_personnel", "contact"]
liste_animaux = ["Hamster", "Perruche", "Chien"]
achat_animaux = []
achat_nourriture = {"Hamster":0, "Dog":0, "Perruche":0}
personnel_a_embaucher = []

#Instanciation
liste_animaleries.append(Petshop.Petshop("A Rebrousse Poil", "20", "15", 4500))
liste_animaleries.append(Petshop.Petshop("Pattoune", "15", "15", 3700))
liste_animaleries.append(Petshop.Petshop("Animalia", "15", "18", 3200))
liste_animaleries.append(Petshop.Petshop("Hamsteragram", "12", "20", 2200))

personnel_a_embaucher.append(Workman.Workman("Nadine", "42", "Maitre"))
personnel_a_embaucher.append(Workman.Workman("Gérard", "53", "Medium"))
personnel_a_embaucher.append(Workman.Workman("Xavier", "24", "Maitre"))
personnel_a_embaucher.append(Workman.Workman("Laurent", "47", "Expert"))
personnel_a_embaucher.append(Workman.Workman("Lucie", "21", "Novice"))
personnel_a_embaucher.append(Workman.Workman("Lola", "20", "Novice"))
personnel_a_embaucher.append(Workman.Workman("Maxime", "28", "Medium"))
personnel_a_embaucher.append(Workman.Workman("Kyllian", "32", "Expert"))

#Fonctions

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

def transfertCommande(player):
	"""Méthode permettant de transférer les commandes vers le stock de l'animalerie"""
	global animalerie_choisie
	global achat_animaux
	global achat_nourriture
	paiementLivraisonAnimaux(player)
	paiementLivraisonNourriture(player)
	for animal in achat_animaux:
		animalerie_choisie.addAnimal(animal)
		print("Un",animal.getRace(),"vient d'être ajouté à votre stock!")
	reinitAchatAnimaux()
	for animal in achat_nourriture:
		animalerie_choisie.addNourritureParAnimal(animal, achat_nourriture[animal])
		print(achat_nourriture[animal],"unités de nourriture pour",animal,"vient d'être ajouté à votre stock!")
	reinitAchatNourriture()
	print("\n")

def paiementLivraisonAnimaux(player):
	"""Méthode permettant de payer la livraison des animaux à l'animalerie -> Si 10 et plus de 10 animaux, paiement de 20 crédits - sinon, 3 * le nombre d'animaux présents"""
	global achat_animaux
	nbrAnimaux = len(achat_animaux)
	if (nbrAnimaux >= 10):
		montant = 20
	else:
		montant = 3 * nbrAnimaux
	player.rmMontant(montant)
	print(nbrAnimaux,"animal(aux) a(ont) été livré(s) - paiement de", montant,"crédits.")

def paiementLivraisonNourriture(player):
	"""Méthode permettant de payer la livraison de la nourriture à l'animalerie -> Si 6 et plus de 6 crédits de nourriture, paiement de 10 crédits - sinon, 2 * le nombre de crédits de nourriture"""
	global achat_nourriture
	nbrNourriture = 0
	for animal in achat_nourriture:
		nbrNourriture = nbrNourriture + achat_nourriture[animal]
	if (nbrNourriture >= 6):
		montant = 10
	else:
		montant = 2 * nbrNourriture
	player.rmMontant(montant)
	print(nbrNourriture,"crédit(s) de nourriture livré(s) - paiement de", montant,"crédits.")

def reinitAchatAnimaux():
	"""Méthode permettant de réinitialiser la liste des animaux achetés"""
	global achat_animaux
	achat_animaux = []

def diminuer_pts_de_vie(pts):
	"""Méthode permettant de diminuer tous les points de vie des animaux présents dans l'animalerie"""
	global animalerie_choisie
	animalerie_choisie.diminuerPtsDeVie(pts)

def consommationDeNourriture():
	"Méthode permettant aux animaux de l'animalerie de consommer de la nourriture"
	global animalerie_choisie
	animalerie_choisie.consommationDeNourriture()

def reinitAchatNourriture():
	"""Méthode permettant de réinitialiser la liste de nourriture achetée"""
	global achat_nourriture
	for animal in achat_nourriture:
		achat_nourriture[animal] = 0

def delAll():
	"""Supprime les objets créés"""
	player.__del__
	for animalerie in liste_animaleries:
		animalerie.__del__

#Fonctions PRINT

def printBienvenue():
	"""Affichage d'un message de bienvenue"""
	print("\nJOUEUR, BIENVENUE DANS \"PETSHOP\"!!\n")

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
	animalerie_choisie.printInfoTour()

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
	print("\t --Les lois de la nature sont imprévisibles! Un papa + une maman = un enfant! Et ça marche aussi avec les animaux... Reproduction aléatoire, mais une nouvelle bouche de plus à nourrir (soit deux unités par femelle enceinte!)")
	print("\t --Faites attention à votre argent! Vous en avez besoin pour vivre. Aussi, vous avez droit à un découvert équivalent à votre somme de départ - si vous le dépassez, c'est foutu...")
	print("\t --La livraison est de 3 crédits par animal, 2 crédits par crédit nourriture.\n\t1 animal -> 3 crédits | 10 et + -> 20 crédits\n\t1 crédit de nourriture -> 2 crédits | 6 et + -> 10 crédits")
	print("\t --Des clients pourraient venir vous apporter de petits animaux abandonnés (so cuuute!) - attention à celà! Les prendre pourraient diminuer drastiquement votre stock de nourriture, mais ne pas les prendre pourraient faire que vos clients vous prennent pour un monstre, vous fasse une mauvaise pub et fasse fuir vos employés...")
	print("\t --C'est bien d'avoir un beau magasin, et d'embaucher du personnel! Attention toutefois: plus vous avez d'animaux et plus de dégâts il y aura! Aussi, il se pourrai qu'un événement inattendu vienne vous causer du tord dans un tour (une tempête, une tornade, etc...). De plus, embaucher beaucoup de personnel coûte, et ils ne seront pas content si jamais vous les payez tard...")
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

def print_personnel_a_embaucher():
	"""Fonction permettant d'afficher la liste du personnel à embaucher"""
	print("======= DEBUT LISTE PERSONNEL =======")
	print("\n")
	i = 1
	for candidat in personnel_a_embaucher:
		print(i,":")
		candidat.printInfo()
		i = i + 1
		print("\n")
	print("======== FIN LISTE PERSONNEL ========")

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
	global achat_animaux
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
	achat_animaux.append(animal)
	print("\n")
	print("Vous venez d'acheter", animal.printInfo())
	print("\n")


def fun_acheter_nourriture(player):
	"""Fonction permettant d'acheter de la nourriture pour un type d'animal, ou plusieurs
		-> Choisir animal
		-> Choisir combien
		-> 3 unités * le nombre de nourriture par animal
	"""
	global liste_animaux
	global achat_nourriture
	choixAnimal = ""
	nbreNourriture = 0
	print("Veuillez entrer l'espèce animale dont vous voulez acheter de la nourriture [Hamster, Perruche, Chien]: ")
	while (choixAnimal not in liste_animaux):
		choixAnimal = sys.stdin.readline().capitalize().strip()
	print("Veuillez entrer le nombre de kgs de nourriture que vous voulez acheter pour cet animal: ")
	nbreNourriture = int(input())
	achat_nourriture[choixAnimal] = achat_nourriture[choixAnimal] + nbreNourriture
	montantAchat = 3 * nbreNourriture
	player.rmMontant(montantAchat)
	print("\n")
	print("Vous venez d'acheter",nbreNourriture,"unités de nourriture pour",choixAnimal,": ",montantAchat,".")
	print("\n")

def fun_embaucher_personnel(player):
	"""Fonction permettant d'afficher toutes les informations utiles quant au personnel à embaucher"""
	global personnel_a_embaucher
	global animalerie_choisie
	choixPersonnel = 0
	print("Voici les candidats:\n")
	print_personnel_a_embaucher()
	while (choixPersonnel > len(personnel_a_embaucher) or choixPersonnel < 1):
		choixPersonnel = int(input("Veuillez sélectionner la personne à embaucher [0 si nul]:"))
	if (choixPersonnel == 0):
		print("Vous n'avez embauché personne...")
	else:
		choixPersonnel = choixPersonnel - 1
		animalerie_choisie.addEmploye(personnel_a_embaucher[choixPersonnel])
		print("Vous avez embauché",personnel_a_embaucher[choixPersonnel],"!")
		print("\n")
		del(personnel_a_embaucher[choixPersonnel])

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
	while (choix_animalerie > len(liste_animaleries) or choix_animalerie < 1):
		choix_animalerie = int(input("Veuillez choisir une animalerie:"))

	#Le joueur devient propriétaire de l'animalerie qu'il a choisi
	liste_animaleries[choix_animalerie - 1].setProprietaire(True)

	animalerie_choisie = liste_animaleries[choix_animalerie - 1]

	player.rmMontant(animalerie_choisie.getPrix())

	print("\nVous avez choisi l'animalerie", animalerie_choisie.getNom())

	animalerie_choisie.setProprietaire(True, player)

	print("\nLe jeu va pouvoir commencer!")

	##LE JEU COMMENCE

	#Instructions
	printInstructions()

	#Variable contenant la commande principale du jeu à rentrer
	commande = ""

	#Condition de sortie -> Le joueur est endetté, et détient une dette de -(argentDepart)
	while (not player.isTerm(-argentDepart)):

		print("Tour n°:", nbrTours)

		#Diminution des points de vie de chaque animal
		diminuer_pts_de_vie(int(animalerie_choisie.getDegats()) / 10)

		#Affichage des infos du joueur
		printInfoJoueur(player)

		print("\n")

		#Affichage des infos de l'animalerie
		printInfoAnimalerie()

		print("\n")

		#Arrivée des commandes et transfert sur le stock de l'animalerie
		if (nbrTours != 0):
			transfertCommande(player)

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
			fun_acheter_nourriture(player)

		if (commande == "contact"):
			print_contact()

		if (commande == "embaucher_personnel"):
			fun_embaucher_personnel()

		consommationDeNourriture()

		nbrTours = nbrTours+1;

	##FIN DU JEU##

	print("Vous avez perdu...")

	#Déconstruction des objets créés auparavant
	delAll()

	#Crédits de fin
	printCredits()