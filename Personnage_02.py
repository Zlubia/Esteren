# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:48:34 2023

@author: Pierrick
"""

from Donnees_Creation_Perso import *



def print_voies_stats(self) :
    """
    Fonction utilitaire pour imprimer les statistiques des voies

    Returns
    -------
    None

    """
    
    print("Combativité : ", self.voies["Combativité"])
    print("Créativité : ", self.voies["Créativité"])
    print("Empathie : ", self.voies["Empathie"])
    print("Idéal : ", self.voies["Idéal"])
    print("Raison : ", self.voies["Raison"])
    


def print_domaines_stats(self) :
    #Fonction pour imprimer proprement les stats des domaines et disciplines
    
    print("Artisanat : " ,self.artisanat["Artisanat"])
    #on imprime la valeur de base
    
    for key in self.artisanat.keys() :
        #on vérifie s'il y a des disciplines qui ont été développée et on les imprimes.
        #les disciplines qui sont à 0 ne sont pas imprimées
        
        if key != "Artisanat" :
            if self.artisanat[key] > 0 :
                
                print ("   --- ", key , " : " , self.artisanat[key])
                
    #Pareil, print stats combat au contact            
    print("\nCombat au Contact : " , self.combat_au_contact["Combat au Contact"])
    
    for key in self.combat_au_contact.keys() :
        
        
        if key != "Combat au Contact" :
            if self.combat_au_contact[key] > 0 :
                
                print ("   --- ", key , " : " , self.combat_au_contact[key])
                
    #Pareil, print stats Discrétion           
    print("\nDiscrétion : " , self.discretion["Discrétion"])
    
    for key in self.discretion.keys() :
         
        if key != "Discrétion" :
            if self.discretion[key] > 0 :
                 
                print ("   --- ", key , " : " , self.discretion[key])
                
    #Pareil, print stats Erudition           
    print("\nÉrudition : " , self.erudition["Érudition"])
    
    for key in self.erudition.keys() :
         
        if key != "Érudition" :
            if self.erudition[key] > 0 :
                 
                print ("   --- ", key , " : " , self.erudition[key])
                
    #Pareil, print stats Magience           
    print("\nMagience : " , self.magience["Magience"])
    
    for key in self.magience.keys() :
         
        if key != "Magience" :
            if self.magience[key] > 0 :
                 
                print ("   --- ", key , " : " , self.magience[key])
                
    #Pareil, print stats Milieu Naturel           
    print("\nMilieu Naturel : " , self.milieu_naturel["Milieu Naturel"])
    
    for key in self.milieu_naturel.keys() :
         
        if key != "Milieu Naturel" :
            if self.milieu_naturel[key] > 0 :
                 
                print ("   --- ", key , " : " , self.milieu_naturel[key])
                
    #Pareil, print stats Mystères Demorthen           
    print("\nMystères Demorthèn : " , self.mysteres_demorthen["Mystères Demorthèn"])
    
    for key in self.mysteres_demorthen.keys() :
         
        if key != "Mystères Demorthèn" :
            if self.mysteres_demorthen[key] > 0 :
                 
                print ("   --- ", key , " : " , self.mysteres_demorthen[key])
                
    #Pareil, print stats Occultisme     
    print("\nOccultisme : " , self.occultisme["Occultisme"])
    
    for key in self.occultisme.keys() :
         
        if key != "Occultisme" :
            if self.occultisme[key] > 0 :
                 
                print ("   --- ", key , " : " , self.occultisme[key])
                
    #Pareil, print stats Perception     
    print("\nPerception : " , self.perception["Perception"])
    
    for key in self.perception.keys() :
         
        if key != "Perception" :
            if self.perception[key] > 0 :
                 
                print ("   --- ", key , " : " , self.perception[key])
                
    #Pareil, print stats Prière     
    print("\nPrière : " , self.priere["Prière"])
    
    for key in self.priere.keys() :
         
        if key != "Prière" :
            if self.priere[key] > 0 :
                 
                print ("   --- ", key , " : " , self.priere[key])
                
    #Pareil, print stats Prouesses
    print("\nProuesses : " , self.prouesses["Prouesses"])
    
    for key in self.prouesses.keys() :
         
        if key != "Prouesses" :
            if self.prouesses[key] > 0 :
                 
                print ("   --- ", key , " : " , self.prouesses[key]) 
                
    #Pareil, print stats Relation
    print("\nRelation : " , self.relation["Relation"])
    
    for key in self.relation.keys() :
         
        if key != "Relation" :
            if self.relation[key] > 0 :
                 
                print ("   --- ", key , " : " , self.relation[key]) 
                
    #Pareil, print stats Représentation
    print("\nReprésentation : " , self.representation["Représentation"])
    
    for key in self.representation.keys() :
         
        if key != "Représentation" :
            if self.representation[key] > 0 :
                 
                print ("   --- ", key , " : " , self.representation[key]) 
                
    #Pareil, print stats Science
    print("\nScience : " , self.science["Science"])
    
    for key in self.science.keys() :
         
        if key != "Science" :
            if self.science[key] > 0 :
                 
                print ("   --- ", key , " : " , self.science[key]) 
                
    #Pareil, print stats Tir et Lancer
    print("\nTir et Lancer : " , self.tir_et_lancer["Tir et Lancer"])
    
    for key in self.tir_et_lancer.keys() :
         
        if key != "Tir et Lancer" :
            if self.tir_et_lancer[key] > 0 :
                 
                print ("   --- ", key , " : " , self.tir_et_lancer[key]) 
                
    #Pareil, print stats Voyage
    print("\nVoyage : " , self.voyage["Voyage"])
    
    for key in self.voyage.keys() :
         
        if key != "Voyage" :
            if self.voyage[key] > 0 :
                 
                print ("   --- ", key , " : " , self.voyage[key]) 
        


def domaine(self, domaine):
    #Fonction qui sert à convertir les strings obtenues dans les inputs en variables de la classe
    
    if domaine == "Artisanat" : return self.artisanat
    elif domaine == "Combat au Contact": return self.combat_au_contact
    elif domaine == "Discrétion" : return self.discretion
    elif domaine ==  "Érudition" : return self.erudition
    elif domaine == "Magience" : return self.magience
    elif domaine == "Milieu Naturel" : return self.milieu_naturel
    elif domaine == "Mystères Demorthèn": return self.mysteres_demorthen
    elif domaine == "Occultisme" : return self.occultisme
    elif domaine == "Perception" : return self.perception
    elif domaine == "Prière" : return self.priere
    elif domaine == "Prouesses" : return self.prouesses
    elif domaine == "Relation" : return self.relation
    elif domaine == "Représentation" : return self.representation
    elif domaine == "Science" : return self.science
    elif domaine == "Tir et Lancer" : return self.tir_et_lancer
    elif domaine == "Voyage" : return self.voyage


def choix_domaine(domaines_dispo):
    """
    Fonction utilitaire pour l'input du choix d'un domaine

    Parameters
    ----------
    domaines_dispo : 
        TYPE : List 
        DESCRIPTION : Liste des domaines parmis lesquels le joueur peut choisir

    Returns
    -------
    domaines_dispo (mis à jour sans le domaine sélectionné)
    domaine_choisi (le domaine sélectionné par le joueur)

    """
    
    for element in domaines_dispo :
        print(element)
        #afficher les domaines parmis lesquels le joueur peut choisir.
    
    #Variable de condition de sortie de boucle :
    choix = False
    
    while choix == False :
        
        domaine_choisi = input("Quel domaine choisissez-vous ? : ")
        
        #vérification de l'input
        for element in domaines_dispo :
            if domaine_choisi == element :
                choix = True
                domaines_dispo.remove(element)
                print("Vous avez choisi le domaine : ",domaine_choisi)
                
        if choix == False :
            print("Erreur, choissisez un autre domaine")
    
    return domaines_dispo, domaine_choisi


def choix_voies(self, niveau) :
    """
    Fonction utilitaire pour l'input du choix d'une voie

    Parameters
    ----------
    niveau : TYPE : Integer
        DESCRIPTION : La valeur à ajouter à la voie

    Returns
    -------
    la liste de voies ajustée.

    """
    #variable de sortie de boucle
    choix = False
    
    while choix == False :
        
        print("\nDans quelle voie souhaitez vous attribuer", niveau, "points ?")
        
        voie = input("")
        
        if voie == "Combativité" or voie == "combativité" :
            if self.voies["Combativité"] == 0 :
                choix = True
                self.voies["Combativité"] = niveau
                print("\nVotre niveau de Combativité est à : ", niveau)
            else :
                print("Erreur, veuillez choisir une autre voie")
            
        elif voie == "Créativité" or voie == "créativité" :
            if self.voies["Créativité"] == 0 :
                choix = True
                self.voies["Créativité"] = niveau
                print("\nVotre niveau de Créativité est à : ", niveau)
            else :
                print("Erreur, veuillez choisir une autre voie")
            
        elif voie == "Empathie" or voie == "empathie" :
            if self.voies["Empathie"] == 0 :
                choix = True
                self.voies["Empathie"] = niveau
                print("\nVotre niveau d'Empathie est à : ", niveau)
            else :
                print("Erreur, veuillez choisir une autre voie")
            
        elif voie == "Raison" or voie == "raison" :
            if self.voies["Raison"] == 0 :
                choix = True
                self.voies["Raison"] = niveau
                print("\nVotre niveau de Raison est à : ", niveau)
            else :
                print("Erreur, veuillez choisir une autre voie")
        
        elif voie == "Idéal" or voie == "idéal" :
            if self.voies["Idéal"] == 0 :
                choix = True
                self.voies["Idéal"] = niveau
                print("\nVotre niveau d'Idéal est à : ", niveau)
            else :
                print("Erreur, veuillez choisir une autre voie")
            
        else :
            print("Erreur, veuillez choisir une voie")
    
    return self.voies
    
    
    
    

class Player:
    """contains everything about a player:
    - nom
    - peuple
    - metier
    -...
    """
    def __init__(self):         # class constructor
       self.name = ""
       self.joueur = ""
       self.sexe = ""
       self.age = 0
       self.peuple = ""
       self.metier = ""
       self.vigueur = 10
       self.voies = {"Combativité" : 0 ,
                     "Empathie" : 0,
                     "Créativité" : 0,
                     "Raison" : 0,
                     "Idéal" : 0}
       self.avantages = []
       self.desavantages = []     
       
       self.artisanat = {"Artisanat" : 0,
                         "Bijouterie" : 0,
                         "Confection" : 0,
                         "Cuisine" : 0,
                         "Distillation" : 0,
                         "Extraction minière" : 0,
                         "Forge" : 0,
                         "Machinerie magientiste" : 0,
                         "Maroquinerie" : 0,
                         "Menuiserie" : 0,
                         "Outil magientiste" : 0,
                         "Peinture" : 0,
                         "Poterie" : 0,
                         "Sculpture" : 0,
                         "Serrurrerie" : 0
                         }
       
       self.combat_au_contact = {"Combat au Contact" : 0,
                                 "Artefact de combat" : 0,
                                 "Armes contondantes" : 0,
                                 "Armes d'hast" : 0,
                                 "Combat à mains nues" : 0,
                                 "Combat aveugle" : 0,
                                 "Épées" : 0,
                                 "Haches" : 0,
                                 "Lames courtes" : 0
                                 }
       
       self.discretion = {"Discrétion" : 0,
                          "Camouflage" : 0,
                          "Furtivité" : 0,
                          "Mimétisme" : 0,
                          "Vol à la tire" : 0
                          }
       
       self.erudition = {"Érudition" : 0,
                        "Astronomie" : 0,
                        "Doctrine du temple" : 0,
                        "Géographie" : 0,
                        "Héraldique" : 0,
                        "Herboristerie" : 0,
                        "Histoire" : 0,
                        "Langues" : 0,
                        "Politique" : 0,
                        "Principes magientistes" : 0,
                        "Traditions demorthèn" : 0
                        }
       
       self.magience = {"Magience" : 0,
                        "Connaissance des flux" : 0,
                        "Extraction de flux" : 0,
                        "Raffinage de flux" : 0,
                        "Réparation d'artefacts" : 0,
                        "Utilisation des artefacts" : 0,
                        "Médecine" : 0
                        }
       
       self.milieu_naturel = {"Milieu Naturel" : 0,
                              "Agriculture" : 0,
                              "Dressage d'animaux" : 0,
                              "Faune et flore" : 0,
                              "Herboristerie" : 0,
                              "Orientation" : 0,
                              "Pistage" : 0,
                              "Premiers soins" : 0,
                              "Survie" : 0
                              }
       
       self.mysteres_demorthen = {"Mystères Demorthèn" : 0,
                                  "Herboristerie" : 0,
                                  "Savoirs demorthèn" : 0,
                                  "Concentration" : 0,
                                  "Méditation" : 0,
                                  "Langue ancienne" : 0,
                                  "Médecine traditionnelle" : 0,
                                  "Sigil Rann" : 0,
                                  "Spiritualité" : 0
                                  }
       
       self.occultisme = {"Occultisme" : 0,
                          "Artefact de combat" : 0,
                          "Ésotérisme" : 0,
                          "Hypnose" : 0,
                          "Interprétation des rêves" : 0,
                          "Outil magientiste" : 0,
                          "Phénomènes mentaux" : 0
                          }
       
       self.perception = {"Perception" : 0,
                          "Évaluation" : 0,
                          "Observation" : 0,
                          "Orientation" : 0,
                          "Lecture sur les lèvres" : 0,
                          "Sens aiguisés" : 0,
                          "Vigilance" : 0
                          }
       
       self.priere = {"Prière" : 0,
                      "Connaissance du temple" : 0,
                      "Concentration" : 0,
                      "Miracles" : 0,
                      "Recueillement" : 0,
                      "Spiritualité" : 0
                      }
       
       self.prouesses = {"Prouesses" : 0,
                         "Accrobaties" : 0,
                         "Course" : 0,
                         "Endurance" : 0,
                         "Escalade" : 0,
                         "Évasion" : 0,
                         "Natation" : 0
                         }
       
       self.relation = {"Relation" : 0,
                        "Baratin" : 0,
                        "Charme" : 0,
                        "Commandement" : 0,
                        "Connaissance d'une faction" : 0,
                        "Diplomatie" : 0,
                        "Étiquette" : 0,
                        "Intimidation" : 0,
                        "Persuasion" : 0
                        }
       
       self.representation = {"Représentation" : 0,
                              "Chant" : 0,
                              "Comédie" : 0,
                              "Danse" : 0,
                              "Jeux" : 0,
                              "Instrument de musique" : 0,
                              "Jonglage" : 0,
                              "Ventriloquie" : 0
                              }
       
       self.science = {"Science" : 0,
                       "Architecture" : 0,
                       "Artefact de combat" : 0,
                       "Botanique" : 0,
                       "Connaissance des troubles mentaux" : 0,
                       "Géologie" : 0,
                       "Ingénierie" : 0,
                       "Mécanique" : 0,
                       "Machinerie magientiste" : 0,
                       "Médecine" : 0,
                       "Outil magientiste" : 0,
                       "Réparation d'artefacts" : 0,
                       "Traitement de l'esprit" : 0
                       }
       
       self.tir_et_lancer = {"Tir et Lancer" : 0,
                             "Arbalètes" : 0,
                             "Arcs" : 0,
                             "Armes de jet" : 0,
                             "Artefact de combat" : 0,
                             }
       
       self.voyage = {"Voyage" : 0,
                      "Attelage" : 0,
                      "Cartographie" : 0,
                      "Chemin de traverse" : 0,
                      "Signes" : 0,
                      "Équitation" : 0,
                      "Navigation" : 0,
                      "Orientation" : 0
                      }
       
       self.conscience = 0
       self.instinct = 0
       self.orientation = ""
       self.trauma = (0, 0) #(Points de Trauma Permanents , Points de Trauma Temporaires)
       self.endurcissement = 0
       self.resistance_mentale = 0
                         
    
    
    def modifier_discipline (self, nom_domaine, quantite) : 
        
        i = 0
        #initialisation compteur de boucle
        
        while i < quantite :
            #on boucle tant qu'on a pas amélioré de la quantité requise
            
            """
            Boucle for qui sert à récupérer la première clef du dictionnaire, celle qui contient le nom de domaine 
            On interromp la boucle immédiatement après.
            """
            for clef in nom_domaine.keys() :
                Stats_de_base = clef
                break
    
            if nom_domaine[Stats_de_base] < 5 :
                #si le domaine n'est pas au niveau 5, on augmente le domaine de 1
                
                nom_domaine[Stats_de_base] += 1
                i += 1
                
            elif nom_domaine[Stats_de_base] == 5 :
                #si le domaine est au niveau 5 on lance la boucle de choix de discipline
                
                
                print("\nVotre domaine", Stats_de_base, "est à 5, vous pouvez améliorer une discipline ou en choisir une  nouvelle")
                
                print("\nVoici les disciplines possibles ainsi que leur niveau :")
                
                #ci-dessous, boucle pour imprimer les différentes disciplines disponibles dans ce domaine
                for key, value in nom_domaine.items() :   
                    if key != Stats_de_base :
                        print( key, " : " , value)
                
                
                selection_discipline = False
                #initialisation de la variable de fin de boucle
                
                while selection_discipline == False :
                #Boucle de selection de la discipline, on boucle tant que l'input n'est pas valable.
                    print(" ")
                    nom_discipline  = input("Choississez une discipline à améliorer :")
                    
                    
                    for key in nom_domaine.keys() :
                    #on parcours les différentes disciplines pour vérifier que la réponse à l'input correspond à l'une des options     
                        
                        if nom_discipline == key :
                            #si ça correspond, on sort de la boucle.
                            selection_discipline = True
                            break
                
                #ensuite on augmente la discipline de 1    
                nom_domaine[nom_discipline] += 1
                
                #et on passe à la boucle suivante s'il reste des points à attribuer
                i += 1
        
                
        return nom_domaine
         
        
        
       
    def creation(self):
        
        print("\n\n-----Création de personnage-----")

        """---------------------------------------------- 1 - CHOIX PEUPLE ------------------------------------------------"""

        print("\n1. Choisir votre peuple")

        selection_peuple = False

        while selection_peuple == False :
            print("\nVous avez le choix parmis 4 options")
            
            print("\nTri-Kazel")
            print("Tarish")
            print("Osag")
            print("Continent")
            
            peuple = input("Choississez un peuple: ")
            
            if peuple == "Tri-Kazel" or peuple == "Osag" or peuple == "Tarish" or peuple == "Continent" :
                selection_peuple = True    
            else :        
                print("\nErreur; Veuillez choisir votre peuple :")

        print("Vous avez choisi ", peuple)

        """-------------------------------------- 2 - CHOIX METIER ---------------------------------------------------"""

        print("\n\n2. Choisir votre métier")
        selection_metier = False
        liste_metiers = list(dictionnaire_metiers.keys())

        while selection_metier == False :
           
            print("\nVous avez le choix parmis cette liste de métiers :\n")
            #afficher la liste de métiers
            for element in liste_metiers :
                print(element)
            
            metier = input("\nChoississez un metier: ")
            
            #vérification de l'input
            for element in liste_metiers :
                
                if metier == element:
                    selection_metier = True    
            
            if selection_metier == False :
                print("\nErreur; Veuillez choisir votre métier :")

        print("\nVous avez choisi :", metier)

        #domaine primaire
        domaine_primaire = dictionnaire_metiers[metier][0]

        print("Votre domaine primaire est :" , domaine_primaire)

        #domaine secondaires
        selection_domaine_secondaire = False

        while selection_domaine_secondaire == False :
           
            print("\nVous avez le choix parmis cette liste de domaines secondaires :\n")
            
            for element in dictionnaire_metiers[metier][1] :
                print(element)
            
            domaine_secondaire = input("\nChoississez un domaine secondaire: ")
            
            #vérification de l'input
            for element in dictionnaire_metiers[metier][1] :
                
                if domaine_secondaire == element:
                    selection_domaine_secondaire = True    
            
            if selection_domaine_secondaire == False :
                print("\nErreur; Veuillez choisir votre domaine secondaire :")

        print("\nVous avez choisi :", domaine_secondaire)
        
        """        
        On modifie la valeur des domaines du perso en fonction des choix précédents. 
        En utilisant la fonction modifier_disciplines. En paramètre on met la fonction Domaines qui sert à
        convertir le string récupéré des inputs, en nom des dictionnaires.
        On mets également en paramètre le nombre de points attribués au domaine.
        """
        self.modifier_discipline(domaine(self, domaine_primaire), 5)
        self.modifier_discipline(domaine(self, domaine_secondaire), 3)

        
        #Autres occupations : un personnage est également compétent dans d'autres activités au choix
        print("\nVotre personnage est également compétent dans d'autres activités.")
        print("Vous avez droit à 2 domaines au niveau 2 ainsi qu'à 2 domaines au niveau 1.")
        print("\nCommencez par choisir les 2 domaines de compétence qui seront au niveau 2.")
        
        print("\nVous avez le choix parmis ces domaines :")
        
        #creer une liste avec les domaines dispos
        domaines_dispo = []
        
        for element in liste_domaines :
            if element != domaine_primaire and element != domaine_secondaire :
                domaines_dispo.append(element)
        
        #On utilise la fonction choix_domaine, qui récupère la liste des domaines dispos mise à jour
        #ainsi que le domaine choisi par le joueur
        domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)
                
        #On ajoute 2 points au domaine choisi :
        self.modifier_discipline(domaine(self, domaine_choisi), 2)

        
        #selection d'un 2ème domaine niveau 2
        print("\nVous avez le choix parmis ces domaines :")

        domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)
        self.modifier_discipline(domaine(self, domaine_choisi), 2)            


        #sélection des domaines niveau 1
        print("\nChoississez maintenant les 2 domaines de compétence qui seront au niveau 1.")
        
        print("\nVous avez le choix parmis ces domaines :")
        
        #On utilise la fonction choix_domaine, qui récupère la liste des domaines dispos mise à jour
        #ainsi que le domaine choisi par le joueur
        domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)
                
        #On ajoute 1 point au domaine choisi :
        self.modifier_discipline(domaine(self, domaine_choisi), 1)    
        
        #selection d'un 2ème domaine niveau 1
        print("\nVous avez le choix parmis ces domaines :")
        
        domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)
        self.modifier_discipline(domaine(self, domaine_choisi), 1)    
               


        #On imprime les stats après cette étape
        print("\nVoici le niveau de vos domaines pour le moment :")
        print_domaines_stats(self)
        
        
        #------------------ CHOIX LIEU DE NAISSANCE -----------------------
        
        print("\n---------------------------------------------------------")
        print("\nChoisir votre lieu de naissance")
        
        alpha = False
        
        while alpha == False :
        
            lieu_naissance = input("\nVotre personnage, a-t-il grandi dans un lieu rural ou dans une ville ?")
            
            
            if lieu_naissance == "rural" or lieu_naissance == "Rural" :
                #Domaine milieu naturel + 1
                domaine_naissance = self.milieu_naturel
                print("\nVous avez grandi en milieu rural, ceci augmente de 1 point votre domaine de Milieu Naturel")
                
                #sortie boucle
                alpha = True
                
            elif lieu_naissance == "ville" or lieu_naissance == "Ville" :
                #Domaine relation + 1
                domaine_naissance = self.relation
                print("\nVous avez grandi en ville, ceci augmente de 1 point votre domaine de Relation")
                
                #sortie boucle
                alpha = True
                
            else :
                print("Erreur, veuillez choisir dans quel milieu votre personnage a grandi")
              
        #on applique la fonction qui modifie les domaines et disciplines :            
        self.modifier_discipline(domaine_naissance, 1)
        
        print("\nEn Tri-Kazel, un service d'ost d'une année est obligatoire.")
        print("Chaque habitant, homme ou femme, est amené à participer à la défense de la communauté")
        print("et se retrouve initié aux combat.")
        print("\nVous obtenez un bonus de +1 niveau dans le domaine de Combat au Contact")
        
        #on applique la fonction qui modifie les domaines et disciplines :    
        self.modifier_discipline(self.combat_au_contact, 1)
        
        #petit impression des domaines et disciplines ajustées.
        print("\nVoici le niveau de vos domaines pour le moment :")
        print_domaines_stats(self)
        
        #----------------------CHOIX DE LA CLASSE SOCIALE----------------
        
        print("\n---------------------------------------------------------")
        print("\nChoisir votre classe sociale")
        
        choix = False
        
        while choix == False :
            
            classe_sociale = input("\nVotre personnage, appartient-il au Clergé, à la Noblesse ou à la roture ? ")
            
            if classe_sociale == "Clergé" or classe_sociale == "clergé" :
                choix = True
                classe_sociale = "Clergé"
            
            elif classe_sociale == "Noblesse" or classe_sociale == "noblesse" :
                choix = True
                classe_sociale = "Noblesse"
                
            elif classe_sociale == "Roture" or classe_sociale == "roture" :
                choix = True
                classe_sociale == "Roture"
                
            else :
                print("Erreur, veuillez choisir votre classe sociale")
                
        if classe_sociale == "Clergé" :
        
            print("\nLes membres du Temple font partie du clergé.")
            print("Un personnage joueur de cette classe obtient +1 dans deux Domaines")
            
            print("\nVous avez le choix parmis les domaines suivants :")
            
            #créer une liste avec les domaines dispos ()
            domaines_dispo = ["Prière", "Érudition" , "Relation", "Voyage"]
            
            #On utilise la fonction choix_domaine, qui récupère la liste des domaines dispos mise à jour
            #ainsi que le domaine choisi par le joueur
            domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)
                    
            #On ajoute un point au domaine choisi :
            self.modifier_discipline(domaine(self, domaine_choisi), 1)
            
            #et on refait la manip pour le 2ème domaine :
            print("\nChoisissez un deuxième domaine.")
            
            domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)

            self.modifier_discipline(domaine(self, domaine_choisi), 1)
            
            
            
        elif classe_sociale == "Noblesse" :
        
            print("\nLes membres de la Noblesse peuvent être d'origine citadine ou rurale.")
            print("Un personnage joueur de cette classe obtient +1 dans deux Domaines")
            
            print("\nVous avez le choix parmis les domaines suivants :")
            
            #créer une liste avec les domaines dispos ()
            domaines_dispo = ["Combat au Contact", "Érudition" , "Relation", "Science"]
            
            #On utilise la fonction choix_domaine, qui récupère la liste des domaines dispos mise à jour
            #ainsi que le domaine choisi par le joueur
            domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)
                    
            #On ajoute un point au domaine choisi :
            self.modifier_discipline(domaine(self, domaine_choisi), 1)
            
            #et on refait la manip pour le 2ème domaine
            print("\nChoisissez un deuxième domaine.")
            domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)

            self.modifier_discipline(domaine(self, domaine_choisi), 1)
            
       
            #------------------- AJOUTER LA ROTURE - CAS PARTICULIER --------------
        
        elif classe_sociale == "Roture" :
            print("\nLa roture forme l'essentiel de la population.")

        
            choix = False
            
            while choix == False :
                
                print("Etes-vous paysan, rural, demorthèn, artisan, ouvrier ou bourgeois ?")
                print("Pensez au métier que vous avez choisi.")
                roture = input("")
                
                if roture == "paysan" or roture == "Paysan" or roture == "Demorthèn" or roture == "demorthèn"  or roture == "rural" or roture == "Rural" :
                    #créer une liste avec les domaines dispos ()
                    domaines_dispo = ["Milieu Naturel", "Perception" , "Prouesses", "Voyage"]
                    choix = True
                
                elif roture == "Artisan" or roture == "Artisan" or roture == "Ouvrier" or roture == "ouvrier" :
                
                    domaines_dispo = ["Artisanat", "Érudition" , "Science", "Relation"]
                    choix = True
                    
                elif roture == "Bourgeois" or roture == "bourgeois" :
                    
                    domaines_dispo = ["Artisanat", "Érudition" , "Représentation", "Relation"]
                    choix = True
                    
                else :
                    print("Erreur, veuillez choisir votre classe sociale")
                    
                
            #On utilise la fonction choix_domaine, qui récupère la liste des domaines dispos mise à jour
            #ainsi que le domaine choisi par le joueur
            domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)
                    
            #On ajoute un point au domaine choisi :
            self.modifier_discipline(domaine(self, domaine_choisi), 1)
            
            print("\nChoisissez un deuxième domaine.")
            domaines_dispo, domaine_choisi = choix_domaine(domaines_dispo)
            self.modifier_discipline(domaine(self, domaine_choisi), 1)
            
        #Print le résultat des stats jusqu'à présent.
        print("\nVoici le niveau de vos domaines pour le moment :")
        print_domaines_stats(self)
        
            
        """--------------------------------- 3 - LES VOIES -----------------------------------------------------------"""
            
                
        print("\n---------------------------------------------------------")
        print("\nChoisir vos scores de Voies")
        
        print("\nLes 5 Voies sont des caractéristiques mentales qui déterminent les traits majeurs de la personnalité")
        print("du Personnage, sa façon de voir le monde et d'agir.")
        print("\nVous répartissez au sein des cinq Voies les scores de 1,2,3,4 et 5,")
        print("ce qui fait que chacune aura un score différent.")
        print("Les 5 voies possibles sont : ")
        print("\nCombativité")
        print("Créativité")
        print("Empathie")
        print("Raison")
        print("Idéal")
        
        
        #On active la fonction choix_voies pour chaque score.
        choix_voies(self, 5)
        choix_voies(self, 4)
        choix_voies(self, 3)
        choix_voies(self, 2)
        choix_voies(self, 1)
        
        print("\nVoici le niveau de vos Voies :")
        print_voies_stats(self)
        #imprimer les voies proprement.
        
        
        """--------------------------------- 4 - Age, Revers et Histoire -------------------------------------------------"""
            
                
        print("\n---------------------------------------------------------")
        print("\nChoisir votre âge et définir vos Revers.")
        
        print("\nA la création, un Personnage Joueur sera au moins âgé de 16 ans. Cela signifie qu'il a été formé à un métier")
        print("et qu'il a accompli un service d'ost.")
        print("Il ne pourra pas avoir plus de 35 ans, car un âge plus avancé serait peu vraisemblable au regard de")
        print("l'expérience qui lui est octroyée à la création.")
        print("\nPlus un Personnage Joueur sera âgé, plus il aura appris de choses et plus il sera marqué par la dureté")
        print("de la vie péninsulaire, ce qui se traduira par un ou plusieurs Revers qui l'auront affecté.")
        
        """ 
        D'abord coder la suite, les jets sur les tableaux de revers peuvent influencer la vigueur, la santé mentale...'               
        """

                    
        """
        On ajoute un point au domaine choisi.
        Cependant il y a une règle supplémentaire qui à de l'importance à partir d'ici :
        A la création, le nombre de disciplines est limité à 2 et leur niveau limité à 6 (5 de base + 1). De plus, les Disciplines
        seront obligatoirement allouées dans les domaines Primaires et Secondaires définis par le choix du métier.
        Si un PJ dépasse 5 dans un autre domaine, il pourra ajouter les points en trop à un autre Domaine au choix, sans dépasser 5.
        Pareil s'il débloque une discipline de trop, ce point sera réparti ailleurs. Voir page 206
        """
        
        
        """--------------------------------- 5 - Traits de caractère, Santé mentale et Personnalité ----------------------------"""
            
                
        print("\n---------------------------------------------------------")
        print("\nChoisir vos Traits de caractère")
        
        print("\nVous allez choisir 2 traits de caractère, l'un sera une qualité, l'autre un défaut.")
        print("Ils sont choisis dans une liste qui est déterminée selon les scores de Voies choisis précédemment.")
        
        print("\nListe des Qualités disponibles :")
        
        if self.voies["Combativité"] == 5 or self.voies["Combativité"] == 4 :
            #Afficher les valeurs majeurs de combativité
            print("\nScore Majeur en Combativité : ")
            print(" ")
            for i in qualite_majeure["Combativité"] :
                print(i)
            
        if self.voies["Créativité"] == 5 or self.voies["Créativité"] == 4 :
            #Afficher les valeurs majeurs de créativité
            print("\nScore Majeur en Créativité : ")
            print(" ")
            for i in qualite_majeure["Créativité"] :
                print(i)
        
        if self.voies["Empathie"] == 5 or self.voies["Empathie"] == 4 :
            #Afficher les valeurs majeurs d'empathie
            print("\nScore Majeur en Empathie : ")
            print(" ")
            for i in qualite_majeure["Empathie"] :
                print(i)
                
        if self.voies["Raison"] == 5 or self.voies["Raison"] == 4 :
            #Afficher les valeurs majeurs de raison
            print("\nScore Majeur en Raison : ")
            print(" ")
            for i in qualite_majeure["Raison"] :
                print(i)
                
        if self.voies["Idéal"] == 5 or self.voies["Idéal"] == 4 :
            #Afficher les valeurs majeurs d'idéal
            print("\nScore Majeur en Idéal : ")
            print(" ")
            for i in qualite_majeure["Idéal"] :
                print(i)
                
        #On passe aux Scores mineurs
        
        if self.voies["Combativité"] == 1 or self.voies["Combativité"] == 2 :
            print("\nScore Mineur en Combativité : ")
            print(" ")
            for i in qualite_mineure["Combativité"] :
                print(i)
            
        if self.voies["Créativité"] == 1 or self.voies["Créativité"] == 2 :
            print("\nScore Mineur en Créativité : ")
            print(" ")
            for i in qualite_mineure["Créativité"] :
                print(i)
        
        if self.voies["Empathie"] == 1 or self.voies["Empathie"] == 2 :
            print("\nScore Mineur en Empathie : ")
            print(" ")
            for i in qualite_mineure["Empathie"] :
                print(i)
                
        if self.voies["Raison"] == 1 or self.voies["Raison"] == 2 :
            print("\nScore Mineur en Raison : ")
            print(" ")
            for i in qualite_mineure["Raison"] :
                print(i)
                
        if self.voies["Idéal"] == 1 or self.voies["Idéal"] == 2 :
            print("\nScore Mineur en Idéal : ")
            print(" ")
            for i in qualite_mineure["Idéal"] :
                print(i)
                
        choix_qualite = input("Choississez une qualité :")
        
        choix_qualite = str(choix_qualite)
        
        print("\nVous avez choisi ", choix_qualite, "comme qualité.")
        
        print("\n\n---Défaut---")
        
        print("\nPassons maintenant au choix du défaut.")
        
        print("\nListe des Défauts disponibles :")
        
        if self.voies["Combativité"] == 5 or self.voies["Combativité"] == 4 :
            #Afficher les valeurs majeurs de combativité
            print("\nScore Majeur en Combativité : ")
            for i in defaut_majeur["Combativité"] :
                print(i)
                
        if self.voies["Créativité"] == 5 or self.voies["Créativité"] == 4 :
            #Afficher les valeurs majeurs de créativité
            print("\nScore Majeur en Créativité : ")
            for i in defaut_majeur["Créativité"] :
                print(i)
        
        if self.voies["Empathie"] == 5 or self.voies["Empathie"] == 4 :
            #Afficher les valeurs majeurs d'empathie
            print("\nScore Majeur en Empathie : ")
            for i in defaut_majeur["Empathie"] :
                print(i)
                
        if self.voies["Raison"] == 5 or self.voies["Raison"] == 4 :
            #Afficher les valeurs majeurs de raison
            print("\nScore Majeur en Raison : ")
            for i in defaut_majeur["Raison"] :
                print(i)
                
        if self.voies["Idéal"] == 5 or self.voies["Idéal"] == 4 :
            #Afficher les valeurs majeurs d'idéal
            print("\nScore Majeur en Idéal : ")
            for i in defaut_majeur["Idéal"] :
                print(i)
                
        #On passe aux Scores mineurs
        
        if self.voies["Combativité"] == 1 or self.voies["Combativité"] == 2 :
            #Afficher les valeurs majeurs de combativité
            print("\nScore Mineur en Combativité : ")
            for i in defaut_mineur["Combativité"] :
                print(i)
            
        if self.voies["Créativité"] == 1 or self.voies["Créativité"] == 2 :
            #Afficher les valeurs majeurs de créativité
            print("\nScore Mineur en Créativité : ")
            for i in defaut_mineur["Créativité"] :
                print(i)
        
        if self.voies["Empathie"] == 1 or self.voies["Empathie"] == 2 :
            #Afficher les valeurs majeurs d'empathie
            print("\nScore Mineur en Empathie : ")
            for i in defaut_mineur["Empathie"] :
                print(i)
                
        if self.voies["Raison"] == 1 or self.voies["Raison"] == 2 :
            #Afficher les valeurs majeurs de raison
            print("\nScore Mineur en Raison : ")
            for i in defaut_mineur["Raison"] :
                print(i)
                
        if self.voies["Idéal"] == 1 or self.voies["Idéal"] == 2 :
            #Afficher les valeurs majeurs d'idéal
            print("\nScore Mineur en Idéal : ")
            for i in defaut_mineur["Idéal"] :
                print(i)
                
        choix_defaut = input("Choississez un défaut :")
        
        choix_defaut = str(choix_defaut)
        
        print("\nVous avez choisi ", choix_defaut, "comme défaut.")
        
        
        """------------------------------- Santé mentale et personalité-------------------"""
        
        print("\n---------------------------------------------------------")
        print("\nLes Aspects représentent les différentes facettes de la personnalité du PJ")
        print("\n----Conscience----")
        print("\nCet Aspect rend compte de l'importance de la rationalité pour le PJ, de son ancrage dans la réalité,")
        print("de sa capacité de logique et de réflexion, et de sa solidité.")
        
        self.conscience = self.voies["Raison"] + self.voies["Idéal"]
        
        print("\nVotre Conscience est de :" + str(self.conscience))
        
        print("\n----Instinct----")
        print("\nL'Instinct concerne toute l'énergie pulsionnelle d'un être vivant. Cet Aspect regroupe notamment les")
        print("instincts de survie et d'autoconservation ainsi que tout ce qui a trait à la sexualité.")
        
        self.instinct = self.voies["Combativité"] + self.voies["Créativité"]
        
        print("\nVotre Instinct est de :" + str(self.instinct))
        
        if self.instinct > self.conscience :
            
            self.orientation = "Instinctive"
            print("\nL'orientation de votre personnalité est Instinctive.")
            
            self.trauma = (self.instinct - self.conscience, 0)
            
            print("L'écart entre votre instinct et votre conscience est de", self.trauma[0])
            print("Ceci signifie que vous souffrez de ", self.trauma[0], "points de Trauma permanents.")
        
        elif self.conscience > self.instinct :
            
            self.orientation = "Rationnelle"
            print("\nL'orientation de votre personnalité est Rationnelle.")
            
            self.trauma = (self.conscience - self.instinct, 0)
            
            print("L'écart entre votre instinct et votre conscience est de", self.trauma[0])
            print("Ceci signifie que vous souffrez de ", self.trauma[0], "points de Trauma permanents.")
        
        else :
            print("\nVous avez une santé mentale équilibrée.")
            
            choix = False
            
            while choix == False :
                print("Vous pouvez choisir si votre orientation de la personnalité est plutôt Instinctive ou Rationnelle")
                
                orientation = input("Quel est votre choix ?")
                
                if orientation == "Rationnelle" or orientation == "rationnelle" :
                    
                    self.orientation = "Rationnelle"
                    print("\nL'orientation de votre personnalité est Rationnelle.")
                    choix = True
                
                elif orientation == "Instinctive" or orientation == "instinctive" :
                    
                    self.orientation = "Instinctive"
                    print("\nL'orientation de votre personnalité est Instinctive.")
                    choix = True
                
                else :
                    print("Erreur, veuillez choisir votre orientation.")
                    
        print("\n----Résistance Mentale----")
        
        print("\nDurant ses aventure le PJ sera amené à voir ou comprendre des choses indicibles.")
        print("A chaque fois que cela se produit, il y a une chance que l'état de sa Santé Mentale se dégrade.")
        
        self.resistance_mentale = self.voies["Idéal"] + 5
        
        print("\nVotre Résistance Mentale est de", self.resistance_mentale)
        
        "--------------choix de désordre mental-----------------------"
                
        
        

        
        

        
        
                
        
                
        
        
        
        
                
                
                
                
                
                
                
        
        
        



#--------------------DEBUT PROGRAMME ------------------


print("\nBienvenue dans les Ombres d'Esteren")

print("\nVeuillez commencer par créer votre personnage.")

perso = Player()
#Perso est un objet de la classe Player
perso.creation()
#On active la fonction de création du personnage


