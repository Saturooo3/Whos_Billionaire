import random
from colorama import Fore, Style


def create_wrong_capitals(capital_of_country_dict) -> list:
    """
    takes a dict of capital cities and returns a list with capital and
    a list of a country, the capital and a list of 3 wrong capital cities
    """
    rand_country = random.choice(list(capital_of_country_dict.keys()))
    capital: str = capital_of_country_dict[rand_country]
    wrong_capitals_list: list = []
    num_of_wrong_capitals: int = 0
    for wrong_capital in capital_of_country_dict.values():
        if wrong_capital != capital and num_of_wrong_capitals < 3:
            wrong_capitals_list.append(wrong_capital)
            num_of_wrong_capitals += 1
    return [rand_country, capital, wrong_capitals_list]


def create_dict_for_answer_options(capital_of_country_dict) -> list:
    """
    takes a dict of capital cities and returns a dict of 4 capital cities
    """
    answer_options: dict = {}
    rand_country, capital, wrong_capital_list = create_wrong_capitals(capital_of_country_dict)
    answer_options_capitals: list = wrong_capital_list.copy()
    answer_options_capitals.append(capital)
    random.shuffle(answer_options_capitals)
    keys: list = ["A", "B", "C", "D"]
    for key, city in zip(keys, answer_options_capitals):
        answer_options[key] = city
    return [rand_country, capital, answer_options]


def check_answer():
    """
    prints answer options, asks user to choose and reacts to the choice
    """
    capital_of_country_dict: dict = {"Germany": "Berlin", "England": "London", "France": "Paris",
                                     "United Arab Emirates": "Abu Dhabi", "Türkiye": "Ankara"}
    rand_country, capital, answer_options = create_dict_for_answer_options(capital_of_country_dict)
    print(f"What is the capital of {rand_country}?")
    for index, answer in answer_options.items():
        print(f"{index}: {answer}")
    while True:
        try:
            user_choice = input("\nEnter your answer (A, B, C, D): ").upper()
            if capital == answer_options[user_choice]:
                print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            else:
                print(Fore.RED + "You're wrong!" + Style.RESET_ALL)
            break
        except KeyError:
            print("Expected: A, B, C ,D")
            continue


def main():
    check_answer()


if __name__ == "__main__":
    main()
