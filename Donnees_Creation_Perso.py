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
        
    def __repr__(self):
        return f"{self.name}"



mélancholie = Desordre_mental(
    "Mélancolie", 
    "Idéal", 
    "Combativité", 
    
    """Abbatu, manquant d'énergie, le sujet mélancolique est assailli par le pessimisme, la tristesse et une sensation de fatalité qui peuvent le mettre en danger.""", 
    
    {"Déprime" : 
     """Une personne mélancolique devient progressivement plus dure avec elle-même ; 
     le sujet ne se sent pas à la hauteur de ses idéaux. Mais plus que tout, elle souffre d'une perte d'énergie et de motivation"""
    },
    
    {"Dépression" :
     """Le sujet est triste, sans énergie, il peut même avoir du mal à se lever. Il parle peu ou au contraire se plaint en permanence.""",
     "Crise" : "Insomnies et/ou hypersomnies et crises de larmes sans raison apparente.",
     "Aptitude" : 
         ("Résistance Mentale", 2, """Le sujet a moins peur de la mort, bonus de résistance mentale face au danger.""")
    },
  
    {"Mélancolie" : 
     """Le sujet devient désespéré et développe une très mauvaise image de lui-même. Il peut devenir prostré et sans réaction. Son instinct de survie est complètement étouffé et il peut se laisser mourir dans certaines situations.""",
     "Crise" : "Tentative de suicide",
     "Aptitude" : 
         ("Résistance Mentale", 20, """Le sujet n'a peur de rien et surtout pas de mourir. Il réussit tout jet de Résistance mentale face au danger le concernant.""")
    }, 
    "Idéal", 
    "Combativité")
          
paranoia = Desordre_mental(
    "Paranoia", 
    "Raison", 
    "Empathie", 
    
    """Le sujet paranoïaque manque cruellement d'empathie. Il interprète de travers ce qu'il voit ou entend et a tendance à  attribuer aux autres ses propres pensées. Par ailleurs, ce qui est dit ou fait est vécu comme une persécution, ce qui peut aboutir à des réactions violentes de sa part.""", 
    
    {"Méfiance" : 
     """Le sujet se méfie, il soupçonne un complot ou se sent en danger. Il peut devenir suspicieux à l'égard de ses amis ou alliés. En outre, il devient très susceptible et rancunier."""
    },
    
    {"Interprétation abusive" :
     """Le sujet se sent potentiellement menacé par tout ce qui se passe autour de lui. Il est très vigilant et de plus en plus suspicieux.""",
     "Crise" : "Interprétation délirante d'un signe, d'un son, d'une attitude, etc. Réaction à l'interprétation",
     "Aptitude" : 
         ("Vigilance", 2, """Le sujet sera très difficilement surpris, +2 à tout jet de compétence concernant la vigilance""")
    },
  
    {"Délire organisé" : 
     """Le sujet structure un délire autour d'une personne ou d'une entité. Il devient imperméable aux critiques, enfermé dans un raisonnement logique mais basé sur des éléments erronnés ou inventés.""",
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
    
    """Le sujet à tendance à prendre exemple sur des personnes influentes ou charismatiques jusqu'au point de complètement les copier et de devenir incapable de prendre une initiative ou d'imagine quelque chose de nouveau.""", 
    
    {"Référence" : 
     """Générallement peu spontané dans ses actes et pensées, le sujet a un groupe de personnes lui servant de référence et auquel il a toujours tendance à demander conseil : l'armée, les prêtres, les universitaires, etc. Lorsque sa capacité à prendre une décision est sollicitée, il est perdu dans le doute, trouvant difficilement par lui-même le choix à faire."""
    },
    
    {"Mimétisme" :
     """Le sujet est très dépendant de l'avis des autres et surtout du groupe de référence, il élit une personne en particulier qui devient son 'modèle'. Le sujet, fasciné, cherchera à imiter ce que fait la personne, idéalisant ses actes et ses paroles. Ce modèle peut être un personnage vivant ou mort; voir même un personnage fictif.""",
     "Crise" : "Curiosité frénétique envers son 'modèle'. Possible incapacité à prendre une décision sans l'avis de celui-ci.",
     "Aptitude" : 
         ("Imitation ou leurre", 2, """Le sujet obtient un bonus de +2 à chaque jet de compétence impliquant l'imitation ou le leurre : imitation vocale, déguisement, ventriloquie,...""")
    },
  
    {"Identification" : 
     """Le sujet en arrive à se croire lié à son idole et imagine être son fils ou sa fille caché, son frère jumeau oublié ou tout autre lien 'vraisemblable'. Ses croyances délirantes peuvent en arriver à lui faire croire qu'il est peut-être lui-même son modèle et que celui-ci n'est qu'un sosie, ayant usurpé sa vie.""",
     "Crise" : "persuasion d'être victime d'une machination dans laquelle le modèle du sujet est un sosie lui ayant volé sa place.",
     "Aptitude" : 
         ("Imitation ou leurre", 4, """Le sujet obtient un bonus de +4 à chaque jet de compétence impliquant l'imitation ou le leurre : imitation vocale, déguisement, ventriloquie,...""")
    }, 
    "Empathie", 
    "Créativité")
          
          
obsession = Desordre_mental(
    "Obsession", 
    "Raison", 
    "Créativité", 
    
    """Le sujet pense trop et ses réflexions peuvent s'enliser rapidement et tourner à l'obsession. Il manque de plus en plus de créativité à mesure que son champ de pensée se focalise sur son obsession.""", 
    
    {"Idée obsédante" : 
     """Le sujet a tendance à se focaliser sur un thème ou une idée fixe, ce qui peut l'entraver dans ses autres activités. 
     Il peut devenir anxieux s'il n'a pas l'occasion de respecter les actions appropriées (rituel religieux, vérification, etc).
     Le sujet obsessionnel a tendance à être méticuleux (maniaque) et assez froid dans ses relations avec les autres."""
    },
    
    {"Obsession" :
     """En plus de penser tout le temps à son thème de prédilection, le sujet a tendance à se sentir angoissé. Il développe de nouveaux rituels, qu'il doit executer sous peine de se sentir envahi par l'angoisse (par exemple : vérifier son équipement en sortant d'un lieu, faire une prière après une certaine action, compter ses daols, etc.).""",
     "Crise" : """Sentiment d'oppression violente nécessitant l'exécution du même rituel à plusieurs reprises, en lien avec son sujet de prédilection""",
     "Aptitude" : 
         ("Jets concernant son obsession", 2, """Le sujet obtient un bonus de +2 à chaque jet concernant son obsession""")
    },
  
    {"Ritualisation" : 
     """Chaque action ou pensée du sujet est contaminée par son obsession. Une culpabilité diffuse et écrasante l'envahit s'il ne se consacre pas totalement à son thème privilégié. Menacé par l'angoisse, il peut connaître de graves moments de tristesse et de mal-être.""",
     "Crise" : "Usage de tous les moyens pour arriver à ses fins, avec recours à la violence si nécessaire.",
     "Aptitude" : 
         ("Jets concernant son obsession", 4, """Le sujet obtient un bonus de +4 à chaque jet concernant son obsession""")
    }, 
    "Raison", 
    "Créativité")
                                                                                          

mysticisme = Desordre_mental(
    "Mysticisme", 
    ("Idéal","Empathie"), 
    None, 
    
    """Les croyances, qui peuvent être de toute nature, risquent de prendre une place de plus en plus importante dans la vie du sujet au point de le faire sombrer dans des délires mystiques.""", 
    
    {"Mysticisme" : 
     """Sur un premier versant, les convictions du sujet se durcissent au point qu’il devient obsédé par la bonne observance des rites propres à ses croyances. Sur un autre versant, il apparaît continuellement à l’écoute des “signes” de son environnement, plongé dans un état méditatif. Il peut apparaître comme un mystique, voire un marginal aux yeux des autres."""
    },
    
    {"Fanatisme" :
     """Le discours et les pensées du sujet sont principalement tournés vers ses croyances. Il supporte de moins en moins les remises en question de ses convictions et réagit de manière imprévisible vis à vis de ceux qui ne les partagent pas.""",
     "Crise" : """moment mystique pendant lequel le sujet semble tantôt coupé du reste du monde, absorbé dans ses pensées, tantôt exalté.""",
     "Aptitude" : 
         ("Score d'exaltation ou de Rindath", 5, """Le sujet obtient +5 à son score maximal d'Exaltation ou de Rindath.""")
    },
  
    {"Délire Mystique" : 
     """Le sujet se pense en contact direct avec des entités supérieures ou est persuadé d’être investi d’une mission spéciale qu’il doit accomplir coûte que coûte. Ses convictions deviennent pratiquement impossibles à remettre en question. Il peut prendre des risques inconsidérés, devenir violent ou encore entamer un voyage dangereux dans un but mystique improbable.""",
     "Crise" : "persuasion d’être témoin d’un 'signe' donnant des moments intenses d’exaltation et l’abandon de l’action en cours.",
     "Aptitude" : 
         ("Score d'exaltation ou de Rindath", 15, """Le sujet obtient +15 à son score maximal d'Exaltation ou de Rindath.""")
    }, 
    ("Idéal", "Empathie"), 
    "Raison")
    

frénésie = Desordre_mental(
    "Frénésie", 
    "Combativité", 
    None, 
    
    """Agressif et téméraire, le frénétique a tendance à réaliser des actes violents et impulsifs sans éprouver ni remords, ni culpabilité.""", 
    
    {"Agressivité" : 
     """Le sujet devient irritable et agressif pour un rien. Il a tendance à essayer de contrôler et de dominer les autres."""
    },
    
    {"Impulsivité" :
     """D’humeur instable, la combativité du sujet se traduit le plus souvent par la violence et l’agressivité. Il est perçu comme tyrannique et d’humeur lunatique.""",
     "Crise" : """acte violent, non respect de l’ordre établi ou prise soudaine d’un risque inconsidéré.""",
     "Aptitude" : 
         ("Survie", 1, """Le nombre maximal de points de Survie augmente d'un point.""")
    },
  
    {"Fureur" : 
     """Le sujet est en permanence sous tension et réagit de manière violente à pratiquement toutes les situations. Parallèlement, les processus de pensée sont très affaiblis et la capacité à éprouver des émotions émoussée.""",
     "Crise" : "furie destructrice pouvant facilement aller jusqu’au meurtre.",
     "Aptitude" : 
         ("Survie", 2, """Le nombre maximal de points de Survie augmente de 2 points.""")
    }, 
    "Combativité", 
    "Raison")
    

hallucination = Desordre_mental(
    "Hallucination", 
    ("Créativité","Empathie"), 
    None, 
    
    """Dépassé par son imaginaire foisonnant et envahissant sa réalité, le sujet croit percevoir des choses qui n’ont pourtant aucune existence concrète. Les hallucinations peuvent concerner les cinq sens mais l’audition est privilégiée. Le vécu hallucinatoire peut être sur un versant mystique ou persécutif. Dans ce dernier cas, il est lié à des scènes ou souvenirs traumatisants revenant hanter le sujet.""", 
    
    {"Illusion" : 
     """Le sujet a l’impression que ses sens lui jouent des tours. Une ombre au coin de la ruelle ou dans un bosquet, un chuchotement dans les allées sombres d’une cité..."""
    },
    
    {"Fausses perceptions" :
     """Assailli par des perceptions qu’il ressent comme étranges, le sujet commence à construire une théorie autour d’un thème précis. Il ne s’agit généralement pas d’hallucinations directes mais plutôt de symptômes d’illusion marqués, accompagnés d’un sentiment diffus de mysticisme ou d’angoisse.""",
     "Crise" : """hallucinations directes mettant en jeu l’un des cinq sens. Persuasion de la réalité des visions ou des ressentis.""",
     "Aptitude" : 
         ("Score d'exaltation ou de Rindath", 5, """Le sujet obtient +15 à son score maximal d'Exaltation ou de Rindath. sur le versant mystique""",
          "Jets de vigilance", 3, """Le sujet est attentif à tout 'signe extérieur'. Il sera très difficilement surpris. sur le versant persécutif""")
    },
  
    {"Hallucination" : 
     """Le sujet est harcelé par ses hallucinations qui prennent clairement une dimension mystique ou une dimension paranoïaque.Son rapport au monde est profondément distordu car pratiquement toutes ses interactions sont contaminées par des éléments hallucinatoires qu’il croit réels.""",
     "Crise" : """coupure totale avec le monde extérieur, Visions et sensations qui envahissent totalement le sujet. Mise en grand danger sans s’en rendre compte.""",
     "Aptitude" : 
         ("Score d'exaltation ou de Rindath", 15, """Le sujet obtient +15 à son score maximal d'Exaltation ou de Rindath. sur le versant mystique""",
          "Jets de vigilance", 20, """Le sujet est attentif à tout 'signe extérieur'. Il ne peut être surpris. sur le versant persécutif""")
    }, 
    "Créativité", 
    "Raison")
          

          
hystérie = Desordre_mental(
    "Hystérie", 
    "Empathie", 
    None, 
    
    """Plutôt désinhibé et à l’aise en société, le sujet (en majorité féminin) hystérique est très expressif et très sensible à l’attention qu’on lui porte. La part de séduction dans ses relations quotidiennes est forte. D’une nature plutôt capricieuse et d’humeur changeante, passant rapidement du rire aux larmes, l’hystérique se démarque par son immaturité et sa tendance à dramatiser.""", 
    
    {"Agitation" : 
     """Le sujet est très sensible, pouvant passer d’une émotion à l’autre en quelques instants. Ses caprices s’accentuent autant que sa propension à dramatiser et à théâtraliser le moindre événement de la vie quotidienne, ce qui le rend très difficilement supportable."""
    },
    
    {"Hystérie" :
     """Le sujet vit dans une agitation émotionnelle pratiquement permanente, sensible à tout ce qui peut se dérouler autour de lui et réagissant toujours à l’excès.""",
     "Crise" : """agitation devenant une crise de nerfs violente. Phase de dépression. Plus rarement, déchaînement épileptique aussi violent que soudain.""",
     "Aptitude" : 
         ("Jet de relation", 0, """Le sujet aura une capacité accrue à séduire ses interlocuteurs. En cas de réussite sur un jet de Relation, le résultat sera toujours meilleur que ce qu'il aurait dû être : des soldats bourrus deviennent aimables, un convive aimable sera charmé, etc...""")
    },
  
    {"Erotomanie" : 
     """Le sujet se croit amoureux d’une personne. Cet amour délirant à sens unique peut déboucher sur des actes fous tel que le harcèlement continuel, la séduction outrancière et l’intrusion progressive dans sa vie privée. Lorsque le sujet se rend compte que ses tentatives sont vaines, il peut vivre de grands moments de tristesse pouvant aller jusqu’à l’aggression.""",
     "Crise" : """amour fou d’une personne et persuasion d’être aimé en retour.""",
     "Aptitude" : 
         ("Jet de Relation", 0, """Le sujet aura une capacité à littéralement ensorceler ses interlocuteurs sur un jet de Relation réussi. Charmées, les cibles auront tencande à tout faire pour être aimable, aider, etc. en revanche, un échec sur un jet de Relation aura des effets dévastateurs : les interlocuteurs trouveront le sujet insupportale et auront tendance à éprouver de l'aressivité à son égard. Notez qu'un interlocuteur précédemment charmé pout voir son humeur se renverser et inversement.""")
    }, 
    "Empathie", 
    "Idéal")
          


confusion_mentale = Desordre_mental(
    "Confusion Mentale", 
    "Créativité", 
    "Raison", 
    
    """Ce trouble perturbe gravement les fonctions mentales et enraye le travail de la pensée à mesure que le sujet s’enfonce dans un univers intérieur étrange et fantasmagorique.""", 
    
    {"Étourderie" : 
     """Le sujet est atteint de troubles de l’attention. Il a tendance à avoir du mal à rester concentré, oublie souvent ce qu’on lui a dit plus tôt et peut montrer des troubles du sommeil. Il se montre lunatique, tantôt méditatif, tantôt très expansif."""
    },
    
    {"Confusion" :
     """En plus de montrer des signes de plus en plus inquiétants d’inattention, de troubles de la mémoire et du sommeil, le sujet subit une désorientation spatio-temporelle doublée d’une désorganisation de la pensée pouvant se traduire par des propos incompréhensibles. S’il est artiste ou de nature créative, il apparaît excentrique et doté d’une imagination débordante.""",
     "Crise" : """incapacité du sujet à suivre ce qui se passe autour de lui. Confusion et absorbsion dans son monde onirique. Prostration ou au contraire exaltation.""",
     "Aptitude" : 
         ("Compétence artistique", 2, """Le sujet n'a besoin de dormir que 6 heures par nuit et a +2 à toutes compétence artistique.""")
    },
  
    {"État crépusculaire" : 
     """Le plus souvent perdu dans un syndrome confusionnel grave, le sujet finit par sombrer dans un état où ses troubles de la pensée vont provoquer des mauvaises interprétations de la réalité. De plus, il a tendance à vivre la nuit.""",
     "Crise" : """production d’images visuelles parfois effrayantes qui surgissent dans la conscience alors que le sujet apparaît somnolent et incapable de penser dans la réalité.""",
     "Aptitude" : 
         ("Compétence artistique", 4, """Le sujet ne dort que 3 heures par nuit et obtient un bonus supplémentaire de +2 à toute compétence artistique, puisant l'inspiration dans ses visions.""")
    }, 
    "Créativité", 
    "Raison")
          

         
exaltation = Desordre_mental(
    "Exaltation", 
    "Combativité", 
    "Idéal", 
    
    """Désinhibé, le sujet se sent en pleine forme, capable de tout, et exprime ses idées de grandeur sans aucune retenue. Il peut devenir impulsif et irritable tout en se dispersant dans ses projets.""", 
    
    {"Trouble de l'humeur" : 
     """Le sujet se montre avenant et désinhibé, il est excité, parle vite et fait preuve d’un enthousiasme pouvant paraître exagéré. Un rien peut le contrarier, l’irriter, voire le mettre en colère."""
    },
    
    {"Exaltation" :
     """Perdant la notion des convenances sociales, l’exalté se montre très extraverti, négligeant son langage et sa tenue dans des circonstances inadaptées. Un langage très familier avec un haut dignitaire peut sans doute mettre tout le monde mal à l’aise… Hyperactif, le sujet a aussi toutes sortes de projets et d’idées. Il change souvent d’avis, se montrant impatient et irritable.""",
     "Crise" : """mise en danger en concrétisant l’un de ses projets de manière impulsive et irraisonnée. Violente colère si entravé ou contrarié.""",
     "Aptitude" : 
         ("Prouesses", 2, """Le sujet obtient +2 à chaque jet de Prouesses.""")
    },
  
    {"Mégalomanie" : 
     """Le sujet se pense réellement capable de tout. Il fait de grands projets qui sembleront irréalistes ou délirants à ses compagnons. Passant d’une familiarité exubérante avec un étranger à une colère injustifiée, l’humeur du sujet pose de gros problèmes au quotidien. Il a également tendance à réaliser des achats compulsifs, pouvant même lourdement s’endetter.""",
     "Crise" : """mise en acte de l’un des projets délirants ou colère pouvant devenir violente et meurtrière.""",
     "Aptitude" : 
         ("Prouesses", 4, """Le sujet obtient +2 supplémentaire à chaque jet de Prouesses.""")
    }, 
    "Combativité", 
    "Idéal")          

          
phobie = Desordre_mental(
    "Phobie", 
    None, 
    None, 
    
    """Une personnalité phobique est la conséquence de craintes irrationnelles ou de traumatismes réels. Tout d’abord peur vivace d’une chose ou d’une situation en particulier, la phobie peut devenir grave au point d’empêcher le sujet de vivre correctement.""", 
    
    {"Peur" : 
     """Le sujet répugne à se trouver en présence de son objet phobique ou dans une situation pouvant provoquer l’angoisse. Il fait tout pour se dégager ou s’en éloigner. S’il est obligé d’être en contact physique ou à proximité et de manière prolongée avec l’objet de sa peur, il doit tirer un nouveau jet de Résistance Mentale pour éviter une dégradation immédiate de sa psyché."""
    },
    
    {"Phobie" :
     """Le phobique prend tout le temps en considération la possibilité qu’il peut rencontrer son objet phobique ou la situation source d’angoisse. Il se montre anxieux et il est difficile de le calmer. Toujours sur le qui-vive dès qu’une situation est jugée dangereuse, il refuse obstinément de se confronter à sa némésis. S’il y est contraint, cela déclenche une réaction immédiate à sa crise.""",
     "Crise" : """croyance délirante que la némésis du phobique est là, quelque part, tout près. Il fait tout pour s’éloigner des lieux, quitte à se mettre en danger.""",
     "Aptitude" : 
         ("Connaissances de son objet de phobie", 2, """Le sujet obtient +2 impliquant les connaissances concernant son objet phobique ou les actions pour s'en éloigner.""")
    },
  
    {"Phobie" : 
     """Le sujet est envahi par ses angoisses. Il se montre anxieux et apeuré en permanence, craignant d’être piégé dans une situation où sa phobie le terrasserait.""",
     "Crise" : """véritables hallucinations au cours desquelles le sujet est aux prises avec sa némésis.""",
     "Aptitude" : 
         ("Connaissances de son objet de phobie", 4, """Le sujet obtient +4 impliquant les connaissances concernant son objet phobique ou les actions pour s'en éloigner.""")
    }, 
    "Raison", 
    "Combativité") 
          

forteresse_vide = Desordre_mental(
    "Forteresse Vide", 
    None, 
    None, 
    
    """À force d’affronter l’horreur et les traumatismes, l’esprit se replie et se rigidifie, pouvant aller jusqu’à se couper complètement du monde extérieur. Mais derrière cette forteresse, se cache bien souvent un esprit dévasté qui n’est plus qu’une coquille vide.""", 
    
    {"Emoussement" : 
     """Le sujet a des phases de démotivation pendant lesquelles il ressent une grande fatigue, aussi bien intellectuelle que physique. À d’autres moments, il apparaît sur le plan émotionnel peu réactif par rapport à ce qui se déroule autour de lui, même lorsque cela devrait déclencher des émotions chez un sujet équilibré.""",
     "Aptitude" : 
         ("Santé Mentale", 3, """Le sujet obtient +3 à tous ses jets de Santé Mentale""")
    },
    
    {"Apathie" :
     """Décrit comme froid et distant, le sujet devient de moins en moins sensible aux émotions. Sur un autre versant, il nie complètement les traumas qu’il a subis ou ce qu’il a vu, prétendant que cela n’a jamais existé.""",
     "Crise" : """prostration, insensibilité aux sollicitations extérieures et quasi incapacité de se mouvoir (défense possible si attaqué).""",
     "Aptitude" : 
         ("Santé Mentale", 6, """Le sujet obtient +6 à tous ses jets de Santé Mentale""",
          "Resiste aux tentatives de charme, persuation, etc", 3, """Le sujet est beaucoup moins sensible aux influences sociales, il bénéficie d'un bonus de 3 pour résister à toute tentative de charme, persuasion, etc.""")
    },
  
    {"Forteresse Vide" : 
     """Le sujet ne montre plus aucune émotion. De plus en plus apathique, il ne fait preuve ni de motivation ni d’enthousiasme, sans pour autant paraître triste à son entourage. Sa créativité est fortement émoussée. Passif, il a tendance à suivre les autres.""",
     "Crise" : """prostration totale pendant laquelle l’ esprit et le corps sont complètement fermés à toute sollicitation extérieure (même si attaqué). Oubli de tout souvenir de ces épisodes de repli.""",
     "Aptitude" : 
         ("Santé Mentale", 9, """Le sujet obtient +9 à tous ses jets de Santé Mentale""",
          "Resiste aux tentatives de charme, persuation, etc", 20, """Fermé, l'esprit du malade ne peut être possédé ni touché par la manipulation, les charmes, les envoûtements, etc.""")
    }, 
    "Raison", 
    "Créativité") 
   

                                                                                       
liste_desordres_mentaux = [mélancholie, paranoia, mimétisme, obsession, mysticisme, frénésie, hallucination, hystérie, confusion_mentale, exaltation, phobie, forteresse_vide] 


