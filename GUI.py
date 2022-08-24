import tkinter as tk
from tkinter.ttk import Combobox


class App:

    def __init__(self):
        self.main_window, self.title_main, self.background_color, self.windows_size = None, None, None, None
        self.windows_width, self.windows_height = None, None

    def basic_setup(self):
        self.title_main = "BJJ_CLUB"
        self.background_color = "black"
        self.windows_size = "1200x800"

        self.windows_width = int(self.windows_size.split("x")[0])
        self.windows_height = int(self.windows_size.split("x")[1])

    def main_page(self):
        self.main_window = tk.Tk()
        self.basic_setup()
        self.main_window.title(self.title_main)
        self.main_window.geometry(self.windows_size)
        self.main_window.resizable(width=False, height=False)

        menu_first_page = self.frame_maker()
        menu_second_page = self.frame_maker()
        menu_third_page = self.frame_maker()
        menu_adding_person = self.frame_maker()

        menu_list = [menu_first_page, menu_second_page, menu_third_page, menu_adding_person]

        for frame in menu_list:
            frame.grid(row=0, column=0, sticky='news')

        self.buttons_main_page(menu_first_page, menu_second_page, menu_third_page)
        self.buttons_client_service(menu_second_page, menu_first_page)
        self.buttons_data_base(menu_third_page, menu_first_page, menu_adding_person)
        self.buttons_menu_adding_person(menu_adding_person, menu_third_page)

        self.menu_adding_person(menu_adding_person)

        menu_first_page.tkraise()

        self.main_window.mainloop()

        return True

    def frame_maker(self):
        return tk.Frame(self.main_window, width=self.windows_width,
                        height=self.windows_height, bg=self.background_color)

    def exit_button(self):
        self.main_window.quit()

    def buttons_main_page(self, master_window, opt1, opt2):
        button1 = tk.Button(master_window, command=lambda: self.frame_changer(opt1), text="1. Obsługa klienta")
        button1.place(x=880, y=50)

        button2 = tk.Button(master_window, command=lambda: self.frame_changer(opt2), text="2. Baza danych")
        button2.place(x=880, y=100)

        button3 = tk.Button(master_window, command="", text="3. Statystyki")
        button3.place(x=880, y=150)

        button4 = tk.Button(master_window, command="", text="6. Dev Tools")
        button4.place(x=880, y=450)

        button5 = tk.Button(master_window, command=self.exit_button, text="0. Wyjście")
        button5.place(x=880, y=500)

    def buttons_client_service(self, master_window, opt1):
        button1 = tk.Button(master_window, command="", text="Here we go")
        button1.place(x=880, y=50)

        button5 = tk.Button(master_window, command=lambda: self.frame_changer(opt1), text="Powrót")
        button5.place(x=880, y=500)

    def buttons_data_base(self, master_window, opt1, opt2):
        button1 = tk.Button(master_window, command=lambda: self.frame_changer(opt2), text="Dodaj nową osobę")
        button1.place(x=880, y=50)

        button2 = tk.Button(master_window, command="", text="Popraw dane osoby")
        button2.place(x=880, y=100)

        button3 = tk.Button(master_window, command="", text="Wyświetl wszystkie osoby")
        button3.place(x=880, y=150)

        button4 = tk.Button(master_window, command="", text="Usuń dane osoby")
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

        self.label_5 = tk.Label(master_window, text="")
        self.label_5.place(x=150, y=350)

        button1 = tk.Button(master_window, command=self.wykonaj, text="Wykonaj")
        button1.place(x=500, y=50)

    def wykonaj(self):
        # Przekazywanie parametrów
        text1 = self.entry_box_1.get()
        text2 = self.entry_box_2.get()
        text3 = self.c1.get()
        text4 = int(self.c2.get())
        self.label_5.configure(text=f"Przekazane Parametry"
                                    f"\n"
                                    f"\nImie: {text1}"
                                    f"\nNazwisko: {text2}"
                                    f"\nPas: {text3}"
                                    f"\nBelki: {text4}",
                               font=16)



    def frame_changer(self, frame):
        frame.tkraise()

