from src.deck import Card

class Hand:
    def __init__(self, deck, player_num, hand = 0):
        self.cards = [] # Cards stored as list
        self.total = 0
        self.out = False
        self.bust = False # Player is 'out' when they stop hitting, but only 'bust' when they are over 21.
        self.player_num = player_num + 1
        if hand == 0: # Standard behaviour, if optional 'hand' isn't supplied
            self.add_card(deck.draw_card())
            self.add_card(deck.draw_card())
        else:
            for c in hand:
                self.add_card(deck.draw_card(int(c))) # Add specific card from deck.
    
    def add_card(self, card):
        self.cards.append(card) # Adds card to hand.
        if card.value == 1: # Special case for Ace.
            if self.total < 10: # Assumption: Players would never choose to bust themselves 
                player_choice = ''
                while (player_choice != '1' and player_choice != '11'): # Only accept 1 or 11 as player input.
                    print('Would you like this Ace to be a 1 or an 11?')
                    player_choice = input()
                self.total += int(player_choice)
            elif self.total == 10: # Players would never choose to count an Ace as a 1 if their current total was a 10
                self.total += 11
            else:
                self.total += card.value
        elif card.value > 10: # Face cards have value of 10.
            self.total += 10
        else:
            self.total += card.value # Simply add other card values to total.
        if self.total > 21:
            print("BUST")
            self.bust = True # If total over 21, bust.
            self.out = True
        elif self.total == 21:
            print("WIN")
            self.out = True # If total equals 21, win.

    def show_hand(self):
        return 'Player ' + str(self.player_num) + ': ' + str(self.cards) + ' = ' + str(self.total) # Displays hand.
