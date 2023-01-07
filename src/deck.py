import random

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(4): # Loop through suits
            for j in range(1, 14, 1): # Loop through the 13 cards in a suit, starting at 1.
                self.cards.append(Card(j))

    def draw_card(self, request=0): # Draw card from deck, returns a single Card and removes it from the deck.
        draw = -1
        if request != 0: # Optional request card, attempts to draw specific card from the deck
            for i, c in enumerate(self.cards): # Loop through cards in deck with a counter.
                if c.value == request: # If card found that matches request. 
                    drawn = self.cards.pop(i)
                    return drawn # Return found card
            print("ERR: No " + str(request) + " in the deck") # If no card found, print error and draw card as standard.

        draw = random.randint(0, len(self.cards) - 1)
        drawn = self.cards.pop(draw)
        return drawn
        

class Card: # Card class. Has value and display. 
    def __init__(self, value): 
        self.value = value
        if value == 1: # Sets display depending on card value.
            self.display = 'A'
        elif value == 11:
            self.display = 'J'
        elif value == 12:
            self.display = 'Q'
        elif value == 13:
            self.display = 'K'
        else:
            self.display = str(self.value) # Number cards display is simply their value.

    def __repr__(self): # Printable representation. Means that printing a list of Cards will display nicely.
        return self.display