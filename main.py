from gui import App
from mysql.connector import errors
from database import DataBaseTester
from termcolor import colored


if __name__ == "__main__":
    print("\nŁączenie się z bazą danych MySQL, podaj dane dostępowe\n")

    while True:
        user = input("User: ")
        password = input("Password: ")
        try:
            check = DataBaseTester(user, password).inicjowanie_bazy_danych()
            break

        except errors.ProgrammingError:
            print(f"\n{colored('Nieprawidłowe dane dostępowe','red')}\n")

    app = App(user, password).main_page()

