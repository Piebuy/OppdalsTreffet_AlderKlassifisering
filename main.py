from time import sleep, time
from services import *
from auth_services import *
from authenticate import main as authenticate

#TODO: Add a function that checks if participant already have a classification so we don't have to fetch it again. This will save time and reduce the number of requests to the server.
#       List of classified participants. check if license number is in the list. If not add participant to a new list.
#       Classify the new list and then merge it with the old list. Save the merged list to excel.
#TODO: Option to update entire list or skip participants that are in the classified list

def main():

    ratelimit = 1  # seconds
    rate_limit_last_calls = [time()-time(),time()-time()]
    current_year = datetime.now().year

    login = False

    while not login:
        login, username = authenticate()


    session,r = get_session(username) #type: ignore

    participants = get_participant_from_excel("Data/deltakere.xlsx")

    print()
    for i, participant in enumerate(participants):
        print(f"Processing participant {i+1}/{len(participants)}")
        licens_number = participant[0]
        if licens_number.lower() == "q":
            loop = False
            break

        while time() - rate_limit_last_calls[0] < ratelimit:
            sleep(0.1)
        rate_limit_last_calls[0] = time()
        player_id = get_player_id(licens_number, session) #type: ignore

        
        while time() - rate_limit_last_calls[1] < ratelimit:
            sleep(0.1)
        rate_limit_last_calls[1] = time()
        page = session.get(f"https://data.bowling.no/oppslagsverk/person/?Id={player_id}")

        soup = BeautifulSoup(page.text, "html.parser")
        birthdate, name = find_birthdate_line(soup.get_text())
        classification = get_class(birthdate, current_year) # type: ignore
        participant[2] = classification

    save_participants_to_excel(participants, "Resultat/deltakere_kategorisert.xlsx")
        


if __name__ == "__main__":
    main()