import random

def start_game():
    print("Guess the number!")
    print("Do you want to play the game?")
    while True:
        player_choice = input("Enter 'Yes' or 'No' : ").lower()
        
        if player_choice == "yes":
            print("Let's start the game!")
            input_number()
            break
        
        elif player_choice == "no":
            print("finished")
            break
        
        else:
            print("Please Enter 'Yes' or 'No'")
            continue

def input_number():
    min_number = int(input("Enter the minimum number : "))
    max_number = int(input("Enter the maximum number : "))
    
    while True:
        if min_number >= max_number:
            print("The maxNumber has to be bigger than the minNumber")
            input_number()
            break
        else:
            play_game(min_number,max_number)
            break

def play_game(min_number,max_number):
    selected_answer = create_random_number(min_number,max_number)
    how_many_answer = number_of_answer()
    count = 1
    
    while count <= how_many_answer:
        player_answer = int(input("Guess the number : "))
        
        if not max_number >= player_answer >= min_number:
            print(f"You should input a number from {min_number} to {max_number}")
            
        elif player_answer == selected_answer:
            print("You are correct!")
            break
        else:
            print("You are wrong")
        
        remains = how_many_answer - count
        if remains > 0:
            print(f"you can answer {remains} more times")
        count += 1
    

def create_random_number(min_number,max_number):
    result = random.randint(min_number,max_number)
    return result


def number_of_answer():
    result = random.randint(1,10)
    return result 

start_game()





