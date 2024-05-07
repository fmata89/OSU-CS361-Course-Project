# Player Menu called by Main Menu

import menu_functions

goodbye = "Thank you for using the Tennis App. We hope to see you soon again. Goodbye!"
yes = 'y'
no = 'n'
exit_app = 'e'


def player_menu(player_entered):
    print("""

ATP Tennis Player Menu:

Type a number to retrieve information about: """ + player_entered)

    print("""
    1. Current ATP Ranking
    2. Highest ATP Ranking & Date
    3. Career Titles
    4. Career Prize Money Singles & Doubles Combined
    5. Career W-L Record
    6. Personal Details (Bio)
    7. Name Pronunciation
    8. Latest News
    
    9. Change Player Name 
    
    'M' to back to Main Menu.
    'FAQ' for general questions.
    
    Press 'E' to Exit App.
    """)
    while True:
        menu_answer = str.lower(input("Enter Number/Key:  "))
        info_list = ['1', '2', '3', '4', '5', '6', '7', '8']
        if menu_answer == exit_app:
            return print(goodbye)
        elif menu_answer == 'faq':
            menu_functions.faq()
            return player_menu(player_entered)
        elif menu_answer in info_list:
            # 1. Current ATP Ranking
            if menu_answer == '1':
                print('Ranking')
            # 2. Highest ATP Ranking & Date
            elif menu_answer == '2':
                print('High')
            # 3. Career Titles
            elif menu_answer == '3':
                print('Titles')
            # 4. Career Prize Money Singles & Doubles Combined
            elif menu_answer == '4':
                print('Money')
            # 5. Career W-L Record
            elif menu_answer == '5':
                print('Record')
            # 6. Personal Details (Bio)
            elif menu_answer == '6':
                print('Bio')
            # 7. Name Pronunciation
            elif menu_answer == '7':
                print('Audio')
            # 8. Latest News
            elif menu_answer == '8':
                print('News')
            print("Type 'A' to view ATP Player Menu Again or type 'M' for Main Menu:  ")
            continue_answer = str.lower(input())
            if continue_answer == 'm':
                return menu_functions.main_menu()
            return player_menu(player_entered)
        elif menu_answer == '9':
            return menu_functions.player_name()
        elif menu_answer == 'm':
            return menu_functions.main_menu()
        else:
            print("Invalid option. Please try again.")


def curr_ranking():
    return


def highest_ranking():
    return


def titles():
    return


def prize_money():
    return


def wl_record():
    return


def player_bio():
    return


def prononciation():
    return


def latest_news():
    return

