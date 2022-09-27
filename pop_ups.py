import tkinter as tk
from tkinter import ttk
import basic_setup as settings
from database import DataBase
from tkinter import Menu
import customtkinter as ct
import basic_setup as bs
# from PIL import Image, ImageTk


class PopUps(DataBase):

    def __init__(self):
        DataBase.__init__(self)
        self.label_wynik = None
        self.label_wynik_spr_karnetu = None
        self.label_wynik_wydawanie_kluczyka = None
        self.label_wynik_aktywnosc_osoby = None
        self.label_wynik_sell = None
        self.label_remove_result = None

        self.btn_submit_fg_color = bs.buttons_zatwierdzenie_fg_color
        self.btn_submit_hov_color = bs.buttons_zatwierdzenie_hover_color
        self.btn_submit_bor_color = bs.buttons_zatwierdzenie_border_color
        self.btn_submit_bor_width = bs.buttons_zatwierdzenie_border_width
        self.btn_submit_corner_rad = bs.buttons_zatwierdzenie_corner_rad

    def confirm_adding_people(self, *args):
        imie = args[0]
        nazwisko = args[1]
        pas = args[2]
        belki = args[3]

        decision = self.window_maker(size="300x280", bg="#F6FFFF")

        label1 = ct.CTkLabel(decision, width=200, height=100, corner_radius=5,
                             text_font=("Bold", 14),
                             text=f"Przekazane Parametry"
                                  f"\n"
                                  f"\nImie: {imie}"
                                  f"\nNazwisko: {nazwisko}"
                                  f"\nPas: {pas}"
                                  f"\nBelki: {belki}")
        label1.place(x=50, y=20)

        label2 = ct.CTkLabel(decision, text="Zatwierdzić ?", text_font=("Bold", 16))
        label2.place(x=85, y=180)

        button1 = ct.CTkButton(decision,
                               command=lambda: [decision.destroy(),
                                                self.error_info(off=True) if
                                                self.dodawanie_osob(imie, nazwisko, pas, belki) else
                                                self.error_info(
                                                    mess="Error 1: Taka osoba już się znajduję w bazie danych")
                                                ],
                               text="Tak",
                               text_font=("Bold", 16),
                               width=80,
                               height=30,
                               corner_radius=5,
                               fg_color="green",
                               hover_color="green"
                               )
        button1.place(x=65, y=220)

        button2 = ct.CTkButton(decision, command=lambda: decision.destroy(), text="Nie",
                               text_font=("Bold", 16), fg_color="red", width=80, height=30, corner_radius=5,
                               hover_color="red")
        button2.place(x=150, y=220)

        decision.tkraise()
        decision.mainloop()

    def error_info(self, mess="", off=False):
        if off:
            return None

        message_app = self.window_maker(size="450x100", bg="grey")

        label = tk.Label(message_app, text=mess, fg="red", font=('Helvetica', 12, 'bold'))
        label.pack(pady=5)

        button = tk.Button(message_app, command=lambda: [message_app.quit(),
                                                         message_app.destroy()
                                                         ], text="Dalej")
        button.pack(side="bottom", pady=5)

        message_app.tkraise()
        message_app.mainloop()

    def confirm_db_reset(self):

        decision = self.window_maker(size="270x150", bg="grey")

        label2 = tk.Label(decision, text=f"\nChcesz zresetować baze danych?"
                                         f"\n(Wszystkie dane zostaną utracone)",
                          font=16)
        label2.place(x=12, y=6)

        button1 = tk.Button(decision,
                            command=lambda: [decision.destroy(),
                                             self.reset_bazy_danych()],
                            text="Tak", font=16, bg="green")
        button1.place(x=94, y=84)

        button2 = tk.Button(decision, command=lambda: decision.destroy(), text="Nie", font=16, bg="red")
        button2.place(x=146, y=84)

        decision.tkraise()
        decision.mainloop()

    def list_of_people(self):

        message_app = self.window_maker(size="480x530")
        label = tk.Label(message_app, text="Lista osoób trenujących", bg="white", font=14)
        label.pack(side="top", pady=15)

        text = self.show_all_people()
        scrol_bar = tk.Scrollbar(message_app)
        scrol_bar.pack(side="right", fill="y")
        tree_view = ttk.Treeview(message_app, yscrollcommand=scrol_bar.set, height=25)
        tree_view.pack(side="left", padx=40, pady=15)
        scrol_bar.config(command=tree_view.yview)

        # Kolumny tabeli
        col = ("1", "2", "3", "4", "5")
        col_names = ["id", "Imię", "Nazwisko", "Pas", "Belki"]
        col_width = [35, 60, 100, 100, 80]
        tree_view['columns'] = col

        tree_view.column("#0", width=0)
        for i in range(len(col)):
            tree_view.column(f"{col[i]}", width=col_width[i], anchor="center")

        # Nagłówki kolumn
        tree_view.heading("#0", text="")
        for i in range(len(col)):
            tree_view.heading(f"{col[i]}", text=f"{col_names[i]}", anchor="center")
        for i in text:
            tree_view.insert(parent="", index="end", text="", values=i)

        # Menu Bar
        menu_bar = Menu(message_app)
        message_app.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=False)
        # Tkinter z defaultu dodaje pasek na górze który wyłączamy przez tearoff

        print_out_menu = Menu(file_menu, tearoff=False)
        print_out_menu.add_command(label="Plik tekstowy .txt", command=lambda: self.print_to_txt())
        print_out_menu.add_command(label="Arkusz kalkulacyjny .xlsx", command=lambda: self.print_to_excel())

        file_menu.add_cascade(label="Wydruk", menu=print_out_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=message_app.destroy)

        help_menu = Menu(menu_bar, tearoff=False)
        help_menu.add_command(label="#### Under Construction #####")
        help_menu.add_command(label='Q&A')
        help_menu.add_command(label='Help.txt')
        help_menu.add_command(label="#### Under Construction #####")

        menu_bar.add_cascade(label="Opcje", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        message_app.tkraise()
        message_app.mainloop()

    def id_finder_frame(self):

        decision = self.window_maker()

        label_info = ct.CTkLabel(decision, text="Id finder", text_font=("Bold", 16))
        label_imie = ct.CTkLabel(decision, text="Imię")

        entry_box_imie_id_finder = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                               corner_radius=2, border_color="#26B9EF", border_width=2)

        label_nazwisko = ct.CTkLabel(decision, text="Nazwisko")

        entry_box_nazwisko_id_finder = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                                   corner_radius=2, border_color="#26B9EF", border_width=2)

        button_szukaj = ct.CTkButton(decision,
                                     text="Szukaj",
                                     fg_color=self.btn_submit_fg_color,
                                     corner_radius=self.btn_submit_corner_rad,
                                     border_width=self.btn_submit_bor_width,
                                     border_color=self.btn_submit_bor_color,
                                     hover_color=self.btn_submit_hov_color,
                                     command=lambda: self.id_finder_operation(entry_box_imie_id_finder.get(),
                                                                              entry_box_nazwisko_id_finder.get()))

        self.label_wynik = ct.CTkLabel(decision, text="", text_font=("Bold", 14))

        label_info.pack(side="top", pady=15)
        label_imie.pack(side="top")
        entry_box_imie_id_finder.pack(side="top")
        label_nazwisko.pack(side="top")
        entry_box_nazwisko_id_finder.pack(side="top")
        button_szukaj.pack(side="top", pady=25)
        self.label_wynik.pack(side="top", pady=25)

        decision.tkraise()
        decision.mainloop()

    def id_finder_operation(self, imie, nazwisko):

        wynik = self.id_finder(imie, nazwisko)

        if not wynik:
            self.label_wynik.configure(text="Nie znaleziono takiej osoby", text_color="red")
        else:
            self.label_wynik.configure(text=f"Nr id szukanej osoby: {wynik}", text_color="black")

    def sprawdzanie_karnetu_frame(self):

        decision = self.window_maker()

        label_info = ct.CTkLabel(decision, text="Sprawdzanie karnetu", text_font=("Bold", 16))
        label_imie = ct.CTkLabel(decision, text="Imię")

        entry_box_imie_spr_karnetu = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                                 corner_radius=2, border_color="#26B9EF", border_width=2)

        label_nazwisko = ct.CTkLabel(decision, text="Nazwisko")

        entry_box_nazwisko_spr_karnetu = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                                     corner_radius=2, border_color="#26B9EF", border_width=2)

        button_szukaj = ct.CTkButton(decision,
                                     text="Sprawdź",
                                     fg_color=self.btn_submit_fg_color,
                                     corner_radius=self.btn_submit_corner_rad,
                                     border_width=self.btn_submit_bor_width,
                                     border_color=self.btn_submit_bor_color,
                                     hover_color=self.btn_submit_hov_color,
                                     command=lambda: self.spr_karnet_operation(entry_box_imie_spr_karnetu.get(),
                                                                               entry_box_nazwisko_spr_karnetu.get()
                                                                               )
                                     )

        self.label_wynik_spr_karnetu = ct.CTkLabel(decision, text="", text_font=("Bold", 14))

        label_info.pack(side="top", pady=15)
        label_imie.pack(side="top")
        entry_box_imie_spr_karnetu.pack(side="top")
        label_nazwisko.pack(side="top")
        entry_box_nazwisko_spr_karnetu.pack(side="top")
        button_szukaj.pack(side="top", pady=25)
        self.label_wynik_spr_karnetu.pack(side="top", pady=25)

        decision.tkraise()
        decision.mainloop()

    def spr_karnet_operation(self, imie, nazwisko):

        user_id = self.id_finder(imie, nazwisko)

        wynik = self.ticket_check(user_id)

        # Przypadek 1 -> Karnet normalny
        # Przypadek 2 -> Karnet Open
        # Przypadek 3 -> Karnet Wykorzystany
        # Przypadek 4 -> Nie ma takiej osoby w bazie

        if wynik[0] and wynik[1] < 100:
            self.label_wynik_spr_karnetu.configure(text=f"Karnet aktywny \nPozostało {wynik[1]} wejść do wykorzystania",
                                                   text_color="black")
        elif wynik[0] and wynik[1] > 100:
            self.label_wynik_spr_karnetu.configure(text="Karnet Open \nNielimitowany dostęp", text_color="black")
        elif not wynik[0] and not wynik[1]:
            self.label_wynik_spr_karnetu.configure(text="Karnet został wykorzystany", text_color="red")
        else:
            self.label_wynik_spr_karnetu.configure(text="Nie znaleziono takiej osoby", text_color="red")

    def wydawanie_kluczyka_frame(self):

        decision = self.window_maker()

        label_info = ct.CTkLabel(decision, text="Wydawanie kluczyka", text_font=("Bold", 16))
        label_imie = ct.CTkLabel(decision, text="Imię")

        entry_box_imie_wydawanie_kluczyka = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                                        corner_radius=2, border_color="#26B9EF", border_width=2)

        label_nazwisko = ct.CTkLabel(decision, text="Nazwisko")

        entry_box_nazwisko_wydawanie_kluczyka = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                                            corner_radius=2, border_color="#26B9EF", border_width=2)

        button_szukaj = ct.CTkButton(decision,
                                     text="Wydawanie kluczyka",
                                     fg_color=self.btn_submit_fg_color,
                                     corner_radius=self.btn_submit_corner_rad,
                                     border_width=self.btn_submit_bor_width,
                                     border_color=self.btn_submit_bor_color,
                                     hover_color=self.btn_submit_hov_color,
                                     command=lambda: self.wydawanie_kluczyka_operacja(
                                         entry_box_imie_wydawanie_kluczyka.get(),
                                         entry_box_nazwisko_wydawanie_kluczyka.get()
                                     )
                                     )

        self.label_wynik_wydawanie_kluczyka = ct.CTkLabel(decision, text="", text_font=("Bold", 14))

        label_info.pack(side="top", pady=15)
        label_imie.pack(side="top")
        entry_box_imie_wydawanie_kluczyka.pack(side="top")
        label_nazwisko.pack(side="top")
        entry_box_nazwisko_wydawanie_kluczyka.pack(side="top")
        button_szukaj.pack(side="top", pady=25)
        self.label_wynik_wydawanie_kluczyka.pack(side="top", pady=25)

        decision.tkraise()
        decision.mainloop()

    def wydawanie_kluczyka_operacja(self, imie, nazwisko):

        user_id = self.id_finder(imie, nazwisko)
        if not user_id:
            return self.label_wynik_wydawanie_kluczyka.configure(text="Nie ma takiej osoby", text_color="red")

        if self.key_giveaway(user_id):
            return self.label_wynik_wydawanie_kluczyka.configure(text="Wydano kluczyk", text_color="black")
        else:
            return self.label_wynik_wydawanie_kluczyka.configure(text="Nie można wydać kluczyka \nKarnet wykorzystany",
                                                                 text_color="red")

    def aktywnosc_klubu_frame(self):

        message_app = self.window_maker(size="380x400")
        label = tk.Label(message_app, text="Aktywność klubu", bg="white", font=14)
        label.pack(side="top", pady=15)

        text = self.wyswietlanie_aktywnosc_klubu()
        if not text:
            text = ["Brak Danych"]

        scrol_bar = tk.Scrollbar(message_app)
        scrol_bar.pack(side="right", fill="y")
        tree_view = ttk.Treeview(message_app, yscrollcommand=scrol_bar.set, height=25)
        tree_view.pack(side="left", padx=40, pady=15)
        scrol_bar.config(command=tree_view.yview)

        # Kolumny tabeli
        col = ("1", "2", "3")
        col_names = ["Ilość wejść", "Miesiac", "Rok"]
        col_width = [120, 90, 60]
        tree_view['columns'] = col

        tree_view.column("#0", width=0)
        for i in range(len(col)):
            tree_view.column(f"{col[i]}", width=col_width[i], anchor="center")

        # Nagłówki kolumn
        tree_view.heading("#0", text="")
        for i in range(len(col)):
            tree_view.heading(f"{col[i]}", text=f"{col_names[i]}", anchor="center")
        for i in text:
            tree_view.insert(parent="", index="end", text="", values=i)

        # Menu Bar
        menu_bar = Menu(message_app)
        message_app.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=False)
        # Tkinter z defaultu dodaje pasek na górze który wyłączamy przez tearoff

        print_out_menu = Menu(file_menu, tearoff=False)
        print_out_menu.add_command(label="Plik tekstowy .txt", command=self.print_to_txt_klub_aktywnosc)
        print_out_menu.add_command(label="Arkusz kalkulacyjny .xlsx", command=self.print_to_excel_klub_aktywnosc)

        file_menu.add_command(label="Wykres", command=self.plot_klub)
        file_menu.add_cascade(label="Wydruk", menu=print_out_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=message_app.destroy)

        help_menu = Menu(menu_bar, tearoff=False)
        help_menu.add_command(label="#### Under Construction #####")
        help_menu.add_command(label='Q&A')
        help_menu.add_command(label='Help.txt')
        help_menu.add_command(label="#### Under Construction #####")

        menu_bar.add_cascade(label="Opcje", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        message_app.tkraise()
        message_app.mainloop()

    def aktywnosc_osoby_parametry_frame(self):
        decision = self.window_maker()

        label_info = ct.CTkLabel(decision, text="Aktywność użytkownika", text_font=("Bold", 16))
        label_imie = ct.CTkLabel(decision, text="Imię")

        entry_box_imie_wydawanie_kluczyka = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                                        corner_radius=2, border_color="#26B9EF", border_width=2)

        label_nazwisko = ct.CTkLabel(decision, text="Nazwisko")

        entry_box_nazwisko_wydawanie_kluczyka = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                                            corner_radius=2, border_color="#26B9EF", border_width=2)

        button_szukaj = ct.CTkButton(decision,
                                     text="Zatwierdź",
                                     fg_color=self.btn_submit_fg_color,
                                     corner_radius=self.btn_submit_corner_rad,
                                     border_width=self.btn_submit_bor_width,
                                     border_color=self.btn_submit_bor_color,
                                     hover_color=self.btn_submit_hov_color,
                                     command=lambda: self.aktywnosc_osoby_frame(
                                         entry_box_imie_wydawanie_kluczyka.get(),
                                         entry_box_nazwisko_wydawanie_kluczyka.get()
                                     )
                                     )

        self.label_wynik_aktywnosc_osoby = ct.CTkLabel(decision, text="", text_font=("Bold", 14))

        label_info.pack(side="top", pady=15)
        label_imie.pack(side="top")
        entry_box_imie_wydawanie_kluczyka.pack(side="top")
        label_nazwisko.pack(side="top")
        entry_box_nazwisko_wydawanie_kluczyka.pack(side="top")
        button_szukaj.pack(side="top", pady=25)
        self.label_wynik_aktywnosc_osoby.pack(side="top", pady=25)

        decision.tkraise()
        decision.mainloop()

    def aktywnosc_osoby_frame(self, imie, nazwisko):

        user_id = self.id_finder(imie, nazwisko)

        if not user_id:
            return self.label_wynik_aktywnosc_osoby.configure(text="Brak takiej osoby", text_color="red")

        try:
            text, first_day = self.stat_entry_by_id(user_id)
        except TypeError:
            return self.label_wynik_aktywnosc_osoby.configure(text="Brak danych", text_color="red")

        if not text:
            text = ["Brak Danych"]

        self.label_wynik_aktywnosc_osoby.configure(text="", text_color="black")

        message_app = self.window_maker(size="380x400")
        label = tk.Label(message_app, text="Aktywność osoby", bg="white", font=14)
        label.pack(side="top", pady=15)

        label = tk.Label(message_app, text=f"Pierwszy trening: {first_day}", bg="white", font=14)
        label.pack(side="top", pady=5)

        scrol_bar = tk.Scrollbar(message_app)
        scrol_bar.pack(side="right", fill="y")
        tree_view = ttk.Treeview(message_app, yscrollcommand=scrol_bar.set, height=25)
        tree_view.pack(side="left", padx=40, pady=15)
        scrol_bar.config(command=tree_view.yview)

        # Kolumny tabeli
        col = ("1", "2", "3")
        col_names = ["Ilość wejść", "Miesiac", "Rok"]
        col_width = [120, 90, 60]
        tree_view['columns'] = col

        tree_view.column("#0", width=0)
        for i in range(len(col)):
            tree_view.column(f"{col[i]}", width=col_width[i], anchor="center")

        # Nagłówki kolumn
        tree_view.heading("#0", text="")
        for i in range(len(col)):
            tree_view.heading(f"{col[i]}", text=f"{col_names[i]}", anchor="center")
        for i in text:
            tree_view.insert(parent="", index="end", text="", values=i)

        # Menu Bar
        menu_bar = Menu(message_app)
        message_app.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=False)
        # Tkinter z defaultu dodaje pasek na górze który wyłączamy przez tearoff

        print_out_menu = Menu(file_menu, tearoff=False)
        print_out_menu.add_command(label="Plik tekstowy .txt", command="lambda: self.print_to_txt()")
        print_out_menu.add_command(label="Arkusz kalkulacyjny .xlsx", command="lambda: self.print_to_excel()")

        file_menu.add_command(label="Wykres", command=lambda: self.plot_aktywnosc_uzytkownika(user_id))
        file_menu.add_cascade(label="Wydruk", menu=print_out_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=message_app.destroy)

        help_menu = Menu(menu_bar, tearoff=False)
        help_menu.add_command(label="#### Under Construction #####")
        help_menu.add_command(label='Q&A')
        help_menu.add_command(label='Help.txt')
        help_menu.add_command(label="#### Under Construction #####")

        menu_bar.add_cascade(label="Opcje", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        message_app.tkraise()
        message_app.mainloop()

    def sell_karnety(self):

        decision = self.window_maker()

        label_info = ct.CTkLabel(decision, text="Sprzedaż karnetów", text_font=("Bold", 16))
        label_imie = ct.CTkLabel(decision, text="Imię")

        entry_box_imie_sell = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                          corner_radius=2, border_color="#26B9EF", border_width=2)

        label_nazwisko = ct.CTkLabel(decision, text="Nazwisko")

        entry_box_nazwisko_sell = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                              corner_radius=2, border_color="#26B9EF", border_width=2)

        button_submit = ct.CTkButton(decision,
                                     text="Dalej",
                                     fg_color=self.btn_submit_fg_color,
                                     corner_radius=self.btn_submit_corner_rad,
                                     border_width=self.btn_submit_bor_width,
                                     border_color=self.btn_submit_bor_color,
                                     hover_color=self.btn_submit_hov_color,
                                     command=lambda: self.sell_karnety_operacja(decision, entry_box_imie_sell.get(),
                                                                                entry_box_nazwisko_sell.get()))

        self.label_wynik_sell = ct.CTkLabel(decision, text="", text_font=("Bold", 14))

        label_info.pack(side="top", pady=15)
        label_imie.pack(side="top")
        entry_box_imie_sell.pack(side="top")
        label_nazwisko.pack(side="top")
        entry_box_nazwisko_sell.pack(side="top")
        button_submit.pack(side="top", pady=25)
        self.label_wynik_sell.pack(side="top", pady=25)

        decision.tkraise()
        decision.mainloop()

    def sell_karnety_operacja(self, frame, imie, nazwisko):
        imie = imie
        nazwisko = nazwisko

        if self.id_finder(imie, nazwisko):
            frame.withdraw()
            self.sell_karnety_2(imie, nazwisko)
            return True
        else:
            self.label_wynik_sell.configure(text="Brak takiej osoby", text_color="red")
            return False

    def sell_karnety_2(self, imie, nazwisko):

        imie = imie
        nazwisko = nazwisko

        decision = self.window_maker()

        label_info = ct.CTkLabel(decision, text="Wybierz płeć", text_font=("Bold", 16))

        label_info_2 = ct.CTkLabel(decision, text=f"Imię: {imie}"
                                                  f"\nNazwisko: {nazwisko}")

        sex = ["Mężczyzna", "Kobieta"]

        cbox_sex = ct.CTkComboBox(decision,
                                  values=sex,
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
        cbox_sex.set(sex[0])

        button_wybierz = ct.CTkButton(decision,
                                      text="Dalej",
                                      fg_color=self.btn_submit_fg_color,
                                      corner_radius=self.btn_submit_corner_rad,
                                      border_width=self.btn_submit_bor_width,
                                      border_color=self.btn_submit_bor_color,
                                      hover_color=self.btn_submit_hov_color,
                                      command=lambda: self.sell_karnety_operacja_2(decision, imie, nazwisko,
                                                                                   cbox_sex.get())
                                      )

        # Dodać przycisk do cofania
        # Dodać powyżej dane imie, naziwsko które zostały podane wcześniej albo podsumować na końcu

        label_info.pack(side="top", pady=15)
        label_info_2.pack(side="top", pady=10)
        cbox_sex.pack(side="top")
        button_wybierz.pack(side="top", pady=25)

        decision.tkraise()
        decision.mainloop()

    def sell_karnety_operacja_2(self, frame, imie, nazwisko, plec=None, back=False):
        imie = imie
        nazwisko = nazwisko
        plec = plec

        if back and plec is None:
            frame.withdraw()
            self.sell_karnety()
        else:
            frame.withdraw()
            self.sell_karnety_3(imie, nazwisko, plec)

    def sell_karnety_3(self, imie, nazwisko, plec):

        imie = imie
        nazwisko = nazwisko
        plec = plec

        decision = self.window_maker()

        label_info = ct.CTkLabel(decision, text="Wybierz typ karnetu", text_font=("Bold", 16))

        label_info_2 = ct.CTkLabel(decision, text=f"Imię: {imie}"
                                                  f"\nNazwisko: {nazwisko}"
                                                  f"\nPłeć: {plec}")

        karnety_men = {"1 Wejście": [1, "30zł"],
                       "4 Wejścia": [4, "100zł"],
                       "8 Wejść": [8, "140zł"],
                       "15 Wejść": [15, "160zł"],
                       "Dzieci 4-7 lat": [999, "120zł"],
                       "Dzieci 8-15 lat": [999, "130zł"],
                       "Open": [999, "220zł"]}

        karnety_women = {"1 Wejście": [1, "30zł"],
                         "4 Wejścia": [4, "100zł"],
                         "8 Wejść": [8, "120zł"],
                         "15 Wejść": [15, "140zł"],
                         "Dzieci 4-7 lat": [999, "120zł"],
                         "Dzieci 8-15 lat": [999, "130zł"],
                         "Open": [999, "200zł"]}

        if plec == "Mężczyzna":
            karnet = karnety_men
        else:
            karnet = karnety_women

        karnet_output = list(karnet.keys())

        ceny = list(karnet.values())
        ceny_output = []
        for i in ceny:
            ceny_output.append(i[1])

        karnet_options = []
        for i in range(len(karnet_output)):
            karnet_options.append(karnet_output[i] + " - " + ceny_output[i])

        cbox_karnet = ct.CTkComboBox(decision,
                                     values=karnet_options,
                                     state="readonly",
                                     width=160,
                                     height=30,
                                     fg_color="#F9F9F9",
                                     dropdown_color="#F9F9F9",
                                     corner_radius=5,
                                     button_color="#26B9EF",
                                     border_width=2,
                                     border_color="#26B9EF"
                                     )
        cbox_karnet.set(karnet_options[0])

        button_wybierz = ct.CTkButton(decision,
                                      text="Dalej",
                                      fg_color=self.btn_submit_fg_color,
                                      corner_radius=self.btn_submit_corner_rad,
                                      border_width=self.btn_submit_bor_width,
                                      border_color=self.btn_submit_bor_color,
                                      hover_color=self.btn_submit_hov_color,
                                      command=lambda: self.sell_karnety_operacja_3(decision, imie, nazwisko, plec,
                                                                                   cbox_karnet.get(), karnet
                                                                                   )
                                      )

        # Dodać przycisk do cofania
        # Dodać powyżej dane imie, naziwsko które zostały podane wcześniej albo podsumować na końcu

        label_info.pack(side="top", pady=15)
        label_info_2.pack(side="top", pady=10)
        cbox_karnet.pack(side="top")
        button_wybierz.pack(side="top", pady=25)

        decision.tkraise()
        decision.mainloop()

    def sell_karnety_operacja_3(self, frame, imie, nazwisko, plec, wybor, karnety, back=False):
        user_id = self.id_finder(imie, nazwisko)
        typ = wybor.split("-")[0].strip()
        amount = karnety.get(typ)[0]

        # Działa
        self.ticket_sell(user_id, typ, amount, plec)

        # Dodać jakieś ostrzeżenie czy zatwierdasz dane + powiadomienie że wszystko się udało
        # oraz powrót do głównego menu

        frame.withdraw()  # Zamknicie okna sprzedaży
        self.sell_karnety_4()

    def sell_karnety_4(self):

        decision = self.window_maker(size="200x200")

        label_info = ct.CTkLabel(decision, text="Karnet Sprzedany !", text_font=("Bold", 16))

        button_choice = ct.CTkButton(decision,
                                     text="Dalej",
                                     fg_color=self.btn_submit_fg_color,
                                     corner_radius=self.btn_submit_corner_rad,
                                     border_width=self.btn_submit_bor_width,
                                     border_color=self.btn_submit_bor_color,
                                     hover_color=self.btn_submit_hov_color,
                                     command=lambda: decision.withdraw()
                                     )

        label_info.pack(side="top", pady=15)
        button_choice.pack(side="top", pady=25)

        decision.tkraise()
        decision.mainloop()

    def window_maker(self, size="400x400", title=settings.title_main, resizable=False, bg="white"):
        window = tk.Toplevel()
        window.title(title)
        window.geometry(size)
        window.resizable(width=resizable, height=resizable)
        window.config(bg=bg)
        main_logo = tk.PhotoImage(file="./icons/logo.png")
        window.wm_iconphoto(False, main_logo)

        return window

    def person_remove(self):

        decision = self.window_maker()

        label_info = ct.CTkLabel(decision, text="Usuwanie Danych", text_font=("Bold", 16))

        label_info_2 = ct.CTkLabel(decision, text="Usunięcie spowoduje zwolnienie id")

        label_imie = ct.CTkLabel(decision, text="Imię")

        entry_box_imie_sell = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                          corner_radius=2, border_color="#26B9EF", border_width=2)

        label_nazwisko = ct.CTkLabel(decision, text="Nazwisko")

        entry_box_nazwisko_sell = ct.CTkEntry(decision, width=140, height=30, fg_color="#F9F9F9",
                                              corner_radius=2, border_color="#26B9EF", border_width=2)

        # Zmienić kolory (np. na czerwony)
        button_wybierz = ct.CTkButton(decision,
                                      text="Usuń",
                                      fg_color=self.btn_submit_fg_color,
                                      corner_radius=self.btn_submit_corner_rad,
                                      border_width=self.btn_submit_bor_width,
                                      border_color=self.btn_submit_bor_color,
                                      hover_color=self.btn_submit_hov_color,
                                      command=lambda: self.remove_operation()
                                      )

        self.label_remove_result = ct.CTkLabel(decision, text="")

        label_info.pack(side="top", pady=15)
        label_info_2.pack(side="top", pady=10)
        label_imie.pack(side="top")
        entry_box_imie_sell.pack(side="top")
        label_nazwisko.pack(side="top")
        entry_box_nazwisko_sell.pack(side="top")
        button_wybierz.pack(side="top", pady=25)
        self.label_remove_result.pack(side="top")

        decision.tkraise()
        decision.mainloop()

    def remove_operation(self):
        pass
        # Tutaj Sprawdzamy czy taka osoba jest w bazie + zwracamy informacje czy udało się
        # usunąc dane tej osoby (zwolnić id) czy też takiej osoby już tam nie ma


        # frame.withdraw()  # Zamknicie okna sprzedaży
