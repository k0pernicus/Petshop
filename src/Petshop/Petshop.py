#Classe Petshop
#Author: Carette Antonin
#Classe permettant d'instancier une animalerie, contenue dans le dossier Petshop

import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Animals import Animal
from Player import Player

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

    def setProprietaire(self, booleen, proprietaire = None):
        "Méthode permettant de modifier le statut 'Proprietaire' du joueur de l'animalerie"
        if (self.getPlayer() is not None):
            self.getPlayer().setProprietaire(booleen)
        
    def getListeEmployes(self):
        "Méthode permettant de retourner la liste d'employés (tous de type 'Player')"
        return self._liste_employes

    def addEmploye(self, employe):
        "Méthode permettant d'ajouter dans la liste d'employés de l'animalerie un objet 'Player' donné"
        self._liste_employes.append(employe)

    def getListeAnimaux(self):
        "Méthode permettant de retourner la liste des animaux, contenue dans l'objet Petshop"
        for animals in self._liste_animaux:
            for animal in self._liste_animaux[animals]:
                animal.printInfo()

    def addAnimal(self, animal):
        "Méthode permettant d'ajouter à la liste des animaux, un animal (donné en paramètre)"
        self._liste_animaux[animal.getRace()].append(animal)

    def setListeAnimaux(self, listeDanimaux):
        "Méthode permettant de modifier toute la liste des animaux"
        self._liste_animaux[listeDanimaux[0].getRace()] = listeDanimaux

    def getNourritureParAnimal(self, animal):
        "Méthode permettant de retourner le nombre de nourriture restante pour un animal donné"
        return self._dict_nourriture[animal]

    def addNourritureParAnimal(self, animal):
        "Méthode permettant d'ajouter de la nourriture à un animal"
        self._dict_nourriture[animal] = self._dict_nourriture[animal] + 1;

    def rmNourritureParAnimal(self, animal):
        "Méthode permettant de supprimer de la nourriture à un animal"
        self._dict_nourriture[animal] = self._dict_nourriture[animal] - 1;

    def printInfo(self):
        "Méthode permettant d'afficher toutes les informations déjà données, sur un objet Petshop"
        print("Nom de l'animalerie:",self.getNom())
        if (self.isProprietaire()):
            print("Vous êtes propriétaire de l'animalerie")
        else:
            print("Vous n'êtes pas propriétaire de l'animalerie")
        print("Surface de l'animalerie:",self.getSurface())
        print("Dégâts occasionnée à l'animalerie:", self.getDegats())
        if (self.isProprietaire()):
            print("Prix de vente de l'animalerie:",self.getPrix())
        else:
            print("Prix d'achat de l'animalerie:",self.getPrix())
        print("Nombre d'employés y travaillant:", len(self.getListeEmployes()))
