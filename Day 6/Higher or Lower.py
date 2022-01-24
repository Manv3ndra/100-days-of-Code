from game_data import data as data
import art
import random
import os
def format_data(account):
    account_name = account['name']
    account_occupation = account['occupation']
    account_country = account['country']
    return f"{account_name}, a {account_occupation}, from {account_country}"

def answer(guess,account_a,account_b):
    if (account_a['followers'] > account_b['followers']):
        return guess == 'A'
    else:
        return guess == 'B'

def clear():
    os.system('cls')

score = 0
print(art.logo)
account_b = random.choice(data)
game_continue = True

while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print("Compare A: ",format_data(account_a))
    print(art.vs)
    print("Compare B: ",format_data(account_b))

    guess = input("Who has more followers A or B: ").upper()

    correct = answer(guess,account_a,account_b)
    clear()
    print(art.logo)

    if correct:
        score += 1
        print("You're Right. Current Score is: ",score)
    else:
        game_continue = False
        print("Sorry, that's wrong. Your Score is: ",score)