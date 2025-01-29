import questions_provider
from capitals_scraper import get_list_of_capitals_and_countries
from oscars_scrapers import get_golden_globe_winners
from elements_scraper import get_elements
import leaderboard
import check_answer
import graphics
import random
from colorama import Fore, Style

NUMBER_OF_JOKERS = 2
REQUIRED_CORRECT_ANSWERS = 10

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
    print(f"\nWelcome to the game, {player_name}!\n\nLet's start!\n\n")

    print("#####################################")
    print("Loading list.")
    print("Please wait...")
    capitals_dicts = get_list_of_capitals_and_countries()
    elements_dict = get_elements()
    oscars_dict = get_golden_globe_winners()
    list_of_dicts = (capitals_dicts, elements_dict, oscars_dict)
    print("Loaded!")
    print("#####################################")

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
