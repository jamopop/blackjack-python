from src.deck import Deck
from src.hand import Hand

import argparse

parser = argparse.ArgumentParser(description="Simulates Blackjack") # Setup command arguments
parser.add_argument("-c", "--hand", action="store", help="allows for user specified hand, seperated by commas")
parser.add_argument("-p", "--players", action="store", help="specifies player count (1-7)")
parser.add_argument("-l", "--limit", action="store", help="round limit")
args = parser.parse_args()
config = vars(args)

def play(players=0, test_hand=0, round_limit=0): # Game set up.
    print('Welcome to Blackjack.') 
    deck = Deck()
    hands = []
    hand_count = -1
    if players != 0:
        hand_count = players
    while hand_count < 0 or hand_count > 7: # Usually 2-7. Too many players won't work with a single deck. 
        print('How many players (1-7)?')
        try: # Try catch in case input is not a number
            hand_count = int(input()) 
        except ValueError: # ValueError means that aborts still work.
            continue
    if test_hand != 0: # Optional argument, if a test hand is supplied then player 1 will have that.
        hand = test_hand.split(',')
        hands.append(Hand(deck, 0, hand))
    for i in range(hand_count):
        if test_hand != 0 and i == 0: # If first hand is already set, skip
            continue
        hands.append(Hand(deck, i)) # Deck gets passed in, allows for initial drawing of 2 cards.
    print('---------')
    return round(deck, hands, 0, round_limit) # Return allows for easier unit testing.

def round(deck, hands, i, round_limit): # Game loop
    game_over = True 
    for hand in hands: # Loop through every players hand
        if not hand.out: 
            game_over = False # If any hand is still "in", game isn't over
            print(hand.show_hand()) 
            if len(deck.cards) <= 0: # If deck empty, game is over
                print("EMPTY DECK")
                game_over = True
            else:
                print("Hit? (y/n)")
                response = input()
                if response.capitalize()[0] == 'Y': # If player responds with 'y' (or anything beginning with y), they hit.
                    drawn = deck.draw_card()
                    hand.add_card(drawn)
                    print(hand.show_hand())
                else:
                    hand.out = True # If they don't hit, they're "out"
                print('---------')
    i += 1 # Round counter, for optional round limit. 
    if not game_over and (i < round_limit or round_limit <= 0): # If game isn't over and rounds haven't exceeded limit.
        return round(deck, hands, i, round_limit) # Another round, recursive
    else:
        return game_summary(hands) # Summarise game, returns final set of hands.

def game_summary(hands):
    winning_score = 0
    winner = -1
    i = 0
    for hand in hands: # Loop through all players hands
        if hand.total > winning_score and not hand.bust: # If the hand total > current stored highest AND not bust, it is the new highest.
            winning_score = hand.total
            winner = i # Tracks player number.
        i += 1
    if winner != -1:
        print("Winner: " + hands[winner].show_hand())
    else:
        print("No Winner.")
    return hands 


if __name__ == '__main__':
    players = 0
    test_hand = 0
    round_limit = 0

    if config["players"]: # Loads command arguments.
        players = int(config["players"])
    if config["hand"]:
        test_hand = config["hand"]
    if config["limit"]:
        round_limit = int(config["limit"])

    play(players, test_hand, round_limit)
