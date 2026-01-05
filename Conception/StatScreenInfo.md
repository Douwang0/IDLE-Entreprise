Toujours Afficher

Argent : game.player.mget()
ArgentParSeconde game.mps
Taux D'impots (en pourcentage): game.impots * 100
Jour Actuel : game.day
Temps avant le prochain jour (en secondes) : int(game.daylenth-game.tick)

on auris pu avoir une courbe d'argent mais ca a pas encore ete fait TwT (pas ULTRA important)

Ecran de pause / Fin de journee

Benefices de la journee : game.benefices_journee
Quota : game.quota * game.impots
Pourcentage du quota actuel : 100 if game.benefices_journee >= game.quota * game.impots else game.benefices_journee/(game.quota * game.impots) * 100
Chiffre D'affaires : game.chiffre_daffaires