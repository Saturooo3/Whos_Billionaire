import questions_provider
from capitals_scraper import get_list_of_capitals_and_countries
from oscars_scraper import get_golden_globe_winners
from elements_scraper import get_elements
import check_answer
import graphics
import random
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


    capitals_dicts = get_list_of_capitals_and_countries()
    elements_dict = get_elements()
    oscars_dict = get_golden_globe_winners()
    list_of_dicts = (capitals_dicts, elements_dict, oscars_dict)

    asked_questions = []

    while round <= 10 and not game_ended:
        rand_dict = random.choice(list_of_dicts)
        rand_key, value_of_rand_key, answer_options = questions_provider.create_dict_for_answer_options(
            rand_dict, asked_questions)

        print(graphics.display_hangman(round))

        if rand_key in capitals_dicts:
            print(f"Which country is {rand_key} the capital of?")
        elif rand_key in elements_dict:
            print(f"What element is {rand_key} ?")
        elif rand_key in oscars_dict:
            print(f"Who won the oscar in {rand_key}")

        for index, answer in answer_options.items():
            print(f"{index}: {answer}")

        while True:
            user_choice = input("\nEnter your answer (A, B, C, D, E): ").upper()
            if check_answer.is_user_choice_valid(user_choice):
                jokers, price, round, game_ended = check_answer.check_answer(answer_options[user_choice],
                                                                             value_of_rand_key, jokers, price,
                                                                             round, game_ended)
                asked_questions.append(rand_dict[rand_key])
                break
            else:
                print(Fore.LIGHTYELLOW_EX + "\nValid choice: A, B, C ,D, E" + Style.RESET_ALL)

        print("jokers", jokers)
        print("price", price)
        print("round", round)


if __name__ == "__main__":
    main()