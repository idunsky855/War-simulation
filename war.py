'''Game of War between two virtual players.'''
import random

card_value_dict = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace":14
}
suits = ("Hearts", "Diamonds",  "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven","Eight"
         , "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Card:
    '''
    A card in a deck of cards.
    Each card has a suit and a rank, and an integer value for convenience
    '''
    def __init__(self, suit,  rank):
        self.suit = suit
        self.rank = rank
        self.value = card_value_dict[rank]

    def __str__(self):
        return self.rank + '  of  ' + self.suit

class Deck:
    '''
    A deck of cards
    Contains 52 cards
    13 of each suit
    '''
    def __init__(self):
        '''Create a new deck of cards'''
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #Create a new card for each rank and suit
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        '''Shuffle the cards in the deck'''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''Deal one card from the deck'''
        return self.all_cards.pop()

class Player:
    '''
    A player in a game of War
    Contains a name and a deck of cards
    '''
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        '''
        Remove the first card from the players hand
        '''
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        '''
        Add cards to players hand
        '''
        if type(new_cards) == type([]):
            #list of multiple cards
            self.all_cards.extend(new_cards)
        else:
            #single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player: {self.name} has {len(self.all_cards)} cards'


if  __name__ == "__main__":
    player_one = Player("Alice")
    player_two = Player("Bob")

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        #dealing each player half of the deck randomly
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    GAME_ON = True
    ROUND_NUM = 0

    while GAME_ON:
        ROUND_NUM +=1
        print(f'Currently on round {ROUND_NUM}')

        if len(player_one.all_cards ) == 0:
            print(f'{player_one.name} is out of cards! {player_two.name} Wins!!!')
            GAME_ON = False
            break

        if len(player_two.all_cards) == 0:
            print(f'{player_two.name} is out of cards! {player_one.name} Wins!!!')
            GAME_ON = False
            break

        player_one_cards = []
        player_two_cards = []

        player_one_cards.append(player_one.remove_one())
        player_two_cards.append(player_two.remove_one())

        AT_WAR = True
        while AT_WAR:

            if player_one_cards[-1].value > player_two_cards[-1].value:
               #Player one wins round
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                AT_WAR = False
                print(f'{player_one.name} won the round!')


            elif player_one_cards[-1].value < player_two_cards[-1].value:
                #player two wins round
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                AT_WAR = False
                print(f'{player_two.name} won the round!')

            else:
                print('WAR!')

                if len(player_one.all_cards) < 5:
                    print(f'{player_one.name} does not have enough '+
                        f'cards to go to war! {player_two.name} Wins!!')
                    GAME_ON = False
                    AT_WAR = False
                    break

                elif len(player_two.all_cards) < 5:
                    print(f'{player_two.name} does not have enough ' +
                        f'cards to go to war! {player_one.name} Wins!!')
                    GAME_ON = False
                    AT_WAR = False
                    break

                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())
                