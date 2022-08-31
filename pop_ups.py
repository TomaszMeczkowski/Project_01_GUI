import tkinter as tk
from tkinter import ttk
import basic_setup as settings
from database import DataBase


class PopUps(DataBase):

    def __init__(self, user, password):
        DataBase.__init__(self, user, password)

    def confirm_adding_people(self, *args):
        imie = args[0]
        nazwisko = args[1]
        pas = args[2]
        belki = args[3]

        decision = tk.Toplevel()
        decision.title(settings.title_main)
        decision.geometry("300x250")
        decision.resizable(width=False, height=False)
        decision.config(bg="grey")

        label2 = tk.Label(decision, text=f"Przekazane Parametry"
                                         f"\n"
                                         f"\nImie: {imie}"
                                         f"\nNazwisko: {nazwisko}"
                                         f"\nPas: {pas}"
                                         f"\nBelki: {belki}",
                          font=16)
        label2.place(x=60, y=20)

        label1 = tk.Label(decision, text="Zatwierdzić", bg="grey", font=16)
        label1.place(x=100, y=150)

        button1 = tk.Button(decision,
                            command=lambda: [decision.destroy(),
                                             self.error_info(off=True) if
                                             self.dodawanie_osob(imie, nazwisko, pas, belki) else
                                             self.error_info(mess="Error 1: Taka osoba już się znajduję w bazie danych")
                                             ],
                            text="Tak", font=16, bg="green")

        button1.place(x=95, y=180)

        button2 = tk.Button(decision, command=lambda: decision.destroy(), text="Nie", font=16, bg="red")
        button2.place(x=150, y=180)

        decision.tkraise()
        decision.mainloop()

    def error_info(self, mess="", size="450x100", off=False):
        if off:
            return None

        message_app = tk.Toplevel()
        message_app.title(settings.title_main)
        message_app.geometry(size)
        message_app.resizable(width=False, height=False)
        message_app.config(bg="grey")

        label = tk.Label(message_app, text=mess, fg="red", font=('Helvetica', 12, 'bold'))
        label.pack(pady=5)

        button = tk.Button(message_app, command=lambda: [message_app.quit(),
                                                         message_app.destroy()
                                                         ], text="Dalej")
        button.pack(side="bottom", pady=5)

        message_app.tkraise()
        message_app.mainloop()

    def confirm_db_reset(self):

        decision = tk.Toplevel()
        decision.title(settings.title_main)
        decision.geometry("270x150")
        decision.resizable(width=False, height=False)
        decision.config(bg="grey")

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

    def list_of_people(self, mess="", size="450x550", off=False):
        if off:
            return None

        message_app = tk.Toplevel()
        message_app.title(settings.title_main)
        message_app.geometry(size)
        message_app.resizable(width=False, height=True)
        message_app.config(bg="white")

        text = self.show_all_people()

        scrol_bar = tk.Scrollbar(message_app)
        scrol_bar.pack(side="right", fill="y")

        tree_view = ttk.Treeview(message_app, yscrollcommand=scrol_bar.set, height=25)
        tree_view.pack(side="left", padx=25)

        scrol_bar.config(command=tree_view.yview)

        # Kolumny tabeli
        col = ("1", "2", "3", "4", "5")
        col_names = ["id", "Imię", "Nazwisko", "Pas", "Belki"]
        col_width = [25, 60, 100, 100, 80]
        tree_view['columns'] = col

        tree_view.column("#0", width=0, stretch=False)

        for i in range(len(col)):
            tree_view.column(f"{col[i]}", width=col_width[i], anchor="center")

        # Nagłówki kolumn
        tree_view.heading("#0", text="", anchor='center')

        for i in range(len(col)):
            tree_view.heading(f"{col[i]}", text=f"{col_names[i]}", anchor="center")

        for i in text:
            tree_view.insert(parent="", index="end", text="", values=i)

        message_app.tkraise()
        message_app.mainloop()
