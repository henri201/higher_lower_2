# display art
import random
from data import data
from art import logo, vs

# format the account data into printable
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_desc}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# display art

print(logo)

# generate random account to compare and get their info
account_a = random.choice(data)
account_b = random.choice(data)
if person_a == person_b:
    person_b = random.choice(data)

print(f"Compare A: {format_data(person_a)}.")
print(vs)
print(f"Against B: {format_data(person_b)}.")


# type a or b to guess
guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()
a_flollowers = account_a["follower_count"]
b_flollowers = account_b["follower_count"]
#compares the two answers and your guess 
## get follower count of each account
## use if statements to check if user is correct




# if the guess was right promt another one , if it was wrong , end the game




# add a scoring system, that keeps track of your score 




# give an option to start the game again