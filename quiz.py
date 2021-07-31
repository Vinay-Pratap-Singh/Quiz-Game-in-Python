import json
import random

# Main Menu to control game and provide start up for user
def main_menu():
    print("\n*****Welcome to the Quiz Game*****\nCreated and Designed by Vinay Pratap Singh")

    print('''
    1: Start Quiz
    2: Instructions
    3: Exit''')
    try:
        choice = int(input("\nChoose Your Option: "))
    except:
        print("Invalid Option Selected")
        main_menu()

# Iterating according to the choice of the User using nesting of the if elif
    if choice>3:
        print("Invalid Option Selected")
        main_menu()
    elif choice == 3:
        print("Thanks for playing this Game")
        exit(0)
    elif choice == 1:
        start_game()
    elif choice == 2:
        with open("instruction.txt", "r") as f:
            instruct = f.read()
            print(instruct)
        main_menu()

def start_game():
    print("\nSelect the Topic of the Quiz\n")
    print('''
    1: Computer Fundamental
    2: Python Programming
    3: Cyber Security
    4: Main Menu
    5: Exit''')

    try:
        choice = int(input("\nChoose Your Option: "))
    except:
        print("Invalid Option Selected")
        start_game()
    
    if choice >5:
        print("Invalid Option Selected")
        start_game()
    elif choice == 5:
        print("Thanks for playing this Game")
        exit(0)
    elif choice == 4:
        main_menu()
    elif choice == 3:
        play_game(choice)
    elif choice == 2:
        play_game(choice)
    elif choice == 1:
        play_game(choice)
    
def play_game(choice):

    # Reading my Json file which contains the Questions, Answers and Options
    if choice == 1:
        with open("computer_funda.json", "r") as f:
            file = f.read()
            data = json.loads(file)
    elif choice == 2:
        with open("python.json", "r") as f:
            file = f.read()
            data = json.loads(file)
    elif choice == 3:
        with open("cyber_security.json", "r") as f:
            file = f.read()
            data = json.loads(file)


    # Extracting the data from the Json file in as a list
    question = data.get("ques")
    option = data.get("opt")
    answer = data.get("ans")
    # Counter for Counting the Correct Answers
    count = 0

    # Creating a Random List of Questions, so that every time questions gets radomized of their own
    ques_pattern = []
    while len(ques_pattern)<10:
        pattern = random.randint(0, len(question)-1)
        if pattern not in ques_pattern:
            ques_pattern.append(pattern)
        else:
            continue

    # Main program part to perform Quiz
    print("*****Welcome to the Quiz Game*****")
    print("Created and Designed By: Vinay Pratap Singh")
    for i in ques_pattern:
        print(question[i])
        print(option[i])
        try:
            user_answer = int(input("\nSelect your Answer: "))
            if user_answer>4:
                print("Invalid Option Selected")
                continue
            if user_answer == answer[i]:
                count+=1
            else:
                print("Wrong Answer")
                print("Correct Answer is: Option",answer[i])
                print("\n")
        except:
            print("Invalid Option Selected")
            continue
            
    print(f"\nTotal Marks: {count}/10")
    # Finding percentage of Marks upto 2 Decimal Digit only
    percentage = (count/10)*100
    percentage = "{0:.2f}".format(percentage)
    print(f"Marks Percentage: ",percentage)

    main_menu()

# Main Function to Start our Program
if __name__=='__main__':
    main_menu()