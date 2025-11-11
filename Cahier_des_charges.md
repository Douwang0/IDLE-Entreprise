
# - Historique des modifications -

- 06/11/2025
Charles - Ajout des parties 3, 4, 5, 6

# - En-Tête -

Nom de l'équipe : Wall Street Umas
Membres : Charles, Giulian, Lylian, Evan C.
Rôles : 
- Charles : Lead Programmeur full-stack, Dev GUI
- Giulian : Chef de projet, Back-end
- Lylian : Programmeur full-stack
- Evan : Designer GUI
Titre du projet : Idle Entreprise
Date de début : 13/10/2025
Date de fin prévue : 27/11/2025

# - 1. Contexte et objectifs

• Problématique à résoudre : Créer un logiciel utilisant la programmation orientée objet
• Objectif général : Créer un simulateur de gestion d'entreprise avec interface graphique, a titre humoristique
• Public cible / utilisateurs : Personnes voulant simuler une entreprise de manière non réaliste, a titre de divertissement. 

# - 2. Fonctionnalités attendues

L’application est un jeu de gestion humoristique reposant sur un système de jours successifs et d’événements aléatoires. L’objectif du joueur est de faire prospérer son entreprise le plus longtemps possible avant la faillite.

### **2.1 Boucle de jeu**

- Le jeu est organisé en **journées** successives, dont la durée est **dégressive** (diminue au fur et à mesure de la progression).
    
- Le joueur doit **tenir le plus de jours possible** avant la faillite.
    
- À chaque journée, des **événements aléatoires** (bonus ou malus) peuvent survenir et impacter différents paramètres du jeu :
    
    - durée de la journée
        
    - prix du marché
        
    - production ou rendement
        
    - taxes, frais, moral, etc.
        
- La **défaite** survient lorsque l’argent du joueur passe sous un seuil critique (faillite).
    

### **2.2 Interface générale**

- L’application est composée d’une **fenêtre principale** avec plusieurs onglets accessibles via une barre latérale :
    
    1. **Accueil**
        
    2. **Éléments (achat/vente)**
        
    3. **Générateurs / Employés**
        
- Une **bandeau d’information** est affiché en permanence, contenant :
    
    - messages d’actualité humoristiques aléatoires
        
    - le pourcentage d’impôts
        
    - le compteur de jours
        
    - le temps restant avant la fin de la journée en cours.
        

### **2.3 Onglet Accueil**

- Affichage d’un **compteur d’argent** augmenté en temps réel (animation continue).
    
- Présence d’un **graphique décoratif** affichant des courbes aléatoires (non liées au gameplay).
    
- Vue synthétique des revenus par seconde.
    

### **2.4 Onglet Éléments (Achat / Vente)**

- Permet l’achat et la revente d’éléments soumis à **un marché fluctuant**.
    
- Exemple emblématique : **le Kayou**, qui sert de ressource de base en début de partie :
    
    - achat/vente **manuels**
        
    - **prix faible et fluctuations lentes**
        
    - **quantité limitée** pour éviter les abus, car le Kayou est gratuit à la base.
        
- L’achat se fait **par quantité choisie** (pas de génération automatique).
    

### **2.5 Onglet Générateurs / Employés**

- Contient les éléments qui **produisent de l’argent de manière automatique**.
    
- Ces générateurs représentent :
    
    - des **employés**,
        
    - des **actions/droits** donnant des **dividendes**.
        
- Chaque générateur possède :
    
    - un **coût d’achat**
        
    - une **production automatique par seconde**
        
    - un **rendement variable** selon les événements du jour
        
    - une possible montée en niveau ou effet d’optimisation (si implémenté).
        

### **2.6 Système d’économie**

- Prix et rendements soumis à **fluctuations** influencées par :
    
    - les bonus/malus aléatoires
        
    - la progression dans le jeu
        
    - les actions du joueur
        
- Taxes globales pouvant varier d’un jour à l’autre.
    

### **2.7 Sauvegarde et progression**

- **Aucune sauvegarde d’état de partie** (logique roguelike).
    
- Seul le **meilleur score (nombre de jours tenus)** est enregistré.
    
- Stockage du score dans un **fichier texte (.txt)**.
    

### **2.8 Style & Humour**

- Ton humoristique **subtil**, intégré dans :
    
    - les messages du bandeau
        
    - les descriptions d’objets
        
    - certains noms d’éléments et événements
        
- L’humour reste secondaire et ne gêne pas la lisibilité du jeu.

# 3 - Architecture technique
Langage : Python 3.14
Paradigme : POO
Bibliothèques : CustomTkinter

# 4 - Schéma de classes (UML simplifié)
Inclure : classes principales, attributs, méthodes, relations.

# 5 -  Planning prévisionnel
Semaine | Étape | Tâches | Responsable(s)
1 | Idéation | Choix du thème | Équipe
2 | Conception | Schéma de classes | Dev POO
3 | Dev 1 | Implémentation | Dev POO
4 | Persistance & IHM | Sauvegarde / Interface | Dev Persistance / Interface
5 | Tests & Intégration | Débogage | Dev Tests
6 | Doc & Présentation | Rapport | Équipe

# 6 - Critères de réussite
• Application fonctionnelle
• Bonne utilisation de la POO
• Données sauvegardées
• Code clair et documenté