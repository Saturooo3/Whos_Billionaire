from colorama import Fore, Style
import graphics
import leaderboard
import os


def check_answer(user_answer, correct_answer, jokers, money, round, game_ended, player_name):
    if user_answer == correct_answer:
        print(Fore.GREEN + "Correct! You've earned $1,000,000!" + Style.RESET_ALL)
        money += 1000000
        round += 1
        print(Fore.GREEN + f"So far you've earned ${money:,}!" + Style.RESET_ALL)

        input('Press enter to continue')

        if round == 10:
            game_ended = True

    elif user_answer == "SKIP" and jokers > 0:
        print(Fore.BLUE + "Question skipped." + Style.RESET_ALL)
        jokers -= 1

        input('Press enter to continue')

    else:
        os.system("clear")
        print(Fore.RED + "Wrong! That was incorrect." + Style.RESET_ALL)

        print(f"The correct answer was: {correct_answer}")
        print(graphics.game_over())
        game_ended = True
        leaderboard.update_leaderboard(player_name, 0)

        input("Press enter to see leaderboard")
        os.system("clear")

        leaderboard.display_leaderboard()

        input('Press enter to end')

    return jokers, money, round, game_ended

def is_user_choice_valid(user_choice, jokers):
    user_choice_list = ["A", "B", "C", "D"]
    if jokers > 0:
        user_choice_list.append("E")

    return user_choice in user_choice_list
