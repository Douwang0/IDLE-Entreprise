# Documentation technique – Far From Bankruptcy

## Architecture du projet

- `main.py` : point d’entrée du programme
- `logic.py` : logique principale du jeu
- `joueur.py` : gestion du joueur et de l’argent
- `elements.py` : objets achetables et vendables
- `courbe.py` : variation des prix
- `upgrades.py` : améliorations du joueur
- `events.py` : événements aléatoires
- `gui.py` : interface graphique

## Programmation orientée objet
Le projet utilise plusieurs classes :
- Player
- Game
- Element
- Employes
- Events

Chaque classe a un rôle précis et interagit avec les autres.

## Gestion du temps
- Le jeu fonctionne par ticks
- Un jour correspond à un nombre fixe de ticks
- La difficulté augmente à chaque jour

## Gestion économique
- Gains automatiques
- Dépenses
- Impôts
- Bonus multiplicateurs

## Sauvegarde
- Le highscore est sauvegardé dans un fichier texte
