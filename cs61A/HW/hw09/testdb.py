points={"J":10,"Q":10,"K":10,"A":1}
points.update({n: n for n in range(2,11)})

def hand_score(hand):
    total = sum([points[card] for card in hand])
    return total
my_hand={'A','K',2}
print(hand_score(my_hand))

