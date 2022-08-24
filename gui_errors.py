import tkinter as tk
import basic_setup as settings


def error_app(mess="", size="450x100", off=False):
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
