import customtkinter as ctk

class UserInterface(ctk.CTk):

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

        def __init__(self, master) -> None:

            self.title_screen_frame = ctk.CTkFrame(master)
            self.title_screen_frame.place(relx=0.5, rely=0.5, anchor="center")
            ...

    class GameScreen:

        """
        Classe encapsulant les fonctionnalités de l'écran du jeu en gameplay.
        Architecture en cours...
        """

        def __init__(self, master) -> None:

            # Setup de la side barre
            self.side_bar = ctk.CTkFrame(master, width=300, height=1080, fg_color="white")
            self.side_bar.place(relx= 0, rely=0, anchor="nw")
            self.side_bar.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsw")

            # Setup de la barre d'événements
            self.event_bar = ctk.CTkFrame(master, width=1600, height=110, fg_color="green")
            self.event_bar.place(relx= 1, rely=0, anchor="sw")
            self.event_bar.grid(row=0, column=0, padx=10, pady=(0,10), sticky="se")
            
            # Setup de la frame de l'accueil
            self.stats = ctk.CTkFrame(master, width=1600, height=1000, fg_color="green")
            self.stats.place(relx= 0.15, rely=0.8, anchor="sw")
            self.stats.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ne")

            # Setup de la frame d'éléments
            self.elements = ctk.CTkFrame(master, width=1600, height=1000, fg_color="red")
            self.elements.place(relx= 0.15, rely=0.8, anchor="sw")
            self.elements.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ne")

            # Setup de la frame des générateurs
            self.generators = ctk.CTkFrame(master, width=1600, height=1000, fg_color="gray")
            self.generators.place(relx= 0.15, rely=0.8, anchor="sw")
            self.generators.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ne")

            self.current_tab = self.stats

        def switch_tab(self, new_tab : int) -> None:
            
            """
            Change l'onglet actuel avec un nouveau.
            0 : Statistiques
            1 : Eléments
            2 : Générateurs / Employés
            """

            assert isinstance(new_tab, int), f'ValueError : {new_tab} a été donnée pour <new_tab : int> dans <UserInterface.GameScreen.switch_tab()>.'
            
            # Ajouter code pour setup le nouvel onglet, clear l'actuel et replace


    def __init__(self) -> None:

        super().__init__()

        self.title("Far From Bankruptcy")
        self.geometry("1280x720")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        """# Inititalisation écran titre
        self.title_screen = self.TitleScreen(self)"""
        # Inititalisation écran de jeu
        self.game_screen = self.GameScreen(self)

        self.game_update(lambda : print("CTk c la vie!"))

        self.update()
        self.mainloop()
    
    def game_update(self, update_func):
        update_func()
        self.after(1000, self.game_update, update_func)

if __name__ == "__main__":

    App = UserInterface()