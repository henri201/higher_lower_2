# display art
import os
import random
from data import data
from art import logo, vs

# format the account data into printable
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_desc}, from {account_country}")

# compares the two answers and your guess
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# to clear the system after restart
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# make game repeatable
while game_should_continue:
    # generate random account to compare and get their info
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    # type a or b to guess, get follower count of each account
    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers, b_followers)

    # clear the screen between rounds
    clear()

    ## use if statements to check if user is correct
    # if the guess was right promt another one , if it was wrong , end the game
    # add a scoring system, that keeps track of your score 
    if is_correct:
        score += 1
        print(f"you're right, the score is: {score} ")
        
    else:
        game_should_continue = False
        print(f"you're wrong, the final score is {score}")