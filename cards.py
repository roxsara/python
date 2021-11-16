suits = {"d": "Diamonds", "s": "Spades", "h": "Hearts", "c": "Clubs"}
values = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
          8: "Eight", 9: "Nine", 10: "Ten", 12: "Jack", 13: "Queen", 14: "King"}


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def __str__(self):

        my_card = str(values[self.value]) + ' of ' + str(suits[self.suit])
        return my_card


one_card = Card(3, 'd')
print(one_card)