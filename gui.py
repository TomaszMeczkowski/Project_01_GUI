import tkinter as tk
import basic_setup as bs
from pop_ups import PopUps
import customtkinter as ct
from database import DataBaseTester
from mysql.connector import errors
from PIL import Image, ImageTk


class App(PopUps):

    def __init__(self):
        PopUps.__init__(self)

        self.main_window, self.title_main, self.foreground_color, self.windows_size = None, None, None, None
        self.windows_width, self.windows_height = None, None
        self.entry_box_imie, self.entry_box_nazwisko, self.cbox_pasy, self.cbox_belki = None, None, None, None
        self.fg_col, self.font, self.hov_col = None, None, None
        self.width_but, self.heigh_but, self.corner_rad = None, None, None
        self.menu_first_page, self.entry_box_user, self.entry_box_pass, self.label_info_bottom = None, None, None, None
        self.menu_logging_page, self.asterix_decision, self.password_show_button = None, None, None
        self.icon_show, self.icon_hide, self.but_bor_col, self.but_bor_width = None, None, None, None

    def db_setup(self):
        self.inicjowanie_bazy_danych()
        self.inicjowanie_tabel()
        self.auto_ticket_month_check()

    def basic_gui_setup(self):
        self.title_main = bs.title_main
        self.foreground_color = bs.foreground_color
        self.windows_size = bs.windows_size

        self.windows_width = bs.windows_width
        self.windows_height = bs.windows_height

        self.fg_col = bs.buttons_fg_col
        self.hov_col = bs.buttons_hover_col
        self.font = bs.buttons_text_font
        self.width_but = bs.buttons_width
        self.heigh_but = bs.buttons_height
        self.corner_rad = bs.buttons_corner_rad
        self.but_bor_width = bs.buttons_border_width
        self.but_bor_col = bs.buttons_border_color

    def main_page(self, custom_enterance=None, user=None, password=None):
        self.main_window = ct.CTk()
        self.basic_gui_setup()
        self.main_window.title(self.title_main)
        self.main_window.geometry(self.windows_size)
        self.main_window.resizable(width=False, height=False)
        # main_logo = ImageTk.PhotoImage(Image.open("./icons/logo.png").resize((30, 30), Image.ANTIALIAS))
        main_logo = tk.PhotoImage(file="./icons/logo.png")
        self.main_window.iconphoto(False, main_logo)
        # self.main_window.resizable(width=True, height=True)

        self.menu_logging_page = self.frame_maker()
        self.menu_first_page = self.frame_maker()
        menu_second_page = self.frame_maker()
        menu_third_page = self.frame_maker()
        menu_adding_person = self.frame_maker()
        menu_dev_tools = self.frame_maker()
        menu_list_people = self.frame_maker()
        menu_statistics = self.frame_maker()

        menu_list = [self.menu_logging_page, self.menu_first_page, menu_second_page, menu_third_page,
                     menu_adding_person, menu_dev_tools, menu_list_people, menu_statistics]

        self.logging_page_frame()

        for frame in menu_list:
            frame.grid(row=0, column=0, sticky='news')

        self.buttons_main_page(self.menu_first_page, menu_second_page, menu_third_page, opt_dev=menu_dev_tools,
                               opt_stat=menu_statistics)
        self.buttons_client_service(menu_second_page, self.menu_first_page)
        self.buttons_data_base(menu_third_page, self.menu_first_page, menu_adding_person)

        self.menu_adding_person(menu_adding_person, menu_third_page)
        self.menu_dev_tools(menu_dev_tools, self.menu_first_page)
        self.menu_stat(menu_statistics, self.menu_first_page)

        if custom_enterance:
            self.user = user
            self.password = password
            self.menu_logging_page.destroy()
            self.db_setup()
            self.menu_first_page.tkraise()

        else:
            self.menu_logging_page.tkraise()

        self.main_window.mainloop()

        return True

    def logging_page_frame(self):
        label_info = ct.CTkLabel(self.menu_logging_page, text="Łączenie z bazą MySQL", text_font=("Bold", 16))

        label_user = ct.CTkLabel(self.menu_logging_page, text="User")

        self.entry_box_user = ct.CTkEntry(self.menu_logging_page, width=140, height=30, fg_color="#F9F9F9",
                                          corner_radius=2, border_color="#26B9EF", border_width=2)

        label_passowrd = ct.CTkLabel(self.menu_logging_page, text="Password")

        self.entry_box_pass = ct.CTkEntry(self.menu_logging_page, width=140, height=30, fg_color="#F9F9F9",
                                          corner_radius=2, border_color="#26B9EF", border_width=2, show="*")

        self.icon_show = ImageTk.PhotoImage(Image.open("./icons/show.png").resize((30, 30), Image.ANTIALIAS))
        self.icon_hide = ImageTk.PhotoImage(Image.open("./icons/hide.png").resize((30, 30), Image.ANTIALIAS))

        self.password_show_button = ct.CTkButton(self.menu_logging_page, image=self.icon_show, text="",
                                                 command=self.asterix_log_page, width=40, fg_color="white",
                                                 hover_color="#F7F7F7")

        logging_button = ct.CTkButton(self.menu_logging_page, text="Zaloguj się", fg_color="#3BE519", corner_radius=5,
                                      hover_color="#80F069", command=self.click_log_page)
        # logging_button.bind("<Return>", self.click_log_page)
        # self.menu_logging_page.bind("<Return>", self.click_log_page)
        # self.menu_logging_page.bind("<Return>", lambda: self.click_log_page)
        # self.menu_logging_page.bind("<Enter>", self.click_log_page)

        self.label_info_bottom = ct.CTkLabel(self.menu_logging_page, text="", text_color="red", text_font=("Bold", 16))

        label_info.pack(side="top", pady=15)
        label_user.pack(side="top")
        self.entry_box_user.pack(side="top")
        label_passowrd.pack(side="top")
        self.entry_box_pass.pack(side="top")
        self.password_show_button.place(x=334, y=142)
        logging_button.pack(side="top", pady=25)
        self.label_info_bottom.pack(side="top")

        self.asterix_decision = True

    def click_log_page(self):
        self.user = self.entry_box_user.get()
        self.password = self.entry_box_pass.get()

        try:
            DataBaseTester(self.user, self.password).inicjowanie_bazy_danych()
            self.menu_logging_page.destroy()
            self.db_setup()
            self.frame_changer(self.menu_first_page)

        except errors.ProgrammingError:
            self.label_info_bottom.configure(text=f"Nieprawidłowe dane")

    def asterix_log_page(self):

        if self.asterix_decision:
            self.entry_box_pass.configure(show="")
            self.password_show_button.configure(image=self.icon_hide)
            self.asterix_decision = False
        else:
            self.entry_box_pass.configure(show="*")
            self.password_show_button.configure(image=self.icon_show)
            self.asterix_decision = True

    def frame_maker(self, width=0, height=0, custom=False):
        if custom:
            return ct.CTkFrame(self.main_window, width=width, height=height, fg_color=self.foreground_color)
        else:
            return ct.CTkFrame(self.main_window, width=self.windows_width, height=self.windows_height,
                               fg_color=self.foreground_color)

    def frame_changer(self, frame):
        frame.tkraise()

    def exit_button(self):
        self.main_window.quit()
        quit()

    def buttons_main_page(self, master_window, opt1, opt2, opt_dev=None, opt_stat=None):
        button1 = ct.CTkButton(master_window,
                               text="1. Obsługa klienta",
                               width=self.width_but,
                               height=self.heigh_but,
                               command=lambda: self.frame_changer(opt1),
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button2 = ct.CTkButton(master_window,
                               text="2. Baza danych",
                               width=self.width_but,
                               height=self.heigh_but,
                               command=lambda: self.frame_changer(opt2),
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button3 = ct.CTkButton(master_window,
                               text="3. Statystyki",
                               width=self.width_but,
                               height=self.heigh_but,
                               command=lambda: self.frame_changer(opt_stat),
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button4 = ct.CTkButton(master_window,
                               text="6. Dev Tools",
                               width=self.width_but,
                               height=self.heigh_but,
                               command=lambda: self.frame_changer(opt_dev),
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button5 = ct.CTkButton(master_window,
                               text="Wyjście",
                               width=150,
                               height=40,
                               command=self.exit_button,
                               corner_radius=5,
                               fg_color=self.fg_col,
                               hover_color="#DC4848",
                               text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color="#DC4848")

        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=45)
        button5.pack(pady=25)

    def buttons_client_service(self, master_window, opt1):
        button1 = ct.CTkButton(master_window,
                               text="1. Wydaj kluczyk",
                               width=self.width_but,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=self.wydawanie_kluczyka_frame,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button2 = ct.CTkButton(master_window,
                               text="2. Sprzedaj karnet",
                               width=self.width_but,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=self.sell_karnety,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button3 = ct.CTkButton(master_window,
                               text="3. Sprawdź karnet",
                               width=self.width_but,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=self.sprawdzanie_karnetu_frame,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button4 = ct.CTkButton(master_window,
                               text="4. id finder",
                               width=self.width_but,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=lambda: self.id_finder_frame(),
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        button5 = ct.CTkButton(master_window,
                               text="Powrót",
                               width=self.width_but - 50,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               command=lambda: self.frame_changer(opt1),
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=5)
        button5.pack(pady=50)

    def buttons_data_base(self, master_window, opt1, opt2):
        button1 = ct.CTkButton(master_window, text="1. Dodaj nową osobę", width=250, height=40,
                               command=lambda: self.frame_changer(opt2), corner_radius=self.corner_rad,
                               fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button2 = ct.CTkButton(master_window, text="2. Popraw dane osoby", width=250, height=40,
                               corner_radius=self.corner_rad, fg_color=self.fg_col, hover_color=self.hov_col,
                               text_font=self.font, state=tk.DISABLED,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button3 = ct.CTkButton(master_window, text="3. Lista osób", width=250, height=40,
                               command=lambda: self.list_of_people(), corner_radius=self.corner_rad,
                               fg_color=self.fg_col, hover_color=self.hov_col, text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button4 = ct.CTkButton(master_window, text="4. Usuń dane osoby", width=250, height=40,
                               corner_radius=self.corner_rad, fg_color=self.fg_col, hover_color=self.hov_col,
                               text_font=self.font,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col,
                               command=lambda: self.person_remove())

        button5 = ct.CTkButton(master_window, text="Powrót", width=250 - 50, height=40,
                               corner_radius=self.corner_rad, fg_color=self.fg_col, hover_color=self.hov_col,
                               text_font=self.font, command=lambda: self.frame_changer(opt1),
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col)

        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=5)
        button5.pack(pady=50)

    def menu_adding_person(self, master_window, opt1):
        label_info = ct.CTkLabel(master_window, text="Dodawanie nowej osoby", text_font=("Bold", 16))
        label_imie = ct.CTkLabel(master_window, text="Imię:")
        self.entry_box_imie = ct.CTkEntry(master_window,
                                          width=140,
                                          height=30,
                                          fg_color="#F9F9F9",
                                          corner_radius=2,
                                          border_color="#26B9EF",
                                          border_width=2)

        label_nazwisko = ct.CTkLabel(master_window, text="Nazwisko:")

        self.entry_box_nazwisko = ct.CTkEntry(master_window,
                                              width=140,
                                              height=30,
                                              fg_color="#F9F9F9",
                                              corner_radius=2,
                                              border_color="#26B9EF",
                                              border_width=2)

        pasy = ["Czarny", "Brązowy", "Purpurowy", "Niebieski", "Biały"]

        label_pas = ct.CTkLabel(master_window, text="Pas:")

        self.cbox_pasy = ct.CTkComboBox(master_window,
                                        values=pasy,
                                        state="readonly",
                                        width=140,
                                        height=30,
                                        fg_color="#F9F9F9",
                                        dropdown_color="#F9F9F9",
                                        corner_radius=5,
                                        button_color="#26B9EF",
                                        border_width=2,
                                        border_color="#26B9EF"
                                        )
        self.cbox_pasy.set(pasy[-1])

        belki = ["0", "1", "2", "3", "4"]

        label_belki = ct.CTkLabel(master_window, text="Belki:")

        self.cbox_belki = ct.CTkComboBox(master_window,
                                         values=belki,
                                         state="readonly",
                                         width=140,
                                         height=30,
                                         fg_color="#F9F9F9",
                                         dropdown_color="#F9F9F9",
                                         corner_radius=5,
                                         button_color="#26B9EF",
                                         border_width=2,
                                         border_color="#26B9EF"
                                         )
        self.cbox_belki.set(belki[0])

        button_wykonaj = ct.CTkButton(master_window,
                                      text="Wykonaj",
                                      fg_color=self.btn_submit_fg_color,
                                      corner_radius=self.btn_submit_corner_rad,
                                      border_width=self.btn_submit_bor_width,
                                      border_color=self.btn_submit_bor_color,
                                      hover_color=self.btn_submit_hov_color,
                                      command=self.wykonaj
                                      )

        button_return = ct.CTkButton(master_window,
                                     text="Powrót",
                                     corner_radius=5,
                                     fg_color="white",
                                     hover_color="#FC8383",
                                     border_width=self.btn_submit_bor_width,
                                     border_color="#FC8383",
                                     command=lambda: self.frame_changer(opt1)
                                     )

        label_info.pack()
        label_imie.pack()
        self.entry_box_imie.pack()
        label_nazwisko.pack()
        self.entry_box_nazwisko.pack()
        label_pas.pack()
        self.cbox_pasy.pack()
        label_belki.pack()
        self.cbox_belki.pack()
        button_wykonaj.pack(side="left", padx=70)
        button_return.pack(side="left", padx=5)

    def wykonaj(self):
        # Przekazywanie parametrów
        imie = self.entry_box_imie.get()
        nazwisko = self.entry_box_nazwisko.get()
        pas = self.cbox_pasy.get()
        belki = int(self.cbox_belki.get())

        self.confirm_adding_people(imie, nazwisko, pas, belki)

    def menu_dev_tools(self, master_window, opt1):
        button1 = ct.CTkButton(master_window,
                               text="1. Predefiniowane osoby",
                               width=self.width_but,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=lambda: self.dev_tool_osoby(),
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        button2 = ct.CTkButton(master_window,
                               text="2. Reset Bazy Danych",
                               width=self.width_but,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=lambda: self.confirm_db_reset(),
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        button3 = ct.CTkButton(master_window,
                               text="3. dane stat. dla osób 1-5",
                               width=self.width_but,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=lambda: self.dev_tool_statistics_01(),
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        button4 = ct.CTkButton(master_window,
                               text="4. Dane stat. klubu",
                               width=self.width_but,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=lambda: self.dev_tool_klub_stat(),
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        button5 = ct.CTkButton(master_window,
                               text="Powrót",
                               width=self.width_but - 50,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=lambda: self.frame_changer(opt1),
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=5)
        button5.pack(pady=50)

    def menu_stat(self, master_window, opt1):
        but_add_width = 20

        button1 = ct.CTkButton(master_window,
                               text="1. Aktywność klubu",
                               width=self.width_but + but_add_width,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=self.aktywnosc_klubu_frame,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        button2 = ct.CTkButton(master_window,
                               text="2. Aktywność użytkowników",
                               width=self.width_but + but_add_width,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=self.aktywnosc_osoby_parametry_frame,
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        # button3 = ct.CTkButton(master_window,
        #                        text="3. Wykresy aktywności osób",
        #                        width=self.width_but + but_add_width,
        #                        height=self.heigh_but,
        #                        corner_radius=self.corner_rad,
        #                        fg_color=self.fg_col,
        #                        hover_color=self.hov_col,
        #                        text_font=self.font,
        #                        state=tk.DISABLED
        #                        )

        # button4 = ct.CTkButton(master_window,
        #                        text="4. Wykresy aktywności klubu",
        #                        width=self.width_but + but_add_width,
        #                        height=self.heigh_but,
        #                        corner_radius=self.corner_rad,
        #                        fg_color=self.fg_col,
        #                        hover_color=self.hov_col,
        #                        text_font=self.font,
        #                        command=self.plot_klub
        #                        )

        button5 = ct.CTkButton(master_window,
                               text="Powrót",
                               width=self.width_but - 50,
                               height=self.heigh_but,
                               corner_radius=self.corner_rad,
                               fg_color=self.fg_col,
                               hover_color=self.hov_col,
                               text_font=self.font,
                               command=lambda: self.frame_changer(opt1),
                               border_width=self.but_bor_width,
                               border_color=self.but_bor_col
                               )

        button1.pack(pady=5)
        button2.pack(pady=5)
        # button3.pack(pady=5)
        # button4.pack(pady=5)
        button5.pack(pady=50)
