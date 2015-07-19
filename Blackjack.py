# Blackjack
# I like to play blackjack using cards. I'm not addicted to gambling. I'm addicted to sitting in a semi-circle.
# So I have impelmented "Black Jack" game in Python using Code Skulptor Tool.
# To know more about Black Jack go to this link:  http://en.wikipedia.org/wiki/Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com

CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables

in_play = False
outcome = ""
score = 0
cover = 1

# define globals for cards

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class

class Card:

    def __init__(self, suit, rank):

        if (suit in SUITS) and (rank in RANKS):

            self.suit = suit
            self.rank = rank

        else:

            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):

        return self.suit + self.rank

    def get_suit(self):

        return self.suit

    def get_rank(self):

        return self.rank

    def draw(self, canvas, pos):

        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class

class Hand:

    def __init__(self):

        self.cards = []

    def __str__(self):

        s = "Cards in hand: "

        for i in self.cards:

            s = s + str(i) + " "

        return s

    def add_card(self, card):

        self.cards.append(card)

    def get_value(self):

        value = 0
        isAcePresent = False

        for i in self.cards:

            value = value + VALUES[i.get_rank()]

            if value == 1:

                isAcePresent = True

        if (isAcePresent) and ((value + 10) <= 21):

            value = value + 10

        return value


    def draw(self, canvas, pos):

        j = 0

        for i in self.cards:

            i.draw(canvas, [(pos[0] + (j * 80)), pos[1]])
            j = j + 1

# define deck class 

class Deck:

    def __init__(self):

        self.cards = []

        for suit in SUITS:

            for rank in RANKS:

                self.cards.append(Card(suit, rank))

    def shuffle(self):

        random.shuffle(self.cards)

    def deal_card(self):

        return self.cards.pop()

    def __str__(self):

        s = "Cards in deck: "

        for i in self.cards:

            s = s + str(i) + " "

        return s

#define event handlers for buttons

def deal():

    global outcome, in_play, score, card, deck, hand, dealer, cover

    if in_play:

            in_play = False
            outcome = "You lose! New deal?"
            cover = 0
            score = score - 1

    else:

            new_deck = Deck()
            new_hand = Hand()
            new_dealer = Hand()

            deck = new_deck
            hand = new_hand
            dealer = new_dealer

            deck.shuffle()

            hand.add_card(deck.deal_card())
            hand.add_card(deck.deal_card())

            dealer.add_card(deck.deal_card())
            dealer.add_card(deck.deal_card())

            cover = 1
            outcome = "Hit or stand?"
            in_play = True

def hit():

    global outcome, in_play, score, card, deck, hand, dealer, cover

    if in_play:

        card = deck.deal_card()
        hand.add_card(card)
   
        if hand.get_value() > 21:

            in_play = False
            outcome = "Busted! You lose! New deal?"
            cover = 0
            score = score - 1

def stand():

    global outcome, in_play, score, card, deck, hand, dealer, cover

    if in_play:

        cover = 0

        while dealer.get_value() < 17:

            card = deck.deal_card()
            dealer.add_card(card)

        if dealer.get_value() > 21:

            outcome = "You win! New deal?"
            in_play = False
            score = score + 1

        else:

            if dealer.get_value() >= hand.get_value():

                outcome = "You lose! New deal?"
                in_play = False
                score = score - 1

            else:

                outcome = "You win! New deal?"
                in_play = False
                score = score + 1

# draw handler  

def draw(canvas):

    global outcome, in_play, score, card, deck, hand, dealer, cover

    canvas.draw_text("Blackjack", (210, 70), 48, 'Black')
    canvas.draw_text("Score: " + str(score), (250, 110), 32, 'Black')
    canvas.draw_text("Dealer:", (250, 180), 32, 'Black')
    canvas.draw_text("Player:", (250, 390), 32, 'Black')
    dealer.draw(canvas, [100, 210])
    hand.draw(canvas, [100, 420])
    canvas.draw_text(outcome, (150, 560), 32, 'Black')

    if cover == 1:

        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [136.5, 259], CARD_SIZE)

# initialize frame

frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Orange")

# initialize data

card = Card("S", "A")
deck = Deck()
hand = Hand()
dealer = Hand()

#create buttons and canvas callback

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling

deal()
frame.start()
