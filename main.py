from art import *
from data import data
import random


def random_account():
    """return random account from data list"""
    account = random.choice(data)
    return account


def print_accounts(a, b):
    """prints accounts info"""
    # test
    print(a["follower_count"])
    print(b["follower_count"])

    print(f"Compare A: {a['name']} a {a['description']} from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']} a {b['description']} from {b['country']}")


def compare_accounts(a, b):
    score = 0
    game_over = False
    while not game_over:
        a_followers = a["follower_count"]
        b_followers = b["follower_count"]

        print_accounts(a, b)

        guess = input("Who has more followers? 'A' or 'B': ").lower()

        if a_followers > b_followers and guess == "a" or b_followers > a_followers and guess == "b":
            score += 1
            print(f"Correct, your score is {score}")

            if a_followers > b_followers:
                a = random_account()
                print_accounts(b, a)
            else:
                b = random_account()
                print_accounts(a, b)
        else:
            print(f"Sorry, you lost. Your final score is {score}")
            game_over = True


print(logo)

# pick accounts
a = random_account()
b = random_account()

compare_accounts(a, b)
