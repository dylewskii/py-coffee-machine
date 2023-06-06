import art
import random

def clear():
    print("\n" * 50)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(current_cards):
    score = sum(current_cards)
    ace = 11
    if len(current_cards) == 2 and score == 21:
        return 0

    if ace in current_cards and score > 21:
        current_cards.remove(ace)
        current_cards.append(1)
    return score


def compare(pc_score, score):
    if score == pc_score:
        return "It's a draw!"
    elif pc_score == 0:
        return "You lost - your opponent has a blackjack!"
    elif score == 0:
        return "You win - you have a blackjack!"
    elif score > 21:
        return "You lost - you went bust!"
    elif pc_score > 21:
        return "You win - your opponent went bust!"
    elif score > pc_score:
        return "You win - you had a higher score!"
    else:
        return "You lost - your opponent had a higher score!"


def play_game():
    print(art.logo)

    deck = []
    pc_deck = []
    is_game_over = False

    for _ in range(2):
        deck.append(deal_card())
        pc_deck.append(deal_card())

    while not is_game_over:
        score = calculate_score(deck)
        pc_score = calculate_score(pc_deck)

        print(f"Your cards: {deck}, current score: {sum(deck)}")
        print(f"Computer's first card: {pc_deck[0]}")

        if score == 0 or pc_score == 0 or score > 21:
            is_game_over = True
        else:
            cont = input("----- Type 'y' to get another card, type 'n' to pass: -----\n").lower()
            if cont == 'y':
                deck.append(deal_card())
            else:
                is_game_over = True

        while pc_score != 0 and pc_score < 17:
            pc_deck.append(deal_card())
            pc_score = calculate_score(pc_deck)

        print(f"   Your final hand: {deck}, final score: {score}")
        print(f"   Computer's final hand: {pc_deck}, final score: {pc_score}")
        print(compare(score, pc_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


