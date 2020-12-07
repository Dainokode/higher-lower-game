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


def compare(a, b):
    score = 0
    game_over = False
    while not game_over:
        # followers
        a_followers = a["follower_count"]
        b_followers = b["follower_count"]
        # print accounts info - a vs b
        print_accounts(a, b)
        # prompt user
        guess = input("Who has more followers? 'A' or 'B'? ")
        # game logic
        if a_followers > b_followers and guess == "a":
            score += 1
            print(f"Correct! Your score is {score}")
            a = b
            b = random_account()
        elif b_followers > a_followers and guess == "b":
            score += 1
            print(f"Correct! Your score is {score}")
            a = b
            b = random_account()
        else:
            print(f"Sorry, you lost. Your final score is {score}")
            game_over = True


print(logo)

a = random_account()
b = random_account()

compare(a, b)
