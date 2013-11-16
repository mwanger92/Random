import System
cards as List = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
suits as List = ["Hearts", "Diamonds", "Spades", "Clubs"]
playedCards as List = []
count = 0
_rand as Random
_rand = Random()

def getCard():
	card = cards[_rand.Next(0,12)]
	suit = suits[_rand.Next(0,3)]
	card = "$card"
	playedCard = "$card $suit"
	if playedCard in playedCards:
		getCard()
	else:
		print playedCard
		playedCards.Add(playedCard)
	if card isa string:
		if card == "Ace" and count + 11 <= 21:
			count = count + 11
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "Ace" and count + 11 > 21:
			count = count + 1
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "Jack" or card == "Queen" or card == "King":
			count = count + 10
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "2":
			count = count + 2
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "3":
			count = count + 3
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "4":
			count = count + 4
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "5":
			count = count + 5
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "6":
			count = count + 6
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "7":
			count = count + 7
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "8":
			count = count + 8
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "9":
			count = count + 9
			print "Your score is $count"
			print "Your cards are $playedCards"
		elif card == "10":
			count = count + 10
			print "Your score is $count"
			print "Your cards are $playedCards"

def hitOrStay():
	if count == 21:
		print "Blackjack! You got $count"
	elif count > 21:
		print "Bust! You got $count"
	else:
		print "Would you like to hit or stay?(type hit or stay)"
		ans = Console.ReadLine()
		if ans == "hit":
			getCard()
			hitOrStay()
		elif ans == "stay":
			print "You got a $count"
		else:
			print "I don't know what you are talking about."
			hitOrStay()

print "Welome to Black Jack\nHere are your cards:"
getCard()
getCard()
hitOrStay()
print playedCards
