import tkinter
import tkinter as tk
import basic_setup
import basic_setup as settings
from pop_ups import PopUps
import customtkinter


class App(PopUps):

    def __init__(self, user, password):
        PopUps.__init__(self, user, password)
        self.db_setup()

        self.main_window, self.title_main, self.foreground_color, self.windows_size = None, None, None, None
        self.windows_width, self.windows_height = None, None
        self.entry_box_1, self.entry_box_2, self.c1, self.c2 = None, None, None, None
        self.fg_col, self.font, self.hov_col = None, None, None
        self.width_but = None
        self.heigh_but = None
        self.corner_rad = None

    def db_setup(self):
        self.inicjowanie_bazy_danych()
        self.inicjowanie_tabel()
        self.auto_ticket_month_check()

    def basic_gui_setup(self):
        self.title_main = basic_setup.title_main
        self.foreground_color = basic_setup.foreground_color
        self.windows_size = basic_setup.windows_size

        self.windows_width = basic_setup.windows_width
        self.windows_height = basic_setup.windows_height

        self.fg_col = basic_setup.buttons_fg_col
        self.hov_col = basic_setup.buttons_hover_col
        self.font = basic_setup.buttons_text_font
        self.width_but = basic_setup.buttons_width
        self.heigh_but = basic_setup.buttons_height
        self.corner_rad = basic_setup.buttons_corner_rad

    def main_page(self):
        self.main_window = customtkinter.CTk()
        self.basic_gui_setup()
        self.main_window.title(self.title_main)
        self.main_window.geometry(self.windows_size)
        self.main_window.resizable(width=False, height=False)
        # self.main_window.resizable(width=True, height=True)

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
        self.buttons_data_base(menu_third_page, menu_first_page, menu_adding_person)
        self.buttons_menu_adding_person(menu_adding_person, menu_third_page)

        self.menu_adding_person(menu_adding_person)
        self.menu_dev_tools(menu_dev_tools, menu_first_page)
        self.menu_stat(menu_statistics, menu_first_page)

        menu_first_page.tkraise()

        self.main_window.mainloop()

        return True

    def frame_maker(self):
        return customtkinter.CTkFrame(self.main_window, width=self.windows_width, height=self.windows_height,
                                      fg_color=self.foreground_color)

    def frame_changer(self, frame):
        frame.tkraise()

    def exit_button(self):
        self.main_window.quit()
        quit()

    def buttons_main_page(self, master_window, opt1, opt2, opt_dev=None, opt_stat=None):
        button1 = customtkinter.CTkButton(master_window,
                                          text="1. Obsługa klienta",
                                          width=self.width_but,
                                          height=self.heigh_but,
                                          command=lambda: self.frame_changer(opt1),
                                          corner_radius=self.corner_rad,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font)

        button2 = customtkinter.CTkButton(master_window,
                                          text="2. Baza danych",
                                          width=self.width_but,
                                          height=self.heigh_but,
                                          command=lambda: self.frame_changer(opt2),
                                          corner_radius=self.corner_rad,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font)

        button3 = customtkinter.CTkButton(master_window,
                                          text="3. Statystyki",
                                          width=self.width_but,
                                          height=self.heigh_but,
                                          command=lambda: self.frame_changer(opt_stat),
                                          corner_radius=self.corner_rad,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font)

        button4 = customtkinter.CTkButton(master_window,
                                          text="6. Dev Tools",
                                          width=self.width_but,
                                          height=self.heigh_but,
                                          command=lambda: self.frame_changer(opt_dev),
                                          corner_radius=self.corner_rad,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font)

        button5 = customtkinter.CTkButton(master_window,
                                          text="Wyjście",
                                          width=150,
                                          height=40,
                                          command=self.exit_button,
                                          corner_radius=20,
                                          fg_color="#A81717",
                                          hover_color="#DC4848",
                                          text_font=self.font)

        button1.place(x=880, y=50)
        button2.place(x=880, y=100)
        button3.place(x=880, y=150)
        button4.place(x=880, y=450)
        button5.place(x=930, y=500)

        # button1.pack(pady=5)
        # button2.pack(pady=5)
        # button3.pack(pady=5)
        # button4.pack(pady=5)
        # button5.pack(pady=50)

    def buttons_client_service(self, master_window, opt1):
        button1 = customtkinter.CTkButton(master_window,
                                          text="1. Wydaj kluczyk",
                                          width=250,
                                          height=40,
                                          corner_radius=20,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font,
                                          state=tkinter.DISABLED)

        button2 = customtkinter.CTkButton(master_window,
                                          text="2. Sprzedaj karnet",
                                          width=250,
                                          height=40,
                                          corner_radius=20,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font,
                                          state=tkinter.DISABLED)

        button3 = customtkinter.CTkButton(master_window,
                                          text="3. Sprawdź karnet",
                                          width=250,
                                          height=40,
                                          corner_radius=20,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font,
                                          state=tkinter.DISABLED)

        button4 = customtkinter.CTkButton(master_window,
                                          text="4. id finder",
                                          width=250,
                                          height=40,
                                          corner_radius=20,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font,
                                          state=tkinter.DISABLED)

        button5 = customtkinter.CTkButton(master_window,
                                          text="Powrót",
                                          width=250,
                                          height=40,
                                          command=lambda: self.frame_changer(opt1),
                                          corner_radius=20,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font)

        button1.place(x=880, y=50)
        button2.place(x=880, y=100)
        button3.place(x=880, y=150)
        button4.place(x=880, y=200)
        button5.place(x=880, y=500)

    def buttons_data_base(self, master_window, opt1, opt2):
        button1 = customtkinter.CTkButton(master_window, text="1. Dodaj nową osobę", width=250, height=40,
                                          command=lambda: self.frame_changer(opt2), corner_radius=20,
                                          fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font)

        button2 = customtkinter.CTkButton(master_window, text="2. Popraw dane osoby", width=250, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, state=tkinter.DISABLED)

        button3 = customtkinter.CTkButton(master_window, text="3. Lista osób", width=250, height=40,
                                          command=lambda: self.list_of_people(), corner_radius=20,
                                          fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font)

        button4 = customtkinter.CTkButton(master_window, text="4. Usuń dane osoby", width=250, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, state=tkinter.DISABLED)

        button5 = customtkinter.CTkButton(master_window, text="Powrót", width=250, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, command=lambda: self.frame_changer(opt1))

        button1.place(x=880, y=50)
        button2.place(x=880, y=100)
        button3.place(x=880, y=150)
        button4.place(x=880, y=200)
        button5.place(x=880, y=500)

    def buttons_menu_adding_person(self, master_window, opt1):
        button5 = customtkinter.CTkButton(master_window, text="Powrót", width=250, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, command=lambda: self.frame_changer(opt1))
        button5.place(x=880, y=500)

    def menu_adding_person(self, master_window):
        label_1 = customtkinter.CTkLabel(master_window, text="Imię:", width=80, height=30, fg_color=self.fg_col,
                                         corner_radius=5)
        label_1.place(x=200, y=50)

        self.entry_box_1 = customtkinter.CTkEntry(master_window, width=120, height=30, fg_color="#43D6E1",
                                                  corner_radius=5)
        self.entry_box_1.place(x=300, y=50)

        label_2 = customtkinter.CTkLabel(master_window, text="Nazwisko:", width=80, height=30, fg_color=self.fg_col,
                                         corner_radius=5)
        label_2.place(x=200, y=90)

        self.entry_box_2 = customtkinter.CTkEntry(master_window, width=120, height=30, fg_color="#43D6E1",
                                                  corner_radius=5)
        self.entry_box_2.place(x=300, y=90)

        pasy = ["Czarny", "Brązowy", "Purpurowy", "Niebieski", "Biały"]
        label_3 = customtkinter.CTkLabel(master_window, text="Pas:", width=80, height=30, fg_color=self.fg_col,
                                         corner_radius=5)
        label_3.place(x=200, y=130)

        self.c1 = customtkinter.CTkComboBox(master_window, values=pasy, state="readonly", width=140, height=30,
                                            fg_color="#43D6E1", dropdown_color="#43D6E1", corner_radius=5)
        self.c1.set(pasy[-1])
        self.c1.place(x=300, y=130)

        belki = ["0", "1", "2", "3", "4"]
        label_4 = customtkinter.CTkLabel(master_window, text="Belki:", width=80, height=30, fg_color=self.fg_col,
                                         corner_radius=5)
        label_4.place(x=200, y=170)

        self.c2 = customtkinter.CTkComboBox(master_window, values=belki, state="readonly", width=140, height=30,
                                            fg_color="#43D6E1", dropdown_color="#43D6E1", corner_radius=5)
        self.c2.set(belki[0])
        self.c2.place(x=300, y=170)

        button1 = customtkinter.CTkButton(master_window, text="Wykonaj", width=150, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, command=self.wykonaj)
        button1.place(x=500, y=50)

    def wykonaj(self):
        # Przekazywanie parametrów
        imie = self.entry_box_1.get()
        nazwisko = self.entry_box_2.get()
        pas = self.c1.get()
        belki = int(self.c2.get())

        self.confirm_adding_people(imie, nazwisko, pas, belki)

    def menu_dev_tools(self, master_window, opt1):
        button1 = customtkinter.CTkButton(master_window,
                                          text="1. Predefiniowant zestaw osób",
                                          width=150,
                                          height=40,
                                          corner_radius=20,
                                          fg_color=self.fg_col,
                                          hover_color=self.hov_col,
                                          text_font=self.font,
                                          command=lambda: self.dev_tool_osoby()
                                          )

        button2 = customtkinter.CTkButton(master_window, text="2. Reset Bazy Danych", width=150, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, command=lambda: self.confirm_db_reset())

        button3 = customtkinter.CTkButton(master_window, text="3. dane stat. dla osób 1-5", width=150, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, command=lambda: self.dev_tool_statistics_01())

        button4 = customtkinter.CTkButton(master_window, text="4. Dane stat. klubu", width=150, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, command=lambda: self.dev_tool_klub_stat())

        button5 = customtkinter.CTkButton(master_window, text="Powrót", width=150, height=40,
                                          corner_radius=20, fg_color=self.fg_col, hover_color=self.hov_col,
                                          text_font=self.font, command=lambda: self.frame_changer(opt1))

        button1.place(x=880, y=50)
        button2.place(x=880, y=100)
        button3.place(x=880, y=150)
        button4.place(x=880, y=200)
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
