# UI functions to call

import player_functions
import os

goodbye = "Thank you for using the Tennis App. We hope to see you soon again. Goodbye!"
yes = 'y'
no = 'n'
exit_app = 'e'


def welcome():
    print("""
              ______                 _         ____  __                          
             /_  __/__  ____  ____  (_)____   / __ \/ /___ ___  _____  __________ ®
              / / / _ \/ __ \/ __ \/ / ___/  / /_/ / / __ `/ / / / _ \/ ___/ ___/
             / / /  __/ / / / / / / (__  )  / ____/ / /_/ / /_/ /  __/ /  (__  ) 
            /_/  \___/_/ /_/_/ /_/_/____/  /_/   /_/\__,_/\__, /\___/_/  /____/  
                                                         /____/                 

        Welcome to the CS361 dedicated App to retrieving ATP Tennis Player information.
        Questions about the App? Read our FAQ by typing "FAQ" at any menu.

                  Press the 'Y' key to continue... or 'E' to Exit.
                            
                                 Version S1.6 - 1.0.0
                               Made by: Fernando D. Mata
                            OSU CS361 Software Engineering I 
    """)
    while True:
        welcome_answer = str.lower(input("Enter Key: "))
        if welcome_answer == exit_app:
            return print(goodbye)
        elif welcome_answer == 'faq':
            faq()
            print("""Press the 'Y' key to continue... or 'E' to Exit.""")
        elif welcome_answer == yes:
            return main_menu()
        else:
            print("Invalid option. Please try again.")


def main_menu():
    print("""
MAIN MENU:
    
Type:
1. to Enter ATP Tennis Player name.
2. to Learn About the App

'FAQ' for general questions.
    
Press 'E' to Exit App.
    """)
    while True:
        main_menu_answer = str.lower(input("Enter Key: "))
        if main_menu_answer == exit_app:
            return print(goodbye)
        elif main_menu_answer == 'faq':
            faq()
            return main_menu()
        elif main_menu_answer == '1':
            return player_name()
        elif main_menu_answer == '2':
            learn_about()
            return main_menu()
        else:
            print("Invalid option. Please try again.")


def learn_about():
    while True:
        # Open Learn About text file.
        # print("Current Working Directory:", os.getcwd())
        # file_path = './learn-about.txt'
        file_path = r'C:\Users\Darian\PycharmProjects\CS361 Software Engineering I\Course Project\learn-about.txt'
        # Open the file with the default application
        os.startfile(file_path)
        return


def faq():
    while True:
        # Open Learn About text file.
        # print("Current Working Directory:", os.getcwd())
        # file_path = './faq.txt'
        file_path = r'C:\Users\Darian\PycharmProjects\CS361 Software Engineering I\Course Project\faq.txt'
        # Open the file with the default application
        os.startfile(file_path)
        return


def player_name():
    while True:
        player_entered = input("Enter ATP Player Name: ")
        print('You entered: ' + player_entered)
        print('Is that correct? Y/N')
        is_correct = str.lower(input())
        if is_correct == yes:
            return player_functions.player_menu(player_entered)