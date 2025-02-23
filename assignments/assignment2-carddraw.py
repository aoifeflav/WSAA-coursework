# This program deals 5 cards and prints the value and suit of each card
#Author: Aoife Flavin

# Imports the url and prints out the deck id, confirms it was shuffled and says there are 52 cards remaining
import requests
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
data = response.json()
#print(data)

#Result: {'success': True, 'deck_id': 'ddzhfvywced7', 'remaining': 52, 'shuffled': True}

#Draw 5 cards from the deck
draw_response = requests.get("https://deckofcardsapi.com/api/deck/ddzhfvywced7/draw/?count=5")
draw_5 = draw_response.json()


#Print them
cards_drawn = draw_5["cards"]
print("Cards dealt:")
for card in draw_5["cards"]:
    print(f"{card['value']} of {card['suit']}")

# Map the values of the cards to their numerical value to make it easier to compare
value_map = {'ACE': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'JACK': 11, 'QUEEN': 12, 'KING': 13}

#Define value of cards vs suits
values = [value_map[card['value']] for card in cards_drawn]
suits = [card['suit'] for card in cards_drawn]

#Count the occurances of each value
value_counts = {}
for value in values:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

# Count occurrences of each suit
suit_counts = {}
for suit in suits:
    if suit in suit_counts:
        suit_counts[suit] += 1
    else:
        suit_counts[suit] = 1

# Check for pair, triple or quad
has_pair = any(count == 2 for count in value_counts.values())
has_triple = any(count == 3 for count in value_counts.values())
has_quad = any(count == 4 for count in value_counts.values())

# check for straight
values.sort()
is_straight = all(values[i] + 1 == values[i + 1] for i in range(len(values) - 1))

# Check for all cards of the same suit
all_same_suit = len(suit_counts) == 1

# print message
if has_pair:
    print("Congratulations - You drew a pair!")
if has_triple:
    print("Congratulations - You drew a triple!")
if is_straight:
    print("Congratulations - You drew a straight!")
if all_same_suit:
    print("Congratulations - All your cards are the same suit!")
if not (has_pair or has_triple or is_straight or all_same_suit):
    print("You had no special combinations drawn")


#Sources
#https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item
#https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python
#Perplexity.ai