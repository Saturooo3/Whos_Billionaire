from colorama import Fore, Style
import graphics
import leaderboard

def check_answer(user_answer, correct_answer, jokers, money, round, game_ended, player_name):
    if user_answer == correct_answer:
        print(Fore.GREEN + "Correct! You've earned $1,000,000!" + Style.RESET_ALL)
        money += 1000000
        round += 1
        print(Fore.GREEN + f"So far you've earned ${money:,}!" + Style.RESET_ALL)

        if round == 10:
            game_ended = True

    elif user_answer == "SKIP" and jokers > 0:
        print(Fore.BLUE + "Question skipped." + Style.RESET_ALL)
        jokers -= 1

    else:
        print(Fore.RED + "Wrong! That was incorrect." + Style.RESET_ALL)
        print(graphics.game_over())
        game_ended = True
        # TODO: SHOW LEADERBOARD
        leaderboard.update_leaderboard(player_name, 0)
        leaderboard.display_leaderboard()

    return jokers, money, round, game_ended

def is_user_choice_valid(user_choice, jokers):
    user_choice_list = ["A", "B", "C", "D"]
    if jokers > 0:
        user_choice_list.append("E")

    return user_choice in user_choice_list
