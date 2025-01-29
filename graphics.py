from colorama import Fore, Back, Style, init
import os

def clear_screen():
    os.system('clear')

def game_splash():
    splash = fr"""
    {Fore.MAGENTA}================================================================================
            {Fore.CYAN}TEAM BILLIONAIRES CLUB PRESENTS: {Fore.RED}WHO'S BILLIONAIRE?                    
    {Fore.MAGENTA}================================================================================

        {Fore.YELLOW}||====================================================================||
        ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
        ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
        ||\\$//        ~         '------========--------'                \\$//||
        ||<< /        /$\              // ____ \\                         \ >>||
        ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
        ||<<|        \\ //           || <||  >\  ||                        |>>||
        ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
        ||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
        ||>>|  12                     *\\/___\_//*   1989                  |<<||
        ||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
        ||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
        ||(100)===================  ONE BILLION DOLLARS =================(100)||
        ||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
        ||====================================================================||
    {Fore.RED}--------------------------------------------------------------------------------
                    {Fore.GREEN}ARE YOU READY TO BECOME THE NEXT BILLIONAIRE?
                                PRESS ENTER TO START!{Style.RESET_ALL}    
    {Fore.RED}--------------------------------------------------------------------------------{Style.RESET_ALL} 
    """

    # Game rules text
    game_rules = ("\n\n\n\t- The game consists of 10 rounds, with 3 randomly selected question categories.\n"
                  "\t- The categories are: Geography, Periodic Table of Elements, Golden Globe Winners.\n"
                  "\t- In each round, the player will be asked a question with 4 possible answers,\n"
                  "\t  of which only one is correct.\n"
                  "\t- For each correct answer, the player achieves 1 million.\n"
                  "\t- If the player doesn't know the answer, they can skip a question twice (2 jokers).\n"
                  "\t- If the player answers all 10 questions correctly and has used jokers, \n"
                  "\t  they win the accumulated amount.\n"
                  "\t- If the player answers all 10 questions correctly without using any jokers,\n"
                  "\t  they win the full billion and become a member of the Billionaires Club.\n"
                  "\t- If the player answers a question incorrectly, the game is over and all the money is gone...\n")

    # Show splash screen first
    print(splash)

    # Wait for user to press Enter to continue with game rules
    input("")

    # Clean Screen
    clear_screen()

    # After Enter is pressed, show the game rules
    print(game_rules)

    # After displaying the game rules, wait for the user to press Enter again to start
    input("START PLAYING ?$? -- PRESS ENTER !!!")

    # Return True to indicate that the game is starting
    return True


def display_hangman(question_num):
    """Displays the current state of the gallows."""
    # ASCII-Art for gallow
    hangman_pics = [
        r"""
         +---+
             |
             |
             |
            ===
        """,
        r"""
         +---+
         O   |
             |
             |
            ===
        """,
        r"""
         +---+
         O   |
         |   |
             |
            ===
        """,
        r"""
         +---+
         O   |
        /|   |
             |
            ===
        """,
        r"""
         +---+
         O   |
        /|\  |
             |
            ===
        """,
        r"""
         +---+
         O   |
        /|\\ |
             |
            ===
        """,
        r"""
         +---+
         O   |
        /|\\ |
        /    |
            ===
        """,
        r"""
         +---+
         O   |
        /|\\ |
        / \  |
            ===
        """,
        r"""
         +---+
         O   |
        /|\\ |
        / \\ |
            ===
        """,
        r"""
         +---+
         ()  |
        /|\\ |
        / \\ |
            ===
        """
    ]
    # List of colors to cycle through
    color_cycle = [Fore.WHITE, Fore.GREEN, Fore.GREEN, Fore.YELLOW, Fore.YELLOW, Fore.CYAN, Fore.CYAN, Fore.MAGENTA,
                   Fore.MAGENTA, Fore.RED]

    # Get the color based on the current question number, cycling through colors
    color = color_cycle[question_num % len(color_cycle)]

    # Return the hangman picture with the selected color
    return color + hangman_pics[question_num] + "\n\tQUESTION: " + str(question_num+1) + "/10" +Style.RESET_ALL


def game_over():
    over = r"""
            888888888888888888888888888888888888888888888888888888888888
            888888888888888888888888888888888888888888888888888888888888
            8888888888888888888888888P""  ""9888888888888888888888888888
            8888888888888888P"88888P          988888"9888888888888888888
            8888888888888888  "9888            888P"  888888888888888888
            888888888888888888bo "9  d8o  o8b  P" od88888888888888888888
            888888888888888888888bob 98"  "8P dod88888888888888888888888
            888888888888888888888888    db    88888888888888888888888888
            88888888888888888888888888      8888888888888888888888888888
            88888888888888888888888P"9bo  odP"98888888888888888888888888
            88888888888888888888P" od88888888bo "98888888888888888888888
            888888888888888888   d88888888888888b   88888888888888888888
            8888888888888888888oo8888888888888888oo888888888888888888888
            888888888888888888888888888888888888888888888888888888888888

            ***********************************************************
            *  ____    _    __  __ _____    _____     _______ ____  _ *
            * / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \| |*
            *| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) | |*
            *| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ <|_|*
            * \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_(_)*
            ***********************************************************
    """
    return Fore.RED + over + Style.RESET_ALL


def you_win():
    win = r"""
        ( _____________ ) ___    (            )           
    /    _     _    \/ _ \   (  OH YEAH!  )           
   /    (,)   (,)    \/ \ \ /_____________)           
  |         _         | | |               _______     
  |        (_)        | | |   _______    (  . .  )_   
  |     .       .     |/ /   (  . .  )_  |   o   |_)  
   \     '.....'     /__/    |   o   |_)  ) '-' (     
    \               /         ) '-' (    (_______)    
     )_____________(         (_______)                
____(_______________)_________________________________
    *************************************************
    *__   _____  _   _  __        _____ _   _    _  *
    *\ \ / / _ \| | | | \ \      / /_ _| \ | |  | | *
    * \ V / | | | | | |  \ \ /\ / / | ||  \| | / __)*
    *  | || |_| | |_| |   \ V  V /  | || |\  | \__ \*
    *  |_| \___/ \___/     \_/\_/  |___|_| \_| (   /*
    *                                           |_| *
    *************************************************
    """
    return Fore.GREEN + win + Style.RESET_ALL


def win_as_billionaire():
    billion = r"""
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'               `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$'                   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$'`$$$$$$$$$$$$$'`$$$$$$!                       !$$$$$$'`$$$$$$$$$$$$$'`$$$
    $$$$  $$$$$$$$$$$  $$$$$$$                         $$$$$$$  $$$$$$$$$$$  $$$$
    $$$$. `$' \' \$`  $$$$$$$!                         !$$$$$$$  '$/ `/ `$' .$$$$
    $$$$$. !\  i  i .$$$$$$$$                           $$$$$$$$. i  i  /! .$$$$$
    $$$$$$   `--`--.$$$$$$$$$                           $$$$$$$$$.--'--'   $$$$$$
    $$$$$$L        `$$$$$^^$$                           $$^^$$$$$'        J$$$$$$
    $$$$$$$.   .'   ""~   $$$    $.                 .$  $$$   ~""   `.   .$$$$$$$
    $$$$$$$$.  ;      .e$$$$$!    $$.             .$$  !$$$$$e,      ;  .$$$$$$$$
    $$$$$$$$$   `.$$$$$$$$$$$$     $$$.         .$$$   $$$$$$$$$$$$.'   $$$$$$$$$
    $$$$$$$$    .$$$$$$$$$$$$$!     $$`$$$$$$$$'$$    !$$$$$$$$$$$$$.    $$$$$$$$
    $JT&yd$     $$$$$$$$$$$$$$$$.    $    $$    $   .$$$$$$$$$$$$$$$$     $by&TL$
                                     $    $$    $
                                     $.   $$   .$
                                     `$        $'
                                      `$$$$$$$$'


    (\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)
    (/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)
    (\o/)   ____ ___ _     _     ___ ___  _   _    _    ___ ____  _____   (\o/)
    (/|\)  | __ )_ _| |   | |   |_ _/ _ \| \ | |  / \  |_ _|  _ \| ____|  (/|\)
    (\o/)  |  _ \| || |   | |    | | | | |  \| | / _ \  | || |_) |  _|    (\o/)
    (/|\)  | |_) | || |___| |___ | | |_| | |\  |/ ___ \ | ||  _ <| |___   (/|\)
    (\o/)  |____/___|_____|_____|___\___/|_| \_/_/   \_\___|_| \_\_____|  (\o/)
    (/|\)                                                                 (/|\)
    (\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)(\o/)
    (/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)(/|\)
    """
    return Fore.GREEN + billion + Style.RESET_ALL

# Testing the Splash
#game_splash()

# Testing Hangman
#print(display_hangman(9,12))

# Test Billionaire
# print(win_as_billionaire())