import random
from arts import *
def myTurn(player):
  my_choice = input("Do you want to hit or stand (type 'hit' or 'stand')? ")
  if my_choice.lower() == 'hit':
    Hit(result=myresult, player="you", card_name=mycards)
  elif my_choice.lower() == 'stand':
    dealerTurn(player="dealer")
  else:
    print("Invalid Input")


def Hit(result, player, card_name):
  drawn_card = random.choice(cards)
  global count
  global dealer_hidden_result
  global myresult
  global j

  if drawn_card == 11:
    if result + 11 <= 21:
      drawn_card = 11
    else:
      drawn_card = 1

  for card in range(j,len(card_name)):
    if card_name[card] == 11:
      j=card+1
      if result + drawn_card > 21:
        result = result - 10
      else:
        result = result

  result = result + drawn_card
  card_name.append(drawn_card)

  if player.lower() == "dealer":
    if count < 1:
      print(
        f"The dealer cards are {card_name} (the dealer now has flipped the hidden card and has also drawn a card({drawn_card})=> result={result}) "
      )
      count = count + 1
    else:
      print(f"The dealer cards are {card_name} (result={result})")

    # update the global variable dealer_hidden_result with the new value of result
    dealer_hidden_result = result

  elif player.lower() == "you":
    print(
      f"The drawn card is {drawn_card} => your cards are {card_name} (result={result})"
    )
    # update the global variable myresult with the new value of result
    myresult = result

  if result > 21:
    print(
      f"{player.upper()} lost because the total result({result}) exceeds 21")
  elif result == 21:
    if result == myresult:
      if result != dealer_hidden_result:
        print(f"{player.upper()} won")
      else:
        print("draw")
    elif result == dealer_hidden_result:
      if result != myresult:
        print(f"{player.upper()} won")
      else:
        print("draw")
  else:
    if player.lower() == "dealer":
      if result == myresult:
        print("Draw")
      else:
        dealerTurn(player="dealer")
    elif player.lower() == "you":
      if result == dealer_hidden_result:
        #print(f"Draw,(the dealer's cards value with the hidden one is {dealer_hidden_result})")
        print(f"Draw (the dealer cards are {card_name})")
      else:
        myTurn(player="you")


def dealerTurn(player):
  # global player
  if player.lower() == "dealer":
    if dealer_hidden_result <= 16:
      Hit(result=dealer_hidden_result, player="dealer", card_name=dealer_cards)
    elif dealer_hidden_result > 16 and dealer_hidden_result <= 21:
      if dealer_hidden_result == 21:
        print(
          f"Dealer Wins as a balackjack!! (dealer's cards are {dealer_cards})")
      else:
        if dealer_hidden_result > myresult:
          print(
            f"Dealer wins, since it's result is greater than yours (your result={myresult}) (dealer's cards={dealer_cards})"
          )
          #{dealer_hidden_result}

        elif dealer_hidden_result < myresult:
          print(
            f"You won, since your result is greater than the dealer's result({dealer_hidden_result})(dealer cards are ={dealer_cards})"
          )
        else:

          print(
            f"Draw, your score is {myresult} and the dealer's result({dealer_hidden_result}) are equal(dealer cards are {dealer_cards} )."
          )

          #(dealer's result with the hidden card ={dealer_hidden_result})")


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
myresult = 0
dealer_hidden_result = 0
dealer_visible_result = []
mycards = random.choices(cards, k=2)
dealer_cards = random.choices(cards, k=2)
print(logo)
print(f"\n\n{wlcm}\n\n")
print(remark)
print("\n\n")
for card in mycards:
  myresult += card
card = 0
for card in dealer_cards:
  dealer_hidden_result += card
dealer_visible_result.append(dealer_hidden_result - card)
k = 0
count = 0
j=0

if (10 in mycards and 11 in mycards):
  print("BlackJack!!!! , your first 2 cards are [11,10] so you won!!!!")
elif mycards[0] == 11 and mycards[1] == 11:
  myresult = 12  #one ace counted 11 and one counted as 1

else:
  while k < 1:
    print(f"Your cards are {mycards} (The result is {myresult})")
    # print(
    #   f"The dealer has two cards, one of them is {dealer_visible_result[0]} and the another one is hidden (result is {dealer_visible_result[0]})"
    # )
    print(f"The dealer cards are [{dealer_visible_result[0]}, Hidden Card]")
    k += 1
  myTurn(player="you")



