import customtkinter as ctk

class UserInterface:

    """
    Classe implémentant une interface utilisateur pour le jeu.
    Gère l'écran titre et l'écran en jeu.
    Architecture en cours...
    """

    class TitleScreen:

        """
        Classe encapsulant les fonctionnalités de l'écran titre (séparé de l'interface en jeu).
        Architecture en cours...
        """

        def __init__(self) -> None:

            pass

    class GameScreen:

        """
        Classe encapsulant les fonctionnalités de l'écran du jeu en gameplay.
        Architecture en cours...
        """

        def __init__(self) -> None:

            self.current_tab = None
            ...

        def switch_tab(self, new_tab : int) -> None:
            
            """
            Change l'onglet actuel avec un nouveau.
            0 : Accueil
            1 : Générateur d'argent
            2 : Magasin
            """

            assert isinstance(new_tab, int), f'ValueError : {new_tab} a été donnée pour <new_tab : int> dans <UserInterface.GameScreen.switch_tab()>.'
            
            # Ajouter code pour setup le nouvel onglet, clear l'actuel et replace


    def __init__(self) -> None:

        # Fenêtre principale
        self.root_ctk = ctk.CTk()

        self.root_ctk.title("Far From Bankruptcy")
        self.root_ctk.geometry("1280x720")

        # Inititalisation écran titre
        self.title_screen = self.TitleScreen()
        # Inititalisation écran de jeu
        self.game_screen = self.GameScreen()

        self.root_ctk.update()

        self.root_ctk.mainloop()

if __name__ == "__main__":

    App = UserInterface()