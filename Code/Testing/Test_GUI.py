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

            self.master = master

            # Setup de la frame de l'écran titre
            self.title_screen_frame = ctk.CTkFrame(self.master, width=1920, height=1080, corner_radius=10, fg_color="gray")
            self.title_screen_frame.place(relx=0.5, rely=0.5, anchor="center")
            self.title_screen_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            self.add_screen()

        def add_screen(self):

            """
            Ajout de l'écran titre à l'écran. Efface l'interface actuelle avant.
            """
            
            self.clear_title_screen()

            title = ctk.CTkLabel(self.title_screen_frame, text="Far From Bankruptcy™",width=256, height=64, corner_radius=16, font=("Arial", 64))
            title.place(relx=0.5, rely=0.45, anchor="center")

            start_btn = ctk.CTkButton(self.title_screen_frame, command=lambda : self.master.switch_to_gameplay(), text="Start Game", width=256, height=64, fg_color="#40008f", hover_color="#6202d7", font=("Arial", 16))
            start_btn.place(relx=0.5, rely=0.55, anchor="center")
        
        def clear_title_screen(self):
            for widget in self.title_screen_frame.winfo_children(): widget.destroy()

    class GameScreen:

        """
        Classe encapsulant les fonctionnalités de l'écran du jeu en gameplay.
        Architecture en cours...
        """

        def __init__(self, master) -> None:
            
            self.master = master

            # Setup de la side bar
            self.side_bar = ctk.CTkFrame(self.master, width=300, height=1080, fg_color="#272533")
            self.side_bar.place(relx= 0, rely=0, anchor="nw")
            self.side_bar.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsw")

            # Setup de la barre d'événements
            self.event_bar = ctk.CTkFrame(self.master, width=1600, height=110, fg_color="#3B553C")
            self.event_bar.place(relx= 1, rely=0, anchor="sw")
            self.event_bar.grid(row=0, column=0, padx=10, pady=(0,10), sticky="se")

            # Setup de la frame de l'accueil
            self.main_frame = ctk.CTkFrame(self.master, width=1600, height=1100, fg_color="#333B46")
            self.main_frame.place(relx= 0.15, rely=0.8, anchor="sw")
            self.main_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ne")

            # Mise en place des tabs
            self.current_tab : int = -1
            self.switch_tab(0)

        def switch_tab(self, new_tab : int) -> None:

            """
            Change l'onglet actuel avec un nouveau.
            0 : Statistiques
            1 : Eléments
            2 : Générateurs / Employés
            """

            assert isinstance(new_tab, int), f'ValueError : {new_tab} a été donnée pour <new_tab : int> dans <UserInterface.GameScreen.switch_tab()>.'
            assert self.main_frame != None, f'ValueError : <self.main_frame> a {self.main_frame} pour valeur dans <UserInterface.GameScreen.switch_tab()>.'

            if self.current_tab == new_tab : return

            def update_tab_buttons(new_tab : int):

                for widget in self.side_bar.winfo_children(): widget.destroy()
                
                # Mise en place des couleurs des boutons
                fg_colors = ["#ada43b" if self.current_tab == i else "#424242" for i in range(3)]
                hover_colors = ["#d2c646" if self.current_tab == i else "#696969" for i in range(3)]
                
                stats_btn = ctk.CTkButton(self.side_bar, command=lambda : self.switch_tab(0), text="Stats", width=256, height=64,
                                          fg_color=fg_colors[0], hover_color=hover_colors[0], font=("Arial", 16))
                stats_btn.place(relx=0.5, rely=0.375, anchor="center")

                elements_btn = ctk.CTkButton(self.side_bar, command=lambda : self.switch_tab(1), text="Elements", width=256, height=64,
                                             fg_color=fg_colors[1], hover_color=hover_colors[1], font=("Arial", 16))
                elements_btn.place(relx=0.5, rely=0.45, anchor="center")

                generator_btn = ctk.CTkButton(self.side_bar, command=lambda : self.switch_tab(2), text="Generators", width=256, height=64,
                                              fg_color=fg_colors[2], hover_color=hover_colors[2], font=("Arial", 16))
                generator_btn.place(relx=0.5, rely=0.525, anchor="center")

            def setup_stats():
                print("Switched to Stats Frame.")
                self.current_tab = 0
            
            def setup_element():
                print("Switched to Element Frame.")
                self.current_tab = 1
            
            def setup_generator():
                print("Switched to Generator Frame.")
                self.current_tab = 2

            match new_tab:
                case 0: setup_stats()
                case 1: setup_element()
                case 2: setup_generator()

            update_tab_buttons(new_tab)

    def __init__(self) -> None:

        super().__init__()

        self.title("Far From Bankruptcy")
        self.geometry("1280x720")

        self.wm_attributes("-fullscreen",True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Inititalisation écran titre
        self.title_screen = self.TitleScreen(self)
        # Inititalisation écran de jeu
        self.game_screen = None

        self.game_update(lambda : print("TICK"))

        self.update()
        self.mainloop()

    def clear_screen(self):

        """
        Supprime tous les widgets présents sur l'écran.
        """

        for widget in self.winfo_children(): widget.destroy()

    def switch_to_gameplay(self):

        """
        Fonction faisant la transition entre l'écran titre et l'écran de jeu.
        """

        self.title_screen.clear_title_screen()
        self.game_screen = self.GameScreen(self)

    
    def game_update(self, update_func):
        update_func()
        self.after(1000, self.game_update, update_func)

if __name__ == "__main__":

    App = UserInterface()