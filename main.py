# imports
from art import *
from data import data
import random


def random_account():
    """Returns a random account from data list"""
    return random.choice(data)


def print_accounts(a, b):
    print(f"Compare A: {a['name']} a {a['description']} from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']} a {b['description']} from {b['country']}\n")


print(logo)

account_a = random_account()
account_b = random_account()
# print(account_a['follower_count'])
# print(account_b['follower_count'])

print_accounts(account_a, account_b)

user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

game_over = False
score = 0
while game_over == False:
    if user_choice == "a" and account_a["follower_count"] > account_b["follower_count"] or user_choice == "b" and account_b["follower_count"] > account_a["follower_count"]:
        score += 1
        print(f"You're right! Your score is: {score}\n")

        account_loser = None

        if account_a["follower_count"] < account_b["follower_count"]:
            account_loser = account_a
        else:
            account_loser = account_b

        account_a = random_account()
        account_b = random_account()

        # print(account_loser['follower_count'])
        # print(account_b['follower_count'])

        print_accounts(account_loser, account_b)

        user_choice = input(
            "Who has more followers? Type 'A' or 'B': ").lower()
    else:
        print(f"Sorry, that's wrong. Your final score is {score}")
        game_over = True
