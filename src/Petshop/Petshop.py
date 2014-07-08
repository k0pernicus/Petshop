#Classe Petshop
#Author: Carette Antonin
#Classe permettant d'instancier une animalerie, contenue dans le dossier Petshop

import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Animals import Animal
from Person import Person
from Person import Player

class Petshop(object):
    "Classe permettant d'instancier une animalerie, contenue dans le dossier Petshop"

    #Constructeur de la classe Petshop
    def __init__(self, nom, surface, degats, prix, player = None, proprietaire = False):
        """Constructeur d'une animalerie, caractérisé par:
            -son nom
            -sa surface
            -ses dégâts
            -le joueur (optionnel)
            -si le joueur donné précédemment est propriétaire ou non de l'animalerie (optionnel)
            -son prix"""
        self._nom = nom
        self._surface = surface
        self._degats = degats
        self._prix = prix
        self._player = player
        self._proprietaire = proprietaire
        self._liste_employes = []
        self._liste_animaux = {"Hamster": [], "Dog": [], "Perruche": []}
        self._dict_nourriture = {"Hamster":0, "Dog":0, "Perruche":0}
        self._nbr_visites = 0

    def __del__(self):
        """Déconstructeur d'une animalerie"""
        print("L'animalerie", self.getNom(), "a été détruite...")

    def getNom(self):
        "Méthode permettant de retourner le nom de l'animalerie"
        return self._nom

    def setNom(self, nom):
        "Méthode permettant de modifier le nom de l'animalerie"
        self._nom = nom

    def getSurface(self):
        "Méthode permettant de retourner la surface totale de l'animalerie"
        return self._surface

    def setSurface(self, surface):
        "Méthode permettant de modifier la surface totale de l'animalerie"
        self._surface = surface

    def getDegats(self):
        "Méthode permettant de retourner les dégâts de l'animalerie"
        return self._degats

    def setDegats(self, degats):
        "Méthode permettant de modifier les dégâts de l'animalerie"
        self._degats = degats

    def getPrix(self):
        "Méthode permettant de retourner le prix d'achat/vente de l'animalerie"
        return self._prix

    def setPrix(self, prix):
        "Méthode permettant de modifier le prix d'achat/vente de l'animalerie"
        self._prix = prix

    def getPlayer(self):
        "Méthode permettant de renvoyer le joueur"
        return self._player

    def isProprietaire(self):
        "Méthode permettant de savoir si le joueur principal est propriétaire ou non de l'animalerie"
        if (self.getPlayer() is not None):
            return self.getPlayer().isProprietaire()
        return False

    def setProprietaire(self, booleen, joueur = None):
        "Méthode permettant de modifier le statut 'Proprietaire' du joueur de l'animalerie"
        if (joueur is not None):
            self._player = joueur
        if (self.getPlayer() is not None):
            self.getPlayer().setProprietaire(booleen)
        
    def getListeEmployes(self):
        "Méthode permettant de retourner la liste d'employés (tous de type 'Player')"
        return self._liste_employes

    def addEmploye(self, employe):
        "Méthode permettant d'ajouter dans la liste d'employés de l'animalerie un objet 'Player' donné"
        self._liste_employes.append(employe)

    def rmEmploye(self, employe):
        "Méthode permettant de virer / faire démissionner un employé"
        self._liste_employes.remove(employe)

    def returnListeAnimaux(self):
        "Méthode permettant de retourner la liste des animaux, contenue dans l'objet Petshop"
        return self._liste_animaux

    def getListeAnimaux(self):
        "Méthode permettant d'imprimer la liste des animaux, contenue dans l'objet Petshop"
        if (len(self._liste_animaux) == 0):
            print("Vous n'avez pas d'animaux dans votre animalerie...")
        for animals in self._liste_animaux:
            for animal in self._liste_animaux[animals]:
                animal.printInfo()

    def getNbrAnimaux(self):
        "Méthode permettant de retourner le nombre d'animaux restants"
        nbrAnimaux = 0
        for animals in self._liste_animaux.values():
            for animal in animals:
                nbrAnimaux = nbrAnimaux + 1
        return nbrAnimaux

    def getNbrSpecificAnimal(self, animal):
        "Méthode permettant de retourner le nombre d'animaux restants, pour une race donnée en paramètre"
        return len(self._liste_animaux[animal])

    def addAnimal(self, animal):
        "Méthode permettant d'ajouter à la liste des animaux, un animal (donné en paramètre)"
        self._liste_animaux[animal.getRace()].append(animal)

    def returnAnimal(self, animal):
        "Méthode permettant de retourner le premier élément de l'espèce animale demandée"
        if self.getNbrSpecificAnimal(animal) > 0:
            return self._liste_animaux[animal][0]
        else:
            return "None"

    def delAnimal(self, animal):
        "Méthode permettant de supprimer le premier élément de l'espèce animale demandée dans la liste de l'animalerie - utile si vente d'un animal"
        if self.getNbrSpecificAnimal(animal) > 0:
            premier_animal = self._liste_animaux[animal][0]
            #L'animalerie ne contient plus l'animal...
            self._liste_animaux[animal].remove(premier_animal)
            #On supprime l'animal définitivement du programme
            premier_animal.vendu()
        else:
            print("\nPas assez d'animaux d'espèce", animal,"en vente... Pensez à en racheter! ;-)\n")

    def setListeAnimaux(self, listeDanimaux):
        "Méthode permettant de modifier toute la liste des animaux"
        self._liste_animaux[listeDanimaux[0].getRace()] = listeDanimaux

    def rmAnimalMort(self):
        "Méthode permettant de dénombrer, et de supprimer les animaux morts au cours de la nuit"
        nbrMort = 0
        for animals in self._liste_animaux.values():
            for animal in animals:
                if (animal.isMort()):
                    animals.remove(animal)
                    animal.mort()
                    nbrMort = nbrMort+1
        return nbrMort

    def diminuerPtsDeVie(self, pts):
        "Méthode permettant de diminuer les points de vie de chaque animal, d'un certain nombre de points"
        for animals in self._liste_animaux.values():
            for animal in animals:
                animal.diminuerPtsDeVie(pts)

    def getNourritureParAnimal(self, animal):
        "Méthode permettant de retourner le nombre de nourriture restante pour un animal donné"
        return self._dict_nourriture[animal]

    def addNourritureParAnimal(self, animal, conso = 1):
        "Méthode permettant d'ajouter de la nourriture à un animal"
        self._dict_nourriture[animal] = self._dict_nourriture[animal] + conso;

    def rmNourritureParAnimal(self, animal, conso):
        "Méthode permettant de supprimer de la nourriture à un animal"
        self._dict_nourriture[animal] = self._dict_nourriture[animal] - conso;

    def consommationDeNourriture(self):
        "Méthode permettant aux animaux présents dans l'animalerie de consommer de la nourriture -> Si plus de nourriture, diminution des points de vie!"
        pasContent = False
        for animals in self._liste_animaux.values():
            for animal in animals:
                if self._dict_nourriture[animal.getRace()] > 0:
                    self.rmNourritureParAnimal(animal.getRace(), animal.getConsommationUnite())
                else:
                    animal.diminuerPtsDeVie(1)
                    print("Un animal de type", animal.getRace(), "n'a plus de nourriture...")
                    pasContent = True
        if pasContent:
            for employe in self.getListeEmployes():
                employe.decrContent()
        print("\n")

    def getNbrVisites(self):
        "Méthode permettant de retourner le nombre de visites du magasin"
        return self._nbr_visites

    def addNbrVisites(self, nbr):
        "Méthode permettant d'incrémenter le nombre de visites du magasin"
        self._nbr_visites = self._nbr_visites + nbr

    def printInfo(self):
        "Méthode permettant d'afficher toutes les informations déjà données, sur un objet Petshop"
        print("Nom de l'animalerie:",self.getNom())
        if (self.isProprietaire()):
            print("Vous êtes propriétaire de l'animalerie")
        else:
            print("Vous n'êtes pas propriétaire de l'animalerie")
        print("Surface de l'animalerie:",self.getSurface())
        print("Dégâts occasionnés à l'animalerie:", self.getDegats())
        if (self.isProprietaire()):
            print("Prix de vente de l'animalerie:",self.getPrix())
        else:
            print("Prix d'achat de l'animalerie:",self.getPrix())
        print("Nombre d'employés y travaillant:", len(self.getListeEmployes()))

    def printInfoTour(self):
        "Méthode permettant d'afficher les informations concernant l'animalerie, au début d'un tour"
        print("Nom de l'animalerie:", self.getNom())
        print("Dégâts occasionnés à l'animalerie:", self.getDegats())
        print("Nombre d'animaux morts par nuit:", self.rmAnimalMort())
        print("Nombre d'animaux restants:", self.getNbrAnimaux())
        print("Nombre d'employés y travaillant:", len(self.getListeEmployes()))
