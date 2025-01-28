import questions_provider
import capitals_scraper
import check_answer
import graphics
from colorama import Fore, Style


def main():
    # Testing the Splash
    graphics.game_splash()

    """
    prints answer options, asks user to choose and reacts to the choice
    """
    jokers = 2
    price = 0
    round = 0
    game_ended = False

    capital_of_country_dict = capitals_scraper.get_list_of_capitals_and_countries()
    asked_questions = []

    while round <= 10 and not game_ended:

        rand_country, capital, answer_options = questions_provider.create_dict_for_answer_options(
            capital_of_country_dict, asked_questions)

        print(graphics.display_hangman(round))
        print(f"In what country is this city: {rand_country}?")

        for index, answer in answer_options.items():
            print(f"{index}: {answer}")

        while True:
            user_choice = input("\nEnter your answer (A, B, C, D, E): ").upper()
            if check_answer.is_user_choice_valid(user_choice):
                jokers, price, round, game_ended = check_answer.check_answer(answer_options[user_choice], capital,
                                                                             jokers, price, round, game_ended)
                asked_questions.append(capital_of_country_dict[rand_country])
                break
            else:
                print(Fore.LIGHTYELLOW_EX + "\nValid choice: A, B, C ,D, E" + Style.RESET_ALL)

        print("jokers", jokers)
        print("price", price)
        print("round", round)


if __name__ == "__main__":
    main()

    # Spielername abfragen
    player_name = input("Bitte gib deinen Namen ein: ").strip()
    print(f"Willkommen im Spiel, {player_name}!")

LEADERBOARD_FILE = "leaderboard.txt"


def load_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = []
            for line in file.readlines():
                name, score = line.strip().split(" - ")
                leaderboard.append({"name": name, "score": int(score)})
            return leaderboard
    except FileNotFoundError:
        return []


def save_leaderboard(leaderboard):
    with open("leaderboard.txt", "w") as file:
        for entry in leaderboard:
            file.write(f"{entry['name']} - {entry['score']}\n")


def update_leaderboard(player_name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({"name": player_name, "score": score})
    leaderboard.sort(key=lambda x: x['score'], reverse=True)  # Sortiere nach Punktzahl absteigend
    save_leaderboard(leaderboard)


def display_leaderboard():
    leaderboard = load_leaderboard()
    print("\n=== Leaderboard ===")
    for idx, entry in enumerate(leaderboard, 1):
        print(f"{idx}. {entry['name']} - {entry['score']}")
    print("====================\n")

    # Update Leaderboard
    update_leaderboard(player_name, price)

    # Leaderboard anzeigen
    display_leaderboard()