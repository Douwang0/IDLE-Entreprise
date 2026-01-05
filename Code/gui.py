
import customtkinter as ctk
from elements import Element, Kayou, Chemise
from PIL import Image

class UserInterface(ctk.CTk):

    """
    Classe implémentant une interface utilisateur pour le jeu.
    Gère l'écran titre et l'écran en jeu.
    Architecture en cours...
    """

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
    
    def run(self): 
        """
        Lance la boucle principale de tkinter
        """
        self.game_update()
        self.mainloop()

    def set_game_ref(self, game_ref):
        """
        Update la référence à la classe Game pour effectuer toutes les updates
        """
        self.game = game_ref

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
    
    def game_update(self):
        """
        Fonction permettant la gestion du jeu.
        """

        if self.game_screen.game_has_begun:
            # Marketplace
            self.game_screen.marketplace.add_game_ref(self.game)
            self.game_screen.marketplace.update_elements({"kayou" : self.game.kayou, **self.game.elements}) # Pas juste self.game.elements car sinon le kayou n'est pas inclus
            if self.game_screen.marketplace.object_exists() and self.game_screen.current_tab == 1:
                self.game_screen.marketplace.add_marketplace(True)
            # Side bar
            self.game_screen.update_text_sidebar(self.game)
            self.game.update()

            print(
                self.game.tick,
                self.game.day,
                self.game.daylenth,
                self.game.player.mget()
            )

        self.after(1000, self.game_update)

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

        def __init__(self, master) -> None:
            
            # Référence au widget principal
            self.master = master
            self.is_event_on : bool = False
            self.game_has_begun : bool = False
        
        def start_game(self):

            # Setup de la side bar
            self.side_bar = ctk.CTkFrame(self.master, fg_color="#272533", width=300, height=1080)
            self.side_bar.place(relx= 0, rely=0, anchor="nw")
            self.side_bar.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsw")

            # Ajout des infos de gameplay sur la side bar
            self.money_amount = ctk.CTkLabel(self.side_bar, text="Money")
            self.money_amount.place(relx=0.1, rely=0.8, anchor="center")

            self.mps_amount = ctk.CTkLabel(self.side_bar, text="mps")
            self.mps_amount.place(relx=0.1, rely=0.85, anchor="center")

            self.impot_amount = ctk.CTkLabel(self.side_bar, text="impot")
            self.impot_amount.place(relx=0.1, rely=0.9, anchor="center")

            self.day = ctk.CTkLabel(self.side_bar, text="day")
            self.day.place(relx=0.1, rely=0.6, anchor="center")

            self.time_left = ctk.CTkLabel(self.side_bar, text="time left")
            self.time_left.place(relx=0.1, rely=0.7, anchor="center")

            # Setup de la main frame
            self.main_frame = ctk.CTkFrame(self.master, fg_color="#333B46", width=1600, height=1060)
            self.main_frame.place(relx= 0.15, rely=0.8, anchor="sw")
            self.main_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ne")

            # Setup de la barre d'événements
            self.event_bar = ctk.CTkFrame(self.master, fg_color="#3B553C", width=1600, height=120)
            self.event_bar.place(relx= 1, rely=0, anchor="sw")
            self.event_bar.grid(row=0, column=0, padx=10, pady=(0,10), sticky="se")

            # Ajout Tab Element du Marketplace
            self.marketplace = self.__Tab_Elements(self.main_frame)

            # Mise en place des tabs
            self.current_tab : int = -1
            self.switch_tab(0)

            self.game_has_begun = True
        def update_text_sidebar(self, game_ref):
            self.game = game_ref
            self.money_amount.configure(text = f"Argent : {self.game.player.mget()}")
            self.mps_amount.configure(text=f"ApS : {self.game.mps}")
            self.impot_amount.configure(text = f"Taux d'Impots : {self.game.impots * 100}%")
            self.day.configure(text = f" Jour {self.game.day}")
            self.time_left.configure(text = f"Temps Restant : {int(self.game.daylenth-self.game.tick)}s ")
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

                for widget in self.side_bar.winfo_children(): 
                    if widget != self.time_left and widget != self.day and widget != self.impot_amount and widget != self.money_amount and widget != self.mps_amount:
                        widget.destroy()
                
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
                if self.marketplace != None: self.marketplace.remove_marketplace()
            
            def setup_element():

                print("Switched to Element Frame.")

                self.current_tab = 1
                self.marketplace.add_marketplace()
            
            def setup_generator():

                print("Switched to Generator Frame.")

                self.current_tab = 2
                if self.marketplace != None: self.marketplace.remove_marketplace()

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

        class __Tab_Stats:
            
            def __init__(self):
                pass

            class __Graphs:

                def __init__(self) -> None:
                    pass

        class __Tab_Elements:

            def __init__(self, frame_ref : ctk.CTkFrame):
                
                self.frame_ref = frame_ref
                self.obj_container : None | ctk.CTkFrame = None
                self.shift = 0
                self.elements = {}

            def update_elements(self, elements):  self.elements = elements
            def add_game_ref(self, game): self.game = game
            def object_exists(self): return hasattr(self, "current_obj") and self.current_obj is not None

            def remove_marketplace(self):
                if self.obj_container != None: self.obj_container.destroy()

            def rs_cycle_objs(self):
                
                """
                Change l'objet actuel pour celui à sa droite.
                """
                old = self.shift
                self.shift = self.shift + 1 if self.shift < len(self.elements.keys()) - 1 else 0
                self.add_marketplace(True, (old == 0 or self.shift == 0) and old != self.shift)

            def ls_cycle_objs(self):

                """
                Change l'objet actuel pour celui à sa gauche.
                """
                old = self.shift
                self.shift = self.shift - 1 if self.shift > 0 else len(self.elements.keys()) - 1
                self.add_marketplace(True, (old == 0 or self.shift == 0) and old != self.shift)

            def add_marketplace(self, update : bool = False, reload : bool = False):

                """
                Ajoute le marketplace à l'écran lorsque l'on est dans la tab elements
                """
                
                if not update:
                    self.obj_container = ctk.CTkFrame(self.frame_ref, 1300, 700)
                    self.obj_container.place(relx=0.1, rely=0.1)
                    
                    self.btn_rs_cycle = ctk.CTkButton(self.obj_container, width=64, height=64, text="->", anchor="center", command=self.rs_cycle_objs)
                    self.btn_rs_cycle.place(relx=0.85, rely=0.5)

                    self.btn_ls_cycle = ctk.CTkButton(self.obj_container, width=64, height=64, text="<-", anchor="center", command=self.ls_cycle_objs)
                    self.btn_ls_cycle.place(relx=.1, rely=0.5)

                    # Ajoute l'objet à l'écran
                    obj = list(self.elements.keys())[self.shift]
                    self.add_object([obj, self.elements[obj].price, self.elements[obj].qty])
                
                elif not reload:
                    obj = list(self.elements.keys())[self.shift]
                    self.current_obj.update_object(obj, self.elements[obj].price, self.elements[obj].qty)

                else:
                    self.rm_object()
                    obj = list(self.elements.keys())[self.shift]
                    self.add_object([obj, self.elements[obj].price, self.elements[obj].qty])

            def add_object(self, obj_details : list):
                
                """
                obj_details :
                0 -> name
                1 -> price
                2 -> qty
                """

                self.current_obj = self.__Object(self.obj_container, obj_details[0], obj_details[1], obj_details[2], self.game)
            def rm_object(self):
                if hasattr(self, "current_obj") and self.current_obj is not None:
                    self.current_obj.destroy_object()  # cleanly destroy the widget
                    self.current_obj = None            # remove reference
            
            class __Object:

                def __init__(self, master, name : str, price : float, qty : int, game_ref) -> None:
                    
                    self.master_container = master
                    self.name : str = name
                    self.price : float = price
                    self.qty : int = qty

                    self.game_ref = game_ref
                    self.construct_object()

                def construct_object(self):

                    print(self.game_ref.tick)
                    
                    self.container = ctk.CTkFrame(self.master_container, 870, 620)
                    self.container.place(relx=0.5, rely=0.5, anchor="center")

                    self.image = ctk.CTkImage(light_image=Image.open('Images/Elements_Placeholder.jpg'),
                                              dark_image=Image.open('Images/Elements_Placeholder.jpg'),
                                              size=(480,480))
                    
                    self.img_label = ctk.CTkLabel(self.container, text='', anchor="center", image=self.image)
                    self.img_label.place(relx=0.1, rely=0.1)

                    if self.name != "kayou":
                        self.label = ctk.CTkLabel(self.container, anchor="center", text=f'Nom : {self.name} \n Prix : {self.price}€ \n Quantitée : {self.qty}', font=('Arial', 24), wraplength=200)
                        self.label.place(relx=0.725, rely=0.3)

                        self.amount_entry = ctk.CTkEntry(
                            self.container,
                            width=120,
                            placeholder_text="Quantité"
                        )
                        self.amount_entry.insert(0, "1")
                        self.amount_entry.place(relx=0.75, rely=0.5, anchor="center")

                        self.btn_buy = ctk.CTkButton(self.container, 64, 64, anchor="center", text="Buy", command=self.buy_object)
                        self.btn_buy.place(relx=0.75, rely=0.6)

                        self.btn_sell = ctk.CTkButton(self.container, 64, 64, anchor="center", text="Sell", command=self.sell_object)
                        self.btn_sell.place(relx=0.85, rely=0.6)
                    else :
                        self.label = ctk.CTkLabel(self.container, anchor="center", text=f"Nom : {self.name} \n Prix : {self.price}€ Mais Gratuit a L'Achat \n Quantitée : {self.qty}", font=('Arial', 24), wraplength=200)
                        self.label.place(relx=0.725, rely=0.3)

                        self.btn_buy = ctk.CTkButton(self.container, 64, 64, anchor="center", text="Buy", command=lambda :self.game_ref.buy(self.name,"kayou"))
                        self.btn_buy.place(relx=0.75, rely=0.6)

                        self.btn_sell = ctk.CTkButton(self.container, 64, 64, anchor="center", text="Sell", command=lambda :self.game_ref.sell(self.name,"kayou"))
                        self.btn_sell.place(relx=0.85, rely=0.6)

                def update_object(self, name : str, price : float, qty : int) -> None:
                    
                    self.name, self.price, self.qty = name, price, qty
                    self.label.configure(text=f'Nom : {self.name} \n Prix : {self.price}€ \n Quantitée : {self.qty}' if self.name != "kayou" else f"Nom : {self.name} \n Prix : {self.price}€ Mais Gratuit a L'Achat \n Quantitée : {self.qty}")

                    self.label.update()

                def buy_object(self):
                    try:
                        amount = int(self.amount_entry.get())
                    except ValueError:
                        print("Valeur invalide")
                        return

                    print(f"BUY {amount} x {self.name}")
                    
                    self.game_ref.buy(self.name,"element", amount)


                def sell_object(self):
                    try:
                        amount = int(self.amount_entry.get())
                    except ValueError:
                        print("Valeur invalide")
                        return

                    print(f"SELL {amount} x {self.name}")
                    # Example:
                    self.game_ref.sell(self.name,"element", amount)

                def destroy_object(self):
                    if hasattr(self, "container"):
                        self.container.destroy()  # destroys frame + all child widgets
                    # remove references to widgets
                    self.container = None
                    self.label = None
                    self.img_label = None
                    self.amount_entry = None
                    self.btn_buy = None
                    self.btn_sell = None


        class __Tab_Generator:
            
            def __init__(self):
                pass

            class __Field:

                def __init__(self) -> None:
                    pass

if __name__ == "__main__":

    App = UserInterface()