import random
from colorama import Fore, Style
import capitals_scraper

def create_wrong_capitals(capital_of_country_dict, asked_questions) -> list:
    """
    takes a dict of capital cities and returns a list with capital and
    a list of a country, the capital and a list of 3 wrong capital cities
    """
    rand_country = ""

    while True:
        rand_country = random.choice(list(capital_of_country_dict.keys()))

        if rand_country in asked_questions:
            continue
        else:
            break

    capital: str = capital_of_country_dict[rand_country]
    wrong_capitals_list: list = []
    num_of_wrong_capitals: int = 0
    wrong_answers_list = list(capital_of_country_dict.values())
    random.shuffle(wrong_answers_list)
    for wrong_capital in wrong_answers_list:
        if wrong_capital != capital and num_of_wrong_capitals < 3 and wrong_capital not in wrong_capitals_list:
            wrong_capitals_list.append(wrong_capital)
            num_of_wrong_capitals += 1
    return [rand_country, capital, wrong_capitals_list]


def create_dict_for_answer_options(capital_of_country_dict, asked_questions) -> list:
    """
    takes a dict of capital cities and returns a dict of 4 capital cities
    """
    answer_options: dict = {}
    rand_country, capital, wrong_capital_list = create_wrong_capitals(capital_of_country_dict, asked_questions)
    answer_options_capitals: list = wrong_capital_list.copy()
    answer_options_capitals.append(capital)
    random.shuffle(answer_options_capitals)
    answer_options_capitals.append("SKIP")
    keys: list = ["A", "B", "C", "D", "E"]
    for key, city in zip(keys, answer_options_capitals):
        answer_options[key] = city
    return [rand_country, capital, answer_options]
