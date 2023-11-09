# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:38:50 2023

@author: Pierrick
"""

SYMPTOME = "Symptôme"
SYNDROME = "Syndrome"
FOLIE = "Folie"


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

#Liste des désordre mentaux

class Desordre_mental :
    
    def __init__(self, name, majeur, mineur, description, symptome, syndrome, folie, accentuation, affaiblissement ):
        # class constructor
        """Objet Désordre mental"""
        self.name = name
        self.majeur = majeur
        self.mineur = mineur
        self.description = description
        self.symptome = symptome
        self.syndrome = syndrome
        self.folie = folie
        self.accentuation = accentuation
        self.affaiblissement = affaiblissement



mélancholie = Desordre_mental(
    "Mélancolie", 
    "Idéal", 
    "Combativité", 
    
    """Abbatu, manquant d'énergie, le sujet mélancolique est assailli par le pessimisme, la tristesse et
    une sensation de fatalité qui peuvent le mettre en danger.""", 
    
    {"Déprime" : 
     """Une personne mélancolique devient progressivement plus dure avec elle-même ; 
     le sujet ne se sent pas à la hauteur de ses idéaux. Mais plus que tout, elle souffre
     d'une perte d'énergie et de motivation"""
    },
    
    {"Dépression" :
     """Le sujet est triste, sans énergie, il peut même avoir du mal à se lever. Il parle peu ou au
     contraire se plaint en permanence.""",
     "Crise" : "Insomnies et/ou hypersomnies et crises de larmes sans raison apparente.",
     "Aptitude" : 
         ("Résistance Mentale", 2, """Le sujet a moins peur de la mort, bonus de résistance
          mentale face au danger.""")
    },
  
    {"Mélancolie" : 
     """Le sujet devient désespéré et développe une très mauvaise image de lui-même. Il peut devenir
     prostré et sans réaction. Son instinct de survie est complètement étouffé et il peut se laisser
     mourir dans certaines situations.""",
     "Crise" : "Tentative de suicide",
     "Aptitude" : 
         ("Résistance Mentale", 20, """Le sujet n'a peur de rien et surtout pas de mourir. Il
          réussit tout jet de Résistance mentale face au danger le concernant.""")
    }, 
    "Idéal", 
    "Combativité")
          
paranoia = Desordre_mental(
    "Paranoia", 
    "Raison", 
    "Empathie", 
    
    """Le sujet paranoïaque manque cruellement d'empathie. Il interprète de travers ce qu'il voit ou entend et a tendance à
    attribuer aux autres ses propres pensées. Par ailleurs, ce qui est dit ou fait est vécu comme une persécution, ce qui
    peut aboutir à des réactions violentes de sa part.""", 
    
    {"Méfiance" : 
     """Le sujet se méfie, il soupçonne un complot ou se sent en danger. Il peut devenir suspicieux à l'égard de ses amis ou
     alliés. En outre, il devient très susceptible et rancunier."""
    },
    
    {"Interprétation abusive" :
     """Le sujet se sent potentiellement menacé par tout ce qui se passe autour de lui. Il est très vigilant et de plus en plus
     suspicieux.""",
     "Crise" : "Interprétation délirante d'un signe, d'un son, d'une attitude, etc. Réaction à l'interprétation",
     "Aptitude" : 
         ("Vigilance", 2, """Le sujet sera très difficilement surpris, +2 à tout jet de compétence concernant la vigilance""")
    },
  
    {"Délire organisé" : 
     """Le sujet structure un délire autour d'une personne ou d'une entité. Il devient imperméable aux critiques, enfermé dans
     un raisonnement logique mais basé sur des éléments erronnés ou inventés.""",
     "Crise" : "Acte de protection extravagant ou passage à l'acte violent",
     "Aptitude" : 
         ("Surprise", 20, """Ne peut être surpris""")
    }, 
    "Combativité", 
    "Empathie")

                                    
mimétisme = Desordre_mental(
    "Mimétisme", 
    None, 
    "Créativité", 
    
    """Le sujet à tendance à prendre exemple sur des personnes influentes ou charismatiques jusqu'au point de complètement les
    copier et de devenir incapable de prendre une initiative ou d'imagine quelque chose de nouveau.""", 
    
    {"Référence" : 
     """Générallement peu spontané dans ses actes et pensées, le sujet a un groupe de personnes lui servant de référence et auquel il
     a toujours tendance à demander conseil : l'armée, les prêtres, les universitaires, etc. Lorsque sa capacité à prendre une
     décision est sollicitée, il est perdu dans le doute, trouvant difficilement par lui-même le choix à faire."""
    },
    
    {"Mimétisme" :
     """Le sujet est très dépendant de l'avis des autres et surtout du groupe de référence, il élit une personne en particulier
     qui devient son 'modèle'. Le sujet, fasciné, cherchera à imiter ce que fait la personne, idéalisant ses actes et ses
     paroles. Ce modèle peut être un personnage vivant ou mort; voir même un personnage fictif.""",
     "Crise" : "Curiosité frénétique envers son 'modèle'. Possible incapacité à prendre une décision sans l'avis de celui-ci.",
     "Aptitude" : 
         ("Imitation ou leurre", 2, """Le sujet obtient un bonus de +2 à chaque jet de compétence impliquant l'imitation
          ou le leurre : imitation vocale, déguisement, ventriloquie,...""")
    },
  
    {"Identification" : 
     """Le sujet en arrive à se croire lié à son idole et imagine être son fils ou sa fille caché, son frère jumeau oublié ou 
     tout autre lien 'vraisemblable'. Ses croyances délirantes peuvent en arriver à lui faire croire qu'il est peut-être 
     lui-même son modèle et que celui-ci n'est qu'un sosie, ayant usurpé sa vie.""",
     "Crise" : "persuasion d'être victime d'une machination dans laquelle le modèle du sujet est un sosie lui ayant volé sa place.",
     "Aptitude" : 
         ("Imitation ou leurre", 4, """Le sujet obtient un bonus de +4 à chaque jet de compétence impliquant l'imitation
          ou le leurre : imitation vocale, déguisement, ventriloquie,...""")
    }, 
    "Empathie", 
    "Créativité")


