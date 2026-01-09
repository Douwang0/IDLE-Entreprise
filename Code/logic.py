"""
logic.py

Module central contenant la logique principale du jeu Idle
"Far From Bankruptcy".

Il gère :
- l'état global de la partie
- la progression du temps (ticks / jours)
- les achats et ventes
- les bénéfices, impôts et conditions de fin
"""

from joueur import Player
from elements import Element, Kayou, Chemise
from upgrades import Employes
from courbe import Courbe
from events import EventManager


def highscore(new_score=0, filename="highscore.txt"):
    """
    Met à jour ou récupère le meilleur score enregistré.

    Paramètres
    ----------
    new_score : int
        Score à comparer avec l'ancien (par défaut 0 pour simple lecture)
    filename : str
        Fichier contenant le highscore

    Retour
    ------
    int
        Le highscore actuel
    """
    try:
        with open(filename, "r") as file:
            stored_score = int(file.read().strip())
    except FileNotFoundError:
        stored_score = 0

    if new_score > stored_score:
        with open(filename, "w") as file:
            file.write(str(new_score))
        return new_score

    return stored_score


class Game:
    """
    Classe principale représentant une partie de jeu.

    Elle gère :
    - le temps (ticks, jours)
    - le joueur
    - les éléments achetables
    - les upgrades
    - les bénéfices et impôts
    """

    def __init__(self):
        # Temps
        self.tick = 0
        self.day = 0
        self.daylenth = 180  # durée d'un jour en ticks

        # Joueur
        self.player = Player(self)
        
        # GUI
        self.gui = None

        # Élément spécial
        self.kayou = Kayou(self.player, 0.1)

        # Les Events
        self.event = EventManager(self)

        # Économie
        self.mps = 0
        self.impots = 0.01
        self.benefices_journee = 0
        self.benefice_hier = 0
        self.quota = 1000
        self.chiffre_daffaires = 0

        # Éléments du marché
        self.elements = {
            "stylo": Element(self.player, 2),
            "Bouteille": Element(self.player, 20),
            "Chaise": Element(self.player, 50),
            "Chaise (Sophistiquée)": Element(self.player, 80),
            "Samsung 2TM": Element(self.player, 500),
            "Ordinateur Fixe": Element(self.player, 4000),
            "Ordinateur Portatif": Element(self.player, 1500),
            "Ordinateur Quantique": Element(self.player, 3.2),
            "camionnnn": Element(self.player, 2000),
            "voiture (Sophistiquée)": Element(self.player, 5000),
            "Maison": Element(self.player, 800000),
            "The legend of Zelda Souvenir d'Enfance - Matthieu Meriot": Element(self.player, 5),
            "Planètes": Element(self.player, 1e8),
            "gachettes pour manettes": Element(self.player, 36),
            'des touches "cap lock"': Element(self.player, 280),
            "de pixel": Element(self.player, 700),
            "éléments de surprise": Element(self.player, 8e10),
            "Mona Lisa": Element(self.player, 16),
            "la lettre alpha": Element(self.player, 1200),
            "cheveux de Frida Kaloh": Element(self.player, 98000),
            "iphon XX": Element(self.player, 2.5),
            "chemise de Charles": Chemise(self.player, "incommensurable"),
            "boeing 732": Element(self.player, 70000),
            "être humain de droite": Element(self.player, 12000),
            "La chaine Vilbrequin": Element(self.player, 5000000),
        }

        # Upgrades
        self.upgrades = {
            "employes": Employes(100, 1, self.player) # Un peu absuser nan les employees ???? TODO
        }

        # Regroupement de tous les objets à mettre à jour
        self.allcollectables = (
            *self.elements.values(),
            *self.upgrades.values(),
            self.kayou
        )
        self.allIterable = (*self.allcollectables,self.event)
    def elemget(self, elem):
        return self.elements[elem]
    def upgget(self, upg):
        return self.upgrades[upg]
    def set_gui_ref(self,gui):
        self.gui = gui
        self.event.gui = gui
    def update(self):
        """
        Met à jour l'état du jeu à chaque tick.
        """
        self.tick += 1

        # Calcul des gains par seconde
        argent_avant = self.player.mget()

        for item in self.allIterable:
            item.update()

        self.mps = self.player.mget() - argent_avant

        # Passage au jour suivant
        if self.tick >= self.daylenth:
            self.new_day()

        # Condition de défaite
        if self.player.mget() < 0:
            highscore(self.day)
            self.gui.game_over()

    def buy(self, obj_id, obj_type, nbr=1):
        """
        Gère l'achat d'un objet selon son type.
        """
        match obj_type:
            case "kayou":
                self.kayou.buy()
            case "element":
                self.elements[obj_id].buy(nbr)
            case "upgrade":
                self.upgrades[obj_id].buy(nbr)

    def sell(self, obj_id, obj_type, nbr=1):
        """
        Gère la vente d'un objet selon son type.
        """
        match obj_type:
            case "kayou":
                return self.kayou.sell(nbr)
            case "element":
                return self.elements[obj_id].sell(nbr)
            case "upgrade":
                return self.upgrades[obj_id].sell(nbr)
            case "share":
                return self.share[obj_id].sell(nbr)
    def timemodif(self, sec):
        self.daylenth += sec
    def taxmodif(self, mod):
        """
        Docstring for taxmodif
        
        :param mod: Float entre 0 et 1 représentant des pourcentages
        """
        self.impots += mod
    def new_day(self):
        """
        Applique les calculs de fin de journée :
        - impôts
        - quota
        - augmentation de la difficulté
        """
        self.tick = 0

        if self.daylenth != 60:
            self.daylenth -= 5

        impots = (
            self.benefices_journee * self.impots
            if self.benefices_journee > 0
            else 0
        )

        self.benefice_hier = self.benefices_journee
        self.benefices_journee = 0

        # Paiement des impôts et du quota
        self.player.msub(impots, True)
        self.player.msub(self.quota * self.impots, True)

        self.day += 1
        self.impots *= 1.05