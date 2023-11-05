# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:38:50 2023

@author: Pierrick
"""



liste_domaines = ["Artisanat", "Combat au Contact", "Discrétion", "Érudition", "Magience", "Milieu Naturel",
                 "Mystères Demorthèn", "Occultisme", "Perception", "Prière", "Prouesses", "Relation", "Représentation",
                 "Science", "Tir et Lancer", "Voyage"]


#Dictionnaire contenant les métiers. Et sous chaque metier il y a 2 listes, la première
#pour le domaine primaire et la 2ème pour le domaine secondaire
dictionnaire_metiers = {
    "Artisan" : ["Artisanat",["Relation", "Science"]],
    "Barde" : ["Représentation",["Relation","Voyage"]],
    "Chasseur" : ["Milieu Naturel",["Combat au Contact","Tir et Lancer"]],
    "Chevalier" : ["Combat au Contact",["Voyage","Relation"]],
    "Combattant" : ["Combat au Contact",["Tir et Lancer","Prouesses"]],
    "Commerçant" : ["Relation",["Érudition", "Artisanat"]],
    "Demorthèn" : ["Mystères Demorthèn",["Érudition", "Milieu Naturel"]],
    "Érudit" : ["Érudition",["Science", "Occultisme"]],
    "Espion" : ["Perception",["Artisanat", "Combat au Contact", "Discrétion", "Érudition", "Magience", "Milieu Naturel",
                     "Mystères Demorthèn", "Occultisme", "Prière", "Prouesses", "Relation", "Représentation",
                     "Science", "Tir et Lancer", "Voyage"]],
    "Explorateur" : ["Prouesses",["Milieu Naturel", "Voyage"]],
    "Investigateur" : ["Perception",["Artisanat", "Combat au Contact", "Discrétion", "Érudition", "Magience", "Milieu Naturel",
                     "Mystères Demorthèn", "Occultisme", "Prière", "Prouesses", "Relation", "Représentation",
                     "Science", "Tir et Lancer", "Voyage"]],
    "Magientiste" : ["Magience",["Érudition", "Science"]],
    "Malandrin" : ["Discrétion",["Prouesses", "Représentation"]],
    "Médecin" : ["Science",["Érudition", "Relation"]],
    "Occultiste" : ["Occultisme",["Érudition", "Science"]],
    "Paysan" : ["Milieu Naturel",["Artisanat", "Prouesses"]],
    "Religieux du Temple" : ["Prière",["Érudition", "Artisanat", "Relation", "Combat au Contact", "Voyage"]],
    "Varigal" : ["Voyage",["Prouesses", "Milieu Naturel"]],
    }


#Dictionnaires des Traits de Caractères. Séparées en qualité majeure, mineure et défauts majeurs, mineurs
qualite_majeure = {
    "Combativité" : ["combatif","optimiste","dynamique","courageux","pugnace"],
    "Créativité" : ["inventif", "original","débrouillard","drôle","poète"],
    "Empathie" : ["réceptif", "sensible", "intuitif","extraverti"],
    "Raison" : ["réfléchi", "ingénieux", "prudent", "logique", "concentré"],
    "Idéal" : ["droit", "persévérant", "loyal", "incorruptible", "généreux"]             
    }

qualite_mineure = {
    "Combativité" : ["calme","flegmatique","paisible","pondéré"],
    "Créativité" : ["sérieux", "respectueux des traditions ou des règles","discipliné"],
    "Empathie" : ["contrôle de ses émotions", "peu influençable"],
    "Raison" : ["spontané", "téméraire"],
    "Idéal" : ["libre", "indépendant"]             
    }

defaut_majeur = {
    "Combativité" : ["impulsif","outrecuidant","fier","buté", "orgueuilleux", "vaniteux"],
    "Créativité" : ["anticonformiste", "rebelle","indiscipliné","excentrique","menteur"],
    "Empathie" : ["émotif", "influençable","bavard"],
    "Raison" : ["abstraction", "replié","précautionneux","hésitant"],
    "Idéal" : ["rigide", "intolérant", "fanatique", "influençable"]             
    }

defaut_mineur = {
    "Combativité" : ["pessimiste","mou","triste","faible de caractère","peureux","mésestime de soi","lâche"],
    "Créativité" : ["empoté", "esprit étriqué","ascétique" ,"rigide"],
    "Empathie" : ["austère", "insensible" ,"renfermé", "taciturne", "froid" , "individualiste"],
    "Raison" : ["distrait", "imprudent","irréfléchi"],
    "Idéal" : ["capricieux", "inconstant" ,"inconséquent", "immoral","doute", "traître"]  
    }

#Lsite des désordre mentaux

class Frénésie:
    """
    
    """
    
    def __init__(self, voie, niveau_voie):         # class constructor
        """Rocket is initialized"""
        self.voie = "Combativité"
        self.niveau_voie = "majeur"

