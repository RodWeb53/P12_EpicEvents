import datetime
from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text
from rich.table import Table


class UtilsEvent:

    def __init__(self):
        pass

    def display_menu_event_title(self):
        """Demande du nom de l'événement"""
        console = Console()
        print("")
        text = (Text("Entrez le titre de l'événement :", style="blue"))
        console.print(text)
        event_title = Prompt.ask("Votre saisie >> ")

        while not event_title or len(event_title) > 255:
            text = (Text("Le titre ne peut être vide ou supérieur à 255 caractères", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau un titre :", style="red"))
            console.print(text)
            event_title = Prompt.ask("Votre nouvelle saisie >> ")
        return event_title

    def display_menu_date(self, status):
        """Demande de la date et l'heure de début ou fin de l'événement"""
        current_date = datetime.datetime.today()
        current_year = current_date.year
        console = Console()
        print("")

        # Saisie de l'année et les contrôles
        text = (Text(f"Entrez l'année {status} de l'événement' :", style="blue"))
        console.print(text)
        year = Prompt.ask("Votre saisie >> ")
        create_entry_year = True
        while create_entry_year:
            if year.isnumeric():
                if int(year) < current_year:
                    text = (Text("L'année ne peut être inférieur à l'année en cours", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau une année :", style="red"))
                    console.print(text)
                    year = Prompt.ask("Votre nouvelle saisie >> ")
                elif int(year) >= (current_year + 10):
                    text = (Text("L'année ne peut être supérieur aux 10 prochaines années", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau une année :", style="red"))
                    console.print(text)
                    year = Prompt.ask("Votre nouvelle saisie >> ")
                else:
                    create_entry_year = False
            else:
                text = (Text("La valeur saisie n'est pas un chiffre ou est vide ", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau une année :", style="red"))
                console.print(text)
                year = Prompt.ask("Votre nouvelle saisie >> ")

        # Saisie du mois et les contrôles
        text = (Text(f"Entrez le mois {status} de l'événement' :", style="blue"))
        console.print(text)
        month = Prompt.ask("Votre saisie >> ")
        create_entry_month = True
        while create_entry_month:
            if month.isnumeric():
                if int(month) <= 0 or int(month) >= 13:
                    text = (Text("Le mois doit être compris entre 1 et 12", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau un mois :", style="red"))
                    console.print(text)
                    month = Prompt.ask("Votre nouvelle saisie >> ")
                else:
                    create_entry_month = False
            else:
                text = (Text("La valeur saisie n'est pas un chiffre ou est vide ", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un mois :", style="red"))
                console.print(text)
                month = Prompt.ask("Votre nouvelle saisie >> ")

        # Saisie du jour et les contrôles
        text = (Text(f"Entrez le jour {status} de l'événement' :", style="blue"))
        console.print(text)
        day = Prompt.ask("Votre saisie >> ")
        create_entry_day = True
        while create_entry_day:
            if day.isnumeric():
                if int(day) <= 0 or int(day) >= 32:
                    text = (Text("Le jour doit être compris entre 1 et 31", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau un jour :", style="red"))
                    console.print(text)
                    day = Prompt.ask("Votre nouvelle saisie >> ")
                else:
                    create_entry_day = False
            else:
                text = (Text("La valeur saisie n'est pas un chiffre ou est vide ", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un jour :", style="red"))
                console.print(text)
                day = Prompt.ask("Votre nouvelle saisie >> ")

        # Saisie de l'heure et les contrôles
        text = (Text(f"Entrez l'heure {status} de l'événement' :", style="blue"))
        console.print(text)
        hour = Prompt.ask("Votre saisie >> ")
        create_entry_hour = True
        while create_entry_hour:
            if hour.isnumeric():
                if int(hour) < 00 or int(hour) >= 24:
                    text = (Text("L'heure doit être comprise entre 0 et 23", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau une heure :", style="red"))
                    console.print(text)
                    hour = Prompt.ask("Votre nouvelle saisie >> ")
                else:
                    create_entry_hour = False
            else:
                text = (Text("La valeur saisie n'est pas un chiffre ou est vide ", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau une heure :", style="red"))
                console.print(text)
                hour = Prompt.ask("Votre nouvelle saisie >> ")

        # Saisie des minutes et les contrôles
        text = (Text(f"Entrez les minutes {status} de l'événement' :", style="blue"))
        console.print(text)
        minute = Prompt.ask("Votre saisie >> ")
        create_entry_minute = True
        while create_entry_minute:
            if minute.isnumeric():
                if int(minute) < 00 or int(minute) >= 59:
                    text = (Text("Les minutes doivent être comprises entre 0 et 59", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau les minutes :", style="red"))
                    console.print(text)
                    minute = Prompt.ask("Votre nouvelle saisie >> ")
                else:
                    create_entry_minute = False
            else:
                text = (Text("La valeur saisie n'est pas un chiffre ou est vide ", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau les minutes :", style="red"))
                console.print(text)
                minute = Prompt.ask("Votre nouvelle saisie >> ")
        second = 00
        date_return = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), second)

        if date_return < current_date:
            text = (Text("La date saisie est inférieur à la date du jour ", style="red"))
            console.print(text)
            text = (Text("Veuillez resaisir une nouvelle date ", style="red"))
            console.print(text)
            return UtilsEvent.display_menu_start_date(self)

        return date_return

    def display_menu_location(self):
        """Demande de saisir l'adresse de l'événement"""
        console = Console()
        print("")
        text = (Text("Entrez l'adresse de l'événement' :", style="blue"))
        console.print(text)
        location = Prompt.ask("Votre saisie >> ")

        while not location or len(location) > 255:
            text = (Text("Le titre ne peut être vide ou supérieur à 255 caractères", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau une adresse :", style="red"))
            console.print(text)
            location = Prompt.ask("Votre nouvelle saisie >> ")
        return location

    def display_menu_attendees(self):
        """Demande du nombres de personnes attendues"""
        console = Console()
        print("")
        text = (Text("Entrez le nombre de personnes attendues à l'événement :", style="blue"))
        console.print(text)
        attendees = Prompt.ask("Votre saisie >> ")
        while not (attendees.isnumeric()):
            text = (Text("Le nombre de personne ne peut contenir de lettre ou être vide ", style="red"))
            console.print(text)
            text = (Text("Entrez de nouveau le nombre de personnes attendues à l'événement :", style="red"))
            console.print(text)
            attendees = Prompt.ask("Votre nouvelle saisie >> ")

        return attendees

    def display_menu_notes(self):
        """Demande pour ajouter des notes"""
        console = Console()
        print("")
        text = (Text("Entrez vos commentaires (ligne vide pour sortir)\n", style="blue"))
        console.print(text)
        notes = ""
        create_entry = True
        while create_entry:
            note = Prompt.ask("Votre saisie >> ")
            if not note == "":
                notes += note + "\n"
            else:
                create_entry = False
        return notes

    def display_menu_choice_contrat_id(self, contracts):
        """Demande et vérification du N° de contrat dans la BD"""
        list_contratcs = []
        console = Console()
        print("")
        text = (Text("Entrez le N° du contrat :", style="blue"))
        console.print(text)
        contract_id = Prompt.ask("Votre saisie >> ")
        for contract in contracts:
            list_contratcs.append(contract.contract_id)
        create_entry = True

        while create_entry:
            if contract_id.isnumeric():
                if int(contract_id) in list_contratcs:
                    create_entry = False
                    return contract_id
                else:
                    text = (Text("Le numéro du contrat saisie n'est pas connue dans la base de données ", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau un numéro :", style="red"))
                    console.print(text)
                    contract_id = Prompt.ask("Votre nouvelle saisie >> ")
            else:
                text = (Text("Le numéro du contrat saisie n'est pas un chiffre ", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un numéro :", style="red"))
                console.print(text)
                contract_id = Prompt.ask("Votre nouvelle saisie >> ")

    def display_menu_choice_support_id(self, supports):
        """Demande du nom de la personne du support"""
        list_supports = []
        table = Table(title="Liste des utilisateurs support", width=80, style="blue", show_lines=True)

        table.add_column("N°", style="cyan", width=10, justify="center")
        table.add_column("Nom", style="cyan", width=40)
        table.add_column("Prénom", style="cyan", width=40)

        for user in supports:
            list_supports.append(user.id)
            table.add_row(f"{user.id}", f"{user.last_name}", f"{user.first_name}")

        console = Console()
        console.print(table)

        print("")
        text = (Text("Entrez le N° d'employé à affecter' :", style="blue"))
        console.print(text)
        support_id = Prompt.ask("Votre saisie >> ")
        create_entry = True
        while create_entry:
            if support_id.isnumeric():
                if int(support_id) in list_supports:
                    create_entry = False
                    return support_id
                else:
                    text = (Text("Le numéro d'employé saisie n'est pas connue dans la base de données ", style="red"))
                    console.print(text)
                    text = (Text("Entrez de nouveau un numéro :", style="red"))
                    console.print(text)
                    support_id = Prompt.ask("Votre nouvelle saisie >> ")
            else:
                text = (Text("Le numéro d'employé saisie n'est pas un chiffre ", style="red"))
                console.print(text)
                text = (Text("Entrez de nouveau un numéro :", style="red"))
                console.print(text)
                support_id = Prompt.ask("Votre nouvelle saisie >> ")

    def display_menu_event_choice_save(self):
        """Vérification si l'utilisateur veut enregistrer le nouveau contrat'"""
        console = Console()
        verify = True
        while verify:
            print("")
            text = (Text("Confirmez la création du nouvel événement : \n", style="blue"))
            console.print(text)
            text = (Text("   o / n \n", style="red"))
            console.print(text)
            user_choice_save = input("Votre confirmation >>  ")
            if user_choice_save == "o" or user_choice_save == "n":
                verify = False

        return user_choice_save
