import tkinter as tk
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

    def list_of_people(self, mess="", size="600x800", off=False):
        if off:
            return None

        message_app = tk.Toplevel()
        message_app.title(settings.title_main)
        message_app.geometry(size)
        message_app.resizable(width=False, height=False)
        message_app.config(bg="grey")

        master_window = message_app
        text = self.show_all_people()
        counter = 1
        tk.Label(master_window, text="", height=25, width=45).place(x=110, y=120)
        tk.Label(master_window, text="", bg="grey").grid(row=0, column=0, pady=50, padx=50)
        for i in text:
            if i[0] >= 10:
                tk.Label(master_window, text=str(i[0])+".  ",
                         borderwidth=2, relief="solid").grid(row=counter, column=10, sticky="W", pady=2, padx=5)
            elif i[0] >= 100:
                tk.Label(master_window, text=str(i[0]) + ".",
                         borderwidth=2, relief="solid").grid(row=counter, column=10, sticky="W", pady=2, padx=5)
            else:
                tk.Label(master_window, text=str(i[0]) + ".    ",
                         borderwidth=2, relief="solid").grid(row=counter, column=10, sticky="W", pady=2, padx=5)

            tk.Label(master_window, text="  " + str(i[1]) + "  ",
                     borderwidth=2, relief="solid").grid(row=counter, column=11, sticky="W", pady=2, padx=5)
            tk.Label(master_window, text="  " + str(i[2]) + "  ",
                     borderwidth=2, relief="solid").grid(row=counter, column=12, sticky="W", pady=2, padx=5)
            tk.Label(master_window, text="  " + str(i[3]) + "  ",
                     borderwidth=2, relief="solid").grid(row=counter, column=13, sticky="W", pady=2, padx=5)
            tk.Label(master_window, text="  " + str(i[4]) + "  ",
                     borderwidth=2, relief="solid").grid(row=counter, column=14, sticky="W", pady=2, padx=5)
            counter += 1

        # label = tk.Label(message_app, text=mess, fg="red", font=('Helvetica', 12, 'bold'))
        # label.pack(pady=5)
        #
        # button = tk.Button(message_app, command=lambda: [message_app.quit(),
        #                                                  message_app.destroy()
        #                                                  ], text="Dalej")
        # button.pack(side="bottom", pady=5)

        message_app.tkraise()
        message_app.mainloop()
