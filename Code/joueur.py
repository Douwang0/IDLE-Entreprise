"""
joueur.py

Module définissant la classe Player, représentant le joueur.
Il gère l'argent, les gains et les transactions financières.
"""

from logic import *


class Player:
    """
    Classe représentant le joueur.

    Le joueur possède de l'argent, peut en gagner ou en dépenser
    et interagit avec l'économie du jeu.
    """

    def __init__(self, game):
        self.game = game
        self.__argent = 0    # Argent du joueur (privé)
        self.bonus = 1       # Bonus multiplicateur de gains

    def mget(self):
        """
        Retourne l'argent actuel du joueur.
        """
        return self.__argent

    def madd(self, nbr):
        """
        Ajoute de l'argent au joueur en tenant compte du bonus.

        Paramètres
        ----------
        nbr : float
            Montant à ajouter
        """
        nbr *= self.bonus
        self.__argent += nbr
        self.game.benefices_journee += nbr

    def msub(self, nbr, force=False) -> bool:
        """
        Retire de l'argent au joueur.

        Paramètres
        ----------
        nbr : float
            Montant à retirer
        force : bool
            Si True, l'argent est retiré même si le solde est insuffisant

        Retour
        ------
        bool
            True si la transaction a été effectuée, False sinon
        """
        if nbr > self.__argent and not force:
            return False
        else:
            self.__argent -= nbr
            self.game.benefices_journee -= nbr
            return True
    def bonusmodif(self, mod):
        """
        Docstring for bonusmodif
        
        :param mod: Int multipliant les gains globaux
        """
        self.bonus += mod
    def divisargent(self):
        self.__argent / 2