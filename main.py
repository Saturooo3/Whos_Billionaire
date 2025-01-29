import questions_provider
from capitals_scraper import get_list_of_capitals_and_countries
from oscars_scrapers import get_golden_globe_winners
from elements_scraper import get_elements
import leaderboard
import check_answer
import graphics
import random
from colorama import Fore, Style
from multiprocessing import Process, Manager



NUMBER_OF_JOKERS = 2
REQUIRED_CORRECT_ANSWERS = 10


def generate_capitals_dict(shared_dict):
    shared_dict["capitals"] = get_list_of_capitals_and_countries()


def generate_elements_dict(shared_dict):
    shared_dict["elements"] = get_elements()


def generate_oscars_dict(shared_dict):
    shared_dict["oscars"] = get_golden_globe_winners()


def show_winner_screen(jokers, price, player_name):
    if jokers == NUMBER_OF_JOKERS:
        print(graphics.win_as_billionaire())
        leaderboard.update_leaderboard(player_name, 1000000000)
    else:
        print(graphics.you_win())
        leaderboard.update_leaderboard(player_name, price)

    leaderboard.display_leaderboard()

def main():
    # Testing the Splash
    graphics.game_splash()

    """
    prints answer options, asks user to choose and reacts to the choice
    """
    jokers = NUMBER_OF_JOKERS
    price = 0
    round = 0
    game_ended = False
    player_name = ""

    player_name = input("Please add your name: ").strip()
    print(f"\nWelcome to the game, {player_name}!\n\nLet's start!\n")

    print("#####################################")
    print("Loading list.")
    print("Please wait...")

    with Manager() as manager:
        shared_dict = manager.dict()

        capitals_process = Process(target=generate_capitals_dict, args=(shared_dict,))
        elements_process = Process(target=generate_elements_dict, args=(shared_dict,))
        oscars_process = Process(target=generate_oscars_dict, args=(shared_dict,))

        capitals_process.start()
        elements_process.start()
        oscars_process.start()

        capitals_process.join()
        elements_process.join()
        oscars_process.join()

        capitals_dicts = shared_dict["capitals"]
        elements_dict = shared_dict["elements"]
        oscars_dict = shared_dict["oscars"]

    print("Loaded!")
    print("#####################################")

    list_of_dicts = (capitals_dicts, elements_dict, oscars_dict)

    asked_questions = []

    while round <= REQUIRED_CORRECT_ANSWERS and not game_ended:
        rand_dict = random.choice(list_of_dicts)
        rand_key, value_of_rand_key, answer_options = questions_provider.create_dict_for_answer_options(
            rand_dict, asked_questions, jokers)

        print(graphics.display_hangman(round))

        if rand_key in capitals_dicts:
            print(f"Which country is {rand_key} the capital of?")
        elif rand_key in elements_dict:
            print(f"What element is {rand_key}?")
        elif rand_key in oscars_dict:
            print(f"Which film won the golden globe in {rand_key}?")

        for index, answer in answer_options.items():
            print(f"{index}: {answer}")

        while True:
            if jokers > 0 :
                user_choice = input("\nEnter your answer (A, B, C, D, E): ").upper()
            else:
                user_choice = input("\nEnter your answer (A, B, C, D): ").upper()

            if check_answer.is_user_choice_valid(user_choice, jokers):
                jokers, price, round, game_ended = check_answer.check_answer(answer_options[user_choice],
                                                                             value_of_rand_key, jokers, price,
                                                                             round, game_ended, player_name)
                asked_questions.append(rand_dict[rand_key])
                break
            else:
                if jokers > 0:
                    print(Fore.LIGHTYELLOW_EX + "\nValid choice: A, B, C, D, E" + Style.RESET_ALL)
                else:
                    print(Fore.LIGHTYELLOW_EX + "\nValid choice: A, B, C, D" + Style.RESET_ALL)


    if round == REQUIRED_CORRECT_ANSWERS:
        show_winner_screen(jokers, price, player_name)


if __name__ == "__main__":
    main()
