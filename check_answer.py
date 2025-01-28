from colorama import Fore, Style

def check_answer(user_answer, correct_answer, jokers, money, round, game_ended):
    if user_answer == correct_answer:
        print(Fore.GREEN + "Correct! You've earned $1,000,000!" + Style.RESET_ALL)
        money += 1000000
        round += 1

    elif user_answer == "SKIP" and jokers > 0:
        print(Fore.BLUE + "Question skipped." + Style.RESET_ALL)
        jokers -= 1

    else:
        print("=================================")
        print(Fore.RED + "Wrong! That was incorrect." + Style.RESET_ALL)
        print("GAME OVER :(")
        print("=================================")
        game_ended = True

    return jokers, money, round, game_ended

def is_user_choice_valid(user_choice):
    user_choice_list = ["A", "B", "C", "D", "E"]
    return user_choice in user_choice_list
