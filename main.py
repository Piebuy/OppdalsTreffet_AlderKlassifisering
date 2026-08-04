from time import sleep, time
from services import *
from auth_services import *
from authenticate import main as authenticate

def main():

    ratelimit = 1  # seconds
    rate_limit_last_calls = [time()-time(),time()-time()]
    current_year = datetime.now().year

    login = False

    classified_participants = get_classified_participants("Resultat/deltakere_kategorisert.xlsx")
    participants = get_participant_from_excel("Data/deltakere.xlsx")

    new_list = get_new_participants(classified_participants,participants)


    while not login:
        login, username = authenticate()


    session,r = get_session(username) #type: ignore


    option = update_options()
    
    if option == "2":
        classified_participants = []
        new_list = participants
        
        
    print()
    for i, participant in enumerate(new_list):
        print(f"Processing participant {i+1}/{len(new_list)}")
        licens_number = participant[0]

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

    result = classified_participants + new_list
    
    save_participants_to_excel(result, "Resultat/deltakere_kategorisert.xlsx")
        


if __name__ == "__main__":
    main()