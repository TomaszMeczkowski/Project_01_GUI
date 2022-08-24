import tkinter as tk
import Basic_Setup as Settings


def error_01_person_add():
    # Case: Chcemy dodać osobę do bazy danych ale osoba znajduje się już w bazie
    # Case: We are adding person to database(db) but that person is already in db

    message_app = tk.Tk()
    message_app.title(Settings.title_main)
    message_app.geometry("450x150")
    message_app.resizable(width=False, height=False)
    message_app.config(bg="grey")

    label = tk.Label(message_app, text="Error 1: Taka osoba już się znajduję w bazie danych",
                     fg="red", font=16)
    label.pack(pady=5)

    button = tk.Button(message_app, command=lambda: [message_app.quit(),
                                                     message_app.destroy()
                                                     ], text="Dalej")
    button.pack(side="bottom", pady=5)

    message_app.tkraise()
    message_app.mainloop()


def destroy(master_window):
    master_window.destroy()
