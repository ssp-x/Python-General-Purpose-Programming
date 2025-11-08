import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return f"Card(suit={self.suit!r}, rank={self.rank!r})"

class Deck:
    def __init__(self):
        self.cards = []
        self._build_deck()
        self.shuffle()

    def _build_deck(self):
        suits = ["♥", "♦", "♣", "♠"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, num_cards):
        num_cards = min(num_cards, len(self.cards))
        hand = self.cards[-num_cards:]
        self.cards = self.cards[:-num_cards]
        return hand

    def __len__(self):
        return len(self.cards)

def main():
    deck = Deck()
    print("New deck created and shuffled.")

    while len(deck) > 0:
        print(f"\nCards remaining in deck: {len(deck)}")
        user_input = input("How many cards do you want to draw? ")

        try:
            num_cards = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if num_cards <= 0:
            print("Please enter a positive number of cards.")
            continue

        if num_cards > len(deck):
            print(f"Only {len(deck)} cards left. Drawing all remaining cards.")

        hand = deck.draw(num_cards)

        if not hand:
            print("No cards left to draw.")
            break

        print("You drew:")
        for card in hand:
            print(" ", card)

    print("\nWe are out of cards.")

if __name__ == "__main__":
    main()
