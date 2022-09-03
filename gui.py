import tkinter
import tkinter as tk
from tkinter.ttk import Combobox
import basic_setup
import basic_setup as settings
from pop_ups import PopUps
import customtkinter
# from PIL import Image, ImageTk


class App(PopUps):

    def __init__(self, user, password):
        PopUps.__init__(self, user, password)
        self.db_setup()

        self.main_window, self.title_main, self.background_color, self.windows_size = None, None, None, None
        self.windows_width, self.windows_height = None, None
        self.entry_box_1, self.entry_box_2, self.c1, self.c2 = None, None, None, None
        self.fg_col, self.font, self.hov_col = None, None, None

    def db_setup(self):
        self.inicjowanie_bazy_danych()
        self.inicjowanie_tabel()
        self.auto_ticket_month_check()

    def basic_gui_setup(self):
        self.title_main = settings.title_main
        self.background_color = settings.background_color
        self.windows_size = settings.windows_size

        self.windows_width = settings.windows_width
        self.windows_height = settings.windows_height

    def main_page(self):
        self.main_window = tk.Tk()
        self.basic_gui_setup()
        self.main_window.title(self.title_main)
        self.main_window.geometry(self.windows_size)
        self.main_window.resizable(width=False, height=False)

        menu_first_page = self.frame_maker()
        menu_second_page = self.frame_maker()
        menu_third_page = self.frame_maker()
        menu_adding_person = self.frame_maker()
        menu_dev_tools = self.frame_maker()
        menu_list_people = self.frame_maker()
        menu_statistics = self.frame_maker()

        menu_list = [menu_first_page, menu_second_page, menu_third_page, menu_adding_person, menu_dev_tools,
                     menu_list_people, menu_statistics]

        for frame in menu_list:
            frame.grid(row=0, column=0, sticky='news')

        self.buttons_main_page(menu_first_page, menu_second_page, menu_third_page, opt_dev=menu_dev_tools,
                               opt_stat=menu_statistics)
        self.buttons_client_service(menu_second_page, menu_first_page)
        self.buttons_data_base(menu_third_page, menu_first_page, menu_adding_person, menu_list_people)
        self.buttons_menu_adding_person(menu_adding_person, menu_third_page)

        self.menu_adding_person(menu_adding_person)
        self.menu_dev_tools(menu_dev_tools, menu_first_page)
        self.menu_list_people(menu_list_people, menu_third_page)
        self.menu_stat(menu_statistics, menu_first_page)

        menu_first_page.tkraise()

        self.main_window.mainloop()

        return True

    def frame_maker(self):
        return tk.Frame(self.main_window, width=self.windows_width,
                        height=self.windows_height, bg=self.background_color)

    def frame_changer(self, frame):
        frame.tkraise()

    def exit_button(self):
        self.main_window.quit()
        quit()

    def buttons_main_page(self, master_window, opt1, opt2, opt_dev=None, opt_stat=None):

        self.fg_col = basic_setup.buttons_fg_col
        self.hov_col = basic_setup.buttons_hover_col
        self.font = basic_setup.buttons_text_font

        button1 = customtkinter.CTkButton(master_window, text="1. Obsługa klienta", width=250, height=40,
                                          command=lambda: self.frame_changer(opt1), corner_radius=20,
                                          fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font)

        button2 = customtkinter.CTkButton(master_window, text="2. Baza danych", width=250, height=40,
                                          command=lambda: self.frame_changer(opt2), corner_radius=20,
                                          fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font)

        button3 = customtkinter.CTkButton(master_window, text="3. Statystyki", width=250, height=40,
                                          command=lambda: self.frame_changer(opt_stat), corner_radius=20,
                                          fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font)

        button4 = customtkinter.CTkButton(master_window, text="6. Dev Tools", width=250, height=40,
                                          command=lambda: self.frame_changer(opt_dev), corner_radius=20,
                                          fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font)

        button5 = customtkinter.CTkButton(master_window, text="Wyjście", width=150, height=40, command=self.exit_button,
                                          corner_radius=20, fg_color="#A81717", hover_color="#DC4848",
                                          text_font=self.font)
        button1.place(x=880, y=50)
        button2.place(x=880, y=100)
        button3.place(x=880, y=150)
        button4.place(x=880, y=450)
        button5.place(x=930, y=500)

    def buttons_client_service(self, master_window, opt1):
        button1 = customtkinter.CTkButton(master_window, text="1. Wydaj kluczyk", width=250, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, state=tkinter.DISABLED)

        button2 = customtkinter.CTkButton(master_window, text="2. Sprzedaj karnet", width=250, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, state=tkinter.DISABLED)

        button3 = customtkinter.CTkButton(master_window, text="3. Sprawdź karnet", width=250, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, state=tkinter.DISABLED)

        button4 = customtkinter.CTkButton(master_window, text="4. id finder", width=250, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, state=tkinter.DISABLED)

        button5 = customtkinter.CTkButton(master_window, text="Powrót", width=250, height=40,
                                          command=lambda: self.frame_changer(opt1), corner_radius=20,
                                          fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font)

        button1.place(x=880, y=50)
        button2.place(x=880, y=100)
        button3.place(x=880, y=150)
        button4.place(x=880, y=200)
        button5.place(x=880, y=500)

    def buttons_data_base(self, master_window, opt1, opt2, opt3):
        button1 = tk.Button(master_window, command=lambda: self.frame_changer(opt2), text="1. Dodaj nową osobę")
        button1.place(x=880, y=50)

        button2 = tk.Button(master_window, command="", text="2. Popraw dane osoby", state="disabled")
        button2.place(x=880, y=100)

        button3 = tk.Button(master_window, command=lambda: self.frame_changer(opt3), text="3. Lista osoób")
        button3.place(x=880, y=150)

        button4 = tk.Button(master_window, command="", text="4. Usuń dane osoby", state="disabled")
        button4.place(x=880, y=200)

        button5 = tk.Button(master_window, command=lambda: self.frame_changer(opt1), text="Powrót")
        button5.place(x=880, y=500)

    def buttons_menu_adding_person(self, master_window, opt1):
        button5 = tk.Button(master_window, command=lambda: self.frame_changer(opt1), text="Powrót")
        button5.place(x=880, y=500)

    def menu_adding_person(self, master_window):
        label_1 = tk.Label(master_window, text="Imie:")
        label_1.place(x=200, y=50)
        self.entry_box_1 = tk.Entry(master_window)
        self.entry_box_1.place(x=300, y=50)

        label_2 = tk.Label(master_window, text="Nazwisko:")
        label_2.place(x=200, y=90)
        self.entry_box_2 = tk.Entry(master_window)
        self.entry_box_2.place(x=300, y=90)

        pasy = ["Czarny", "Brązowy", "Purpurowy", "Niebieski", "Biały"]
        label_3 = tk.Label(master_window, text="Pas:")
        label_3.place(x=200, y=130)
        self.c1 = Combobox(master_window, values=pasy, state="readonly")
        self.c1.current(4)
        self.c1.place(x=300, y=130)

        belki = ["0", "1", "2", "3", "4"]
        label_4 = tk.Label(master_window, text="Belki:")
        label_4.place(x=200, y=170)
        self.c2 = Combobox(master_window, values=belki, state="readonly")
        self.c2.current(0)
        self.c2.place(x=300, y=170)

        button1 = tk.Button(master_window, command=self.wykonaj, text="Wykonaj")
        button1.place(x=500, y=50)

    def wykonaj(self):
        # Przekazywanie parametrów
        imie = self.entry_box_1.get()
        nazwisko = self.entry_box_2.get()
        pas = self.c1.get()
        belki = int(self.c2.get())

        self.confirm_adding_people(imie, nazwisko, pas, belki)

    def menu_dev_tools(self, master_window, opt1):

        button1 = tk.Button(master_window, command=lambda: self.dev_tool_osoby(), text="1. Predefiniowany zestaw osób")
        button1.place(x=880, y=50)

        button2 = tk.Button(master_window, command=lambda: self.confirm_db_reset(), text="2. Reset Bazy danych")
        button2.place(x=880, y=100)

        button3 = tk.Button(master_window, command=lambda: self.dev_tool_statistics_01(),
                            text="3. dane stat. dla osób 1-5")
        button3.place(x=880, y=150)

        button4 = tk.Button(master_window, command=lambda: self.dev_tool_klub_stat(), text="4. Dane stat. klubu")
        button4.place(x=880, y=200)

        button5 = tk.Button(master_window, command=lambda: self.frame_changer(opt1), text="Powrót")
        button5.place(x=880, y=500)

    def menu_list_people(self, master_window, opt1):
        button1 = tk.Button(master_window, command=lambda: self.list_of_people(), text="1. Lista osób")
        button1.place(x=880, y=150)

        button5 = tk.Button(master_window, command=lambda: self.frame_changer(opt1), text="Powrót")
        button5.place(x=880, y=500)

    def menu_stat(self, master_window, opt1):

        button1 = tk.Button(master_window, command="", text="1. Aktywność klubu", state="disabled")
        button1.place(x=880, y=50)

        button2 = tk.Button(master_window, command="", text="2. Aktywność poszczególnych osób", state="disabled")
        button2.place(x=880, y=100)

        button3 = tk.Button(master_window, command="", text="3. Wykresy aktywności osób", state="disabled")
        button3.place(x=880, y=150)

        button4 = tk.Button(master_window, command="", text="4. Wykresy aktywnośći klubu", state="disabled")
        button4.place(x=880, y=200)

        button5 = tk.Button(master_window, command=lambda: self.frame_changer(opt1), text="Powrót")
        button5.place(x=880, y=500)
