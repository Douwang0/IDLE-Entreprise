Toujours Afficher

Argent : game.player.mget()
ArgentParSeconde game.mps
Taux D'impots (en pourcentage): game.impots * 100
Jour Actuel : self.day

on auris pu avoir une courbe d'argent mais ca a pas encore ete fait TwT (pas ULTRA important)

Ecran de pause / Fin de journee

Benefices de la journee : self.benefices_journee
Quota : self.quota * self.impots
Pourcentage du quota actuel : 100 if self.benefices_journee >= self.quota * self.impots else self.benefices_journee/(self.quota * self.impots) * 100