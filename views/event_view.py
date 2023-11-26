from utils.event import UtilsEvent
# from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text


class EventView:

    def __init__(self):
        self.utils = UtilsEvent

    def add_event(self, token, contracts, supports):
        print("Dans la vue de création d'un événement")
        console = Console()
        new_event_add = {}
        create_entry = True
        start = "du début"
        end = "de fin"
        event_title = self.utils.display_menu_event_title(self)
        # contract_id
        contract_id = self.utils.display_menu_choice_contrat_id(self, contracts)
        while create_entry:
            # if pour controler des dates de début et date de fin
            start_date = self.utils.display_menu_date(self, start)
            end_date = self.utils.display_menu_date(self, end)
            if start_date > end_date:
                text = (Text("La date de fin est supérieur à la date de début", style="red"))
                console.print(text)
                text = (Text("Veuillez resaisir les dates ", style="red"))
                console.print(text)
            else:
                create_entry = False
        # location
        location = self.utils.display_menu_location(self)
        # attendees
        attendees = self.utils.display_menu_attendees(self)
        # notes
        notes = self.utils.display_menu_notes(self)
        # support_id
        support_id = self.utils.display_menu_choice_support_id(self, supports)

        choice_user = self.utils.display_menu_event_choice_save(self)

        create_entry = False
        if choice_user == "o":
            new_event_add = {
                "event_title": str(event_title),
                "start_date": start_date,
                "end_date": end_date,
                "location": str(location),
                "attendees": int(attendees),
                "notes": str(notes),
                "contract_id": int(contract_id),
                "support_id": int(support_id),
            }
            return new_event_add
        elif choice_user == "n":
            return -1
