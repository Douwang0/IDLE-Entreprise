
import customtkinter as ctk

class UserInterface(ctk.CTk):

    """
    Classe implémentant une interface utilisateur pour le jeu.
    Gère l'écran titre et l'écran en jeu.
    Architecture en cours...
    """

    class __TitleScreen:

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
    
    class __EndScreen:

        def __init__(self) -> None:
            pass

    class __GameScreen:

        """
        Classe encapsulant les fonctionnalités de l'écran du jeu en gameplay.
        Architecture en cours...
        """

        class __Tab_Stats:

            class __Graphs:

                def __init__(self) -> None:
                    pass
            
            def __init__(self):
                pass

        class __Tab_Elements:

            class __Object:

                def __init__(self, master, name : str, price : float) -> None:
                    
                    self.master_container = master
                    self.name : str = name
                    self.price : float = price

                    self.construct_object()

                def construct_object(self):
                    
                    self.container = ctk.CTkFrame(self.master_container)
                    #self.image = ctk.CTkImage(...)
                    self.btn_buy = ctk.CTkButton(self.container)
                    self.btn_sell = ctk.CTkButton(self.container)

            def __init__(self, frame_ref : ctk.CTkFrame):
                
                self.frame_ref = frame_ref
                self.obj_container = None
                self.elements = {}

            def update_elements(self, elements):  self.elements = elements

            def remove_marketplace(self):
                if self.obj_container != None: self.obj_container.destroy()

            def add_marketplace(self):

                """
                Ajoute le marketplace à l'écran lorsque l'on est dans la tab elements
                """
                
                if self.obj_container != None: return

                self.obj_container = ctk.CTkScrollableFrame(self.frame_ref, 600, 400)

                for obj in self.elements.keys():
                    self.add_object([obj, self.elements[obj]])

            def add_object(self, obj_details : list):
                
                """
                obj_details :
                0 -> name
                1 -> price
                """

                # Ajouter mise en place des variables pour mettre l'image, le nom, ...
                self.__Object(self.obj_container, obj_details[0], obj_details[1])
        
        class __Tab_Generator:

            class __Field:

                def __init__(self) -> None:
                    pass
            
            def __init__(self):
                pass

        def __init__(self, master) -> None:
            
            # Référence au widget principal
            self.master = master
            
            self.elements = {}
            self.is_event_on : bool = False
        
        def start_game(self):

            # Setup de la side bar
            self.side_bar = ctk.CTkFrame(self.master, fg_color="#272533", width=300, height=1080)
            self.side_bar.place(relx= 0, rely=0, anchor="nw")
            self.side_bar.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsw")

            # Setup de la main frame
            self.main_frame = ctk.CTkFrame(self.master, fg_color="#333B46", width=1600, height=1060)
            self.main_frame.place(relx= 0.15, rely=0.8, anchor="sw")
            self.main_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ne")

            # Setup de la barre d'événements
            self.event_bar = ctk.CTkFrame(self.master, fg_color="#3B553C", width=1600, height=120)
            self.event_bar.place(relx= 1, rely=0, anchor="sw")
            self.event_bar.grid(row=0, column=0, padx=10, pady=(0,10), sticky="se")

            # Mise en place des tabs
            self.current_tab : int = -1
            self.switch_tab(0)

            # Ajout Tab Element du Marketplace
            self.marketplace = self.__Tab_Elements(self.main_frame)


        def switch_tab(self, new_tab : int) -> None:

            """
            Change l'onglet actuel avec un nouveau.
            
            - Valeurs de new_tab - 
            0 : Statistiques
            1 : Eléments
            2 : Générateurs / Employés
            """

            assert isinstance(new_tab, int), f'ValueError : {new_tab} a été donnée pour <new_tab : int> dans <UserInterface.GameScreen.switch_tab()>.'
            assert self.main_frame != None, f'ValueError : <self.main_frame> a {self.main_frame} pour valeur dans <UserInterface.GameScreen.switch_tab()>.'

            if self.current_tab == new_tab : return

            def update_tab_buttons():

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
                self.marketplace.add_marketplace()
            
            def setup_generator():

                print("Switched to Generator Frame.")

                self.current_tab = 2

            match new_tab:

                case 0: setup_stats()
                case 1: setup_element()
                case 2: setup_generator()

            update_tab_buttons()
        
        def request_event_animation(self, event_text : str, time : float) -> None:

            """
            Initialisation de l'animation d'un event.
            
            event_text: str -> texte de l'event à afficher
            time: float -> durée de l'animation
            """

            def scroll_animation():
                
                """
                Animation de scroll de droite à gauche des events. Supprime l'event après que le temps est écoulé.
                """

                if self.event_time > 0:
                    self.event_loc[0] -= 3
                    self.current_event.place(x=self.event_loc[0], rely=0.25, anchor="nw")
                    self.event_time -= 0.005
                    self.current_event.after(5, scroll_animation)
                else:
                    self.current_event.destroy()
                    self.is_event_on = False

            if self.is_event_on: return
            
            self.is_event_on = True

            self.current_event = ctk.CTkLabel(self.event_bar, 28, 28, text=event_text, font=("Arial", 64))
            self.current_event.place(relx=1.0, rely=0.25, anchor="nw")

            self.event_loc = [self.current_event.winfo_x(),self.current_event.winfo_y()]
            self.event_time = time

            scroll_animation()

    def __init__(self) -> None:

        super().__init__()

        self.title("Far From Bankruptcy")

        self.wm_attributes("-fullscreen",True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initialisation écran titre
        self.title_screen = self.__TitleScreen(self)
        # Initialisation écran jeu
        self.game_screen = self.__GameScreen(self)
        # Ref au game
        self.game = None

        self.game_update(lambda : print('Tick...'))

        self.mainloop()

    def set_game_ref(self, game_ref): self.game = game_ref

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
        self.game_screen.start_game()

    
    def game_update(self, update_func):
        update_func()
        self.after(1000, self.game_update, update_func)

if __name__ == "__main__":

    App = UserInterface()