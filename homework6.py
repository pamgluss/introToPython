# Intro to Python homework 5
# Pamela Gluss
class Card():

    counter = 0

    # I decided to go with random card generation, instead of using an existing deck
    # Therefore, when the card is generated, it imports randint
    def __init__(self, rank, suit):
        # First, we'll set parameters for error throwing
        if rank < 0 or rank > 13:
            raise ValueError()
        if type(rank) is not int:
            raise TypeError()
        if suit not in ['c', 'd', 's', 'h']:
            raise ValueError()
        if type(suit) is not str:
            raise TypeError()
        # set the rank using getRank
        # Okay so if the rank can't be found in the dictionary, throw an error.
        try:
            self.rank = self.getRank(rank)
        except TypeError:
            print("Wrong type")
        except ValueError:
            print("Wrong value")
        # Generates rank and suit so that they can index the lists/dictionaries in the following methods.
        self.rank = 1
        self.suit = 0
        self.bjValue = 0
        Card.counter += 1

    # This method takes the randomly generated integer from self.suit and looks in a list to find the string
    # name for the suit. It reassigns self.suit AND returns self.suit.
    def getSuit(self, suit):
        suitList = {"h":"Hearts", "s":"Spades", "c":"Clubs", "d":"Diamonds"}
        return suitList[suit]

    # getRank gives you the string name of each card - 1 being Ace, 11 being Jack, 12 being Queen and 13 being King
    # It also reassigns self.rank and returns the string rank.
    def getRank(self, rank):
        rankSelect = {1: "Ace",
                      2: "Two",
                      3: "Three",
                      4: "Four",
                      5: "Five",
                      6: "Six",
                      7: "Seven",
                      8: "Eight",
                      9: "Nine",
                      10: "Ten",
                      11: "Jack",
                      12: "Queen",
                      13: "King"}
        return rankSelect[rank]

    # getBjValue finds the numerical value of a card in blackjack
    # Ace is 0 because there is code later to decide if it becomes 1 or 11
    # There are also the string alternatives to the keys, in case the rank has been set before the method is called.
    def getBjValue(self, rank):
        bjSel = {1:0, "Ace":0,
                 2:2, "Two": 2,
                 3:3, "Three": 3,
                 4:4, "Four": 4,
                 5:5, "Five": 5,
                 6:6, "Six": 6,
                 7:7, "Seven": 7,
                 8:8, "Eight": 8,
                 9:9, "Nine": 9,
                 10:10, "Ten": 10,
                 11:10, "Jack": 10,
                 12:10, "Queen": 10,
                 13:10, "King": 10}
        return bjSel[rank]

    # readyToPlay simply sets all the values described in the methods above.
    def readyToPlay(self, rank, suit):


        # Next, set the suit using getSuit
        # If the suit can't be found in the dictionary, throw an error
        try:
            self.suit = self.getSuit(suit)
        except TypeError:
            print("Wrong type")
        except ValueError:
            print("Wrong value")

            # Finally, set the blackjack value using the rank
            self.bjValue = self.getBjValue(rank)


    # Returns Rank of Suit (eg. Ace of Spades
    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)

# Ignore this code from assignment 5
"""
def playBlackJack():
    # We start by generating 4 cards - 2 for the player and 2 for the house. readyToPlay() gets the cards primed to
    #compare values and whatnot
    card1 = Card()
    card1.readyToPlay()
    card2 = Card()
    card2.readyToPlay()
    card3 = Card()
    card3.readyToPlay()
    card4 = Card()
    card4.readyToPlay()

    #These statements are just telling us what cards each person has drawn and played.
    print("The dealer lays down his cards. He has:")
    print(card3)
    print(card4)

    print("You lay down your cards.")
    print(card1)
    print(card2)


    # If the player's cards are NOT aces, then we can assign the values normally and add together the player's hand value
    if(card1.rank != "Ace" and card2.rank != "Ace"):
        playHandVal = card1.bjValue + card2.bjValue
    elif(card1.rank is "Ace"):
        # If there IS an ace, we simply see if it brings the hand value over 21. If it doesn't, it will be 11
        # Otherwise, it will be set to 1. This is immutable - so two aces drawn in a row will be 11 and 1, unfortunately.
        if card2.bjValue + 11 > 21:
            card1.bjValue = 1
            playHandVal = card1.bjValue + card2.bjValue
        else:
            card1.bjValue = 11
    elif(card2.rank is "Ace"):
        if card1.bjValue + 11 > 21:
            card2.bjValue = 1
            playHandVal = card1.bjValue + card2.bjValue
        else:
            card2.bjValue = 11
            playHandVal = card1.bjValue + card2.bjValue

    # This just does the same exact thing for the house's hand. A helper function to do this would be good.
    if (card3.rank != "Ace" and card4.rank != "Ace"):
        houseHandVal = card3.bjValue + card4.bjValue
    elif (card3.rank is "Ace"):
        if card4.bjValue + 11 > 21:
            card3.bjValue = 1
            houseHandVal = card3.bjValue + card4.bjValue
        else:
            card3.bjValue = 11
            houseHandVal = card3.bjValue + card4.bjValue
    elif (card4.rank is "Ace"):
        if card3.bjValue + 11 > 21:
            card4.bjValue = 1
            houseHandVal = card3.bjValue + card4.bjValue
        else:
            card4.bjValue = 11
            houseHandVal = card3.bjValue + card4.bjValue

    # Now, before we start drawing more cards, it's time to tell the player what the score is
    print("Your hand total is "+ str(playHandVal))
    print("The dealer's hand total is "+str(houseHandVal))

    # We will keep drawing cards until one of the players goes over 21 in value
    # Or the player chooses to fold, then the function will return
    while playHandVal < 21 and houseHandVal < 21:
        if input("Draw another card? (Y/N)") is "Y":
            # This is a tricky part. I would like to figure out a way to not hardcode the variable name here. For now
            # It resets the value of card5 and card6 every time.
            card5 = Card()
            card5.readyToPlay()
            print("You drew: "+str(card5))

            card6 = Card()
            card6.readyToPlay()
            print("The house drew: "+ str(card6))

            # Now we're doing the Ace check again. I reeeeally need to write that helper function.
            if (card6.rank != "Ace"):
                houseHandVal += int(card6.bjValue)
            else:
                if houseHandVal + 11 > 21:
                    card6.bjValue = 1
                    houseHandVal += int(card6.bjValue)
                else:
                    card6.bjValue = 11
                    houseHandVal += int(card6.bjValue)

            if (card5.rank != "Ace"):
                playHandVal += int(card5.bjValue)
            else:
                if playHandVal + 11 > 21:
                    card5.bjValue = 1
                    playHandVal += int(card5.bjValue)
                else:
                    card5.bjValue = 11
                    playHandVal += int(card5.bjValue)

            # remind the player what the hands are, so they can decide to draw again
            print("Your hand total is " + str(playHandVal))
            print("The dealer's hand total is " + str(houseHandVal))

            if playHandVal > 21 and houseHandVal > 21:
                print("It's a draw.")
            elif (playHandVal is 21 or houseHandVal > 21):
                print("Congratulation, you win!")
            elif (houseHandVal is 21 or playHandVal > 21):
                print("The House always wins.")
        else:
            if playHandVal > houseHandVal:
                print("Congratulation, you win!")
                return
            elif playHandVal < houseHandVal:
                print("The House always wins.")
                return
            else:
                print("It's a draw.")
                return
playBlackJack()
"""
# rank, then suit
card1 = Card(3, 'h')
print(card1.readyToPlay())


