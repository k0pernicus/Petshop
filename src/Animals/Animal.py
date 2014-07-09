#Classe Animal
#Auteur: Carette Antonin
#Classe permettant d'instancier un animal

import random

class Animal(object):
    "Classe permettant d'instancier un animal"

    #Constructeur d'un objet Animal
    def __init__(self, race, pts_de_vie, sexe, prixAchat, prixVente):
        """Constructeur d'un animal, caractérisé par:
            -ses points de vie,
            -son sexe
            -son prix"""
        self._race = race
        self._pts_de_vie_max = pts_de_vie
        self._pts_de_vie = pts_de_vie
        self._sexe = sexe
        self._prixVente = prixVente
        self._prixAchat = prixAchat
        self._enceinte = False
        #Chaque animal consomme, par défaut, une unité de nourriture
        self._consommationUnite = 1
        self._tps_gestation = 0

    def __del__(self):
        "Déconstructeur d'un objet Animal"
        return

    def vendu(self):
        "Méthode de vente d'un animal"
        print("Un", self.getRace(),"a été vendu!")
        del self

    def mort(self):
        "Méthode de décès d'un animal"
        print("Un",self.getRace(),"est mort...")
        del self

    def getRace(self):
        "Méthode permettant de retourner la race de l'objet Animal"
        return self._race

    def getPtsDeVieMax(self):
        "Méthode permettant de retourner les points de vie maximum d'un objet Animal"
        return self._pts_de_vie_max

    def getPtsDeVie(self):
        "Méthode permettant de retourner les points de vie d'un objet Animal"
        return self._pts_de_vie

    def setPtsDeVie(self, pts_de_vie):
        "Méthode permettant de modifier les points de vie d'un objet Animal"
        self._pts_de_vie = pts_de_vie

    def addPtsDeVie(self, pts_de_vie):
        "Méthode permettant d'ajouter des points de vie à un objet Animal"
        self._pts_de_vie = self._pts_de_vie + pts_de_vie

    def diminuerPtsDeVie(self, pts):
        "Méthode permettant de diminuer les points de vie d'un objet Animal"
        self._pts_de_vie = self._pts_de_vie - pts

    def isMort(self):
        "Méthode permettant de savoir si l'animal est mort ou non"
        if (self.getPtsDeVie() <= 0):
            return True
        return False

    def getSante(self):
        "Méthode permettant d'obtenir les informations de santé sur un objet Animal"
        if self.getPtsDeVie() < (self.getPtsDeVieMax()/2):
            return "Malade..."
        else:
            return "En pleine forme!"

    def getSexe(self):
        "Méthode permettant de retourner le sexe d'un objet Animal"
        return self._sexe

    def getPrixAchat(self):
        "Méthode permettant de retourner le prix d'achat de l'animal"
        return self._prixAchat

    def setPrixAchat(self, prix):
        "Méthode permettant de modifier le prix d'achat de l'animal"
        self._prix = prixAchat

    def getPrixVente(self):
        "Méthode permettant de retourner le prix de vente de l'animal"
        return self._prixVente

    def setPrixVente(self, prix):
        "Méthode permettant de modifier le prix de vente de l'animal"
        self._prix = prixVente

    def getConsommationUnite(self):
        "Méthode permettant de retourner le nombre d'unités de nourriture consommé par l'animal"
        return self._consommationUnite

    def setConsommationUnite(self, conso):
        "Méthode permettant de modifier le nombre d'unités de nourriture consommé par l'animal"
        self._consommationUnite = conso

    def getEnceinte(self):
        "Méthode permettant de retourner le booléen de fertilité, caractérisant l'objet Animal"
        return self._enceinte

    def setEnceinte(self):
        "Méthode permettant de modifier le booléen de fertilité, caractérisant l'objet Animal - aussi, l'animal consommera 2 fois plus d'unités de nourriture!"
        if self.getSexe() == "Femelle":
            if self.getEnceinte():
                self._enceinte = False
                self.setConsommationUnite(1)
            else:
                self._enceinte = True
                self.setConsommationUnite(2)

    def decTpsGestation(self):
        "Méthode permettant de décrémenter le temps de gestation d'une femelle enceinte"
        if self.getEnceinte():
            if self._tps_gestation > 0:
                self._tps_gestation = self._tps_gestation - 1
            #else: TODO! -> Ajout d'un animal dans l'animalerie
                #setEnceinte()


    def getTpsGestation(self):
        "Méthode permettant de retourner le temps de gestation de l'objet Animal"
        if self.getEnceinte():
            return self._tps_gestation

    def metBas(self, animalerie):
        "Méthode permettant à l'animal de mettre bas - ajout d'un animal dans l'animalerie concernée"
        alea = random.randrange(0,2,1)
        if (alea == 0):
            sexe = "Male"
        else:
            sexe = "Femelle"
        nouveauNe = Animal.Animal(self.getRace(), self.getPtsDeVieMax(), sexe, self.getPrixAchat(), self.getPrixVente())
        animalerie.addAnimal(nouveauNe)
        self.setEnceinte()

    def printInfo(self):
        "Méthode permettant d'afficher toutes les informations déjà données, d'un objet Animal"
        print("Race:", self.getRace(),"; Sexe:", self.getSexe(),"; Santé: ", self.getSante())
