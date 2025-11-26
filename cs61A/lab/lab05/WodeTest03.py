import random
points={'A':1 ,'J':10 ,'Q':10 ,'K':10}

def hand_score(hand):
    total=sum([points.get(card,card) for card in hand])
    if total<=11 and 'A' in hand:
        return total+10
    return total

def shuffle_cards():
    deck=(['J','Q','K','A']+list(range(2,11)))*4
    random.shuffle(deck)
    return deck

print(shuffle_cards())


