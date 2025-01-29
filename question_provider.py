import random


def create_list_for_answer_options(capital_of_country_dict, asked_questions) -> list:
    """
    takes a dict of capital cities and returns a list with capital and
    a list of a country, the capital and a list of 3 wrong capital cities
    """
    rand_key = ""

    while True:
        rand_key = random.choice(list(capital_of_country_dict.keys()))

        if rand_key in asked_questions:
            continue
        else:
            break

    value_of_rand_key : str = capital_of_country_dict[rand_key]
    wrong_value_list: list = []
    num_of_wrong_values: int = 0
    wrong_answers_list = list(capital_of_country_dict.values())
    random.shuffle(wrong_answers_list)
    for wrong_value in wrong_answers_list:
        if wrong_value != value_of_rand_key and num_of_wrong_values < 3 and wrong_value not in wrong_value_list:
            wrong_value_list.append(wrong_value)
            num_of_wrong_values += 1
    return [rand_key, value_of_rand_key, wrong_value_list]


def create_dict_for_answer_options(capital_of_country_dict, asked_questions) -> list:
    """
    takes a dict of capital cities and returns a dict of 4 capital cities
    """
    answer_options: dict = {}
    rand_key, value_of_rand_key, wrong_value_list = create_list_for_answer_options(capital_of_country_dict, asked_questions)
    answer_options_values: list = wrong_value_list.copy()
    answer_options_values.append(value_of_rand_key)
    random.shuffle(answer_options_values)
    answer_options_values.append("SKIP")
    keys: list = ["A", "B", "C", "D", "E"]
    for key, value in zip(keys, answer_options_values):
        answer_options[key] = value
    return [rand_key, value_of_rand_key, answer_options]
