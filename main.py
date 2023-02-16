
import random
from arts import *
def myTurn(player):
  my_choice = input("Do you want to hit or stand (type 'hit' or 'stand')? ")
  if my_choice.lower() == 'hit':
    Hit(result=myresult, player="you", card_name=my_card_name)
  elif my_choice.lower() == 'stand':
    dealerTurn(player="dealer")
  else:
    print("Invalid Input")


def Hit(result, player, card_name):
  drawn_card = random.choice(cards)
  global count
  global dealer_hidden_result
  global myresult

  if drawn_card == 11:
    drawn_card_name = "Ace"
    if result + 11 <= 21:
      drawn_card=11
    else:
      drawn_card=1
  elif drawn_card == 10:
    drawn_card_name = random.choice(["10", "Jack", "Queen", "King"])
  else:
    drawn_card_name = drawn_card
  
  for card in card_name:
    if card == "Ace":
      if result + drawn_card > 21:
        result = result - 10
      else:
        result = result
  
  result = result + drawn_card

  if player.lower() == "dealer":
    if count < 1:
      print( f"The dealer's drawn card is {drawn_card_name} (value={drawn_card}) and the hidden one is {dealer_hidden_result-dealer_visible_result}(result becomes {result})")
      count = count + 1
    else:
      print( f"The dealer's drawn card is {drawn_card_name} , so the result becomes {result}")
    
    # update the global variable dealer_hidden_result with the new value of result
    dealer_hidden_result = result

  elif player.lower() == "you":
    print( f"The drawn card is {drawn_card_name} (value {drawn_card} ) (the result becomes {result})")
    # update the global variable myresult with the new value of result
    myresult = result
  
  if result > 21:
    print(f"{player} Lost because the value {result} exceeds 21")
  elif result == 21:
    if result == myresult:
      if result != dealer_hidden_result:
        print(f"{player} wins")
      else:
        print("draw")
    elif result == dealer_hidden_result:
      if result != myresult:
        print(f"{player} Wins")
      else:
        print("draw")
  else:
    if player.lower() == "dealer":
        if result==myresult:
            print("Draw")
        else:
            dealerTurn(player="dealer")
    elif player.lower() == "you":
        if result==dealer_hidden_result:
            print(f"Draw,(the dealer's cards value with the hidden one is {dealer_hidden_result})")
        else:
          myTurn(player="you")

def dealerTurn(player):
  # global player
  if player.lower() == "dealer":
    if dealer_hidden_result <= 16:
      Hit(result=dealer_hidden_result,
          player="dealer",
          card_name=dealer_card_name)
    else:
      if dealer_hidden_result > myresult:
        print(f"Dealer wins, since it's result is greater than yours (your result={myresult}) (dealer's result with the hidden card={dealer_hidden_result})")
      elif dealer_hidden_result < myresult:
        print(f"You won, since your result is greater than the dealer's result({dealer_hidden_result})(dealer's result with the hidden card ={dealer_hidden_result})")
      else:

        print(f"Draw, your score is {myresult} and the dealer's result({dealer_hidden_result}) are equal (dealer's result with the hidden card ={dealer_hidden_result})")

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
myresult = 0
dealer_hidden_result = 0
dealer_visible_result = 0
mycards = random.choices(cards, k=2)
dealer_cards = random.choices(cards, k=2)
my_card_name = []
dealer_card_name = []
print(logo)
print(f"\n\n{wlcm}")
print(remark)
for i in range(0, 2):
  if mycards[i] == 11:
    my_card_name.append("Ace")
  elif mycards[i] == 10:
    my_card_name.append(random.choice(["10", "Jack", "Queen", "King"]))
  else:
    my_card_name.append(mycards[i])

for i in range(0, 2):
  if dealer_cards[i] == 11:
    dealer_card_name.append("Ace")
  elif dealer_cards[i] == 10:
    dealer_card_name.append(random.choice(["10", "Jack", "Queen", "King"]))
  else:
    dealer_card_name.append(dealer_cards[i])
for card in mycards:
  myresult += card
card = 0
for card in dealer_cards:
  dealer_hidden_result += card
dealer_visible_result = dealer_hidden_result - card
k = 0
count = 0

if (10 in mycards and 11 in mycards):
  print(
    "BlackJack!!!! , your first 2 cards are an ace and a 10 so you won!!!!")
elif mycards[0]==11 and mycards[1]==11:
    myresult=12 #one ace counted 11 and one counted as 1

else:
  while k < 1:
    print(f"Your cards are {my_card_name[0]} and {my_card_name[1]} (The result is {myresult})")
    print( f"The dealer has two cards, one of them is {dealer_card_name[0]} and the another one is hidden (result is {dealer_visible_result})")
    k += 1
  myTurn(player="you")

