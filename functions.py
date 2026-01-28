import random

def get_suit():
    """Generates a random suit for the card"""
    suit = random.randint(1, 4)
    if suit == 1:
        return "spades"
    elif suit == 2:
        return "clubs"
    elif suit == 3:
        return "diamonds"
    else:
        return "hearts"

def get_rank():
    """Generates a random rank for the card"""
    suit = random.randint(1, 13)
    if suit == 1:
        return "three"
    elif suit == 2:
        return "four"
    elif suit == 3:
        return "five"
    elif suit == 4:
        return "six"
    elif suit == 5:
        return "seven"
    elif suit == 6:
        return "eight"
    elif suit == 7:
        return "nine"
    elif suit == 8:
        return "ten"
    elif suit == 9:
        return "king"
    elif suit == 10:
        return 'jack'
    elif suit == 11:
        return "queen"
    elif suit == 12:
        return "ace"
    else:
        return "two"


def draw_card():
    """draws a random card accounting for the possibility of the two joker cards"""
    joker = random.randint(1, 54)
    if joker > 2:
        suit = get_suit()
        rank = get_rank()
        return f"{rank} of {suit}"
    else:
        return f"joker"
    
def draw_hand(number):
    """draws a certain number of cards with replacement in a hand dependent on the input"""
    hand =""
    for i in range(number):
        hand += (draw_card() + 1*"\n")
    return hand
