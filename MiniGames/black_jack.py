import random

SUITS = {
    'Heart', 'Diamonds', 'Spade', 'Club'
}
RANKS = {
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
    'Ten', 'Jack', 'Queen', 'King', 'Ace',
}
VALUES = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
    'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)


class Deck:

    def __init__(self):
        self.deck = list()
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n%s' % (card.__str__())
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = list()
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # The card passed will be from self.deck, using deal
        self.cards.append(card)
        self.value += VALUES[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10


class Chips:

    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# class BlackJack:
#
#     def __init__(self):
#         self.player_name = 'Nitin'
#         # self.player_name = input('Enter your name: ')
#         self.pc_name = 'Alex (PC)'


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry please provide an Integer!!!')
        else:
            if chips.bet<=0:
                print('Wrong bet value!')
            elif chips.total < chips.bet:
                print('Sorry, You do not have enough chips!!!\n You only have %s' % chips.total)
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Player stands Dealer\'s turn')
            playing = False
        else:
            print('Wrong Input! Enter h or s only.')
            continue
        break


def player_busts(player, dealer, chips):
    print('BUST PLAYER!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Player Wins! Dealer BUSTS')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer Wins')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and player TIE! PUSH')


def show_some(player, dealer):
    print(f'Dealers hand:\nOne card Hidden\n{dealer.cards[1]}\n')
    print('Players hand:', )
    for card in player.cards:
        print(card)
    print('\n')


def show_all(player, dealer):
    print('Dealers hand: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Players hand: ')
    for card in player.cards:
        print(card)
    print('\n')


if __name__ == '__main__':
    """
    Get player name
    Initialize game
    Handover cards
    """
    # bj = BlackJack()
    playing = True
    while True:
        # Welcome message
        print('Wekcome to blackJack!')

        # Setup deck
        deck = Deck()
        deck.shuffle()

        # Player card info
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        # Dealer card info
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set chips of the player
        player_chips = Chips(total=200)

        # Ask the player for bet
        take_bet(player_chips)

        # show the current dealed cards
        show_some(player_hand, dealer_hand)

        while playing:
            # ask user for hit or stand
            hit_or_stand(deck, player_hand)

            # show the player cards
            show_some(player_hand, dealer_hand)

        # check if player got busted
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            show_all(player_hand, dealer_hand)

            # if the player has not busted
        if player_hand.value <=21:
            # Using soft 17 rule i.e. dealer hits until the value exceeds 17
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # show all cards
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
        print(f'\nPlayers total chips are at: {player_chips.total}')
        new_game = input('Want to play again? y/n')
        if new_game[0].lower() == 'y':
            playing = True
        else:
            print('Thanks for playing!')
            break


